#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Fri Mar 10 12:28:44 2023
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
from math import atan2, degrees

# random.uniform? or nonparametric 

# MONKEYS WERE REWARDED DO WE NEED TO REWARD SIGNAL CORRECT?
# TIMING OF DELAY

#Monkeys were trained to sit comfortably in a primate chair inside a sound 
#attenuating behavioral testing booth. They were seated 
#50 cm 
#away from a LCD monitor with a 144-Hz refresh rate (ASUS, Taiwan). 
# (fixation window radius: 2 to 3 visual degrees) 
#cued item together with either one or two distractors 
#presented at the same eccentricity (3° to 8°), 
#but different visual quadrants #as the cued object.

#The position of the cued object and the distractors were 
#always randomly chosen. Monkeys were rewarded with a few drops of diluted 
#juice if they performed a saccade toward the cued item. Behavioral performance 
#was high for each of the monkeys (monkey S: 77% over 41 sessions, monkey L: 
#75% over 30 sessions). Monkeys were trained on this task using a library 
#of 22 sample images. For recordings, we used a subset of these images (12), 
#choosing a total of 3 per session. Most sessions (65 out of 71) used the 3 
#objects depicted in Fig. 1: an orange, a green block, and a blue car.

# 12 delays = 12s
# 12 block = 36s
# 6/6 



trialNum = 9 # 9 trials * 4sec/trial = 36 sec + 12 sec baseline
#trialNum = 50 # long 
#trialNum = 5 # long - 50 

baseline_duration=12
blockNum = 12 
blockNum_count=0 

blockTypes = ["PRED","UNPRED","PRED","UNPRED", 
"PRED","UNPRED","PRED","UNPRED", 
"PRED","UNPRED","PRED","UNPRED"]

#delayTime= .5 
#delayTime_dist = .2
#etrecord_duration=6

# BASTOS 
# monitor_distance = 50 

# OP4
monitor_distance = 54 
monitor_distance = 172

#fmIR? 


fixation_degrees = 2.5 
ecc_upper_deg = 8
ecc_lower_deg = 3 
# fixation radius using monitor distance and fixation degree 2.5 (2 to 3?)
fixation_radius_cm = monitor_distance * tan(fixation_degrees*pi/180)

# calc the x and y components of that diameter 
fixation_x = fixation_radius_cm*2 * cos(45*pi/180)
fixation_y = fixation_radius_cm*2 * sin(45*pi/180)

print(fixation_radius_cm, fixation_x, fixation_y)

eccentricity_upper_range_cm = monitor_distance * tan(ecc_upper_deg*pi/180) 
eccentricity_lower_range_cm = monitor_distance * tan(ecc_lower_deg*pi/180)

#54 upper = 7.58
#54 lower = 2.83

ecc = (eccentricity_upper_range_cm - eccentricity_lower_range_cm)
center_ecc = eccentricity_lower_range_cm + (ecc /2)

center_x_UR = center_ecc * cos(45*pi/180)
center_y_UR = center_ecc * sin(45*pi/180)

center_x_UL = center_ecc * cos(135*pi/180)
center_y_UL = center_ecc * sin(135*pi/180)

center_x_LR = center_ecc * cos(225*pi/180)
center_y_LR = center_ecc * sin(225*pi/180)

center_x_LL = center_ecc * cos(315*pi/180)
center_y_LL = center_ecc * sin(315*pi/180)

pos = [[center_x_UR,center_y_UR],[center_x_UL,center_y_UL],
        [center_x_LR,center_y_LR],[center_x_LL,center_y_LL]]

height = ecc * sin(45*pi/180)
width = ecc * cos(45*pi/180)

#responseImage_size = (4,4)
responseImage_size = (width,height)

print(monitor_distance, eccentricity_upper_range_cm, 
            eccentricity_lower_range_cm, ecc, center_ecc)
# 54 
# 7.589205073929137 2.830020081284225 
# 4.759184992644912 2.379592496322456
print(pos)
print("height: {} width: {}".format(height, width))



myCount1 = 0 
myCount2 = 0 
myCount3 = 0 
myCount4 = 0 
myCount5 = 0 
myCount6 = 0 
myCount7 = 0 
myCount8 = 0 
myCount9 = 0 
myCount10 = 0 
myCount11 = 0 
myCount12 = 0 

#pos=[(.25,.25),(-.25,.25),(.25,-.25),(-.25,-.25)]
#locations = ['topright','topleft','bottomright','bottomleft']
pictures  = ['images/picture_1.png','images/picture_2.png','images/picture_3.png']

# log params 
params = {"height":height, "width":width}

trial_list = []
block_list = [] 
block_paths = []

#blockNum = len(blockTypes)
testing = False 

trial_count = 0 
for i_block in range(blockNum):
    blockType = blockTypes[i_block]
    
    
    if blockType == "PRED": 
        stimImage_i = random.randrange(0,3)
        stimImage = pictures[stimImage_i]


    for i in range(trialNum):
        # 
        
        
        delayTime = random.uniform(0.5, 1.2)
        
        cue_onset=0
        cue_dur=1
        
        circle_onset=0 
        circle_dur=1+delayTime-.25 
        
        delay_onset=1
        delay_dur=delayTime
        
        resp_onset=1+delayTime  
        resp_dur=2-delayTime
        
        rest_onset=3
        rest_dur=1
        
        cross_onset=3
        cross_dir=1 
        



        if blockType == "UNPRED": 
            stimImage_i = random.randrange(0,3)
            stimImage = pictures[stimImage_i]

        print("{} {} {} {}".format(blockType, i_block, i, stimImage_i ))
        
      
        
        location_ind = [0,1,2,3]
        picture_ind =  [0,1,2]
        pos_ind = [0,1,2,3]

        random.shuffle(pos)
        print(pos)

        #random.shuffle(location_ind)
        #random.shuffle(picture_ind)
        #random.shuffle(pos_ind)

        responseImage1              = pictures[picture_ind[0]]
        responseImage1_i            = picture_ind[0]
        #responseImage1_location     = locations[location_ind[0]]
        #responseImage1_location_i   = location_ind[0]
        responseImage1_pos          = pos[0]
        responseImage1_X            = pos[0][0]
        responseImage1_Y            = pos[0][1]

        #responseImage1_pos_ind      = pos_ind[0]

        responseImage2              = pictures[picture_ind[1]]
        responseImage2_i            = picture_ind[1]
        #responseImage2_location     = locations[location_ind[1]]
        #responseImage2_location_i   = location_ind[1]
        responseImage2_pos          = pos[1]
        responseImage2_X            = pos[1][0]
        responseImage2_Y            = pos[1][1]

        #responseImage2_pos_ind      = pos_ind[1]

        responseImage3              = pictures[picture_ind[2]]
        responseImage3_i            = picture_ind[2]
        #responseImage3_location     = locations[location_ind[2]]
        #responseImage3_location_i   = location_ind[2]
        responseImage3_pos          = pos[2]
        responseImage3_X            = pos[2][0]
        responseImage3_Y            = pos[2][1]

        #responseImage3_pos_ind      = pos_ind[2]

        


        app = { "trial_count": trial_count, 
        "blockType":blockType, "blockNum":blockNum, 
        "delay_time":delayTime, 
        "stimImage_i":stimImage_i, "stimImage":stimImage, 
        "responseImage1":responseImage1, 
        "responseImage1_i":responseImage1_i, 
        "responseImage1_pos":responseImage1_pos,
        "responseImage1_X":responseImage1_X,
        "responseImage1_Y":responseImage1_Y,

        "responseImage2":responseImage2, 
        "responseImage2_i":responseImage2_i, 
        "responseImage2_pos":responseImage2_pos, 
        "responseImage2_X":responseImage2_X, 
        "responseImage2_Y":responseImage2_Y, 

        "responseImage3":responseImage3, 
        "responseImage3_i":responseImage3_i, 
        "responseImage3_pos":responseImage3_pos, 
        "responseImage3_X":responseImage3_X, 
        "responseImage3_Y":responseImage3_Y, 

        "cue_onset":cue_onset,
        "cue_dur":cue_dur, 
        "delay_onset":delay_onset,
        "delay_dur":delay_dur, 
        "resp_onset":resp_onset,  
        "resp_dur":resp_dur,
        "rest_onset":rest_onset, 
        "rest_dur":rest_dur,
        "circle_dur":circle_dur, 
        "circle_onset":circle_onset
        }
        
        trial_count += 1 
        
        trial_list.append(app)
    block_list.append(trial_list) 
    trial_list = [] 
    

trial_list1 = block_list[0]
trial_list2 = block_list[1]
trial_list3 = block_list[2]
trial_list4 = block_list[3]
trial_list5 = block_list[4]
trial_list6 = block_list[5]
trial_list7 = block_list[6]
trial_list8 = block_list[7]
trial_list9 = block_list[8]
trial_list10 = block_list[9]
trial_list11 = block_list[10]
trial_list12 = block_list[11]

thisTrial = trial_list1[0]
thisTrial_2 = trial_list2[0]
thisTrial_3 = trial_list3[0]
thisTrial_4 = trial_list4[0]
thisTrial_5 = trial_list5[0]
thisTrial_6 = trial_list6[0]
thisTrial_7 = trial_list7[0]
thisTrial_8 = trial_list8[0]
thisTrial_9 = trial_list9[0]
thisTrial_10 = trial_list10[0]
thisTrial_11 = trial_list11[0]
thisTrial_12 = trial_list12[0]







# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'DMS_BEST_eyetracking_DAN_base_12-36_looped_10minWORKING'  # from the Builder filename that created this script
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
    originPath='/Users/richard/Visual_Attention/DMS_BEST_eyetracking_DAN_base_12-36_looped_10minWORKING_lastrun.py',
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
    size=[1440, 900], fullscr=True, screen=0, 
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
        'blink':('LEFT_BUTTON', 'MIDDLE_BUTTON', 'RIGHT_BUTTON'),
        'saccade_threshold': 0.5,
    }
}
ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='DMS_BEST_eyetracking_DAN_base_12-36_looped_10minWORKING', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='event')

# --- Initialize components for Routine "eyelink" ---

# --- Initialize components for Routine "codeStart" ---
# Run 'Begin Experiment' code from code

dirpath = _thisDir + os.sep + u'data/%s/%s/%s' % (expInfo['participant'], expName, expInfo['date'])
os.makedirs(dirpath, exist_ok=True)

block_paths = []

dfs = []
for i_block in range(len(blockTypes)): 
    block = block_list[i_block]
    blockType = blockTypes[i_block]
    
    df = pd.DataFrame(block)
    outfile = "{}/{}-{}_12-36.csv".format(dirpath, i_block, blockType)
    df.to_csv(outfile)
    print("outfile: {}".format(outfile))
    dfs.append(df)
    
    block_paths.append(outfile)

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
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "codeEnd" ---

# --- Initialize components for Routine "trial" ---
etRecord = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample = visual.ImageStim(
    win=win,
    name='sample', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(fixation_x, fixation_y),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Delay = visual.ShapeStim(
    win=win, name='Delay',
    size=(0.01, 0.01), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
Response_1 = visual.ImageStim(
    win=win,
    name='Response_1', units='cm', 
    image=thisTrial["responseImage1"], mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_2 = visual.ImageStim(
    win=win,
    name='Response_2', units='cm', 
    image=thisTrial["responseImage2"], mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
Response_3 = visual.ImageStim(
    win=win,
    name='Response_3', units='cm', 
    image=thisTrial["responseImage3"], mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)

# --- Initialize components for Routine "baseline" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "iter_block" ---

# --- Initialize components for Routine "baseline" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "codeSave" ---

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "eyelink" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
eyelinkComponents = []
for thisComponent in eyelinkComponents:
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

# --- Run Routine "eyelink" ---
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
    for thisComponent in eyelinkComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "eyelink" ---
for thisComponent in eyelinkComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "eyelink" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
baselineComponents = [text_2]
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
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + baseline_duration-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.stopped')
            text_2.setAutoDraw(False)
    
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
blocks = data.TrialHandler(nReps=blockNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=trialNum, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(block_paths[blockNum_count]),
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
            # Run 'Each Frame' code from code_2
            #print(thisTrial["responseImage1_pos"])
            
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
        # Run 'End Routine' code from code_2
        myCount1 += 1
        
        if myCount1 >= trialNum:
            trials.finished = True
            myCount1 = 0 
         
        #print(myCount1) 
        
        #for k in thisTrial.keys(): 
        #    thisExp.addData(k, thisTrial[k])
        #    
        thisExp.nextEntry()
        
        # the Routine "codeEnd" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        sample.setImage(thisTrial["stimImage"])
        Response_1.setPos([float(thisTrial["responseImage1_X"]), float(thisTrial["responseImage1_Y"])])
        Response_2.setPos([float(thisTrial["responseImage2_X"]), float(thisTrial["responseImage2_Y"])])
        Response_3.setPos([float(thisTrial["responseImage3_X"]), float(thisTrial["responseImage3_Y"])])
        # keep track of which components have finished
        trialComponents = [etRecord, sample, Delay, Response_1, Response_2, Response_3, polygon]
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
        while continueRoutine:
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
                if tThisFlipGlobal > etRecord.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    etRecord.tStop = t  # not accounting for scr refresh
                    etRecord.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('etRecord.stopped', t)
                    etRecord.status = FINISHED
            
            # *sample* updates
            if sample.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
                if tThisFlipGlobal > Delay.tStartRefresh + thisTrial['circle_dur'] -frameTolerance:
                    # keep track of stop time/frame for later
                    Delay.tStop = t  # not accounting for scr refresh
                    Delay.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Delay.stopped')
                    Delay.setAutoDraw(False)
            
            # *Response_1* updates
            if Response_1.status == NOT_STARTED and tThisFlip >= thisTrial['resp_onset']-frameTolerance:
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
                if tThisFlipGlobal > Response_1.tStartRefresh + thisTrial['resp_dur']-frameTolerance:
                    # keep track of stop time/frame for later
                    Response_1.tStop = t  # not accounting for scr refresh
                    Response_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Response_1.stopped')
                    Response_1.setAutoDraw(False)
            
            # *Response_2* updates
            if Response_2.status == NOT_STARTED and tThisFlip >= thisTrial['resp_onset']-frameTolerance:
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
                if tThisFlipGlobal > Response_2.tStartRefresh + thisTrial['resp_dur']-frameTolerance:
                    # keep track of stop time/frame for later
                    Response_2.tStop = t  # not accounting for scr refresh
                    Response_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Response_2.stopped')
                    Response_2.setAutoDraw(False)
            
            # *Response_3* updates
            if Response_3.status == NOT_STARTED and tThisFlip >= thisTrial['resp_onset']-frameTolerance:
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
                if tThisFlipGlobal > Response_3.tStartRefresh + thisTrial['resp_dur']-frameTolerance:
                    # keep track of stop time/frame for later
                    Response_3.tStop = t  # not accounting for scr refresh
                    Response_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Response_3.stopped')
                    Response_3.setAutoDraw(False)
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
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
                if tThisFlipGlobal > polygon.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.stopped')
                    polygon.setAutoDraw(False)
            
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
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed trialNum repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials.saveAsText(filename + 'trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "baseline" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    baselineComponents = [text_2]
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
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + baseline_duration-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                text_2.setAutoDraw(False)
        
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
    
    # --- Prepare to start Routine "iter_block" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    iter_blockComponents = []
    for thisComponent in iter_blockComponents:
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
    
    # --- Run Routine "iter_block" ---
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
        for thisComponent in iter_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "iter_block" ---
    for thisComponent in iter_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_16
    blockNum_count += 1 
    # the Routine "iter_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed blockNum repeats of 'blocks'

# get names of stimulus parameters
if blocks.trialList in ([], [None], None):
    params = []
else:
    params = blocks.trialList[0].keys()
# save data for this loop
blocks.saveAsExcel(filename + '.xlsx', sheetName='blocks',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
blocks.saveAsText(filename + 'blocks.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "baseline" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
baselineComponents = [text_2]
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
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + baseline_duration-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.stopped')
            text_2.setAutoDraw(False)
    
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

# --- Prepare to start Routine "codeSave" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
codeSaveComponents = []
for thisComponent in codeSaveComponents:
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

# --- Run Routine "codeSave" ---
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
    for thisComponent in codeSaveComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "codeSave" ---
for thisComponent in codeSaveComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "codeSave" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# Run 'End Experiment' code from code_7
thisExp.saveAsPickle(filename+"_thisExp.pkl")

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
