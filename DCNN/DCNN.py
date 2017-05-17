import librosa
import librosa.display
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
from audioFileUtility import *
import soundfile as sf
import audioread
import pickle 
from CNN import *
import matplotlib
if __name__ == '__main__':

    #fileAudioPath=getAudioPaths()
    #with open('AudioFilePaths.dat','wb') as hFile:
    #     pickle.dump(fileAudioPath,hFile,pickle.HIGHEST_PROTOCOL)
    with open('AudioFilePaths.dat','rb') as hFile:
        fileAudioPath = pickle.load(hFile)
    
    #for xx in fileAudioPath:
    #    print(os.path.basename(xx))
    #plt.plot( np.array( LoadAudioFiles(fileAudioPath[0])))

    #for x in range(10):
    #     xx,sr= librosa.load(fileAudioPath[x][1])
    #     plt.subplot(10,1,x+1)
    #     plt.plot(xx)
    #plt.show()

    #X,_ = librosa.load(fileAudioPath[4][1])
    #X2,_ = sf.read(fileAudioPath[0][1])
    #plt.figure()
    # y=librosa.stft(X)
    #y=librosa.amplitude_to_db(librosa.stft(X), ref=np.max)
    #librosa.display.specshow(y,y_axis='linear')
    #plt.show()

    # y, sr = librosa.load(librosa.util.example_audio_file())
    # D = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)
    # librosa.display.specshow(D, y_axis='linear')
    # plt.show()

    #plt.figure()
    #librosa.display.waveplot(np.array(X),sr=22050)
    #plt.show()

    #plt.figure()
    #specgram(np.array(X),Fs=22050)
    #plt.show()
    #plt.figure()
    #specgram(np.array(X2),Fs=22050)
    #plt.show()

    #plt.figure()
    #plt.plot(np.array(X2))
    #plt.show()

    #audioData = []
    #audioLabel = []
    #for i in range(49):
    #    audioLabel.append(fileAudioPath[i*40+5][0])
    #    audioData.append(librosa.load(fileAudioPath[i*40+5][1])[0])
    #audioData_label=zip(audioLabel,audioData)
    #with open('audioData_label.dat','wb') as hFile:
    #     pickle.dump(audioData_label,hFile,pickle.HIGHEST_PROTOCOL)
    #plotSpecgram(audioLabel,audioData)

    with open('audiodata_label.dat','rb') as hfile:
        audiodata_label = pickle.load(hfile)

    X=[xx for _,xx in audiodata_label]
    ## plt.figure()
    ## #specgram(X[0],Fs=22050)
    ## plt.plot(X[0])
    ## plt.show()

    log_specgrams = []
    frams = 41
    windows_size = 512 * (frams - 1)
    for (strat, end) in windows(X[0], windows_size):
        if (len(X[0][strat:end]) == windows_size):
            audioSegment = X[0][strat:end]
            melSpec = librosa.feature.melspectrogram(audioSegment, n_mels=60)
            logSpec = librosa.logamplitude(melSpec)
            plt.figure()
            librosa.display.specshow(logSpec,y_axis='linear')
            plt.show()
            logSpec = logSpec.T.flatten()[:, np.newaxis].T
            log_specgrams.append(logSpec)
    #plt.figure()
    #librosa.display.specshow(y,y_axis='linear')
    #plt.show()
    #plt.figure()
    ## for i in range(9):
    ##     plt.subplot(10,1,i+1)
    ##     plt.plot(np.array( log_specgrams[i]).T)
    #plt.plot(melSpec)
    #plt.show()
    #print('the end')
