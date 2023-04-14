# **************************************
# *** GLARE ILLUSION PERCEPTION TASK ***
# **************************************

# Written by: Sharif I. Kronemer
# Last Modified: 3/6/2023

# Version 1
task_version = 'v1'

# ***************************
# *** IMPORTANT LIBRARIES ***
# ***************************

# Python and Psychopy Functions
import random
import warnings
from psychopy import visual, gui, data, core, event, monitors, logging, sound 
from psychopy.hardware import keyboard
import numpy as np
import time
import pylink
import os
import platform
import sys
from scipy.signal import find_peaks
import argparse
from collections import deque
from scipy.io import loadmat, savemat
import statistics 
from scipy.signal import savgol_filter, find_peaks, peak_prominences
from scipy.optimize import curve_fit
import math

# EyeLink Functions
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
from PIL import Image
from string import ascii_letters, digits

# ********************
# *** SETUP SCREEN ***
# ********************

# Setup the subject info screen
info = {'Session #': 0, 'Subject ID': 'Test', 'EyeLink': ['y','n'], 'EyeLink EDF': 'test.edf', 
    'threshold opacity': 1.0, 'Response Condition (1 or 2)': [1, 2]}

dlg = gui.DlgFromDict(info, title = 'Glare Illusion Perception Experiment')

# Find experiment date
info['date'] = data.getDateStr()

# Filename = Subject ID entered above
filename = info['Subject ID']

# Set this variable to True if you use the built-in retina screen as your 
# primary display device on macOS. If have an external monitor, set this 
# variable True if you choose to "Optimize for Built-in Retina Display" 
# in the Displays preference settings.
use_retina = True

# ********************
# *** SETUP WINDOW ***
# ********************

# Setup the window
resolution = [2560, 1440] # Define screen resolution
win = visual.Window(size = resolution, color = [1,1,1], monitor = 'testMonitor', fullscr = True, units ='cm') #Set color and fullscreen mode (True or False)

# *****************************************
# *** MANAGE DATA FOLDERS AND FILENAMES ***
# *****************************************

# Behavioral data file
behavioral_folder = 'Behavioral_Data'

# Eyelink data file
results_folder = 'EyeLink_Data'

# Find experiment date
info['date'] = data.getDateStr()

# Filename = Subject ID entered above
filename = info['Subject ID']

# EyeLink filename
tmp_str = info['EyeLink EDF']

# Strip trailing characters, ignore the ".edf" extension
edf_fname = tmp_str.rstrip().split('.')[0]

# Check if the EyeLink filename is valid (length <= 8 & no special char)
allowed_char = ascii_letters + digits + '_'

# If too many characters in EyeLink filename
if not all([c in allowed_char for c in edf_fname]):
    print('ERROR: *** Invalid EDF filename')
    core.quit()  # abort experiment

elif len(edf_fname) > 8:
    print('ERROR: *** EDF filename should not exceed 8 characters')
    core.quit()  # abort experiment

# We download EDF data file from the EyeLink Host PC to the local hard
# drive at the end of each testing session, here we rename the EDF to
# include session start date/time
time_str = time.strftime("_%Y_%m_%d_%H_%M", time.localtime())
session_identifier = edf_fname + time_str

# Check for the behavioral data directory, otherwise make it
if not os.path.isdir('Behavioral_Data'):
        os.makedirs('Behavioral_Data')  # if this fails (e.g. permissions) we will get error

# Check for the EyeLink data directory, otherwise make it
if not os.path.isdir('EyeLink_Data'):
        os.makedirs('EyeLink_Data') # if this fails (e.g. permissions) we will get error

# Define EyeLink folder - directory of task + folder name
eyelinkFolder = (results_folder + os.path.sep)

# Show only critical log messages in the PsychoPy console
logFile = logging.LogFile(behavioral_folder + os.path.sep + filename + '_Session_'+str(info['Session #'])+'_Glare_Illusion_Perception_'+info['date']+'_'+task_version+'.log', level=logging.EXP)

# ***********************
# *** TASK PARAMETERS ***
# ***********************

# Block
max_num_blocks = 12

#stores left or right location
location_record = []
stim_record = []

# ISI
ISI_min_duration_sec = 3
ISI_max_duration_sec = 5

# Target Stimuli (seconds)
target_duration = 2

# Target location
left_loc = (-12,5)
right_loc = (12,5)

# Behavior 
response_time_max_sec = 1

# Define button press perception yes and no responses
if info['Response Condition (1 or 2)'] == '1':
    Yes = 1
    No = 2

elif info['Response Condition (1 or 2)'] == '2':
    Yes = 2
    No = 1
    
# ********************
# *** TASK STIMULI ***
# ********************

# Setup fixation cross
fixation = visual.TextStim(win, text="+", color = 'black', pos = [0, 0], autoLog = False)

# Setup target stimulus
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Stimuli directories
glare_Filename = _thisDir + os.sep + 'Stimuli' + '/' + 'glare_stim_gray.png';
nonglare_Filename = _thisDir + os.sep + 'Stimuli' + '/' + 'nonglare_stim_gray.png';

# Glare stimuli
glare_target = visual.ImageStim(
    win=win,
    name='glare',
    image=glare_Filename,
    ori=0.0, pos=left_loc, size=(7, 7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=0.0)
   
# Non-glare stimuli 
nonglare_target = visual.ImageStim(
    win=win,
    name='nonglare',
    image=nonglare_Filename,
    ori=0.0, pos=right_loc, size=(7, 7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=0.0)

test_target = visual.ImageStim(win, image = glare_Filename, autoLog=False)

# *************************
# *** TASK INSTRUCTIONS ***
# *************************

# Create text screens to display later:
instructions = visual.TextStim(win, text='', color='white', pos=[0, 2])  #This is an empty instructions screen to be filled with text below
    
# *******************
# *** TASK TIMERS ***
# *******************

block_timer = core.Clock()
timer = core.Clock()
stim_timer = core.Clock()
ISI_timer = core.Clock()
random_stim_timer = core.Clock()
buffer_timer = core.Clock()

# ************************
# *** INITIATE EYELINK ***
# ************************

# EyeLink Dummy mode? - Set to False if testing with actual system
if info['EyeLink'] == 'y':
    dummy_mode = False
    
elif info['EyeLink'] == 'n':
    dummy_mode = True

# Step 1: Connect to the EyeLink Host PC

# The Host IP address, by default, is "100.1.1.1".
# the "el_tracker" objected created here can be accessed through the Pylink
# Set the Host PC address to "None" (without quotes) to run the script
# in "Dummy Mode"
if dummy_mode:
    el_tracker = pylink.EyeLink(None)
else:
    try:
        el_tracker = pylink.EyeLink("100.1.1.1")
    except RuntimeError as error:
        print('ERROR:', error)
        core.quit()
        sys.exit()
    
# Step 2: Open an EDF data file on the Host PC

# Define edf fileanme
edf_file = edf_fname + ".EDF"

try:
    el_tracker.openDataFile(edf_file)
except RuntimeError as err:
    print('ERROR:', err)
    # close the link if we have one open
    if el_tracker.isConnected():
        el_tracker.close()
    core.quit()
    sys.exit()

# Step 3: Configure the tracker

# Put the tracker in offline mode before we change tracking parameters
el_tracker.setOfflineMode()

# Get the software version:  1-EyeLink I, 2-EyeLink II, 3/4-EyeLink 1000,
# 5-EyeLink 1000 Plus, 6-Portable DUO
if dummy_mode:
    eyelink_ver = 0  # set version to 0, in case running in Dummy mode
else:
    eyelink_ver = 5
    
if not dummy_mode:
    vstr = el_tracker.getTrackerVersionString()
    eyelink_ver = int(vstr.split()[-1].split('.')[0])
    # print out some version info in the shell
    print('Running experiment on %s, version %d' % (vstr, eyelink_ver))

# File and Link data control
# what eye events to save in the EDF file, include everything by default
file_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT'
# what eye events to make available over the link, include everything by default
link_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,BUTTON,FIXUPDATE,INPUT'
# what sample data to save in the EDF data file and to make available
# over the link, include the 'HTARGET' flag to save head target sticker
# data for supported eye trackers
if eyelink_ver > 3:
    file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,HTARGET,GAZERES,BUTTON,STATUS,INPUT'
    link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,HTARGET,STATUS,INPUT'
else:
    file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,GAZERES,BUTTON,STATUS,INPUT'
    link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,INPUT'
el_tracker.sendCommand("file_event_filter = %s" % file_event_flags)
el_tracker.sendCommand("file_sample_data = %s" % file_sample_flags)
el_tracker.sendCommand("link_event_filter = %s" % link_event_flags)
el_tracker.sendCommand("link_sample_data = %s" % link_sample_flags)

# Set EyeLink sample rate
if eyelink_ver > 2 and not dummy_mode:
    el_tracker.sendCommand("sample_rate 1000")
    
# Choose a calibration type, H3, HV3, HV5, HV13 (HV = horizontal/vertical),
el_tracker.sendCommand("calibration_type = HV9")
# Set a gamepad button to accept calibration/drift check target
# You need a supported gamepad/button box that is connected to the Host PC
el_tracker.sendCommand("button_function 5 'accept_target_fixation'")

# Shrink the spread of the calibration/validation targets
# if the default outermost targets are not all visible in the bore.
# The default <x, y display proportion> is 0.88, 0.83 (88% of the display
# horizontally and 83% vertically)
el_tracker.sendCommand('calibration_area_proportion 0.88 0.83')
el_tracker.sendCommand('validation_area_proportion 0.88 0.83')

# Get the native screen resolution used by PsychoPy
scn_width, scn_height = win.size

# Resolution fix for Mac retina displays
if 'Darwin' in platform.system():
    if use_retina:
        scn_width = int(scn_width/2.0)
        scn_height = int(scn_height/2.0)
        
# Optional: online drift correction.
# See the EyeLink 1000 / EyeLink 1000 Plus User Manual

# Online drift correction to mouse-click position:
# el_tracker.sendCommand('driftcorrect_cr_disable = OFF')
# el_tracker.sendCommand('normal_click_dcorr = ON')

# Online drift correction to a fixed location, e.g., screen center
el_tracker.sendCommand('driftcorrect_cr_disable = OFF')
el_tracker.sendCommand('online_dcorr_refposn %d,%d' % (int(scn_width/2.0),
                                                        int(scn_height/2.0)))
el_tracker.sendCommand('online_dcorr_button = ON')
el_tracker.sendCommand('normal_click_dcorr = OFF')

# Pass the display pixel coordinates (left, top, right, bottom) to the tracker
# see the EyeLink Installation Guide, "Customizing Screen Settings"
el_coords = "screen_pixel_coords = 0 0 %d %d" % (scn_width - 1, scn_height - 1)
el_tracker.sendCommand(el_coords)

# Write a DISPLAY_COORDS message to the EDF file
# Data Viewer needs this piece of info for proper visualization, see Data
# Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
dv_coords = "DISPLAY_COORDS  0 0 %d %d" % (scn_width - 1, scn_height - 1)
el_tracker.sendMessage(dv_coords)

# Configure a graphics environment (genv) for tracker calibration
genv = EyeLinkCoreGraphicsPsychoPy(el_tracker, win)
print(genv)  # print out the version number of the CoreGraphics library

# Set background and foreground colors for the calibration target
# in PsychoPy, (-1, -1, -1)=black, (1, 1, 1)=white, (0, 0, 0)=mid-gray
foreground_color = (-1, -1, -1)
background_color = win.color # Use the same background color as the entire study
genv.setCalibrationColors(foreground_color, background_color)

# Set up the calibration target

# Use a picture as the calibration target
genv.setTargetType('circle')
genv.setTargetSize(24)
#genv.setPictureTarget(os.path.join('images', 'fixTarget.bmp')) #CALIBRATION TARGET IMAGE

# Configure the size of the calibration target (in pixels)
# this option applies only to "circle" and "spiral" targets
# genv.setTargetSize(24)

# Beeps to play during calibration, validation and drift correction
# parameters: target, good, error
#     target -- sound to play when target moves
#     good -- sound to play on successful operation
#     error -- sound to play on failure or interruption
# Each parameter could be ''--default sound, 'off'--no sound, or a wav file
genv.setCalibrationSounds('off', 'off', 'off')

# Resolution fix for macOS retina display issues
if use_retina:
    genv.fixMacRetinaDisplay()

# Request Pylink to use the PsychoPy window we opened above for calibration
pylink.openGraphicsEx(genv)

#calibration task constants
#set random seed
rng = np.random.default_rng()

#movie File
#ShowMovie = True
#if ShowMovie:
#    #      VIDEO PATH --> from relative path (same dir as script)                                    
#    movie_Filename = _thisDir + os.sep + 'WHITENOISE.avi';
#    if not os.path.exists(movie_Filename):
#        raise RuntimeError("Video File could not be found:" + os.path.split(movie_Filename)[1])
#movie = visual.MovieStim3(win, movie_Filename, size = resolution, pos = (0,0), loop = True, autoLog=False)
#       
# ************************
# *** CUSTOM FUNCTIONS ***
# ************************

def clear_screen(win):
    """ clear up the PsychoPy window""" 
    win.fillColor = genv.getBackgroundColor()
    win.flip()

def terminate_task():
    """ Terminate the task gracefully and retrieve the EDF data file
    file_to_retrieve: The EDF on the Host that we would like to download
    win: the current window used by the experimental script
    """
    el_tracker = pylink.getEYELINK()
    if el_tracker.isConnected():
        error = el_tracker.isRecording()
        if error == pylink.TRIAL_OK:
            abort_trial()
        el_tracker.setOfflineMode()
        el_tracker.sendCommand('clear_screen 0')
        pylink.msecDelay(500)
        el_tracker.closeDataFile()         
        el_tracker.sendMessage('End EyeLink Recording')
        el_tracker.close()
    win.close()
    core.quit()
    sys.exit()
    
def abort_trial():   
    """Ends recording abruptly"""
    el_tracker = pylink.getEYELINK()
    if el_tracker.isRecording():
        pylink.pumpDelay(100)
        el_tracker.stopRecording()  
    clear_screen(win)
    bgcolor_RGB = (116, 116, 116)
    el_tracker.sendMessage('!V CLEAR %d %d %d' % bgcolor_RGB)
    el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_ERROR)
    return pylink.TRIAL_ERROR

def end_experiment() -> None: #DEBUG CRASHES HERE
    '''End of Experiment'''
    logging.log(level=logging.EXP,msg='*** END EXPERIMENT ***')
    el_tracker.sendMessage('*** END EXPERIMENT ***')
    pylink.pumpDelay(100)
    el_tracker.stopRecording()
    terminate_task()
    #instructions_screens('Exiting task!\nPlease hold still.\n\nAn experimenter will communicate with you shortly.') 
    core.wait(2)
    win.close()
   
def quit_task() -> None:
    '''quit task based off of button press'''
    allKeys = event.getKeys(['p','escape'])
    if allKeys != None:
        for thisKey in allKeys:
            if thisKey in ['p', 'escape']:
                end_experiment()
                
def instruction_continue():

    # Wait for key press
    key = event.waitKeys(keyList=['space', 'escape', 'p'])

    # End experiment
    if np.in1d(key,['escape','p']):
        end_experiment()

def MRI_trigger():
    """Wait for MRI to trigger task"""
    
    # Log
    logging.log(level=logging.EXP,msg='Waiting for MRI trigger')
    el_tracker.sendMessage('Waiting for MRI trigger')
        
    # On-screen text
    MRI_instructions = visual.TextStim(win, text='Waiting for MRI to start. Standby...', color = genv.getForegroundColor(), wrapWidth = scn_width/2) 
    MRI_instructions.draw()
    win.flip()

    # Wait for key press
    key = event.waitKeys(keyList=['5','t','escape', 'p'])

    # If pressed escape quit task
    if np.in1d(key,['escape','p']):
       end_experiment()
       
    # Log
    logging.log(level=logging.EXP,msg='MRI trigger received')
    el_tracker.sendMessage('MRI trigger received')
    
def stim_type_randomizer():
    
    stim_index = [0] + [1] 
    
    stim_choice = random.choice(stim_index)
    
    #keep each side about equal
    if(len(stim_record) > 10):
        total_ones = np.sum(stim_record)
        ones_fraction = total_ones/len(stim_record)
        if(ones_fraction > .60):
            stim_choice = 0
        elif(ones_fraction < .40):
            stim_choice = 1
         
    stim_record.append(stim_choice)
    return(stim_choice)

def location_randomizer():
    
    location_index = [0] + [1] 
    
    location_choice = random.choice(location_index)
    
    #keep each side about equal
    if(len(location_record) > 10):
        total_ones = np.sum(location_record)
        ones_fraction = total_ones/len(location_record)
        if(ones_fraction > .60):
            location_choice = 0
        elif(ones_fraction < .40):
            location_choice = 1

    location_record.append(location_choice)
    return location_choice
    
def glare_phase():
    
    '''returns an array of the fraction found to be correct on the right and left side'''
    logging.log(level=logging.EXP,msg='Starting Glare')
    
    #movie.setAutoDraw(True)
    num_stim = 2
    answers = []
    #rng.shuffle(opacities)
    trial_counter = 0
    locations = []
    
    # Block counter reset
    block_counter = 1

    #Loop over blocks
    for block in range(max_num_blocks):
        
        # Block Start Screen
        block_start = visual.TextStim(win, text="Are you ready to start Block "+str(block_counter)+"?", color='black')

        # Show break screen
        block_start.draw()
        win.flip()
        
        # Continue or quit
        instruction_continue()
        
        # MRI trigger
        MRI_trigger()
        
        # Log
        logging.log(level=logging.EXP,msg='Block ' + str(block_counter))

        # Send EyeLink Message
        el_tracker.sendMessage("Block %d" % (block_counter))

        # Track time taken to complete block
        block_start = time.time()
    
        # Loop over trials/stimuli
        for stim in range(num_stim):
            
            quit_task()
           
            # Select the pre and post stimulus durations
            trial_pre_stim_time = random.randint(ISI_min_duration_sec,ISI_max_duration_sec)
            trial_post_stim_time = random.randint(ISI_min_duration_sec,ISI_max_duration_sec)
       
            # Count the number of trials
            trial_counter = trial_counter+1
            
            # Select the stimulus location
            location_choice = location_randomizer()
            
            # Selec the stimulus type
            stim_choice = stim_type_randomizer()
            
            # Wait pre-stimulus ISI
            fixation.setAutoDraw(True)
            timer.reset()
            while timer.getTime() < trial_pre_stim_time:
                win.update()
                pass
            
            # Display stimulus
            
            # If glare stimulus
            if stim_choice == 1:
                
                # Right
                if location_choice == 0:
                    glare_target.pos = right_loc
                    
                # Left
                elif location_choice == 1:
                    glare_target.pos = left_loc
            
                glare_target.setAutoDraw(True)
                
                # Log
                logging.log(level=logging.EXP,msg='Draw Glare Stimulus')
                el_tracker.sendMessage('Draw Glare Stimulus')
    
            # If nonglare stimulus
            else:
               
               # Right
                if location_choice == 0:
                    nonglare_target.pos = right_loc
                    
                # Left
                elif location_choice == 1:
                    nonglare_target.pos = left_loc
            
                nonglare_target.setAutoDraw(True)
            
                # Log
                logging.log(level=logging.EXP,msg='Draw Non-Glare Stimulus')
                el_tracker.sendMessage('Draw Non-Glare Stimulus')
    
            win.update()
            
            # Display for target duration
            timer.reset()
            while timer.getTime() < target_duration:
                win.update()
                pass
            
            key_pressed = False
            glare_target.setAutoDraw(False)
            nonglare_target.setAutoDraw(False)
            win.update()
            
            key_count = 0 #make sure it does not exceed 1 during the time period
            
            # Wait post-stimulus time
            timer.reset()
            while timer.getTime() < trial_post_stim_time:
                win.update()
                thisResp = 0
                allKeys = event.getKeys(['1', '2', 'p','escape']) 
                
                for thisKey in allKeys:
                    key_count +=1
                    key_pressed = True
                    if key_count == 1:
                        
                        # Saw stim
                        if thisKey == '1' or thisKey == '2':
                           thisResp = 1  # correct/seen
                           
                           # Log 
                           logging.log(level=logging.EXP,msg='Perceived Stimulus')
                           el_tracker.sendMessage('Perceived Stimulus')
                        
                        if thisResp == 1:
                            answers = np.append(answers, 1)

                        elif thisKey in ['p', 'escape']:
                            core.quit() 
                        else:
                            thisResp = 0
                            answers = np.append(answers, 0)
                pass
            
            # Stimulus appeared but no key press
            if(key_pressed == False):
                answers = np.append(answers, 0)
                
        # Store cali behaviors and parameters
        answers = np.asarray(answers)
        #movie.setAutoDraw(False)
        fixation.setAutoDraw(False)
        clear_screen(win)
        
        # End of Block
        
        # End block time
        block_end = time.time()

        # Log
        logging.log(level=logging.EXP,msg='Block '+str(block_counter)+' duration: ' + str(block_end-block_start))

        # Block Break Screen
        block_break = visual.TextStim(win, text="Great job! Take a break.\n\nYou completed block "+str(block_counter)+".", color='black')

        # Show break screen
        block_break.draw()
        win.flip()
        
        # Continue or quit
        instruction_continue()
        
        # Add to block counter
        block_counter = block_counter + 1

# ******************************************
# *** Define RealEyeLink Class Functions ***
# ******************************************

class RealEyeLink:
    
    '''Object to create a real eyelink event'''
    
    def __init__(self):
        '''Parameters
           ----------
        eyelink_ver: float
            Version of eyelink this experiment is running on
           '''
                    
    def instruction_continue(self) -> None:
        '''Either allows the subject to continue to the next screen of the task or exit'''
        wait_for_keypress = True # Wait indefinitely, terminates upon any key press
        if wait_for_keypress:
            event.waitKeys(keyList = ['space','escape','p','o'])
            clear_screen(win)
            
    def instructions_screens(self, instruction: str) -> None: 
        '''Function presents all the instructions needed for the task'''
        task_instructions = visual.TextStim(win, instruction, color = genv.getForegroundColor(), wrapWidth = scn_width/2, units = 'cm')
        clear_screen(win)
        task_instructions.draw()
        win.flip()   
        self.instruction_continue()
    
    def start_experiment(self) -> None:
        self.instructions_screens("Main Task Phase.\n\nAre you ready to start?")
        quit_task()

# *********************
# *** MAIN FUNCTION ***
# *********************
    
def main():

    # *********************
    # *** Setup EyeLink ***
    # *********************
    
    rel = RealEyeLink() #sets up real eyelink object

    # If running EyeLink
    if not dummy_mode:
        task_msg = 'Press O to calibrate tracker'
        rel.instructions_screens(task_msg)
    
    if not dummy_mode:
        try:
            el_tracker.doTrackerSetup()
        except RuntimeError as err:
            print('ERROR:', err)
            el_tracker.exitCalibration()
            
    el_tracker.setOfflineMode()
    
    try:
        el_tracker.startRecording(1, 1, 1, 1)
    except RuntimeError as error:
        print("ERROR:", error)
        rel.terminate_task()

    eye_used = el_tracker.eyeAvailable()
    
    if eye_used == 1:
        el_tracker.sendMessage("EYE_USED 1 RIGHT")
    elif eye_used == 0 or eye_used == 2:
        el_tracker.sendMessage("EYE_USED 0 LEFT")
        eye_used = 0
    else:
        print("Error in getting the eye information!")
    pylink.pumpDelay(100)
    
    # *******************************
    # *** Beginning of Experiment ***
    # *******************************
    
    #rel.instructions_screens("Experiment is setup!\n\nLet's get started!")

    # *******************************
    # ********* Test Keys ***********
    # ******************************* 
    
    logging.log(level=logging.EXP,msg='Check that buttons are working')
    #rel.instructions_screens("Let's confirm the buttons are working...")
    
    # Check '1'
    task_instructions = visual.TextStim(win, "Please press '1'",color = 'black', pos = [0, 0], units = 'cm')
    clear_screen(win)
    task_instructions.draw()
    win.flip() 
    
    # Only continue if the subject presses 1
    allKeys = event.waitKeys(keyList = ['1'])
    
    # Check '2'
    task_instructions = visual.TextStim(win, "Please press '2'",color = 'black', pos = [0, 0], units = 'cm')
    clear_screen(win)
    task_instructions.draw()
    win.flip() 
    
    # Only continue if the subject presses 2
    allKeys = event.waitKeys(keyList = ['2'])
    #rel.instructions_screens("Good Job! This key is working.")
    
    # *******************************
    # *** Beginning of Experiment ***
    # *******************************
    #rel.instructions_screens("Please fixate on the\n\nblack fixation point at all times.")
    #rel.instructions_screens("This is the face stimulus you will see.\n\nIt will not be as clear or bright as this example.")

    glare_target.setAutoDraw(True)
    nonglare_target.setAutoDraw(True)
    fixation.setAutoDraw(True)
    win.update()

    allKeys = event.waitKeys(keyList = ['space'])
    
    nonglare_target.setAutoDraw(False)
    glare_target.setAutoDraw(False)
    fixation.setAutoDraw(False)
    win.update()
    
    #rel.instructions_screens("The stimulus will appear and disappear quickly")
#    test_count = 1
#    while test_count < 5:
#        
#        if(test_count%2 == 1):
#            nonglare_target.pos = (-8,0)
#        else:
#            nonglare_target.pos = (8,0)
#        
#        timer.reset()
#        
#        fixation.setAutoDraw(True)
#        nonglare_target.setAutoDraw(True)
#        
#        while timer.getTime() < target_duration:
#            win.update()
#            pass
#        
#        nonglare_target.setAutoDraw(False)
#        win.update()
#        test_count = test_count + 1
#        timer.reset()
#        while timer.getTime() < post_cali_time:
#            win.update()
#            
#    fixation.setAutoDraw(False)
    
    # Glare Phase
    glare_phase()
    
    # *********************************
    # *** Start the Main Experiment ***
    # *********************************
    
#    rel.start_experiment()
#    
#    # Setup block counter
#    block_counter = 1
#    
#    # Log
#    logging.log(level=logging.EXP,msg='Starting Main Task Phase')
#    el_tracker.sendMessage("Starting Main Task Phase")
#    
#    # Loop over task blocks
#    while block_counter <= max_num_blocks:
#        
#        #log 
#        if input_x and block_counter == 1: #if inputs
#            x = input_x
#            fraction = input_fraction
#            lamb_ = input_lambda_
#            k_ = input_k_
#            logging.log(level=logging.EXP,msg='Calibration Fractions ' + str(fraction))
#            logging.log(level=logging.EXP,msg='Calibration sigmoid k ' + str(k_))
#            logging.log(level=logging.EXP,msg='Calibration sigmoid lambda ' + str(lamb_))
#            logging.log(level=logging.EXP,msg='Calibration x-values ' + str(x))
#            
#        
#        # Log
#        #logging.log(level=logging.EXP,msg='Real Time Block ' + str(block_counter))
#        el_tracker.sendMessage('Real Time Block ' + str(block_counter))
#        
#        # Count blocks
#        block_instruction = 'Starting Block #' + str(block_counter) + "\n\nAre you ready?"
#        
#        # Display instructions
#        rel.instructions_screens(block_instruction)
#        
#        # MRI Trigger
#        MRI_trigger()
#        
#        # Initialize variable
#        decision_arr = []
#        
#        # Log
#        logging.log(level=logging.EXP,msg='Starting Block ' + str(block_counter))
#        el_tracker.sendMessage('Starting Block ' + str(block_counter))
#
#        # Reset ISI timer
#        ISI_timer.reset()
#
#        # Reset block timer
#        block_timer.reset()
#        
#        # Wait block duration
#        while block_timer.getTime() < block_duration_sec:
#    
#            #Get all pressed keys
#            allKeys = event.getKeys(['1','2','p','escape'])
#
#            # If a key was pressed
#            if allKeys != None:
#
#                # Loop over key presses
#                for thisKey in allKeys:
#
#                    # Response condition 1
#                    if info['Response Condition (1 or 2)'] == '1':
#                    
#                        # Button Press: 1
#                        if thisKey in '1': # SHARIF NOTE: Add condition to confirm the stimulus is on the left side
#                            # if the stimulus was within the response time (response_time_max_sec)
#                                    
#                            # Log
#                            logging.log(level=logging.EXP,msg='Perceived Stimulus')
#                            el_tracker.sendMessage('Perceived Stimulus')
#                                    
#                        # Button Press: 2
#                        elif thisKey in '2': # SHARIF NOTE: Add condiiotn to confirm the stimulus is on the right side
#                               
#                            #log
#                            logging.log(level=logging.EXP,msg='Perceived Stimulus')
#                            el_tracker.sendMessage('Perceived Stimulus')
#                            
#                            # if the stimulus was within the response time (response_time_max_sec)
#                        # End experiment
#                        elif np.in1d(thisKey,['escape','p']):
#                            end_experiment()
#        
#                    # Response condition 2
#                    elif info['Response condition (1 or 2)'] == '2':
#                        # Button Press: 2
#                        if thisKey in '1':
#                        
#                            # if the stimulus was within the response time (response_time_max_sec)
#                        
#                            # Log
#                            logging.log(level=logging.EXP,msg='Perceived Stimulus')
#                            el_tracker.sendMessage('Perceived Stimulus')
#                                    
#                        # Button Press: 2
#                        elif thisKey in '2':
#                            # if the stimulus was within the response time (response_time_max_sec)
#                                    
#                            # Log
#                            logging.log(level=logging.EXP,msg='Perceived Stimulus')
#                            el_tracker.sendMessage('Perceived Stimulus')
#                                    
#                        # End experiment
#                        elif np.in1d(thisKey,['escape','p']):
#                           quit_task()
#                           
#
#            # Display fixation/movie
#            movie.setAutoDraw(True)
#            fixation.setAutoDraw(True)
#            win.update()
#
#            # Build search window
#            sd.build_search_window()
#
#            # Look for peak/trough and display stimulus is conditions are met
#            decision_arr.append(sd.stim_type())
#        
#        # Log
#        logging.log(level=logging.EXP,msg='All Buffer Duration Times: ' + str(sd.get_buffer_duration_time()))
#        logging.log(level=logging.EXP,msg='All Search Window Exterma Decisions: ' + str(decision_arr))
#        
#        logging.log(level=logging.EXP,msg='Finished Real Time Block ' + str(block_counter))
#        el_tracker.sendMessage('Finished Real Time Block ' + str(block_counter))
#        
#        # Remove fixation
#        movie.setAutoDraw(False)
#        fixation.setAutoDraw(False)
#        win.update()
#        
#        #global fraction
#        random_answers = sd.get_random_stim_correct_count()
#
#        total_correct_random = np.sum(random_answers)
#        random_correct_fraction = total_correct_random/len(random_answers)
#    
#        # Log
#        logging.log(level=logging.EXP,msg='Random Correct Fraction ' + str(random_correct_fraction))
#        
#        #add new fraction to x and fraction
#        fraction = np.append(fraction, random_correct_fraction)
#        fraction.flatten()
#        x = np.append(x,opacity_thresh)
#        x.flatten()
#            
#        # Calculate sigmoid function
#        (k_, lamb_), _ = curve_fit(sigmoid, x, fraction)
#        
#        # Find new threshold opacity value
#        p = -np.log(1 - opacity_threshold_constant)
#        opacity_thresh = lamb_ * math.pow(p, (1/k_))
#            
#        # Log
#        logging.log(level=logging.EXP,msg='New Calibration Fractions ' + str(fraction))
#        logging.log(level=logging.EXP,msg='New Calibration sigmoid k ' + str(k_))
#        logging.log(level=logging.EXP,msg='New Calibration sigmoid lambda ' + str(lamb_))
#        logging.log(level=logging.EXP,msg='New Calibration x-values ' + str(x))
#        logging.log(level=logging.EXP,msg='Opacity Threshold ' + str(opacity_thresh))
#                
#        # change threshold if no peaks found 
#        if(sd.get_peak() == 0):
#            
#            curr_thresh = sd.get_peak_threshold()
#            new_thresh = 0
#
#            # Log
#            logging.log(level=logging.EXP,msg='No Peaks found in this block! Changing threshold')
#            logging.log(level=logging.EXP,msg='New Peak Threshold: ' + str(new_thresh))
#            
#            sd.set_peak_threshold(new_thresh)
#            
#        # change threshold if no troughs found 
#        if(sd.get_trough() == 0):
#            
#            curr_thresh = sd.get_trough_threshold()
#            new_thresh = 0
#            
#            # Log
#            logging.log(level=logging.EXP,msg='No Troughs found in this block! Changing threshold')
#            logging.log(level=logging.EXP,msg='New Trough Threshold: ' + str(new_thresh))
#            
#            sd.set_trough_threshold(new_thresh)
#            
#        rel.instructions_screens('Finished Block #' + str(block_counter))
#        
#        # Add to block counter
#        block_counter = block_counter + 1
#            
    # *******************************
    # ***** End of Experiment *******
    # *******************************
    
    #rel.instructions_screens("Exiting task!\nPlease hold still.\n\nAn experimenter will communicate with you shortly.")
    end_experiment()
            
if __name__ == "__main__":
    main()