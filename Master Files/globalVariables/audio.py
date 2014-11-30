# This loads audio files as global variables from a main library
# Author: Tanya Goncalves (goncat@mcmaster.ca)

import aud
import audio

print("loading audio files and music")

path = "Desktop/globalVariables" # need to place globalVariables folder onto desktop in order for it to work!

# 5 drum loop samples by Matt Hyland
audio.drumloop1 = aud.Factory.file(path+"/5-loops/drum loop 128 bpm 1.wav")
audio.drumloop2 = aud.Factory.file(path+"/5-loops/drum loop 128 bpm 2.wav")
audio.drumloop3 = aud.Factory.file(path+"/5-loops/drum loop 128 bpm 3.wav")
audio.drumloop4 = aud.Factory.file(path+"/5-loops/drum loop 125 bpm 2.wav")
audio.drumloop5 = aud.Factory.file(path+"/5-loops/drum loop 125 bpm 3.wav")

# 10 music sample sets by Matt hyland
audio.snareSolo = aud.Factory.file(path+"/8-samples/snare solo.mp3")
audio.snarehalfbar = aud.Factory.file(path+"/8-samples/snare half bar.mp3")
audio.openHatSolo= aud.Factory.file(path+"/8-samples/open hat solo.mp3")
audio.openHatHalfBar= aud.Factory.file(path+"/8-samples/open hat half bar.mp3")
audio.kickSolo = aud.Factory.file(path+"/8-samples/kick solo.mp3")
audio.dunno = aud.Factory.file(path+"/8-samples/dunno.mp3")
audio.drumsWithLoops = aud.Factory.file(path+"/8-samples/drums with loops.mp3")
audio.drumsTogether = aud.Factory.file(path+"/8-samples/drums together.mp3")
audio.closedHighHatSolo = aud.Factory.file(path+"/8-samples/closed high hat solo.mp3")
audio.closedHighHatHalfBar = aud.Factory.file(path+"/8-samples/closed high hat half bar.mp3")





