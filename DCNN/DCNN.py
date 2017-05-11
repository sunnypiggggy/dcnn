import librosa
import os
import numpy as np
import matplotlib.pyplot as plt
from audioFileUtility import *


if __name__=='__main__':
    #LoadAudioBatch(None)
    #LoadAudioBatch(None,None)
    fileAudioPath=getAudioPaths()
    #for xx in fileAudioPath:
    #    print(os.path.basename(xx))
    #plt.plot( np.array( LoadAudioFiles(fileAudioPath[0])))
    for x in range(10):
         xx,sr= librosa.load(fileAudioPath[x])
         plt.subplot(10,1,x+1)
         plt.plot(xx) 

    plt.show()
    print("The end")