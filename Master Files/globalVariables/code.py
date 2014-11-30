# This loads the global variable sounds and plays it
# Author: Tanya Goncalves (goncat@mcmaster.ca)

import audio
import aud
import bge

device = aud.device()

co = bge.logic.getCurrentController()
sensor = co.sensors["Keyboard"]

for key,status in sensor.events:
    if status == bge.logic.KX_INPUT_JUST_ACTIVATED:
        
        # 5 drum loop sample sets and their key commands
        # Q, W, E, R, T keys control the drum loops
        if key == bge.events.QKEY:
            device.play(audio.drumloop1)
                
        if key == bge.events.WKEY:
            device.play(audio.drumloop2)

        if key == bge.events.EKEY:
            device.play(audio.drumloop3)

        if key == bge.events.RKEY:
            device.play(audio.drumloop4)

        if key == bge.events.TKEY:
            device.play(audio.drumloop5)

        # 10 music sample sets and their key commands
        # A, S, D, F, G, H, J, K, L, ; keys control 10 sample sets
        if key == bge.events.AKEY:
            device.play(audio.snareSolo)

        if key == bge.events.SKEY:
            device.play(audio.snarehalfbar)

        if key == bge.events.DKEY:
            device.play(audio.openHatSolo)

        if key == bge.events.FKEY:
            device.play(audio.openHatHalfBar)

        if key == bge.events.GKEY:
            device.play(audio.kickSolo)

        if key == bge.events.HKEY:
            device.play(audio.dunno)

        if key == bge.events.JKEY:
            device.play(audio.drumsWithLoops)

        if key == bge.events.KKEY:
            device.play(audio.drumsTogether)

        if key == bge.events.LKEY:
            device.play(audio.closedHighHatSolo)

        if key == bge.events.SEMICOLONKEY:
            device.play(audio.closedHighHatHalfBar)