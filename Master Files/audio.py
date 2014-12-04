# This loads audio files as global variables from a main library
# Author: Tanya Goncalves (goncat@mcmaster.ca)

import bge;
import os.path;
import aud;
import audio;

print("loading audio files and music")

# please add all of the remaining audio files here...
# you can add audio files by following the template I have made with the following samples below...

audio.drumloop1 = aud.Factory.file(bge.logic.expandPath("//../5-loops/drum loop 128 bpm 1.wav")) # notice that i have given each loop it's own name (ex. drumloop1)
audio.drumloop2 = aud.Factory.file(bge.logic.expandPath("//../5-loops/drum loop 128 bpm 2.wav")) # notice also that i have set the file path directly from the git Hub folder i made called 5-loops
audio.drumloop3 = aud.Factory.file(bge.logic.expandPath("//../5-loops/drum loop 128 bpm 3.wav")) # that's it!
audio.drumloop4 = aud.Factory.file(bge.logic.expandPath("//../5-loops/drum loop 125 bpm 2.wav"))
audio.drumloop5 = aud.Factory.file(bge.logic.expandPath("//../5-loops/drum loop 125 bpm 3.wav"))

audio.snareSolo = aud.Factory.file(bge.logic.expandPath("//../8-samples/snare solo.mp3"))
audio.snarehalfbar = aud.Factory.file(bge.logic.expandPath("//../8-samples/snare half bar.mp3"))
audio.openHatSolo= aud.Factory.file(bge.logic.expandPath("//../8-samples/open hat solo.mp3"))
audio.openHatHalfBar= aud.Factory.file(bge.logic.expandPath("//../8-samples/open hat half bar.mp3"))
audio.kickSolo = aud.Factory.file(bge.logic.expandPath("//../8-samples/kick solo.mp3"))
audio.dunno = aud.Factory.file(bge.logic.expandPath("//../8-samples/dunno.mp3"))
audio.drumsWithLoops = aud.Factory.file(bge.logic.expandPath("//../8-samples/drums with loops.mp3"))
audio.drumsTogether = aud.Factory.file(bge.logic.expandPath("//../8-samples/drums together.mp3"))
audio.closedHighHatSolo = aud.Factory.file(bge.logic.expandPath("//../8-samples/closed high hat solo.mp3"))
audio.closedHighHatHalfBar = aud.Factory.file(bge.logic.expandPath("//../8-samples/closed high hat half bar.mp3"))





