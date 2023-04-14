#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Tue Nov 29 18:03:58 2022
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

from psychopy.hardware import keyboard
import random 

pos=[(1,1),(-1,1),(1,-1),(-1,-1)]
locations = ['topright','topleft','bottomright','bottomleft']
pictures  = ['images/picture_1.png','images/picture_2.png','images/picture_3.png']

trial_list = []
blockTypes = ["UNPRED","BASELINE","PRED",
"BASELINE","PRED",'UNPRED',"BASELINE","PRED",]

trialNum = 1
#for j in range()
for i in range(trialNum):
    delayTime = random.randrange(5,12)/10
    stimImage_i = random.randrange(0,3)
    stimImage = pictures[stimImage_i]
    
    location_ind = [0,1,2,3]
    picture_ind =  [0,1,2]
    pos_ind = [0,1,2,3]
    
    # get rand seed? 
    
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

#    app = [ delayTime, stimImage_i, stimImage, 
#    responseImage1, responseImage1_i, responseImage1_location, responseImage1_location_i,
#    responseImage2, responseImage2_i, responseImage2_location, responseImage2_location_i,
#    responseImage3, responseImage3_i, responseImage3_location, responseImage3_location_i]
#    
    app = { "delay_time":delayTime, "stimImage_i":stimImage_i, "stimImage":stimImage, 
    "responseImage1":responseImage1, "responseImage1_i":responseImage1_i, "responseImage1_pos":responseImage1_pos, "responseImage1_pos_ind":responseImage1_pos_ind, "responseImage1_location":responseImage1_location,"responseImage1_location_i":responseImage1_location_i,
    "responseImage2":responseImage2, "responseImage2_i":responseImage2_i, "responseImage2_pos":responseImage2_pos, "responseImage2_pos_ind":responseImage2_pos_ind, "responseImage2_location":responseImage2_location, "responseImage2_location_i":responseImage2_location_i,
    "responseImage3":responseImage3, "responseImage3_i":responseImage3_i, "responseImage3_pos":responseImage3_pos, "responseImage3_pos_ind":responseImage3_pos_ind, "responseImage3_location":responseImage3_location, "responseImage3_location_i":responseImage3_location_i}
    
    trial_list.append(app)
    #trial_list.append(app2)
    
    # trial_list[i]["stimImage"]
    
    # trial_list[i]["responseImage1"] 
    # trial_list[i]["responseImage1_location"]
    # trial_list[i]["responseImage1_pos"]
    
    # trial_list[i]["responseImage2"] 
    # trial_list[i]["responseImage2_location"]
    
    # trial_list[i]["responseImage3"] 
    # trial_list[i]["responseImage3_location"]
    
    
    
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'DMS'  # from the Builder filename that created this script
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
    originPath='/Users/richard/Desktop/DMS.py',
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
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "trial" ---
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',
    size=(0.025, 0.025),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
sample = visual.ImageStim(
    win=win,
    name='sample', 
    image='images/picture_2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
    
Delay = visual.ShapeStim(
    win=win, name='Delay', vertices='cross',
    size=(0.025, 0.025),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
    
Response_1 = visual.ImageStim(
    win=win,
    name='Response_1', 
    image='images/picture_2.png', mask=None, anchor='center',
    ori=0.0, pos=(1, 1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Response_2 = visual.ImageStim(
    win=win,
    name='Response_2', 
    image='images/picture_2.png', mask=None, anchor='center',
    ori=0.0, pos=(1, -1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
Response_3 = visual.ImageStim(
    win=win,
    name='Response_3', 
    image='images/picture_2.png', mask=None, anchor='center',
    ori=0.0, pos=(-1, -1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
#trials = data.TrialHandler(nReps=50.0, method='random', 
#    extraInfo=expInfo, originPath=-1,
#    trialList=[None],
#    seed=None, name='trials')
trials = data.TrialHandler(nReps=50.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=trial_list,
    seed=None, name='trials')


thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    
    print(thisTrial)
    
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    trialComponents = [Fixation, sample, Delay, Response_1, Response_2, Response_3]
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
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fixation.started')
            Fixation.setAutoDraw(True)
            
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fixation.stopped')
                Fixation.setAutoDraw(False)
        
        
        
        
        # SAMPLE 
        # *sample* updates
        if sample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sample.frameNStart = frameN  # exact frame index
            sample.tStart = t  # local t and not account for scr refresh
            sample.tStartRefresh = tThisFlipGlobal  # on global time
            
            ##########
            sample.image = thisTrial["stimImage"]
            ##########
            
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
        
        # NEED VARIABLE DELAY 
        # *Delay* updates
        if Delay.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
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
            if tThisFlipGlobal > Delay.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Delay.tStop = t  # not accounting for scr refresh
                Delay.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Delay.stopped')
                Delay.setAutoDraw(False)
        
        # *Response_1* updates
        if Response_1.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            Response_1.frameNStart = frameN  # exact frame index
            Response_1.tStart = t  # local t and not account for scr refresh
            Response_1.tStartRefresh = tThisFlipGlobal  # on global time
            
            #########
            Response_1.image = thisTrial["responseImage1"] 
            Response_1.pos = thisTrial["responseImage1_pos"]
            #########
            
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
            
            ##########
            Response_2.image = thisTrial["responseImage2"] 
            Response_2.pos = thisTrial["responseImage2_pos"]
            ###########
            
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
            
            ######
            Response_3.image = thisTrial["responseImage3"] 
            Response_3.pos = thisTrial["responseImage3_pos"]
            #######

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
        routineTimer.addTime(-4.000000)
    thisExp.nextEntry()
    
# completed 50.0 repeats of 'trials'


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
