
from __future__ import print_function
from __future__ import division
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import time
import copy
import math
import random
import numpy
from array import array
import datetime
from psychopy import prefs
prefs.general['audioLib'] = ['pygame']
from psychopy import visual,core,data,event,gui
from psychopy import sound
from psychopy.constants import *  # things like STARTED, FINISHED

########################################################################################
# Draw a box to get experiment and participant information
########################################################################################
expName = u'Flashing_grid_task'  # Name the experiment
expInfo = {u'Session': u'001', u'Participant': u'001'} # What the box should ask for
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName) # Draw the bloody box!
if dlg.OK == False: core.quit() # If "cancel" is clicked end the whole thing
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
########################################################################################
########################################################################################


########################################################################################
# Where To Write File
########################################################################################
# Setup files for saving
if not os.path.isdir('Flash_Grid_Results'): # Create this folder wherever this script is saved
    os.makedirs('Flash_Grid_Results')  # If this fails (e.g. permissions) we will get error
filename = 'Flash_Grid_Experiment_' + '%s_%s' %(expInfo['Participant'], expInfo['date'])+'.txt'
print('filename used for data is ' +filename)
########################################################################################
########################################################################################

# flag for 'escape' or other condition => quit the exp
endExpNow = False

# Setup the Window
win = visual.Window(size=[1000, 700], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='700 x 700', color='grey', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess 

# Define the main clock
#rtclock = core.Clock() # Defined here


########################################################################################
# Changeable experimental parameters
########################################################################################
# Number of experimental trials
numtrials = 5

# Fixation cross
fcross = visual.TextStim(win, text="+")  

# Introduction text
one = '''Introduction text here.'''
introtext = visual.TextStim(win, text=one)  

# End of experiment text
two = '''The experiment has now finished.'''
endtext = visual.TextStim(win, text=two)  

# orange???
color1 = [0.9686,    0.6392,    0.0353]
#blue
color2 = [-0.8980, 1.0000, 1.0000] 

# Define clock
checkclock = core.Clock()
########################################################################################
########################################################################################


########################################################################################
# List That Will Record Responses & RTs
########################################################################################
#List That Will Record Responses & RTs
keyspressed = []*numtrials
correctresponse = []*numtrials
RT =[]*numtrials
trialNo = []*numtrials
########################################################################################
########################################################################################


########################################################################################
########################################################################################
# Initialize components for Routine "init_experiment"
init_experimentClock = core.Clock()
# set_colors()
# Colors used during the experiment.s
def set_colors():
    global sc_c # screen color
    global f_c # frame color
    global sq_c # square color
    # 1 = white
    # -0.06 = grey 80
    # -0.37 = grey 120
    # -1 = black
    sc_c = 1
    f_c = -0.06
    sq_c = -0.37
    t_c = -0.06

# set_sizes()
# Sizes used during the experiment
def set_sizes():
    global f_s # frame size (square) (frame surrounding the stimulus)
    global sq_s # square size (square where the stimulus is shown)
    global l_s # line size (the width of the line surrounding the stimulus)
    f_s = 540
    sq_s = 800
    l_s = 100

# set_positions()
# Positions used during the experiment
#def set_positions():
#    global fl_p # Where should the flash be drawn
#    fl_p = [-300, 0]

# set_positions()
# Positions used during the experiment
#def set_positions2():
#    global fl_p2 # Where should the flash be drawn
#    fl_p2 = [300, 0]

########################################################################################
# Set main conditions and loop
########################################################################################


# Counter to keep track of things
counter = 0
thecount = 0

# Create trial conditions and shuffle them
trialcondition = [1,1,2,2,1,2,1]
numpy.random.shuffle(trialcondition)
print("trial conditions after shuffle =", trialcondition)

for i in range(numtrials):
    
    # Set the position of left stimulus
    def set_positions():
        global fl_p # Where should the flash be drawn
        if trialconditionx == 2: # Difficult condition
            fl_p = [-100, 0]
        elif trialconditionx == 1: # Easy condition
            fl_p = [-300, 0]
    
    # Set the position of right stimulus
    def set_positions2():
        global fl_p2 # Where should the flash be drawn
        if trialconditionx == 2: # Difficult condition
            fl_p2 = [100, 0]
        elif trialconditionx == 1: # Easy condition
            fl_p2 = [300, 0]
        
    # Set the condition
    trialconditionx = trialcondition[counter]

    # Set difficulty levels
    if trialconditionx == 2: # Difficult condition
        p1 = .45
        p2 = .55
    elif trialconditionx == 1: # Easy condition
        p1 = .70
        p2 = .30


    # flash stimulus functions
    # flash initialization
    def flash_init(win, position=[0,0], position2=[0,0], square_size=10, columns=20, rows=20, percent_color1=p1, percent_color2=p2): # Colour 1 being manipulated
        global flash # The flash stimulus (an array of flashing squares)
        global flash2
        red = [1, -1, -1]
        green = [-1, 1, -1]
        color_set = [color1, color2] # only show two colours for now
        color_set2 = [color1, color2]  # only show two colours for now
        cell_number = columns * rows
    
        num_color1 = int(np.floor(float(cell_number)*percent_color1)) # First colour
        num_color2 = int(np.floor(float(cell_number)*(1-percent_color1))) # Second colour
    
        num_color3 = int(np.floor(float(cell_number)*percent_color2)) # First colour
        num_color4 = int(np.floor(float(cell_number)*(1-percent_color2))) # Second colour
        
        #print(cell_number,num_color1,num_color2)
        
        # fill an array with colors. Each color should appear approximatively the same number of times.
        f_colors = []
        for i in range(num_color1):
            f_colors.append(color_set[0])
        for i in range(num_color2):
            f_colors.append(color_set[1])
        numpy.random.shuffle(color_set)
        i = cell_number - len(f_colors)
        while i > 0:
            f_colors.append(color_set[i])
            i -= 1
        
        f_colors2 = []
        for i in range(num_color3):
            f_colors2.append(color_set2[0])
        for i in range(num_color4):
            f_colors2.append(color_set2[1])
        numpy.random.shuffle(color_set2)
        i = cell_number - len(f_colors2)
        while i > 0:
            f_colors2.append(color_set2[i])
            i -= 1
        
        # randomize color order.
        shuffle(f_colors)
        shuffle(f_colors2)
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys.append((x_left + c * square_size, y_top + l * square_size))
        
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys2 = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys2.append((x_left + c * square_size, y_top + l * square_size))
        
        # MAIN FUNCTION TO CREATE FIRST GRID
        flash = visual.ElementArrayStim(win=win,
                            fieldPos=position,
                            fieldShape='sqr',
                            nElements=cell_number,
                            sizes=square_size,
                            xys=xys,
                            colors=f_colors,
                            elementTex=None,
                            elementMask=None,
                            name='flash',
                            autoLog=False)
                            
        # MAIN FUNCTION TO CREATE SECOND GRID
        flash2 = visual.ElementArrayStim(win=win,
                        fieldPos=position2,
                        fieldShape='sqr',
                        nElements=cell_number,
                        sizes=square_size,
                        xys=xys2,
                        colors=f_colors2,
                        elementTex=None,
                        elementMask=None,
                        name='flash',
                        autoLog=False)
                            
                            
    
    # flash stimulus change
    def flash_change():
        global flash
        shuffle(flash.colors)
        flash.setColors(flash.colors)
    
    def flash2_change():
        global flash2
        shuffle(flash2.colors)
        flash2.setColors(flash2.colors)
    
    # Time variables used during the experiment
    def set_timing():
        global f_t 
        f_t = 5 # The duration (in frame) of a flash image presentation
    
    # data_init
    set_colors()
    set_sizes()
    set_positions()
    set_positions2()
    set_timing()
    
    #############################
    # MAIN FUNCTION HERE
    flash_init(win, fl_p, fl_p2, square_size=5, columns=30, rows=30) # set the parameters here for the function!!
    #############################
    
    # Initialize components for Routine "show_flash"
    show_flashClock = core.Clock()
    frame_fl = visual.ImageStim(win=win, name='frame_fl',
        image=None, mask=None,
        ori=0, pos=fl_p, size=f_s,
        color=f_c, colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    
    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    
    #------Prepare to start Routine "init_experiment"-------
    t = 0
    frameN = -1
    
    #------Prepare to start Routine "show_flash"-------
    t = 0
    show_flashClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # flash begin routine
    f_change = 0
    
    # keep track of which components have finished
    show_flashComponents = []
    show_flashComponents.append(frame_fl)
    for thisComponent in show_flashComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    ########################################################################################
    ########################################################################################
    
    
    ########################################################################################
    # MAIN EXPERIMENT
    ########################################################################################
    
    # Put up the introduction text 
    if counter == 0:
        introtext.draw()
        win.flip()
        keypressed = event.waitKeys(timeStamped=False)
        checkclock.reset()
    
    #---Start Routine "show_flash"-------
    continueRoutine = True
    while continueRoutine:
#        thecount = thecount+1
#        print("The count =", thecount)
#        
#        if thecount == 1:
#            rtclock.reset() # Reset the clock here
            
        # Hides mouse
        mouse = event.Mouse(visible=0)
        
        # get current time
        t = show_flashClock.getTime()
        #print("t =", t)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        # update/draw components on each frame
        #print(frameN)
        
        # *frame_fl* updates
        if t >= 0.0 and frame_fl.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_fl.tStart = t  # underestimates by a little under one frame
            frame_fl.frameNStart = frameN  # exact frame index
            frame_fl.draw()
        # flash each frame
        if frameN >= f_change:
            flash_change()
            flash2_change()
            f_change += f_t
        flash.draw()  # First stimulus is drawn here
        flash2.draw() # Second stimulus is drawn here
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_flashComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
             
        # RESPONSE 1
        if event.getKeys(keyList=["left"]):
            
            # Track response times
            #rt = rtclock.getTime()
#            time2 = checkclock.getTime()
#            print("Response time =", time2)
#            RT.append(time2)
            
            # Keep track of correct/incorrect responses
            if trialconditionx == 2:
                correctresponse.append('1')
            elif trialconditionx == 1:
                correctresponse.append('0')
            print(correctresponse)
            
            # Keep track of keys pressed
            keyspressed.append('left')
            print(keyspressed)
                
            print("actual trial condition just completed", trialconditionx)
            
            # Update the counter
            counter = counter+1
            
            # Keep track of trial number to be saved 
            trialNo.append(counter)
            print(trialNo)
            
            time2 = checkclock.getTime()
            print("Response time =", time2)
            RT.append(time2)
            
            # DRAW FIXATION CROSS AFTER EACH TRIAL
            win.flip() # Clears the window
            fcross.draw() # Draw the fixation cross
            win.flip() # Clears the window
            core.wait(2.0) # Keep the cross on screen for 2 seconds
            checkclock.reset()
            
            # END THE EXPERIMENT HERE AND SAVE DATA
            if counter == numtrials:
                win.flip() # Clears the window
                endtext.draw() # Draw ending message here
                win.flip() # Clears the window
                core.wait(3.0)
                
                #####################################################################
                #Write Data To File
                #####################################################################
                
                # Write RESULTS To A File 
                os.chdir("Flash_Grid_Results") # move to folder called RESULTS, need to CREATE this if it does not exist already.
                fout = open(filename, 'w')
                fout.write('Flash Grid Experiment\n')
                fout.write('This file Name = ' + filename +'\n')
                fout.write('Participant Number = ' + expInfo['Participant'] + '\n')
                fout.write('Date = ' + expInfo['date'] + '\n')
                fout.write('\n')
                
                #Loop to write various results to file
                fout.write('Trial Number, Response, Correct/Incorrect(1/0), RT:\n')
                for i in range(numtrials):
                    fout.write('%d\t'% trialNo[i])
                    fout.write('%s\t'% keyspressed[i])
                    fout.write('%s\t'% correctresponse[i])
                    fout.write('%.3f\t\n'% RT[i])
                
                # Close the results data file
                fout.close()
                
                # Say Where Results Are Written & If Experiment Successful
                print('Results Written To File Called ' + filename) 
                print('Program Completed Successfuly.')
                ####################################################################
                ####################################################################
                
                win.close()
                core.quit()
            break # End the expriment
            
         # RESPONSE 2
        if event.getKeys(keyList=["right"]):
            
#            time2 = checkclock.getTime()
#            print("Response time =", time2)
#            RT.append(time2)
            
            # Keep track of correct/incorrect responses
            if trialconditionx == 1:
                correctresponse.append('1')
            elif trialconditionx == 2:
                correctresponse.append('0')
            print(correctresponse)
            
            # Keep track of keys pressed
            keyspressed.append('right')
            print(keyspressed)
                
            print("actual trial condition just completed", trialconditionx)
            
            # Update the counter
            counter = counter+1
            
            # Keep track of trial number to be saved 
            trialNo.append(counter)
            print(trialNo)
            
            time2 = checkclock.getTime()
            print("Response time =", time2)
            RT.append(time2)
            
            # DRAW FIXATION CROSS AFTER EACH TRIAL
            win.flip() # Clears the window
            fcross.draw() # Draw the fixation cross
            win.flip() # Clears the window
            core.wait(2.0) # Keep the cross on screen for 2 seconds
            checkclock.reset()
            
            # END THE EXPERIMENT HERE AND SAVE DATA
            if counter == numtrials:
                win.flip() # Clears the window
                endtext.draw() # Draw ending message here
                win.flip() # Clears the window
                core.wait(3.0)
                
                #####################################################################
                #Write Data To File
                #####################################################################
                
                # Write RESULTS To A File 
                os.chdir("Flash_Grid_Results") # move to folder called RESULTS, need to CREATE this if it does not exist already.
                fout = open(filename, 'w')
                fout.write('Flash Grid Experiment\n')
                fout.write('This file Name = ' + filename +'\n')
                fout.write('Participant Number = ' + expInfo['Participant'] + '\n')
                fout.write('Date = ' + expInfo['date'] + '\n')
                fout.write('\n')
                
                #Loop to write various results to file
                fout.write('Trial Number, Response, Correct/Incorrect(1/0), RT:\n')
                for i in range(numtrials):
                    fout.write('%d\t'% trialNo[i])
                    fout.write('%s\t'% keyspressed[i])
                    fout.write('%s\t'% correctresponse[i])
                    fout.write('%.3f\t\n'% RT[i])
                
                # Close the results data file
                fout.close()
                
                #Say Where Results Are Written & If Experiment Successful
                print('Results Written To File Called ' + filename) 
                print('Program Completed Successfuly.')
                ####################################################################
                ####################################################################
                
                win.close()
                core.quit()
            break # End the expriment
            
            
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
        
        # END THE EXPERIMENT HERE
        if counter == numtrials:
            win.flip() # Clears the window
            endtext.draw() # Draw ending message here
            win.flip() # Clears the window
            core.wait(3.0)
            win.close()
            core.quit()
            
#-------Ending Routine "show_flash"-------
for thisComponent in show_flashComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
########################################################################################
########################################################################################
