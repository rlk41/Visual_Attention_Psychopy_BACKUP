#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Tue Mar  7 11:42:10 2023
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

# Run 'Before Experiment' code from code

import random
import pandas as pd 



pos=[(.25,.25),(-.25,.25),(.25,-.25),(-.25,-.25)]
locations = ['topright','topleft','bottomright','bottomleft']
pictures  = ['images/picture_1.png','images/picture_2.png','images/picture_3.png']

trial_list = []
block_list = [] 

blockTypes = ["UNPRED","PRED","UNPRED","PRED"]

delayTime= .5 
delayTime_dist = .2

trialNum = 5
blockNum = len(blockTypes)

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




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'DMS_v2b'  # from the Builder filename that created this script
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
    originPath='/Users/kleinrl/Visual_Attention/DMS_v2b_lastrun.py',
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
    monitor='testMonitor', color='black', colorSpace='rgb',
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

# --- Initialize components for Routine "baseline" ---

# --- Initialize components for Routine "trial" ---
sample = visual.ImageStim(
    win=win,
    name='sample', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Response_1 = visual.ImageStim(
    win=win,
    name='Response_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[trial_dict["responseImage1_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_2 = visual.ImageStim(
    win=win,
    name='Response_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[trial_dict["responseImage2_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_3 = visual.ImageStim(
    win=win,
    name='Response_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[trial_dict["responseImage3_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
Delay = visual.ShapeStim(
    win=win, name='Delay',
    size=(0.01, 0.01), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "baseline" ---

# --- Initialize components for Routine "trial" ---
sample = visual.ImageStim(
    win=win,
    name='sample', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Response_1 = visual.ImageStim(
    win=win,
    name='Response_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[trial_dict["responseImage1_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_2 = visual.ImageStim(
    win=win,
    name='Response_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[trial_dict["responseImage2_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_3 = visual.ImageStim(
    win=win,
    name='Response_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[trial_dict["responseImage3_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
Delay = visual.ShapeStim(
    win=win, name='Delay',
    size=(0.01, 0.01), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "baseline" ---

# --- Initialize components for Routine "trial" ---
sample = visual.ImageStim(
    win=win,
    name='sample', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Response_1 = visual.ImageStim(
    win=win,
    name='Response_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[trial_dict["responseImage1_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_2 = visual.ImageStim(
    win=win,
    name='Response_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[trial_dict["responseImage2_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_3 = visual.ImageStim(
    win=win,
    name='Response_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[trial_dict["responseImage3_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
Delay = visual.ShapeStim(
    win=win, name='Delay',
    size=(0.01, 0.01), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "baseline" ---

# --- Initialize components for Routine "trial" ---
sample = visual.ImageStim(
    win=win,
    name='sample', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Response_1 = visual.ImageStim(
    win=win,
    name='Response_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[trial_dict["responseImage1_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_2 = visual.ImageStim(
    win=win,
    name='Response_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[trial_dict["responseImage2_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_3 = visual.ImageStim(
    win=win,
    name='Response_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[trial_dict["responseImage3_pos"]], size=(0.125, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
Delay = visual.ShapeStim(
    win=win, name='Delay',
    size=(0.01, 0.01), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "baseline" ---

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 
# define target for calibration
calibrationTarget = visual.TargetStim(win, 
    name='calibrationTarget',
    radius=0.01, fillColor='', borderColor='black', lineWidth=2.0,
    innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
    colorSpace='rgb', units=None
)
# define parameters for calibration
calibration = hardware.eyetracker.EyetrackerCalibration(win, 
    eyetracker, calibrationTarget,
    units=None, colorSpace='rgb',
    progressMode='time', targetDur=1.5, expandScale=1.5,
    targetLayout='NINE_POINTS', randomisePos=True, textColor='white',
    movementAnimation=True, targetDelay=1.0
)
# run calibration
calibration.run()
# clear any keypresses from during calibration so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# define target for validation
validationTarget = visual.TargetStim(win, 
    name='validationTarget',
    radius=0.01, fillColor='', borderColor='black', lineWidth=2.0,
    innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
    colorSpace='rgb', units=None
)
# define parameters for validation
validation = iohub.ValidationProcedure(win,
    target=validationTarget,
    gaze_cursor='green', 
    positions='NINE_POINTS', randomize_positions=True,
    expand_scale=1.5, target_duration=1.5,
    enable_position_animation=True, target_delay=1.0,
    progress_on_key=None, text_color='auto',
    show_results_screen=True, save_results_screen=False,
    color_space='rgb', unit_type=None
)
# run validation
validation.run()
# clear any keypresses from during validation so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "validation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "codeStart" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code
trial_dict = trial_list[trial_count]

print(trial_count)
print(trial_dict)
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
  
for k in thisTrial.keys():
    thisExp.addData(k, trial_dict[k])

    

# the Routine "codeStart" was not non-slip safe, so reset the non-slip timer
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
    trialList=[None],
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
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample.setImage(trial_list[trial_count]["stimImage"])
    Response_1.setImage(trial_dict["responseImage1"])
    Response_2.setImage(trial_dict["responseImage2"])
    Response_3.setImage(trial_dict["responseImage3"])
    # keep track of which components have finished
    trialComponents = [sample, Response_1, Response_2, Response_3, polygon, Delay]
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
    trialList=[None],
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
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample.setImage(trial_list[trial_count]["stimImage"])
    Response_1.setImage(trial_dict["responseImage1"])
    Response_2.setImage(trial_dict["responseImage2"])
    Response_3.setImage(trial_dict["responseImage3"])
    # keep track of which components have finished
    trialComponents = [sample, Response_1, Response_2, Response_3, polygon, Delay]
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
    trialList=[None],
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
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample.setImage(trial_list[trial_count]["stimImage"])
    Response_1.setImage(trial_dict["responseImage1"])
    Response_2.setImage(trial_dict["responseImage2"])
    Response_3.setImage(trial_dict["responseImage3"])
    # keep track of which components have finished
    trialComponents = [sample, Response_1, Response_2, Response_3, polygon, Delay]
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
    trialList=[None],
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
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample.setImage(trial_list[trial_count]["stimImage"])
    Response_1.setImage(trial_dict["responseImage1"])
    Response_2.setImage(trial_dict["responseImage2"])
    Response_3.setImage(trial_dict["responseImage3"])
    # keep track of which components have finished
    trialComponents = [sample, Response_1, Response_2, Response_3, polygon, Delay]
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
