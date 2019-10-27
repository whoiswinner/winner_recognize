#_*_ coding:utf-8 _*_
# Coded: KuuWangE

import pyaudio
import wave
import audioop
import math
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


print (plt.get_backend())
plt.gcf().canvas.set_window_title('403 일해라 벌레들아아아아아')




class Detector():
    def __init__(self):
        self.Prepare_Audio()

        self.G_Range = 400
        self.X = list()
        self.Y = list()
        for i in range(self.G_Range):
            self.X.append(i)
            if(i < 40):
                self.Y.append(40)
            elif(i > 100):
                self.Y.append(100)
            else:
                self.Y.append(i)
        self.G_i = 0

        plt.ion()
        plt.show()
        self.graph = plt.plot(self.X, self.Y)[0]
        plt.xlabel('Time sequence')
        plt.ylabel('DeciBel')

    def Prepare_Audio(self):
        self.read_index = 0

        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.RECORD_SECONDS = 60 * 60
        self.audio = pyaudio.PyAudio()

        self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                      rate=self.RATE, input=True,
                                      frames_per_buffer=self.CHUNK)
    def RePrepare_Audio(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        self.Prepare_Audio()


    def start(self):
        while(True):
            if(self.read_index < int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
                try:
                    data = self.stream.read(self.CHUNK)
                    rms = audioop.rms(data, 2)  # here's where you calculate the volume
                    volume = 20 * math.log10(rms)
                    print("Measured Amplitude : {} DB : {}".format(rms, volume))
                except:
                    pass
                self.read_index += 1
            else:
                self.RePrepare_Audio()

            self.Update_Graph(volume)
            # put the code you would have put in the `run` loop here
        pass

    def Update_Graph(self, volume):
        print(len(self.Y), self.G_i)
        self.Y[self.G_i] = volume;
        self.G_i += 1
        if(self.G_i>=self.G_Range):
            self.G_i = 0
        # Add Graph Value InDex
        self.graph.set_ydata(self.Y)
        plt.draw()
        plt.pause(0.01)
