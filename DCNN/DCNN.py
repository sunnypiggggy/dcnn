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

if __name__ == '__main__':
    #fileAudioPath=getAudioPaths()
    #with open('AudioFilePaths.dat','wb') as hFile:
    #     pickle.dump(fileAudioPath,hFile,pickle.HIGHEST_PROTOCOL)
    #with open('AudioFilePaths.dat','rb') as hFile:
    #    fileAudioPath = pickle.load(hFile)
    
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

    with open('audioData_label.dat','rb') as hFile:
        audioData_label = pickle.load(hFile)


    