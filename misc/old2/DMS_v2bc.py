#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Tue Mar  7 14:47:18 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard
from psychopy.hardware import camera
from psychopy.sound import microphone

# Run 'Before Experiment' code from code

import random
import pandas as pd 



pos=[(.25,.25),(-.25,.25),(.25,-.25),(-.25,-.25)]
locations = ['topright','topleft','bottomright','bottomleft']
pictures  = ['images/picture_1.png','images/picture_2.png','images/picture_3.png']

trial_list = []
block_list = [] 

blockTypes = ["PRED","UNPRED","PRED","UNPRED"]

delayTime= .5 
delayTime_dist = .2

trialNum = 5
blockNum = len(blockTypes)
testing = False 

trial_count = 0 
for i_block in range(blockNum):
    blockType = blockTypes[i_block]
    
    if blockType == "PRED": 
        stimImage_i = random.randrange(0,3)

    for i in range(trialNum):
        delayTime = random.randrange(5,12)/10

        if blockType == "UNPRED": 
            stimImage_i = random.randrange(0,3)


        stimImage = pictures[stimImage_i]
        
        location_ind = [0,1,2,3]
        picture_ind =  [0,1,2]
        pos_ind = [0,1,2,3]

        random.shuffle(locations)
        random.shuffle(pictures)
        random.shuffle(pos)

        random.shuffle(location_ind)
        random.shuffle(picture_ind)
        random.shuffle(pos_ind)

        responseImage1              = pictures[picture_ind[0]]
        responseImage1_i            = picture_ind[0]
        responseImage1_location     = locations[location_ind[0]]
        responseImage1_location_i   = location_ind[0]
        responseImage1_pos          = pos[0]
        responseImage1_pos_ind      = pos_ind[0]

        responseImage2              = pictures[picture_ind[1]]
        responseImage2_i            = picture_ind[1]
        responseImage2_location     = locations[location_ind[1]]
        responseImage2_location_i   = location_ind[1]
        responseImage2_pos          = pos[1]
        responseImage2_pos_ind      = pos_ind[1]

        responseImage3              = pictures[picture_ind[2]]
        responseImage3_i            = picture_ind[2]
        responseImage3_location     = locations[location_ind[2]]
        responseImage3_location_i   = location_ind[2]
        responseImage3_pos          = pos[2]
        responseImage3_pos_ind      = pos_ind[2]

        app = { "delay_time":delayTime, "stimImage_i":stimImage_i, "stimImage":stimImage, 
        "responseImage1":responseImage1, "responseImage1_i":responseImage1_i, "responseImage1_pos":responseImage1_pos, "responseImage1_pos_ind":responseImage1_pos_ind, "responseImage1_location":responseImage1_location,"responseImage1_location_i":responseImage1_location_i,
        "responseImage2":responseImage2, "responseImage2_i":responseImage2_i, "responseImage2_pos":responseImage2_pos, "responseImage2_pos_ind":responseImage2_pos_ind, "responseImage2_location":responseImage2_location, "responseImage2_location_i":responseImage2_location_i,
        "responseImage3":responseImage3, "responseImage3_i":responseImage3_i, "responseImage3_pos":responseImage3_pos, "responseImage3_pos_ind":responseImage3_pos_ind, "responseImage3_location":responseImage3_location, "responseImage3_location_i":responseImage3_location_i}
        
        trial_list.append(app)
    block_list.append(trial_list) 
    trial_list = [] 
    

trial_list1 = block_list[0]
trial_list2 = block_list[1]
trial_list3 = block_list[2]
trial_list4 = block_list[3]

#trial_dict = trial_list1[0]
thisTrial = trial_list1[0]
thisTrial_2 = trial_list2[0]
thisTrial_3 = trial_list3[0]
thisTrial_4 = trial_list4[0]

#
##dirpath = _thisDir + os.sep + u'data/%s/%s/%s' % (expInfo['participant'], expName, expInfo['date'])
##dirpath = _thisDir + os.sep + u'data/%s/%s/%s' % (expInfo['participant'], expName, expInfo['date'])
#
#dirpath="/Users/kleinrl/Visual_Attention"
#
#os.makedirs(dirpath, exist_ok=True)
#dfs = []
#for i_block in range(len(blockTypes)): 
#    block = block_list[i_block]
#    blockType = blockTypes[i_block]
#    
#    df = pd.DataFrame(block)
#    outfile = "{}/{}-{}.csv".format(dirpath, i_block, blockType)
#    df.to_csv(outfile)
#    
#    dfs.append(df)
#
#df_all = pd.concat(dfs)
#outfile = "{}/{}".format(dirpath,"ALL.csv") 
#df_all.to_csv(outfile)




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'DMS_v2bc'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/kleinrl/Visual_Attention/DMS_v2bc.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='grey', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup eyetracking
ioConfig['eyetracker.hw.mouse.EyeTracker'] = {
    'name': 'tracker',
    'controls': {
        'move': [],
        'blink':('MIDDLE_BUTTON',),
        'saccade_threshold': 0.5,
    }
}
ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "codeStart" ---
# Run 'Begin Experiment' code from code

dirpath = _thisDir + os.sep + u'data/%s/%s/%s' % (expInfo['participant'], expName, expInfo['date'])
os.makedirs(dirpath, exist_ok=True)

dfs = []
for i_block in range(len(blockTypes)): 
    block = block_list[i_block]
    blockType = blockTypes[i_block]
    
    df = pd.DataFrame(block)
    outfile = "{}/{}-{}.csv".format(dirpath, i_block, blockType)
    df.to_csv(outfile)
    print("outfile: {}".format(outfile))
    dfs.append(df)

df_all = pd.concat(dfs)
outfile = "{}/{}".format(dirpath,"ALL.csv") 
df_all.to_csv(outfile)

myCount = 0

# --- Initialize components for Routine "trigger" ---
key_resp = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='awaiting trigger',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "baseline" ---

# --- Initialize components for Routine "codeEnd" ---
# Run 'Begin Experiment' code from code_2
myCount = 0 

# --- Initialize components for Routine "trial" ---
etRecord = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample = visual.ImageStim(
    win=win,
    name='sample', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_1 = visual.ImageStim(
    win=win,
    name='Response_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[thisTrial["responseImage1_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_2 = visual.ImageStim(
    win=win,
    name='Response_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[thisTrial["responseImage2_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_3 = visual.ImageStim(
    win=win,
    name='Response_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[thisTrial["responseImage3_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Delay = visual.ShapeStim(
    win=win, name='Delay',
    size=(0.01, 0.01), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)

# --- Initialize components for Routine "baseline" ---

# --- Initialize components for Routine "codeEnd" ---
# Run 'Begin Experiment' code from code_2
myCount = 0 

# --- Initialize components for Routine "trial_2" ---
etRecord_2 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample_2 = visual.ImageStim(
    win=win,
    name='sample_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response = visual.ImageStim(
    win=win,
    name='Response', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[thisTrial_2["responseImage1_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_4 = visual.ImageStim(
    win=win,
    name='Response_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[thisTrial_2["responseImage2_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_5 = visual.ImageStim(
    win=win,
    name='Response_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[thisTrial_2["responseImage3_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Delay_2 = visual.ShapeStim(
    win=win, name='Delay_2',
    size=(0.01, 0.01), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)

# --- Initialize components for Routine "baseline" ---

# --- Initialize components for Routine "codeEnd" ---
# Run 'Begin Experiment' code from code_2
myCount = 0 

# --- Initialize components for Routine "trial_3" ---
etRecord_3 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample_3 = visual.ImageStim(
    win=win,
    name='sample_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_6 = visual.ImageStim(
    win=win,
    name='Response_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[thisTrial_3["responseImage1_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_7 = visual.ImageStim(
    win=win,
    name='Response_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[thisTrial_3["responseImage2_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_8 = visual.ImageStim(
    win=win,
    name='Response_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[thisTrial_3["responseImage3_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Delay_3 = visual.ShapeStim(
    win=win, name='Delay_3',
    size=(0.01, 0.01), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)

# --- Initialize components for Routine "baseline" ---

# --- Initialize components for Routine "codeEnd" ---
# Run 'Begin Experiment' code from code_2
myCount = 0 

# --- Initialize components for Routine "trial_4" ---
etRecord_4 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample_4 = visual.ImageStim(
    win=win,
    name='sample_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_9 = visual.ImageStim(
    win=win,
    name='Response_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[thisTrial_4["responseImage1_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_10 = visual.ImageStim(
    win=win,
    name='Response_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[thisTrial_4["responseImage2_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_11 = visual.ImageStim(
    win=win,
    name='Response_11', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[thisTrial_4["responseImage3_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Delay_4 = visual.ShapeStim(
    win=win, name='Delay_4',
    size=(0.01, 0.01), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)

# --- Initialize components for Routine "baseline" ---

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "codeStart" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code
myCount = myCount + 1
if myCount > trialNum:
    trials.finished = True
# keep track of which components have finished
codeStartComponents = []
for thisComponent in codeStartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "codeStart" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in codeStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "codeStart" ---
for thisComponent in codeStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
#  
#for k in thisTrial.keys():
#    thisExp.addData(k, trial_dict[k])
#
#    
#
# the Routine "codeStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trigger" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
triggerComponents = [key_resp, text]
for thisComponent in triggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trigger" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['t'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trigger" ---
for thisComponent in triggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "baseline" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
baselineComponents = []
for thisComponent in baselineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "baseline" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "baseline" ---
for thisComponent in baselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "baseline" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("{}/{}-{}.csv".format(dirpath, 0, "PRED")),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "codeEnd" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    if myCount > trialNum:
        trials.finished = True
     
     myCount = myCount + 1
    
    print(myCount)
    # keep track of which components have finished
    codeEndComponents = []
    for thisComponent in codeEndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "codeEnd" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in codeEndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd" ---
    for thisComponent in codeEndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "codeEnd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample.setImage(thisTrial["stimImage"])
    Response_1.setImage(thisTrial["responseImage1"])
    Response_2.setImage(thisTrial["responseImage2"])
    Response_3.setImage(thisTrial["responseImage3"])
    # keep track of which components have finished
    trialComponents = [etRecord, sample, Response_1, Response_2, Response_3, polygon, Delay]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRecord* updates
        if etRecord.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord.frameNStart = frameN  # exact frame index
            etRecord.tStart = t  # local t and not account for scr refresh
            etRecord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord.started', t)
            etRecord.status = STARTED
        if etRecord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                etRecord.tStop = t  # not accounting for scr refresh
                etRecord.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord.stopped', t)
                etRecord.status = FINISHED
        
        # *sample* updates
        if sample.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            sample.frameNStart = frameN  # exact frame index
            sample.tStart = t  # local t and not account for scr refresh
            sample.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sample.started')
            sample.setAutoDraw(True)
        if sample.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sample.tStop = t  # not accounting for scr refresh
                sample.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sample.stopped')
                sample.setAutoDraw(False)
        
        # *Response_1* updates
        if Response_1.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Response_1.frameNStart = frameN  # exact frame index
            Response_1.tStart = t  # local t and not account for scr refresh
            Response_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_1.started')
            Response_1.setAutoDraw(True)
        if Response_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Response_1.tStop = t  # not accounting for scr refresh
                Response_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_1.stopped')
                Response_1.setAutoDraw(False)
        
        # *Response_2* updates
        if Response_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Response_2.frameNStart = frameN  # exact frame index
            Response_2.tStart = t  # local t and not account for scr refresh
            Response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_2.started')
            Response_2.setAutoDraw(True)
        if Response_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Response_2.tStop = t  # not accounting for scr refresh
                Response_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_2.stopped')
                Response_2.setAutoDraw(False)
        
        # *Response_3* updates
        if Response_3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Response_3.frameNStart = frameN  # exact frame index
            Response_3.tStart = t  # local t and not account for scr refresh
            Response_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_3.started')
            Response_3.setAutoDraw(True)
        if Response_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Response_3.tStop = t  # not accounting for scr refresh
                Response_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_3.stopped')
                Response_3.setAutoDraw(False)
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon.started')
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.stopped')
                polygon.setAutoDraw(False)
        
        # *Delay* updates
        if Delay.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Delay.frameNStart = frameN  # exact frame index
            Delay.tStart = t  # local t and not account for scr refresh
            Delay.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Delay, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Delay.started')
            Delay.setAutoDraw(True)
        if Delay.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Delay.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Delay.tStop = t  # not accounting for scr refresh
                Delay.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Delay.stopped')
                Delay.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord.status != FINISHED:
        etRecord.status = FINISHED
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials'


# --- Prepare to start Routine "baseline" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
baselineComponents = []
for thisComponent in baselineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "baseline" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "baseline" ---
for thisComponent in baselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "baseline" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("{}/{}-{}.csv".format(dirpath, 1, "UNPRED")),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "codeEnd" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    if myCount > trialNum:
        trials.finished = True
     
     myCount = myCount + 1
    
    print(myCount)
    # keep track of which components have finished
    codeEndComponents = []
    for thisComponent in codeEndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "codeEnd" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in codeEndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd" ---
    for thisComponent in codeEndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "codeEnd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_2.setImage(thisTrial_2["stimImage"])
    Response.setImage(thisTrial_2["responseImage1"])
    Response_4.setImage(thisTrial_2["responseImage2"])
    Response_5.setImage(thisTrial_2["responseImage3"])
    # keep track of which components have finished
    trial_2Components = [etRecord_2, sample_2, Response, Response_4, Response_5, polygon_2, Delay_2]
    for thisComponent in trial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_2" ---
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRecord_2* updates
        if etRecord_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord_2.frameNStart = frameN  # exact frame index
            etRecord_2.tStart = t  # local t and not account for scr refresh
            etRecord_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord_2.started', t)
            etRecord_2.status = STARTED
        if etRecord_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord_2.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_2.tStop = t  # not accounting for scr refresh
                etRecord_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_2.stopped', t)
                etRecord_2.status = FINISHED
        
        # *sample_2* updates
        if sample_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            sample_2.frameNStart = frameN  # exact frame index
            sample_2.tStart = t  # local t and not account for scr refresh
            sample_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sample_2.started')
            sample_2.setAutoDraw(True)
        if sample_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sample_2.tStop = t  # not accounting for scr refresh
                sample_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sample_2.stopped')
                sample_2.setAutoDraw(False)
        
        # *Response* updates
        if Response.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response.started')
            Response.setAutoDraw(True)
        if Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Response.tStop = t  # not accounting for scr refresh
                Response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response.stopped')
                Response.setAutoDraw(False)
        
        # *Response_4* updates
        if Response_4.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Response_4.frameNStart = frameN  # exact frame index
            Response_4.tStart = t  # local t and not account for scr refresh
            Response_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_4.started')
            Response_4.setAutoDraw(True)
        if Response_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Response_4.tStop = t  # not accounting for scr refresh
                Response_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_4.stopped')
                Response_4.setAutoDraw(False)
        
        # *Response_5* updates
        if Response_5.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Response_5.frameNStart = frameN  # exact frame index
            Response_5.tStart = t  # local t and not account for scr refresh
            Response_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_5.started')
            Response_5.setAutoDraw(True)
        if Response_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Response_5.tStop = t  # not accounting for scr refresh
                Response_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_5.stopped')
                Response_5.setAutoDraw(False)
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_2.started')
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_2.stopped')
                polygon_2.setAutoDraw(False)
        
        # *Delay_2* updates
        if Delay_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Delay_2.frameNStart = frameN  # exact frame index
            Delay_2.tStart = t  # local t and not account for scr refresh
            Delay_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Delay_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Delay_2.started')
            Delay_2.setAutoDraw(True)
        if Delay_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Delay_2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Delay_2.tStop = t  # not accounting for scr refresh
                Delay_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Delay_2.stopped')
                Delay_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_2" ---
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord_2.status != FINISHED:
        etRecord_2.status = FINISHED
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials_2'


# --- Prepare to start Routine "baseline" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
baselineComponents = []
for thisComponent in baselineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "baseline" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "baseline" ---
for thisComponent in baselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "baseline" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("{}/{}-{}.csv".format(dirpath, 2, "PRED")),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "codeEnd" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    if myCount > trialNum:
        trials.finished = True
     
     myCount = myCount + 1
    
    print(myCount)
    # keep track of which components have finished
    codeEndComponents = []
    for thisComponent in codeEndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "codeEnd" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in codeEndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd" ---
    for thisComponent in codeEndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "codeEnd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_3.setImage(thisTrial_3["stimImage"])
    Response_6.setImage(thisTrial_3["responseImage1"])
    Response_7.setImage(thisTrial_3["responseImage2"])
    Response_8.setImage(thisTrial_3["responseImage3"])
    # keep track of which components have finished
    trial_3Components = [etRecord_3, sample_3, Response_6, Response_7, Response_8, polygon_3, Delay_3]
    for thisComponent in trial_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_3" ---
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRecord_3* updates
        if etRecord_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord_3.frameNStart = frameN  # exact frame index
            etRecord_3.tStart = t  # local t and not account for scr refresh
            etRecord_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord_3.started', t)
            etRecord_3.status = STARTED
        if etRecord_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord_3.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_3.tStop = t  # not accounting for scr refresh
                etRecord_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_3.stopped', t)
                etRecord_3.status = FINISHED
        
        # *sample_3* updates
        if sample_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            sample_3.frameNStart = frameN  # exact frame index
            sample_3.tStart = t  # local t and not account for scr refresh
            sample_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sample_3.started')
            sample_3.setAutoDraw(True)
        if sample_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sample_3.tStop = t  # not accounting for scr refresh
                sample_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sample_3.stopped')
                sample_3.setAutoDraw(False)
        
        # *Response_6* updates
        if Response_6.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Response_6.frameNStart = frameN  # exact frame index
            Response_6.tStart = t  # local t and not account for scr refresh
            Response_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_6.started')
            Response_6.setAutoDraw(True)
        if Response_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_6.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Response_6.tStop = t  # not accounting for scr refresh
                Response_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_6.stopped')
                Response_6.setAutoDraw(False)
        
        # *Response_7* updates
        if Response_7.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Response_7.frameNStart = frameN  # exact frame index
            Response_7.tStart = t  # local t and not account for scr refresh
            Response_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_7.started')
            Response_7.setAutoDraw(True)
        if Response_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_7.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Response_7.tStop = t  # not accounting for scr refresh
                Response_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_7.stopped')
                Response_7.setAutoDraw(False)
        
        # *Response_8* updates
        if Response_8.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Response_8.frameNStart = frameN  # exact frame index
            Response_8.tStart = t  # local t and not account for scr refresh
            Response_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_8.started')
            Response_8.setAutoDraw(True)
        if Response_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_8.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Response_8.tStop = t  # not accounting for scr refresh
                Response_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_8.stopped')
                Response_8.setAutoDraw(False)
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_3.started')
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_3.stopped')
                polygon_3.setAutoDraw(False)
        
        # *Delay_3* updates
        if Delay_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Delay_3.frameNStart = frameN  # exact frame index
            Delay_3.tStart = t  # local t and not account for scr refresh
            Delay_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Delay_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Delay_3.started')
            Delay_3.setAutoDraw(True)
        if Delay_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Delay_3.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Delay_3.tStop = t  # not accounting for scr refresh
                Delay_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Delay_3.stopped')
                Delay_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_3" ---
    for thisComponent in trial_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord_3.status != FINISHED:
        etRecord_3.status = FINISHED
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials_3'


# --- Prepare to start Routine "baseline" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
baselineComponents = []
for thisComponent in baselineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "baseline" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "baseline" ---
for thisComponent in baselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "baseline" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("{}/{}-{}.csv".format(dirpath, 3, "UNPRED")),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "codeEnd" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    if myCount > trialNum:
        trials.finished = True
     
     myCount = myCount + 1
    
    print(myCount)
    # keep track of which components have finished
    codeEndComponents = []
    for thisComponent in codeEndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "codeEnd" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in codeEndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd" ---
    for thisComponent in codeEndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "codeEnd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_4.setImage(thisTrial_4["stimImage"])
    Response_9.setImage(thisTrial_4["responseImage1"])
    Response_10.setImage(thisTrial_4["responseImage2"])
    Response_11.setImage(thisTrial_4["responseImage3"])
    # keep track of which components have finished
    trial_4Components = [etRecord_4, sample_4, Response_9, Response_10, Response_11, polygon_4, Delay_4]
    for thisComponent in trial_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_4" ---
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRecord_4* updates
        if etRecord_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord_4.frameNStart = frameN  # exact frame index
            etRecord_4.tStart = t  # local t and not account for scr refresh
            etRecord_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord_4.started', t)
            etRecord_4.status = STARTED
        if etRecord_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord_4.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_4.tStop = t  # not accounting for scr refresh
                etRecord_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_4.stopped', t)
                etRecord_4.status = FINISHED
        
        # *sample_4* updates
        if sample_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            sample_4.frameNStart = frameN  # exact frame index
            sample_4.tStart = t  # local t and not account for scr refresh
            sample_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sample_4.started')
            sample_4.setAutoDraw(True)
        if sample_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sample_4.tStop = t  # not accounting for scr refresh
                sample_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sample_4.stopped')
                sample_4.setAutoDraw(False)
        
        # *Response_9* updates
        if Response_9.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Response_9.frameNStart = frameN  # exact frame index
            Response_9.tStart = t  # local t and not account for scr refresh
            Response_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_9.started')
            Response_9.setAutoDraw(True)
        if Response_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_9.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Response_9.tStop = t  # not accounting for scr refresh
                Response_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_9.stopped')
                Response_9.setAutoDraw(False)
        
        # *Response_10* updates
        if Response_10.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Response_10.frameNStart = frameN  # exact frame index
            Response_10.tStart = t  # local t and not account for scr refresh
            Response_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_10.started')
            Response_10.setAutoDraw(True)
        if Response_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_10.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Response_10.tStop = t  # not accounting for scr refresh
                Response_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_10.stopped')
                Response_10.setAutoDraw(False)
        
        # *Response_11* updates
        if Response_11.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Response_11.frameNStart = frameN  # exact frame index
            Response_11.tStart = t  # local t and not account for scr refresh
            Response_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_11.started')
            Response_11.setAutoDraw(True)
        if Response_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_11.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Response_11.tStop = t  # not accounting for scr refresh
                Response_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_11.stopped')
                Response_11.setAutoDraw(False)
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_4.started')
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_4.stopped')
                polygon_4.setAutoDraw(False)
        
        # *Delay_4* updates
        if Delay_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Delay_4.frameNStart = frameN  # exact frame index
            Delay_4.tStart = t  # local t and not account for scr refresh
            Delay_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Delay_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Delay_4.started')
            Delay_4.setAutoDraw(True)
        if Delay_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Delay_4.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Delay_4.tStop = t  # not accounting for scr refresh
                Delay_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Delay_4.stopped')
                Delay_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_4" ---
    for thisComponent in trial_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord_4.status != FINISHED:
        etRecord_4.status = FINISHED
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials_4'


# --- Prepare to start Routine "baseline" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
baselineComponents = []
for thisComponent in baselineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "baseline" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "baseline" ---
for thisComponent in baselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "baseline" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
