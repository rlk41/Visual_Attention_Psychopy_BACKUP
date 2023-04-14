#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Fri Mar 10 03:10:21 2023
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

blockNum = len(blockTypes)
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
expName = 'DMS_BEST_eyetracking_DAN_base_12-36'  # from the Builder filename that created this script
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
    originPath='/Users/richard/Visual_Attention/DMS_BEST_eyetracking_DAN_base_12-36.py',
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
        'blink':('LEFT_BUTTON', 'MIDDLE_BUTTON', 'RIGHT_BUTTON'),
        'saccade_threshold': 0.5,
    }
}
ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='DMS_BEST_eyetracking_DAN_base_12-36', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='event')

# --- Initialize components for Routine "eyelink" ---

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
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_2 = visual.ImageStim(
    win=win,
    name='Response_2', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
Response_3 = visual.ImageStim(
    win=win,
    name='Response_3', units='cm', 
    image='sin', mask=None, anchor='center',
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

# --- Initialize components for Routine "codeEnd_2" ---

# --- Initialize components for Routine "trial_2" ---
etRecord_2 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample_2 = visual.ImageStim(
    win=win,
    name='sample_2', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(fixation_x,fixation_y),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response = visual.ImageStim(
    win=win,
    name='Response', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_4 = visual.ImageStim(
    win=win,
    name='Response_4', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_5 = visual.ImageStim(
    win=win,
    name='Response_5', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
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
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "codeEnd_3" ---

# --- Initialize components for Routine "trial_3" ---
etRecord_3 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample_3 = visual.ImageStim(
    win=win,
    name='sample_3', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(fixation_x,fixation_y),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_6 = visual.ImageStim(
    win=win,
    name='Response_6', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_7 = visual.ImageStim(
    win=win,
    name='Response_7', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_8 = visual.ImageStim(
    win=win,
    name='Response_8', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
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
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "codeEnd_4" ---

# --- Initialize components for Routine "trial_4" ---
etRecord_4 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample_4 = visual.ImageStim(
    win=win,
    name='sample_4', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(fixation_x,fixation_y),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_9 = visual.ImageStim(
    win=win,
    name='Response_9', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_10 = visual.ImageStim(
    win=win,
    name='Response_10', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_11 = visual.ImageStim(
    win=win,
    name='Response_11', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
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
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "codeEnd_5" ---

# --- Initialize components for Routine "trial_5" ---
etRecord_5 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample_5 = visual.ImageStim(
    win=win,
    name='sample_5', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(fixation_x,fixation_y),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_12 = visual.ImageStim(
    win=win,
    name='Response_12', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_13 = visual.ImageStim(
    win=win,
    name='Response_13', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_14 = visual.ImageStim(
    win=win,
    name='Response_14', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
polygon_5 = visual.ShapeStim(
    win=win, name='polygon_5', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Delay_5 = visual.ShapeStim(
    win=win, name='Delay_5',
    size=(0.01, 0.01), vertices='circle',
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

# --- Initialize components for Routine "codeEnd_6" ---

# --- Initialize components for Routine "trial_6" ---
etRecord_6 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample_6 = visual.ImageStim(
    win=win,
    name='sample_6', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(fixation_x,fixation_y),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_15 = visual.ImageStim(
    win=win,
    name='Response_15', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_16 = visual.ImageStim(
    win=win,
    name='Response_16', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_17 = visual.ImageStim(
    win=win,
    name='Response_17', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
polygon_6 = visual.ShapeStim(
    win=win, name='polygon_6', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Delay_6 = visual.ShapeStim(
    win=win, name='Delay_6',
    size=(0.01, 0.01), vertices='circle',
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

# --- Initialize components for Routine "codeEnd_7" ---

# --- Initialize components for Routine "trial_7" ---
etRecord_7 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample_7 = visual.ImageStim(
    win=win,
    name='sample_7', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(fixation_x,fixation_y),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_18 = visual.ImageStim(
    win=win,
    name='Response_18', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_19 = visual.ImageStim(
    win=win,
    name='Response_19', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_20 = visual.ImageStim(
    win=win,
    name='Response_20', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
polygon_7 = visual.ShapeStim(
    win=win, name='polygon_7', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Delay_7 = visual.ShapeStim(
    win=win, name='Delay_7',
    size=(0.01, 0.01), vertices='circle',
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

# --- Initialize components for Routine "codeEnd_8" ---

# --- Initialize components for Routine "trial_8" ---
etRecord_8 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample_8 = visual.ImageStim(
    win=win,
    name='sample_8', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(fixation_x,fixation_y),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_21 = visual.ImageStim(
    win=win,
    name='Response_21', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_22 = visual.ImageStim(
    win=win,
    name='Response_22', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_23 = visual.ImageStim(
    win=win,
    name='Response_23', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
polygon_8 = visual.ShapeStim(
    win=win, name='polygon_8', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Delay_8 = visual.ShapeStim(
    win=win, name='Delay_8',
    size=(0.01, 0.01), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
etrecord_pos_8 = visual.ShapeStim(
    win=win, name='etrecord_pos_8',
    size=(0.01, 0.01), vertices='triangle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)

# --- Initialize components for Routine "baseline" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "codeEnd_9" ---

# --- Initialize components for Routine "trial_9" ---
etRecord_9 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample_9 = visual.ImageStim(
    win=win,
    name='sample_9', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(fixation_x,fixation_y),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_24 = visual.ImageStim(
    win=win,
    name='Response_24', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_25 = visual.ImageStim(
    win=win,
    name='Response_25', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_26 = visual.ImageStim(
    win=win,
    name='Response_26', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
polygon_9 = visual.ShapeStim(
    win=win, name='polygon_9', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Delay_9 = visual.ShapeStim(
    win=win, name='Delay_9',
    size=(0.01, 0.01), vertices='circle',
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

# --- Initialize components for Routine "codeEnd_10" ---

# --- Initialize components for Routine "trial_10" ---
etRecord_10 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample_10 = visual.ImageStim(
    win=win,
    name='sample_10', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(fixation_x,fixation_y),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_27 = visual.ImageStim(
    win=win,
    name='Response_27', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_28 = visual.ImageStim(
    win=win,
    name='Response_28', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_29 = visual.ImageStim(
    win=win,
    name='Response_29', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
polygon_10 = visual.ShapeStim(
    win=win, name='polygon_10', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Delay_10 = visual.ShapeStim(
    win=win, name='Delay_10',
    size=(0.01, 0.01), vertices='circle',
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

# --- Initialize components for Routine "codeEnd_11" ---

# --- Initialize components for Routine "trial_11" ---
etRecord_11 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample_11 = visual.ImageStim(
    win=win,
    name='sample_11', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(fixation_x,fixation_y),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_30 = visual.ImageStim(
    win=win,
    name='Response_30', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_31 = visual.ImageStim(
    win=win,
    name='Response_31', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_32 = visual.ImageStim(
    win=win,
    name='Response_32', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
polygon_11 = visual.ShapeStim(
    win=win, name='polygon_11', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Delay_11 = visual.ShapeStim(
    win=win, name='Delay_11',
    size=(0.01, 0.01), vertices='circle',
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

# --- Initialize components for Routine "codeEnd_12" ---

# --- Initialize components for Routine "trial_12" ---
etRecord_12 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
sample_12 = visual.ImageStim(
    win=win,
    name='sample_12', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(fixation_x,fixation_y),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Response_33 = visual.ImageStim(
    win=win,
    name='Response_33', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response_34 = visual.ImageStim(
    win=win,
    name='Response_34', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_35 = visual.ImageStim(
    win=win,
    name='Response_35', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=responseImage_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
polygon_12 = visual.ShapeStim(
    win=win, name='polygon_12', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Delay_12 = visual.ShapeStim(
    win=win, name='Delay_12',
    size=(0.01, 0.01), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)

# --- Initialize components for Routine "baselineEnd" ---
text_3 = visual.TextStim(win=win, name='text_3',
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
trials = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=trial_list1, #data.importConditions("{}/{}-{}.csv".format(dirpath, 1, "UNPRED")),
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
    Response_1.setImage(thisTrial["responseImage1"])
    Response_2.setPos([float(thisTrial["responseImage2_X"]), float(thisTrial["responseImage2_Y"])])
    Response_2.setImage(thisTrial["responseImage2"])
    Response_3.setPos([float(thisTrial["responseImage3_X"]), float(thisTrial["responseImage3_Y"])])
    Response_3.setImage(thisTrial["responseImage3"])
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

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=trial_list2, #data.importConditions("{}/{}-{}.csv".format(dirpath, 1, "UNPRED")),
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
    
    # --- Prepare to start Routine "codeEnd_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    codeEnd_2Components = []
    for thisComponent in codeEnd_2Components:
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
    
    # --- Run Routine "codeEnd_2" ---
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
        for thisComponent in codeEnd_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd_2" ---
    for thisComponent in codeEnd_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_3
    myCount2 += 1
    
    if myCount2 > trialNum:
        trials_2.finished = True
     
    #
    #print(myCount2)
    
    #for k in thisTrial_2.keys(): 
    #    thisExp.addData(k, thisTrial_2[k])
    # 
    thisExp.nextEntry()
    
    # the Routine "codeEnd_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_2.setImage(thisTrial_2["stimImage"])
    Response.setPos([thisTrial_2["responseImage1_pos"]])
    Response.setImage(thisTrial_2["responseImage1"])
    Response_4.setPos([thisTrial_2["responseImage2_pos"]])
    Response_4.setImage(thisTrial_2["responseImage2"])
    Response_5.setPos([thisTrial_2["responseImage3_pos"]])
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
    while continueRoutine:
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
            if tThisFlipGlobal > etRecord_2.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_2.tStop = t  # not accounting for scr refresh
                etRecord_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_2.stopped', t)
                etRecord_2.status = FINISHED
        
        # *sample_2* updates
        if sample_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
        if Response.status == NOT_STARTED and tThisFlip >= thisTrial_2['resp_onset']-frameTolerance:
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
            if tThisFlipGlobal > Response.tStartRefresh + thisTrial_2['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response.tStop = t  # not accounting for scr refresh
                Response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response.stopped')
                Response.setAutoDraw(False)
        
        # *Response_4* updates
        if Response_4.status == NOT_STARTED and tThisFlip >= thisTrial_2['resp_onset']-frameTolerance:
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
            if tThisFlipGlobal > Response_4.tStartRefresh + thisTrial_2['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response_4.tStop = t  # not accounting for scr refresh
                Response_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_4.stopped')
                Response_4.setAutoDraw(False)
        
        # *Response_5* updates
        if Response_5.status == NOT_STARTED and tThisFlip >= thisTrial_2['resp_onset']-frameTolerance:
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
            if tThisFlipGlobal > Response_5.tStartRefresh + thisTrial_2['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response_5.tStop = t  # not accounting for scr refresh
                Response_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_5.stopped')
                Response_5.setAutoDraw(False)
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
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
            if tThisFlipGlobal > polygon_2.tStartRefresh + 1-frameTolerance:
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
            if tThisFlipGlobal > Delay_2.tStartRefresh + thisTrial_2['circle_dur']-frameTolerance:
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
    # the Routine "trial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
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

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=trial_list3, #data.importConditions("{}/{}-{}.csv".format(dirpath, 2, "PRED")),
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
    
    # --- Prepare to start Routine "codeEnd_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    codeEnd_3Components = []
    for thisComponent in codeEnd_3Components:
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
    
    # --- Run Routine "codeEnd_3" ---
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
        for thisComponent in codeEnd_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd_3" ---
    for thisComponent in codeEnd_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_4
    myCount3 += 1
    
    if myCount3 > trialNum:
        trials_3.finished = True
     
    
    print(myCount3)
    
    #for k in thisTrial_3.keys(): 
    #    thisExp.addData(k, thisTrial_3[k])
    
    thisExp.nextEntry()
    
    # the Routine "codeEnd_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_3.setImage(thisTrial_3["stimImage"])
    Response_6.setPos([thisTrial_3["responseImage1_pos"]])
    Response_6.setImage(thisTrial_3["responseImage1"])
    Response_7.setPos([thisTrial_3["responseImage2_pos"]])
    Response_7.setImage(thisTrial_3["responseImage2"])
    Response_8.setPos([thisTrial_3["responseImage3_pos"]])
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
    while continueRoutine:
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
            if tThisFlipGlobal > etRecord_3.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_3.tStop = t  # not accounting for scr refresh
                etRecord_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_3.stopped', t)
                etRecord_3.status = FINISHED
        
        # *sample_3* updates
        if sample_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
        if Response_6.status == NOT_STARTED and tThisFlip >= thisTrial_3['resp_onset']-frameTolerance:
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
            if tThisFlipGlobal > Response_6.tStartRefresh + thisTrial_3['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response_6.tStop = t  # not accounting for scr refresh
                Response_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_6.stopped')
                Response_6.setAutoDraw(False)
        
        # *Response_7* updates
        if Response_7.status == NOT_STARTED and tThisFlip >= thisTrial_3['resp_onset']-frameTolerance:
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
            if tThisFlipGlobal > Response_7.tStartRefresh + thisTrial_3['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response_7.tStop = t  # not accounting for scr refresh
                Response_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_7.stopped')
                Response_7.setAutoDraw(False)
        
        # *Response_8* updates
        if Response_8.status == NOT_STARTED and tThisFlip >= thisTrial_3['resp_onset']-frameTolerance:
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
            if tThisFlipGlobal > Response_8.tStartRefresh + thisTrial_3['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response_8.tStop = t  # not accounting for scr refresh
                Response_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_8.stopped')
                Response_8.setAutoDraw(False)
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
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
            if tThisFlipGlobal > polygon_3.tStartRefresh + 1-frameTolerance:
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
            if tThisFlipGlobal > Delay_3.tStartRefresh + thisTrial_3['circle_dur']-frameTolerance:
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
    # the Routine "trial_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials_3'

# get names of stimulus parameters
if trials_3.trialList in ([], [None], None):
    params = []
else:
    params = trials_3.trialList[0].keys()
# save data for this loop
trials_3.saveAsExcel(filename + '.xlsx', sheetName='trials_3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_3.saveAsText(filename + 'trials_3.csv', delim=',',
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

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=trial_list4, #data.importConditions("{}/{}-{}.csv".format(dirpath, 3, "UNPRED")),
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
    
    # --- Prepare to start Routine "codeEnd_4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    codeEnd_4Components = []
    for thisComponent in codeEnd_4Components:
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
    
    # --- Run Routine "codeEnd_4" ---
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
        for thisComponent in codeEnd_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd_4" ---
    for thisComponent in codeEnd_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_5
    
    myCount4 += 1
    if myCount4 > trialNum:
        trials_4.finished = True
     
    
    print(myCount4)
    
    #for k in thisTrial_4.keys(): 
    #    thisExp.addData(k, thisTrial_4[k])
    #    
    thisExp.nextEntry()
    
    # the Routine "codeEnd_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_4.setImage(thisTrial_4["stimImage"])
    Response_9.setPos([thisTrial_4["responseImage1_pos"]])
    Response_9.setImage(thisTrial_4["responseImage1"])
    Response_10.setPos([thisTrial_4["responseImage2_pos"]])
    Response_10.setImage(thisTrial_4["responseImage2"])
    Response_11.setPos([thisTrial_4["responseImage3_pos"]])
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
    while continueRoutine:
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
            if tThisFlipGlobal > etRecord_4.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_4.tStop = t  # not accounting for scr refresh
                etRecord_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_4.stopped', t)
                etRecord_4.status = FINISHED
        
        # *sample_4* updates
        if sample_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
        if Response_9.status == NOT_STARTED and tThisFlip >= thisTrial_4['resp_onset']-frameTolerance:
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
            if tThisFlipGlobal > Response_9.tStartRefresh + thisTrial_4['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response_9.tStop = t  # not accounting for scr refresh
                Response_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_9.stopped')
                Response_9.setAutoDraw(False)
        
        # *Response_10* updates
        if Response_10.status == NOT_STARTED and tThisFlip >= thisTrial_4["resp_onset"]-frameTolerance:
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
            if tThisFlipGlobal > Response_10.tStartRefresh + thisTrial_4["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_10.tStop = t  # not accounting for scr refresh
                Response_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_10.stopped')
                Response_10.setAutoDraw(False)
        
        # *Response_11* updates
        if Response_11.status == NOT_STARTED and tThisFlip >= thisTrial_4["resp_onset"]-frameTolerance:
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
            if tThisFlipGlobal > Response_11.tStartRefresh + thisTrial_4["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_11.tStop = t  # not accounting for scr refresh
                Response_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_11.stopped')
                Response_11.setAutoDraw(False)
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
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
            if tThisFlipGlobal > polygon_4.tStartRefresh + 1-frameTolerance:
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
            if tThisFlipGlobal > Delay_4.tStartRefresh + thisTrial_4["circle_dur"]-frameTolerance:
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
    # the Routine "trial_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials_4'

# get names of stimulus parameters
if trials_4.trialList in ([], [None], None):
    params = []
else:
    params = trials_4.trialList[0].keys()
# save data for this loop
trials_4.saveAsExcel(filename + '.xlsx', sheetName='trials_4',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_4.saveAsText(filename + 'trials_4.csv', delim=',',
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

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=trial_list5, #data.importConditions("{}/{}-{}.csv".format(dirpath, 4, "PRED")),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "codeEnd_5" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    codeEnd_5Components = []
    for thisComponent in codeEnd_5Components:
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
    
    # --- Run Routine "codeEnd_5" ---
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
        for thisComponent in codeEnd_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd_5" ---
    for thisComponent in codeEnd_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_8
    
    myCount4 += 1
    if myCount5 > trialNum:
        trials_5.finished = True
     
    
    print(myCount5)
    
    #for k in thisTrial_5.keys(): 
    #    thisExp.addData(k, thisTrial_5[k])
    #    
    thisExp.nextEntry()
    
    # the Routine "codeEnd_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_5" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_5.setImage(thisTrial_5["stimImage"])
    Response_12.setPos([thisTrial_5["responseImage1_pos"]])
    Response_12.setImage(thisTrial_5["responseImage1"])
    Response_13.setPos([thisTrial_5["responseImage2_pos"]])
    Response_13.setImage(thisTrial_5["responseImage2"])
    Response_14.setPos([thisTrial_5["responseImage3_pos"]])
    Response_14.setImage(thisTrial_5["responseImage3"])
    # keep track of which components have finished
    trial_5Components = [etRecord_5, sample_5, Response_12, Response_13, Response_14, polygon_5, Delay_5]
    for thisComponent in trial_5Components:
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
    
    # --- Run Routine "trial_5" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRecord_5* updates
        if etRecord_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord_5.frameNStart = frameN  # exact frame index
            etRecord_5.tStart = t  # local t and not account for scr refresh
            etRecord_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord_5.started', t)
            etRecord_5.status = STARTED
        if etRecord_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord_5.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_5.tStop = t  # not accounting for scr refresh
                etRecord_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_5.stopped', t)
                etRecord_5.status = FINISHED
        
        # *sample_5* updates
        if sample_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sample_5.frameNStart = frameN  # exact frame index
            sample_5.tStart = t  # local t and not account for scr refresh
            sample_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sample_5.started')
            sample_5.setAutoDraw(True)
        if sample_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sample_5.tStop = t  # not accounting for scr refresh
                sample_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sample_5.stopped')
                sample_5.setAutoDraw(False)
        
        # *Response_12* updates
        if Response_12.status == NOT_STARTED and tThisFlip >= thisTrial_5['resp_onset']-frameTolerance:
            # keep track of start time/frame for later
            Response_12.frameNStart = frameN  # exact frame index
            Response_12.tStart = t  # local t and not account for scr refresh
            Response_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_12.started')
            Response_12.setAutoDraw(True)
        if Response_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_12.tStartRefresh + thisTrial_5['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response_12.tStop = t  # not accounting for scr refresh
                Response_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_12.stopped')
                Response_12.setAutoDraw(False)
        
        # *Response_13* updates
        if Response_13.status == NOT_STARTED and tThisFlip >= thisTrial_5["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_13.frameNStart = frameN  # exact frame index
            Response_13.tStart = t  # local t and not account for scr refresh
            Response_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_13.started')
            Response_13.setAutoDraw(True)
        if Response_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_13.tStartRefresh + thisTrial_5["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_13.tStop = t  # not accounting for scr refresh
                Response_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_13.stopped')
                Response_13.setAutoDraw(False)
        
        # *Response_14* updates
        if Response_14.status == NOT_STARTED and tThisFlip >= thisTrial_5["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_14.frameNStart = frameN  # exact frame index
            Response_14.tStart = t  # local t and not account for scr refresh
            Response_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_14.started')
            Response_14.setAutoDraw(True)
        if Response_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_14.tStartRefresh + thisTrial_5["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_14.tStop = t  # not accounting for scr refresh
                Response_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_14.stopped')
                Response_14.setAutoDraw(False)
        
        # *polygon_5* updates
        if polygon_5.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.tStart = t  # local t and not account for scr refresh
            polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_5.started')
            polygon_5.setAutoDraw(True)
        if polygon_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_5.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                polygon_5.tStop = t  # not accounting for scr refresh
                polygon_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_5.stopped')
                polygon_5.setAutoDraw(False)
        
        # *Delay_5* updates
        if Delay_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Delay_5.frameNStart = frameN  # exact frame index
            Delay_5.tStart = t  # local t and not account for scr refresh
            Delay_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Delay_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Delay_5.started')
            Delay_5.setAutoDraw(True)
        if Delay_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Delay_5.tStartRefresh + thisTrial_5["circle_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Delay_5.tStop = t  # not accounting for scr refresh
                Delay_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Delay_5.stopped')
                Delay_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_5" ---
    for thisComponent in trial_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord_5.status != FINISHED:
        etRecord_5.status = FINISHED
    # the Routine "trial_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials_5'

# get names of stimulus parameters
if trials_5.trialList in ([], [None], None):
    params = []
else:
    params = trials_5.trialList[0].keys()
# save data for this loop
trials_5.saveAsExcel(filename + '.xlsx', sheetName='trials_5',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_5.saveAsText(filename + 'trials_5.csv', delim=',',
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

# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=trial_list6, #data.importConditions("{}/{}-{}.csv".format(dirpath, 5, "UNPRED")),
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # add the loop to the experiment
thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
if thisTrial_6 != None:
    for paramName in thisTrial_6:
        exec('{} = thisTrial_6[paramName]'.format(paramName))

for thisTrial_6 in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6:
            exec('{} = thisTrial_6[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "codeEnd_6" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    codeEnd_6Components = []
    for thisComponent in codeEnd_6Components:
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
    
    # --- Run Routine "codeEnd_6" ---
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
        for thisComponent in codeEnd_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd_6" ---
    for thisComponent in codeEnd_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_9
    
    myCount6 += 1
    if myCount6 > trialNum:
        trials_6.finished = True
     
    
    print(myCount6)
    #
    #for k in thisTrial_6.keys(): 
    #    thisExp.addData(k, thisTrial_6[k])
    #    
    thisExp.nextEntry()
    
    # the Routine "codeEnd_6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_6" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_6.setImage(thisTrial_6["stimImage"])
    Response_15.setPos([thisTrial_6["responseImage1_pos"]])
    Response_15.setImage(thisTrial_6["responseImage1"])
    Response_16.setPos([thisTrial_6["responseImage2_pos"]])
    Response_16.setImage(thisTrial_6["responseImage2"])
    Response_17.setPos([thisTrial_6["responseImage3_pos"]])
    Response_17.setImage(thisTrial_6["responseImage3"])
    # keep track of which components have finished
    trial_6Components = [etRecord_6, sample_6, Response_15, Response_16, Response_17, polygon_6, Delay_6]
    for thisComponent in trial_6Components:
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
    
    # --- Run Routine "trial_6" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRecord_6* updates
        if etRecord_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord_6.frameNStart = frameN  # exact frame index
            etRecord_6.tStart = t  # local t and not account for scr refresh
            etRecord_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord_6.started', t)
            etRecord_6.status = STARTED
        if etRecord_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord_6.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_6.tStop = t  # not accounting for scr refresh
                etRecord_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_6.stopped', t)
                etRecord_6.status = FINISHED
        
        # *sample_6* updates
        if sample_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sample_6.frameNStart = frameN  # exact frame index
            sample_6.tStart = t  # local t and not account for scr refresh
            sample_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sample_6.started')
            sample_6.setAutoDraw(True)
        if sample_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample_6.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sample_6.tStop = t  # not accounting for scr refresh
                sample_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sample_6.stopped')
                sample_6.setAutoDraw(False)
        
        # *Response_15* updates
        if Response_15.status == NOT_STARTED and tThisFlip >= thisTrial_6['resp_onset']-frameTolerance:
            # keep track of start time/frame for later
            Response_15.frameNStart = frameN  # exact frame index
            Response_15.tStart = t  # local t and not account for scr refresh
            Response_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_15.started')
            Response_15.setAutoDraw(True)
        if Response_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_15.tStartRefresh + thisTrial_6['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response_15.tStop = t  # not accounting for scr refresh
                Response_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_15.stopped')
                Response_15.setAutoDraw(False)
        
        # *Response_16* updates
        if Response_16.status == NOT_STARTED and tThisFlip >= thisTrial_6["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_16.frameNStart = frameN  # exact frame index
            Response_16.tStart = t  # local t and not account for scr refresh
            Response_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_16.started')
            Response_16.setAutoDraw(True)
        if Response_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_16.tStartRefresh + thisTrial_6["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_16.tStop = t  # not accounting for scr refresh
                Response_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_16.stopped')
                Response_16.setAutoDraw(False)
        
        # *Response_17* updates
        if Response_17.status == NOT_STARTED and tThisFlip >= thisTrial_6["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_17.frameNStart = frameN  # exact frame index
            Response_17.tStart = t  # local t and not account for scr refresh
            Response_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_17.started')
            Response_17.setAutoDraw(True)
        if Response_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_17.tStartRefresh + thisTrial_6["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_17.tStop = t  # not accounting for scr refresh
                Response_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_17.stopped')
                Response_17.setAutoDraw(False)
        
        # *polygon_6* updates
        if polygon_6.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            polygon_6.frameNStart = frameN  # exact frame index
            polygon_6.tStart = t  # local t and not account for scr refresh
            polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_6.started')
            polygon_6.setAutoDraw(True)
        if polygon_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_6.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                polygon_6.tStop = t  # not accounting for scr refresh
                polygon_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_6.stopped')
                polygon_6.setAutoDraw(False)
        
        # *Delay_6* updates
        if Delay_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Delay_6.frameNStart = frameN  # exact frame index
            Delay_6.tStart = t  # local t and not account for scr refresh
            Delay_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Delay_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Delay_6.started')
            Delay_6.setAutoDraw(True)
        if Delay_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Delay_6.tStartRefresh + thisTrial_6["circle_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Delay_6.tStop = t  # not accounting for scr refresh
                Delay_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Delay_6.stopped')
                Delay_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_6" ---
    for thisComponent in trial_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord_6.status != FINISHED:
        etRecord_6.status = FINISHED
    # the Routine "trial_6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials_6'

# get names of stimulus parameters
if trials_6.trialList in ([], [None], None):
    params = []
else:
    params = trials_6.trialList[0].keys()
# save data for this loop
trials_6.saveAsExcel(filename + '.xlsx', sheetName='trials_6',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_6.saveAsText(filename + 'trials_6.csv', delim=',',
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

# set up handler to look after randomisation of conditions etc
trials_7 = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=trial_list7, #data.importConditions("{}/{}-{}.csv".format(dirpath, 6, "PRED")),
    seed=None, name='trials_7')
thisExp.addLoop(trials_7)  # add the loop to the experiment
thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
if thisTrial_7 != None:
    for paramName in thisTrial_7:
        exec('{} = thisTrial_7[paramName]'.format(paramName))

for thisTrial_7 in trials_7:
    currentLoop = trials_7
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7:
            exec('{} = thisTrial_7[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "codeEnd_7" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    codeEnd_7Components = []
    for thisComponent in codeEnd_7Components:
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
    
    # --- Run Routine "codeEnd_7" ---
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
        for thisComponent in codeEnd_7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd_7" ---
    for thisComponent in codeEnd_7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_10
    
    myCount7 += 1
    if myCount7 > trialNum:
        trials_7.finished = True
     
    
    print(myCount7)
    
    #for k in thisTrial_7.keys(): 
    #    thisExp.addData(k, thisTrial_7[k])
    #    
    thisExp.nextEntry()
    
    # the Routine "codeEnd_7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_7" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_7.setImage(thisTrial_7["stimImage"])
    Response_18.setPos([thisTrial_7["responseImage1_pos"]])
    Response_18.setImage(thisTrial_7["responseImage1"])
    Response_19.setPos([thisTrial_7["responseImage2_pos"]])
    Response_19.setImage(thisTrial_7["responseImage2"])
    Response_20.setPos([thisTrial_7["responseImage3_pos"]])
    Response_20.setImage(thisTrial_7["responseImage3"])
    # keep track of which components have finished
    trial_7Components = [etRecord_7, sample_7, Response_18, Response_19, Response_20, polygon_7, Delay_7]
    for thisComponent in trial_7Components:
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
    
    # --- Run Routine "trial_7" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRecord_7* updates
        if etRecord_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord_7.frameNStart = frameN  # exact frame index
            etRecord_7.tStart = t  # local t and not account for scr refresh
            etRecord_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord_7.started', t)
            etRecord_7.status = STARTED
        if etRecord_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord_7.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_7.tStop = t  # not accounting for scr refresh
                etRecord_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_7.stopped', t)
                etRecord_7.status = FINISHED
        
        # *sample_7* updates
        if sample_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sample_7.frameNStart = frameN  # exact frame index
            sample_7.tStart = t  # local t and not account for scr refresh
            sample_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sample_7.started')
            sample_7.setAutoDraw(True)
        if sample_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample_7.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sample_7.tStop = t  # not accounting for scr refresh
                sample_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sample_7.stopped')
                sample_7.setAutoDraw(False)
        
        # *Response_18* updates
        if Response_18.status == NOT_STARTED and tThisFlip >= thisTrial_7['resp_onset']-frameTolerance:
            # keep track of start time/frame for later
            Response_18.frameNStart = frameN  # exact frame index
            Response_18.tStart = t  # local t and not account for scr refresh
            Response_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_18.started')
            Response_18.setAutoDraw(True)
        if Response_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_18.tStartRefresh + thisTrial_7['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response_18.tStop = t  # not accounting for scr refresh
                Response_18.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_18.stopped')
                Response_18.setAutoDraw(False)
        
        # *Response_19* updates
        if Response_19.status == NOT_STARTED and tThisFlip >= thisTrial_7["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_19.frameNStart = frameN  # exact frame index
            Response_19.tStart = t  # local t and not account for scr refresh
            Response_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_19.started')
            Response_19.setAutoDraw(True)
        if Response_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_19.tStartRefresh + thisTrial_7["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_19.tStop = t  # not accounting for scr refresh
                Response_19.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_19.stopped')
                Response_19.setAutoDraw(False)
        
        # *Response_20* updates
        if Response_20.status == NOT_STARTED and tThisFlip >= thisTrial_7["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_20.frameNStart = frameN  # exact frame index
            Response_20.tStart = t  # local t and not account for scr refresh
            Response_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_20, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_20.started')
            Response_20.setAutoDraw(True)
        if Response_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_20.tStartRefresh + thisTrial_7["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_20.tStop = t  # not accounting for scr refresh
                Response_20.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_20.stopped')
                Response_20.setAutoDraw(False)
        
        # *polygon_7* updates
        if polygon_7.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            polygon_7.frameNStart = frameN  # exact frame index
            polygon_7.tStart = t  # local t and not account for scr refresh
            polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_7.started')
            polygon_7.setAutoDraw(True)
        if polygon_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_7.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                polygon_7.tStop = t  # not accounting for scr refresh
                polygon_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_7.stopped')
                polygon_7.setAutoDraw(False)
        
        # *Delay_7* updates
        if Delay_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Delay_7.frameNStart = frameN  # exact frame index
            Delay_7.tStart = t  # local t and not account for scr refresh
            Delay_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Delay_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Delay_7.started')
            Delay_7.setAutoDraw(True)
        if Delay_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Delay_7.tStartRefresh + thisTrial_7["circle_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Delay_7.tStop = t  # not accounting for scr refresh
                Delay_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Delay_7.stopped')
                Delay_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_7" ---
    for thisComponent in trial_7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord_7.status != FINISHED:
        etRecord_7.status = FINISHED
    # the Routine "trial_7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials_7'

# get names of stimulus parameters
if trials_7.trialList in ([], [None], None):
    params = []
else:
    params = trials_7.trialList[0].keys()
# save data for this loop
trials_7.saveAsExcel(filename + '.xlsx', sheetName='trials_7',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_7.saveAsText(filename + 'trials_7.csv', delim=',',
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

# set up handler to look after randomisation of conditions etc
trials_8 = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=trial_list8, #data.importConditions("{}/{}-{}.csv".format(dirpath, 7, "UNPRED")),
    seed=None, name='trials_8')
thisExp.addLoop(trials_8)  # add the loop to the experiment
thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
if thisTrial_8 != None:
    for paramName in thisTrial_8:
        exec('{} = thisTrial_8[paramName]'.format(paramName))

for thisTrial_8 in trials_8:
    currentLoop = trials_8
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
    if thisTrial_8 != None:
        for paramName in thisTrial_8:
            exec('{} = thisTrial_8[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "codeEnd_8" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    codeEnd_8Components = []
    for thisComponent in codeEnd_8Components:
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
    
    # --- Run Routine "codeEnd_8" ---
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
        for thisComponent in codeEnd_8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd_8" ---
    for thisComponent in codeEnd_8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_11
    
    myCount8 += 1
    if myCount8 > trialNum:
        trials_8.finished = True
     
    
    print(myCount8)
    #
    #for k in thisTrial_8.keys(): 
    #    thisExp.addData(k, thisTrial_8[k])
    #    
    thisExp.nextEntry()
    
    # the Routine "codeEnd_8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_8" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_8.setImage(thisTrial_8["stimImage"])
    Response_21.setPos([thisTrial_8["responseImage1_pos"]])
    Response_21.setImage(thisTrial_8["responseImage1"])
    Response_22.setPos([thisTrial_8["responseImage2_pos"]])
    Response_22.setImage(thisTrial_8["responseImage2"])
    Response_23.setPos([thisTrial_8["responseImage3_pos"]])
    Response_23.setImage(thisTrial_8["responseImage3"])
    # keep track of which components have finished
    trial_8Components = [etRecord_8, sample_8, Response_21, Response_22, Response_23, polygon_8, Delay_8, etrecord_pos_8]
    for thisComponent in trial_8Components:
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
    
    # --- Run Routine "trial_8" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRecord_8* updates
        if etRecord_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord_8.frameNStart = frameN  # exact frame index
            etRecord_8.tStart = t  # local t and not account for scr refresh
            etRecord_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord_8.started', t)
            etRecord_8.status = STARTED
        if etRecord_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord_8.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_8.tStop = t  # not accounting for scr refresh
                etRecord_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_8.stopped', t)
                etRecord_8.status = FINISHED
        
        # *sample_8* updates
        if sample_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sample_8.frameNStart = frameN  # exact frame index
            sample_8.tStart = t  # local t and not account for scr refresh
            sample_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sample_8.started')
            sample_8.setAutoDraw(True)
        if sample_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample_8.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sample_8.tStop = t  # not accounting for scr refresh
                sample_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sample_8.stopped')
                sample_8.setAutoDraw(False)
        
        # *Response_21* updates
        if Response_21.status == NOT_STARTED and tThisFlip >= thisTrial_8['resp_onset']-frameTolerance:
            # keep track of start time/frame for later
            Response_21.frameNStart = frameN  # exact frame index
            Response_21.tStart = t  # local t and not account for scr refresh
            Response_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_21, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_21.started')
            Response_21.setAutoDraw(True)
        if Response_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_21.tStartRefresh + thisTrial_8['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response_21.tStop = t  # not accounting for scr refresh
                Response_21.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_21.stopped')
                Response_21.setAutoDraw(False)
        
        # *Response_22* updates
        if Response_22.status == NOT_STARTED and tThisFlip >= thisTrial_8["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_22.frameNStart = frameN  # exact frame index
            Response_22.tStart = t  # local t and not account for scr refresh
            Response_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_22.started')
            Response_22.setAutoDraw(True)
        if Response_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_22.tStartRefresh + thisTrial_8["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_22.tStop = t  # not accounting for scr refresh
                Response_22.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_22.stopped')
                Response_22.setAutoDraw(False)
        
        # *Response_23* updates
        if Response_23.status == NOT_STARTED and tThisFlip >= thisTrial_8["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_23.frameNStart = frameN  # exact frame index
            Response_23.tStart = t  # local t and not account for scr refresh
            Response_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_23.started')
            Response_23.setAutoDraw(True)
        if Response_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_23.tStartRefresh + thisTrial_8["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_23.tStop = t  # not accounting for scr refresh
                Response_23.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_23.stopped')
                Response_23.setAutoDraw(False)
        
        # *polygon_8* updates
        if polygon_8.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            polygon_8.frameNStart = frameN  # exact frame index
            polygon_8.tStart = t  # local t and not account for scr refresh
            polygon_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_8.started')
            polygon_8.setAutoDraw(True)
        if polygon_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_8.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                polygon_8.tStop = t  # not accounting for scr refresh
                polygon_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_8.stopped')
                polygon_8.setAutoDraw(False)
        
        # *Delay_8* updates
        if Delay_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Delay_8.frameNStart = frameN  # exact frame index
            Delay_8.tStart = t  # local t and not account for scr refresh
            Delay_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Delay_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Delay_8.started')
            Delay_8.setAutoDraw(True)
        if Delay_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Delay_8.tStartRefresh + thisTrial_8["circle_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Delay_8.tStop = t  # not accounting for scr refresh
                Delay_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Delay_8.stopped')
                Delay_8.setAutoDraw(False)
        
        # *etrecord_pos_8* updates
        if etrecord_pos_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etrecord_pos_8.frameNStart = frameN  # exact frame index
            etrecord_pos_8.tStart = t  # local t and not account for scr refresh
            etrecord_pos_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etrecord_pos_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'etrecord_pos_8.started')
            etrecord_pos_8.setAutoDraw(True)
        if etrecord_pos_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etrecord_pos_8.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                etrecord_pos_8.tStop = t  # not accounting for scr refresh
                etrecord_pos_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'etrecord_pos_8.stopped')
                etrecord_pos_8.setAutoDraw(False)
        if etrecord_pos_8.status == STARTED:  # only update if drawing
            etrecord_pos_8.setPos([etRecord.pos], log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_8" ---
    for thisComponent in trial_8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord_8.status != FINISHED:
        etRecord_8.status = FINISHED
    # the Routine "trial_8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials_8'

# get names of stimulus parameters
if trials_8.trialList in ([], [None], None):
    params = []
else:
    params = trials_8.trialList[0].keys()
# save data for this loop
trials_8.saveAsExcel(filename + '.xlsx', sheetName='trials_8',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_8.saveAsText(filename + 'trials_8.csv', delim=',',
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

# set up handler to look after randomisation of conditions etc
trials_9 = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=trial_list9, #data.importConditions("{}/{}-{}.csv".format(dirpath, 8, "PRED")),
    seed=None, name='trials_9')
thisExp.addLoop(trials_9)  # add the loop to the experiment
thisTrial_9 = trials_9.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
if thisTrial_9 != None:
    for paramName in thisTrial_9:
        exec('{} = thisTrial_9[paramName]'.format(paramName))

for thisTrial_9 in trials_9:
    currentLoop = trials_9
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
    if thisTrial_9 != None:
        for paramName in thisTrial_9:
            exec('{} = thisTrial_9[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "codeEnd_9" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    codeEnd_9Components = []
    for thisComponent in codeEnd_9Components:
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
    
    # --- Run Routine "codeEnd_9" ---
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
        for thisComponent in codeEnd_9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd_9" ---
    for thisComponent in codeEnd_9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_12
    
    myCount9 += 1
    if myCount9 > trialNum:
        trials_9.finished = True
     
    
    print(myCount9)
    #
    #for k in thisTrial_9.keys(): 
    #    thisExp.addData(k, thisTrial_9[k])
    #    
    thisExp.nextEntry()
    
    # the Routine "codeEnd_9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_9" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_9.setImage(thisTrial_9["stimImage"])
    Response_24.setPos([thisTrial_9["responseImage1_pos"]])
    Response_24.setImage(thisTrial_9["responseImage1"])
    Response_25.setPos([thisTrial_9["responseImage2_pos"]])
    Response_25.setImage(thisTrial_9["responseImage2"])
    Response_26.setPos([thisTrial_9["responseImage3_pos"]])
    Response_26.setImage(thisTrial_9["responseImage3"])
    # keep track of which components have finished
    trial_9Components = [etRecord_9, sample_9, Response_24, Response_25, Response_26, polygon_9, Delay_9]
    for thisComponent in trial_9Components:
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
    
    # --- Run Routine "trial_9" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRecord_9* updates
        if etRecord_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord_9.frameNStart = frameN  # exact frame index
            etRecord_9.tStart = t  # local t and not account for scr refresh
            etRecord_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord_9.started', t)
            etRecord_9.status = STARTED
        if etRecord_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord_9.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_9.tStop = t  # not accounting for scr refresh
                etRecord_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_9.stopped', t)
                etRecord_9.status = FINISHED
        
        # *sample_9* updates
        if sample_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sample_9.frameNStart = frameN  # exact frame index
            sample_9.tStart = t  # local t and not account for scr refresh
            sample_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sample_9.started')
            sample_9.setAutoDraw(True)
        if sample_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample_9.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sample_9.tStop = t  # not accounting for scr refresh
                sample_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sample_9.stopped')
                sample_9.setAutoDraw(False)
        
        # *Response_24* updates
        if Response_24.status == NOT_STARTED and tThisFlip >= thisTrial_9['resp_onset']-frameTolerance:
            # keep track of start time/frame for later
            Response_24.frameNStart = frameN  # exact frame index
            Response_24.tStart = t  # local t and not account for scr refresh
            Response_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_24, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_24.started')
            Response_24.setAutoDraw(True)
        if Response_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_24.tStartRefresh + thisTrial_9['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response_24.tStop = t  # not accounting for scr refresh
                Response_24.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_24.stopped')
                Response_24.setAutoDraw(False)
        
        # *Response_25* updates
        if Response_25.status == NOT_STARTED and tThisFlip >= thisTrial_9["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_25.frameNStart = frameN  # exact frame index
            Response_25.tStart = t  # local t and not account for scr refresh
            Response_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_25.started')
            Response_25.setAutoDraw(True)
        if Response_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_25.tStartRefresh + thisTrial_9["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_25.tStop = t  # not accounting for scr refresh
                Response_25.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_25.stopped')
                Response_25.setAutoDraw(False)
        
        # *Response_26* updates
        if Response_26.status == NOT_STARTED and tThisFlip >= thisTrial_9["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_26.frameNStart = frameN  # exact frame index
            Response_26.tStart = t  # local t and not account for scr refresh
            Response_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_26, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_26.started')
            Response_26.setAutoDraw(True)
        if Response_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_26.tStartRefresh + thisTrial_9["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_26.tStop = t  # not accounting for scr refresh
                Response_26.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_26.stopped')
                Response_26.setAutoDraw(False)
        
        # *polygon_9* updates
        if polygon_9.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            polygon_9.frameNStart = frameN  # exact frame index
            polygon_9.tStart = t  # local t and not account for scr refresh
            polygon_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_9.started')
            polygon_9.setAutoDraw(True)
        if polygon_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_9.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                polygon_9.tStop = t  # not accounting for scr refresh
                polygon_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_9.stopped')
                polygon_9.setAutoDraw(False)
        
        # *Delay_9* updates
        if Delay_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Delay_9.frameNStart = frameN  # exact frame index
            Delay_9.tStart = t  # local t and not account for scr refresh
            Delay_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Delay_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Delay_9.started')
            Delay_9.setAutoDraw(True)
        if Delay_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Delay_9.tStartRefresh + thisTrial_9["circle_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Delay_9.tStop = t  # not accounting for scr refresh
                Delay_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Delay_9.stopped')
                Delay_9.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_9" ---
    for thisComponent in trial_9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord_9.status != FINISHED:
        etRecord_9.status = FINISHED
    # the Routine "trial_9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials_9'

# get names of stimulus parameters
if trials_9.trialList in ([], [None], None):
    params = []
else:
    params = trials_9.trialList[0].keys()
# save data for this loop
trials_9.saveAsExcel(filename + '.xlsx', sheetName='trials_9',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_9.saveAsText(filename + 'trials_9.csv', delim=',',
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

# set up handler to look after randomisation of conditions etc
trials_10 = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=trial_list10, #data.importConditions("{}/{}-{}.csv".format(dirpath, 9, "UNPRED")),
    seed=None, name='trials_10')
thisExp.addLoop(trials_10)  # add the loop to the experiment
thisTrial_10 = trials_10.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
if thisTrial_10 != None:
    for paramName in thisTrial_10:
        exec('{} = thisTrial_10[paramName]'.format(paramName))

for thisTrial_10 in trials_10:
    currentLoop = trials_10
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
    if thisTrial_10 != None:
        for paramName in thisTrial_10:
            exec('{} = thisTrial_10[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "codeEnd_10" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    codeEnd_10Components = []
    for thisComponent in codeEnd_10Components:
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
    
    # --- Run Routine "codeEnd_10" ---
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
        for thisComponent in codeEnd_10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd_10" ---
    for thisComponent in codeEnd_10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_13
    
    myCount10 += 1
    if myCount10 > trialNum:
        trials_10.finished = True
     
    
    print(myCount10)
    
    #for k in thisTrial_10.keys(): 
    #    thisExp.addData(k, thisTrial_10[k])
    #    
    thisExp.nextEntry()
    
    # the Routine "codeEnd_10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_10" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_10.setImage(thisTrial_10["stimImage"])
    Response_27.setPos([thisTrial_10["responseImage1_pos"]])
    Response_27.setImage(thisTrial_10["responseImage1"])
    Response_28.setPos([thisTrial_10["responseImage2_pos"]])
    Response_28.setImage(thisTrial_10["responseImage2"])
    Response_29.setPos([thisTrial_10["responseImage3_pos"]])
    Response_29.setImage(thisTrial_10["responseImage3"])
    # keep track of which components have finished
    trial_10Components = [etRecord_10, sample_10, Response_27, Response_28, Response_29, polygon_10, Delay_10]
    for thisComponent in trial_10Components:
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
    
    # --- Run Routine "trial_10" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRecord_10* updates
        if etRecord_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord_10.frameNStart = frameN  # exact frame index
            etRecord_10.tStart = t  # local t and not account for scr refresh
            etRecord_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord_10.started', t)
            etRecord_10.status = STARTED
        if etRecord_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord_10.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_10.tStop = t  # not accounting for scr refresh
                etRecord_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_10.stopped', t)
                etRecord_10.status = FINISHED
        
        # *sample_10* updates
        if sample_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sample_10.frameNStart = frameN  # exact frame index
            sample_10.tStart = t  # local t and not account for scr refresh
            sample_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sample_10.started')
            sample_10.setAutoDraw(True)
        if sample_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample_10.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sample_10.tStop = t  # not accounting for scr refresh
                sample_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sample_10.stopped')
                sample_10.setAutoDraw(False)
        
        # *Response_27* updates
        if Response_27.status == NOT_STARTED and tThisFlip >= thisTrial_10['resp_onset']-frameTolerance:
            # keep track of start time/frame for later
            Response_27.frameNStart = frameN  # exact frame index
            Response_27.tStart = t  # local t and not account for scr refresh
            Response_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_27, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_27.started')
            Response_27.setAutoDraw(True)
        if Response_27.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_27.tStartRefresh + thisTrial_10['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response_27.tStop = t  # not accounting for scr refresh
                Response_27.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_27.stopped')
                Response_27.setAutoDraw(False)
        
        # *Response_28* updates
        if Response_28.status == NOT_STARTED and tThisFlip >= thisTrial_10["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_28.frameNStart = frameN  # exact frame index
            Response_28.tStart = t  # local t and not account for scr refresh
            Response_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_28, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_28.started')
            Response_28.setAutoDraw(True)
        if Response_28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_28.tStartRefresh + thisTrial_10["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_28.tStop = t  # not accounting for scr refresh
                Response_28.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_28.stopped')
                Response_28.setAutoDraw(False)
        
        # *Response_29* updates
        if Response_29.status == NOT_STARTED and tThisFlip >= thisTrial_10["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_29.frameNStart = frameN  # exact frame index
            Response_29.tStart = t  # local t and not account for scr refresh
            Response_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_29, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_29.started')
            Response_29.setAutoDraw(True)
        if Response_29.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_29.tStartRefresh + thisTrial_10["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_29.tStop = t  # not accounting for scr refresh
                Response_29.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_29.stopped')
                Response_29.setAutoDraw(False)
        
        # *polygon_10* updates
        if polygon_10.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            polygon_10.frameNStart = frameN  # exact frame index
            polygon_10.tStart = t  # local t and not account for scr refresh
            polygon_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_10.started')
            polygon_10.setAutoDraw(True)
        if polygon_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_10.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                polygon_10.tStop = t  # not accounting for scr refresh
                polygon_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_10.stopped')
                polygon_10.setAutoDraw(False)
        
        # *Delay_10* updates
        if Delay_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Delay_10.frameNStart = frameN  # exact frame index
            Delay_10.tStart = t  # local t and not account for scr refresh
            Delay_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Delay_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Delay_10.started')
            Delay_10.setAutoDraw(True)
        if Delay_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Delay_10.tStartRefresh + thisTrial_10["circle_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Delay_10.tStop = t  # not accounting for scr refresh
                Delay_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Delay_10.stopped')
                Delay_10.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_10" ---
    for thisComponent in trial_10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord_10.status != FINISHED:
        etRecord_10.status = FINISHED
    # the Routine "trial_10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials_10'

# get names of stimulus parameters
if trials_10.trialList in ([], [None], None):
    params = []
else:
    params = trials_10.trialList[0].keys()
# save data for this loop
trials_10.saveAsExcel(filename + '.xlsx', sheetName='trials_10',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_10.saveAsText(filename + 'trials_10.csv', delim=',',
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

# set up handler to look after randomisation of conditions etc
trials_11 = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=trial_list11, #data.importConditions("{}/{}-{}.csv".format(dirpath, 10, "PRED")),
    seed=None, name='trials_11')
thisExp.addLoop(trials_11)  # add the loop to the experiment
thisTrial_11 = trials_11.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
if thisTrial_11 != None:
    for paramName in thisTrial_11:
        exec('{} = thisTrial_11[paramName]'.format(paramName))

for thisTrial_11 in trials_11:
    currentLoop = trials_11
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
    if thisTrial_11 != None:
        for paramName in thisTrial_11:
            exec('{} = thisTrial_11[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "codeEnd_11" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    codeEnd_11Components = []
    for thisComponent in codeEnd_11Components:
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
    
    # --- Run Routine "codeEnd_11" ---
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
        for thisComponent in codeEnd_11Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd_11" ---
    for thisComponent in codeEnd_11Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_14
    
    myCount11 += 1
    if myCount11 > trialNum:
        trials_11.finished = True
     
    
    print(myCount11)
    
    #for k in thisTrial_11.keys(): 
    #    thisExp.addData(k, thisTrial_11[k])
    #    
    thisExp.nextEntry()
    
    # the Routine "codeEnd_11" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_11" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_11.setImage(thisTrial_11["stimImage"])
    Response_30.setPos([thisTrial_11["responseImage1_pos"]])
    Response_30.setImage(thisTrial_11["responseImage1"])
    Response_31.setPos([thisTrial_11["responseImage2_pos"]])
    Response_31.setImage(thisTrial_11["responseImage2"])
    Response_32.setPos([thisTrial_11["responseImage3_pos"]])
    Response_32.setImage(thisTrial_11["responseImage3"])
    # keep track of which components have finished
    trial_11Components = [etRecord_11, sample_11, Response_30, Response_31, Response_32, polygon_11, Delay_11]
    for thisComponent in trial_11Components:
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
    
    # --- Run Routine "trial_11" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRecord_11* updates
        if etRecord_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord_11.frameNStart = frameN  # exact frame index
            etRecord_11.tStart = t  # local t and not account for scr refresh
            etRecord_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord_11.started', t)
            etRecord_11.status = STARTED
        if etRecord_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord_11.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_11.tStop = t  # not accounting for scr refresh
                etRecord_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_11.stopped', t)
                etRecord_11.status = FINISHED
        
        # *sample_11* updates
        if sample_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sample_11.frameNStart = frameN  # exact frame index
            sample_11.tStart = t  # local t and not account for scr refresh
            sample_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sample_11.started')
            sample_11.setAutoDraw(True)
        if sample_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample_11.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sample_11.tStop = t  # not accounting for scr refresh
                sample_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sample_11.stopped')
                sample_11.setAutoDraw(False)
        
        # *Response_30* updates
        if Response_30.status == NOT_STARTED and tThisFlip >= thisTrial_11['resp_onset']-frameTolerance:
            # keep track of start time/frame for later
            Response_30.frameNStart = frameN  # exact frame index
            Response_30.tStart = t  # local t and not account for scr refresh
            Response_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_30, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_30.started')
            Response_30.setAutoDraw(True)
        if Response_30.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_30.tStartRefresh + thisTrial_11['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response_30.tStop = t  # not accounting for scr refresh
                Response_30.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_30.stopped')
                Response_30.setAutoDraw(False)
        
        # *Response_31* updates
        if Response_31.status == NOT_STARTED and tThisFlip >= thisTrial_11["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_31.frameNStart = frameN  # exact frame index
            Response_31.tStart = t  # local t and not account for scr refresh
            Response_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_31, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_31.started')
            Response_31.setAutoDraw(True)
        if Response_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_31.tStartRefresh + thisTrial_11["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_31.tStop = t  # not accounting for scr refresh
                Response_31.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_31.stopped')
                Response_31.setAutoDraw(False)
        
        # *Response_32* updates
        if Response_32.status == NOT_STARTED and tThisFlip >= thisTrial_11["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_32.frameNStart = frameN  # exact frame index
            Response_32.tStart = t  # local t and not account for scr refresh
            Response_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_32, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_32.started')
            Response_32.setAutoDraw(True)
        if Response_32.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_32.tStartRefresh + thisTrial_11["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_32.tStop = t  # not accounting for scr refresh
                Response_32.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_32.stopped')
                Response_32.setAutoDraw(False)
        
        # *polygon_11* updates
        if polygon_11.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            polygon_11.frameNStart = frameN  # exact frame index
            polygon_11.tStart = t  # local t and not account for scr refresh
            polygon_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_11.started')
            polygon_11.setAutoDraw(True)
        if polygon_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_11.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                polygon_11.tStop = t  # not accounting for scr refresh
                polygon_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_11.stopped')
                polygon_11.setAutoDraw(False)
        
        # *Delay_11* updates
        if Delay_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Delay_11.frameNStart = frameN  # exact frame index
            Delay_11.tStart = t  # local t and not account for scr refresh
            Delay_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Delay_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Delay_11.started')
            Delay_11.setAutoDraw(True)
        if Delay_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Delay_11.tStartRefresh + thisTrial_11["circle_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Delay_11.tStop = t  # not accounting for scr refresh
                Delay_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Delay_11.stopped')
                Delay_11.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_11Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_11" ---
    for thisComponent in trial_11Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord_11.status != FINISHED:
        etRecord_11.status = FINISHED
    # the Routine "trial_11" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials_11'

# get names of stimulus parameters
if trials_11.trialList in ([], [None], None):
    params = []
else:
    params = trials_11.trialList[0].keys()
# save data for this loop
trials_11.saveAsExcel(filename + '.xlsx', sheetName='trials_11',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_11.saveAsText(filename + 'trials_11.csv', delim=',',
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

# set up handler to look after randomisation of conditions etc
trials_12 = data.TrialHandler(nReps=trialNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=trial_list12, #data.importConditions("{}/{}-{}.csv".format(dirpath, 11, "UNPRED")),
    seed=None, name='trials_12')
thisExp.addLoop(trials_12)  # add the loop to the experiment
thisTrial_12 = trials_12.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
if thisTrial_12 != None:
    for paramName in thisTrial_12:
        exec('{} = thisTrial_12[paramName]'.format(paramName))

for thisTrial_12 in trials_12:
    currentLoop = trials_12
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
    if thisTrial_12 != None:
        for paramName in thisTrial_12:
            exec('{} = thisTrial_12[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "codeEnd_12" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    codeEnd_12Components = []
    for thisComponent in codeEnd_12Components:
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
    
    # --- Run Routine "codeEnd_12" ---
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
        for thisComponent in codeEnd_12Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "codeEnd_12" ---
    for thisComponent in codeEnd_12Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_15
    
    myCount12 += 1
    if myCount12 > trialNum:
        trials_12.finished = True
     
    
    print(myCount12)
    
    #for k in thisTrial_12.keys(): 
    #    thisExp.addData(k, thisTrial_12[k])
    #    
    thisExp.nextEntry()
    
    # the Routine "codeEnd_12" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_12" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_12.setImage(thisTrial_12["stimImage"])
    Response_33.setPos([thisTrial_12["responseImage1_pos"]])
    Response_33.setImage(thisTrial_12["responseImage1"])
    Response_34.setPos([thisTrial_12["responseImage2_pos"]])
    Response_34.setImage(thisTrial_12["responseImage2"])
    Response_35.setPos([thisTrial_12["responseImage3_pos"]])
    Response_35.setImage(thisTrial_12["responseImage3"])
    # keep track of which components have finished
    trial_12Components = [etRecord_12, sample_12, Response_33, Response_34, Response_35, polygon_12, Delay_12]
    for thisComponent in trial_12Components:
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
    
    # --- Run Routine "trial_12" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRecord_12* updates
        if etRecord_12.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord_12.frameNStart = frameN  # exact frame index
            etRecord_12.tStart = t  # local t and not account for scr refresh
            etRecord_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord_12.started', t)
            etRecord_12.status = STARTED
        if etRecord_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord_12.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_12.tStop = t  # not accounting for scr refresh
                etRecord_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_12.stopped', t)
                etRecord_12.status = FINISHED
        
        # *sample_12* updates
        if sample_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sample_12.frameNStart = frameN  # exact frame index
            sample_12.tStart = t  # local t and not account for scr refresh
            sample_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sample_12.started')
            sample_12.setAutoDraw(True)
        if sample_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample_12.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sample_12.tStop = t  # not accounting for scr refresh
                sample_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sample_12.stopped')
                sample_12.setAutoDraw(False)
        
        # *Response_33* updates
        if Response_33.status == NOT_STARTED and tThisFlip >= thisTrial_12['resp_onset']-frameTolerance:
            # keep track of start time/frame for later
            Response_33.frameNStart = frameN  # exact frame index
            Response_33.tStart = t  # local t and not account for scr refresh
            Response_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_33, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_33.started')
            Response_33.setAutoDraw(True)
        if Response_33.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_33.tStartRefresh + thisTrial_12['resp_dur']-frameTolerance:
                # keep track of stop time/frame for later
                Response_33.tStop = t  # not accounting for scr refresh
                Response_33.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_33.stopped')
                Response_33.setAutoDraw(False)
        
        # *Response_34* updates
        if Response_34.status == NOT_STARTED and tThisFlip >= thisTrial_12["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_34.frameNStart = frameN  # exact frame index
            Response_34.tStart = t  # local t and not account for scr refresh
            Response_34.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_34, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_34.started')
            Response_34.setAutoDraw(True)
        if Response_34.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_34.tStartRefresh + thisTrial_12["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_34.tStop = t  # not accounting for scr refresh
                Response_34.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_34.stopped')
                Response_34.setAutoDraw(False)
        
        # *Response_35* updates
        if Response_35.status == NOT_STARTED and tThisFlip >= thisTrial_12["resp_onset"]-frameTolerance:
            # keep track of start time/frame for later
            Response_35.frameNStart = frameN  # exact frame index
            Response_35.tStart = t  # local t and not account for scr refresh
            Response_35.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_35, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Response_35.started')
            Response_35.setAutoDraw(True)
        if Response_35.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_35.tStartRefresh + thisTrial_12["resp_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Response_35.tStop = t  # not accounting for scr refresh
                Response_35.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response_35.stopped')
                Response_35.setAutoDraw(False)
        
        # *polygon_12* updates
        if polygon_12.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            polygon_12.frameNStart = frameN  # exact frame index
            polygon_12.tStart = t  # local t and not account for scr refresh
            polygon_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_12.started')
            polygon_12.setAutoDraw(True)
        if polygon_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_12.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                polygon_12.tStop = t  # not accounting for scr refresh
                polygon_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_12.stopped')
                polygon_12.setAutoDraw(False)
        
        # *Delay_12* updates
        if Delay_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Delay_12.frameNStart = frameN  # exact frame index
            Delay_12.tStart = t  # local t and not account for scr refresh
            Delay_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Delay_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Delay_12.started')
            Delay_12.setAutoDraw(True)
        if Delay_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Delay_12.tStartRefresh + thisTrial_12["circle_dur"]-frameTolerance:
                # keep track of stop time/frame for later
                Delay_12.tStop = t  # not accounting for scr refresh
                Delay_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Delay_12.stopped')
                Delay_12.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_12Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_12" ---
    for thisComponent in trial_12Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord_12.status != FINISHED:
        etRecord_12.status = FINISHED
    # the Routine "trial_12" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialNum repeats of 'trials_12'

# get names of stimulus parameters
if trials_12.trialList in ([], [None], None):
    params = []
else:
    params = trials_12.trialList[0].keys()
# save data for this loop
trials_12.saveAsExcel(filename + '.xlsx', sheetName='trials_12',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_12.saveAsText(filename + 'trials_12.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "baselineEnd" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
baselineEndComponents = [text_3]
for thisComponent in baselineEndComponents:
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

# --- Run Routine "baselineEnd" ---
while continueRoutine and routineTimer.getTime() < 24.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 24-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.stopped')
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baselineEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "baselineEnd" ---
for thisComponent in baselineEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-24.000000)

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
