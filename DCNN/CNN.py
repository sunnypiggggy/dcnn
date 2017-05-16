import os 
import librosa 
import librosa.core as librosaCore
import tensorflow as tf 
import numpy as np
import matplotlib.pyplot as plt

def windows(data, window_size):
    start = 0
    while start < len(data):
        yield start, start + window_size
        start += (window_size / 2)
        
        
def extract_features(parent_dir,sub_dirs,file_ext="*.wav",bands = 60, frames = 41):
    window_size = 512 * (frames - 1)
    log_specgrams = []
    labels = []
    for l, sub_dir in enumerate(sub_dirs):
        for fn in glob.glob(os.path.join(parent_dir, sub_dir, file_ext)):
            sound_clip,s = librosa.load(fn)
            label = fn.split('/')[2].split('-')[1]
            for (start,end) in windows(sound_clip,window_size):
                if(len(sound_clip[start:end]) == window_size):
                    signal = sound_clip[start:end]
                    melspec = librosa.feature.melspectrogram(signal, n_mels = bands)
                    logspec = librosa.logamplitude(melspec)
                    logspec = logspec.T.flatten()[:, np.newaxis].T
                    log_specgrams.append(logspec)
                    labels.append(label)
            
    log_specgrams = np.asarray(log_specgrams).reshape(len(log_specgrams),bands,frames,1)
    features = np.concatenate((log_specgrams, np.zeros(np.shape(log_specgrams))), axis = 3)
    for i in range(len(features)):
        features[i, :, :, 1] = librosa.feature.delta(features[i, :, :, 0])
    
    return np.array(features), np.array(labels,dtype = np.int)

def extract_feature(label,rawSound,bands=60,frames=41):
    window_size = 512 * (frames - 1)
    log_specgrams = []
    for (start,end) in windows(rawSound,window_size):
        if(len(rawSound[start:end]) == window_size):
            soundSegment = rawSound[start:end]
            melSpec = librosa.feature.melspectrogram(soundSegment,n_mels=bands)
            logSpec = librosa.logamplitude(melSpec)
            logSpec = logSpec.T.flatten()[:,np.newaxis].T
            log_specgrams.append(logSpec)
    log_specgrams = np.asarray(log_specgrams).reshape(len(log_specgrams),bands,frames,1)
    features = np.concatenate((log_specgrams,np.zeros(np.shape(log_specgrams))),axis=3)
    for i in range(features):
        features[i,:,:,1] = librosa.feature.delta(features[i,:,:,0])

    return zip(label,np.array(features))


def one_hot_encode(labels):
    n_labels = len(labels)
    n_unique_labels = len(np.unique(labels))
    one_hot_encode = np.zeros((n_labels,n_unique_labels))
    one_hot_encode[np.arange(n_labels), labels] = 1
    return one_hot_encode