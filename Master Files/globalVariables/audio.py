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

# 8 music sample sets by Matt hyland
audio.snareSolo = aud.Factory.file(path+"/8-samples/snape solo.wav")
audio.snarehalfbar = aud.Factory.file(path+"/8-samples/snare half bar.wav")
audio.openHatSolo= aud.Factory.file(path+"/8-samples/open hat solo.wav")
audio.openHatHalfBar= aud.Factory.file(path+"/8-samples/open hat half bar.wav")
audio.kickSolo = aud.Factory.file(path+"/8-samples/kick solo.wav")
audio.dunno = aud.Factory.file(path+"/8-samples/dunno.wav")
audio.drumsWithLoops = aud.Factory.file(path+"/8-samples/drums with loops.wav")
audio.drumsTogether = aud.Factory.file(path+"/8-samples/drums together.wav")
audio.closedHighHatSolo = aud.Factory.file(path+"/8-samples/closed high hat solo.wav")
audio.closedHighHatHalfBar = aud.Factory.file(path+"/8-samples/closed high hat half bar.wav")





