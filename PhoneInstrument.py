# PhoneInstrument
# Authors: Pangur Brougham-Cook, Lawton Stalvey, Gabrielle Cozart
# Date: 1/26/19
# Version 1


#import libraries
from osc import *
from music import *
from gui import *

#Set global variables
noteTrigger = -2.0
currentShake = 0.0
currentRoll = 0.0
volume = 64
pitch = 64
instrument = PIANO

# Create OSCIn Device
phone1 = OscIn(5700)

########### note trigger function ###############
def shake(message):
   global noteTrigger, currentShake,phrase, volume, pitch, instrument
   
   args = message.getArguments()
   
   currentShake = args[2]
   
   if(noteTrigger > currentShake):
      Play.setInstrument(instrument)
      Play.noteOn(pitch, volume, 0)
      Play.noteOff(pitch, 0)
 
############# Update Atributes ##################      
   
def changeVolume(message):
   global volume
   
   args = message.getArguments()
   volumeFloat = args[0]
   volume = mapValue(volumeFloat, 0.0, 1.0, 15, 127)
   
def changePitch(message):
   global pitch
   
   args = message.getArguments()
   pitchFloat = args[0]
   pitch = mapValue(pitchFloat, 0.0, 1.0, 0, 127)
   
############# Set Instruments ################## 

def setTaiko(message):
   global instrument
   
   args = message.getArguments()
   change = args[0]
   
   if(change == 1.0):
      instrument = TAIKO
      
def setSteel(message):
   global instrument
   
   args = message.getArguments()
   change = args[0]
   
   if(change == 1.0):
      instrument = STEEL_DRUM
      
def setWoodblock(message):
   global instrument
   
   args = message.getArguments()
   change = args[0]
   
   if(change == 1.0):
      instrument = WOODBLOCK
      
def setMeltom(message):
   global instrument
   
   args = message.getArguments()
   change = args[0]
   
   if(change == 1.0):
      instrument = TOM_TOM
      
def setSynthDrum(message):
   global instrument
   
   args = message.getArguments()
   change = args[0]
   
   if(change == 1.0):
      instrument = SYNTH_DRUM
      
def setVibe(message):
   global instrument
   
   args = message.getArguments()
   change = args[0]
   
   if(change == 1.0):
      instrument = VIBES
      
def setMarimba(message):
   global instrument
   
   args = message.getArguments()
   change = args[0]
   
   if(change == 1.0):
      instrument = MARIMBA
      
def setBells(message):
   global instrument
   
   args = message.getArguments()
   change = args[0]
   
   if(change == 1.0):
      instrument = TUBULAR_BELL

def setPiano(message):
   global instrument
   
   args = message.getArguments()
   change = args[0]
   
   if(change == 1.0):
      instrument = PIANO
      
   
######## Callback methods ########
phone1.onInput("/accxyz", shake)
phone1.onInput("/1/fader2", changeVolume)
phone1.onInput("/1/fader1", changePitch)

######## button methods ##########
phone1.onInput("/1/push1", setTaiko)
phone1.onInput("/1/push2", setSteel)
phone1.onInput("/1/push3", setWoodblock)
phone1.onInput("/1/push4", setMeltom)
phone1.onInput("/1/push5", setSynthDrum)
phone1.onInput("/1/push6", setVibe)
phone1.onInput("/1/push7", setMarimba)
phone1.onInput("/1/push8", setBells)
phone1.onInput("/1/push9", setPiano)

# Hide Messages
phone1.hideMessages()