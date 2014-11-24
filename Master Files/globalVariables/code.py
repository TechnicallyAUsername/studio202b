# This loads the global variable sounds and plays it
# Author: Tanya Goncalves (goncat@mcmaster.ca)

import audio
import aud

device = aud.device()

device.play(audio.drumloop1)
