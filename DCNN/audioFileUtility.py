import librosa
import librosa.display
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram

def LoadAudioFiles(filePath):
   rawSound=[]
   for fp in filePath:
       X,SampleRate =librosa.load(fp)
       rawSound.append(X)
   return rawSound

    
def getAudioPaths():
    filePathList=[]
    rootPath=os.getcwd()
    f= os.path.join(rootPath,'ESC-50-master')
    classDirNames=[ name for name in os.listdir(f) if os.path.isdir(os.path.join(f,name))]
    for subDirName in classDirNames:
        #print(subDirName)
        fileRootPath=os.path.join(f,subDirName)
        filePath=[ name for name in os.listdir(fileRootPath) if os.path.isfile(os.path.join(fileRootPath,name))]
        for xx in range(len(filePath)-1):
            #print(os.path.join(fileRootPath,filePath[xx]))       
            filePathList.append((subDirName, os.path.join(fileRootPath,filePath[xx])))
    return filePathList


def plotWave(soundName,rawSound):
    hfig=plt.figure()
    i=1
    for n,f in zip(soundName,rawSound):
        plt.subplot(10,1,i)
        librosa.display.waveplot(np.array(f),sr=22050)
        plt.title(n.title())
        i +=1;
    plt.show()

def plotSpecgram(soundName,rawSound):
    i=1
   # hfig=plt.figure(figsize=(25,60),dpi=900)
    hfig=plt.figure()
    for n,f in zip(soundName,rawSound):
        plt.subplot(10,1,i)
        specgram(np.array(f),Fs=22050)
        plt.title(n)
        i+=1
    #plt.subtitle("Figure 2: Spectrogram",x=0.5, y=0.915,fontsize=18)
    plt.show()
