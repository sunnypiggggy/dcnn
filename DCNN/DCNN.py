import librosa
import librosa.display
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
from audioFileUtility import *


if __name__=='__main__':
    #LoadAudioBatch(None)
    #LoadAudioBatch(None,None)
    fileAudioPath=getAudioPaths()
    #for xx in fileAudioPath:
    #    print(os.path.basename(xx))
    #plt.plot( np.array( LoadAudioFiles(fileAudioPath[0])))

    #for x in range(10):
    #     xx,sr= librosa.load(fileAudioPath[x][1])
    #     plt.subplot(10,1,x+1)
    #     plt.plot(xx) 
    #plt.show()
    X,_=librosa.load(fileAudioPath[2][1])
    #plt.figure()
    #librosa.display.waveplot(np.array(X),sr=22050)
    #plt.show()
    plt.figure()
    specgram(np.array(X),Fs=22050)
    plt.show()

    print("The end")