#This file analyses the beats of each song and the amplitudes at each beat 
#in order for the notes to play in the game. This file takes forever to run 
#and would slow down the game so it is prerun and the output that each song 
# produces when ran are in chords.py
import numpy
import librosa

'''song1 = aubio.source('eyeOfTiger.mp3')
# samplerate = 44100 ,  channels = 2, duration = 14435712'''

'''
audio,sfreq = librosa.load("eyeOfTiger.wav")
time = numpy.arange(0,len(audio)) / sfreq
print(onset)'''

class ProduceChords(object): #change everything to OOP because songname, beatList can be kept track off
    def __init__(self,song):
        self.song = song
        self.y, self.sr = librosa.load(self.song)
        self.onset = librosa.onset.onset_strength(self.y,sr=self.sr,aggregate=numpy.median) #14097
        self.tempo, self.beatTimes = librosa.beat.beat_track(y=self.y, sr=self.sr,units = "time")
        self.beatList = [] #571
        for number in self.beatTimes:
            t = (number*10)/10
            time = float("%0.3f"% t)
            self.beatList.append(time)
        self.chords = []
        self.amplitudeList = set()
        for beat in self.beatList:
            beat = int(beat)
            amp = self.amplitude(beat)
            self.amplitudeList.add(amp)
        
        

    def noteProduce(self):
        for time in self.beatList: #for each time produces the key 
            output = self.beatKey(time)
            self.chords.append(output)
        print(self.chords)
    
    def beatKey(self,time): #outputs list [0,1,1,0,0, time]
        amp = self.amplitude(time)
        ampRange = self.amplitudeRange(amp)
        if ampRange == 1:
            key = [(1,0,0,0,0),time]
        elif ampRange == 2:
            key = [(0,1,0,0,0),time]
        elif ampRange == 3:
            key = [(0,0,1,0,0),time]
        elif ampRange == 4:
            key = [(0,0,0,1,0),time]
        elif ampRange == 5:
            key = [(0,0,0,0,1),time]
        elif ampRange == 6:
            key = [(1,1,0,0,0),time]
        elif ampRange == 7:
            key = [(1,0,1,0,0),time]
        elif ampRange == 8:
            key = [(1,0,0,1,0),time]
        elif ampRange == 9:
            key = [(1,0,0,0,1),time]
        elif ampRange == 10:
            key = [(0,1,1,0,0),time]
        elif ampRange == 11:
            key = [(0,1,0,1,0),time]
        elif ampRange == 12:
            key = [(0,1,0,0,1),time]
        elif ampRange == 13:
            key = [(0,0,1,1,0),time]
        elif ampRange == 14:
            key = [(0,0,1,0,1),time]
        elif ampRange == 15:
            key = [(0,0,0,1,1),time]
        
        
        return key

    def amplitude(self,time): #can only take int times
        hop_length = 512
        n_fft = 1024

        array = numpy.abs(librosa.core.stft(self.y, n_fft=n_fft, hop_length=hop_length))
        fft_bin = 14
        time_idx = int(time)

        #print('amplitude: ', array[fft_bin, time_idx])
        return (array[fft_bin, time_idx])

    def maxAmp(self):
        maxAmp = max(self.amplitudeList)
        return maxAmp 
    
    def amplitudeRange(self,amp):
        maxAmp = self.maxAmp()
        r1h = (maxAmp/15) #range 1 high
        r2h = (maxAmp/15)*2
        r3h = (maxAmp/15)*3
        r4h = (maxAmp/15)*4
        r5h = (maxAmp/15)*5
        r6h = (maxAmp/15)*6
        r7h = (maxAmp/15)*7
        r8h = (maxAmp/15)*8
        r9h = (maxAmp/15)*9
        r10h = (maxAmp/15)*10
        r11h = (maxAmp/15)*11
        r12h = (maxAmp/15)*12
        r13h = (maxAmp/15)*13
        r14h = (maxAmp/15)*14
        r15h = (maxAmp/15)*15
        ampRange1 = 1
        if amp >= 0 and amp < r1h:
            ampRange1 = 1
        elif amp>= r1h and amp < r2h:
            ampRange1 = 2
        elif amp>= r2h and amp < r3h:
            ampRange1 = 3
        elif amp>= r3h and amp < r4h:
            ampRange1 = 4
        elif amp>= r4h and amp < r5h:
            ampRange1 = 5
        elif amp>= r5h and amp < r6h:
            ampRange1 = 6
        elif amp>= r6h and amp < r7h:
            ampRange1 = 7
        elif amp>= r7h and amp < r8h:
            ampRange1 = 8
        elif amp>= r8h and amp < r9h:
            ampRange1 = 9
        elif amp>= r9h and amp < r10h:
            ampRange1 = 10
        elif amp>= r10h and amp < r11h:
            ampRange1 = 11
        elif amp>= r11h and amp < r12h:
            ampRange1 = 12
        elif amp>= r12h and amp < r13h:
            ampRange1 = 13
        elif amp>= r13h and amp < r14h:
            ampRange1 = 14
        elif amp>= r14h and amp < r15h:
            ampRange1 = 15
       
        return ampRange1




#these were run inorder to get the chords that were copied into chords.py

'''song1run = ProduceChords('eyeOfTiger.wav')
song1run.noteProduce()

song2run = ProduceChords('hitme.wav')
song2run.noteProduce()


song3run = ProduceChords('smoke.wav')
song3run.noteProduce()


song4run = ProduceChords('sunshine.wav')
song4run.noteProduce()


song5run = ProduceChords('slowRide.wav')
song5run.noteProduce()
'''
