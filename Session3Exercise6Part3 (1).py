## Exercise 6 Part 3 ##   Made by Magnus
from psychopy import visual, event, core, gui, data
import glob
import random

# Setup
images = glob.glob('stimuli/stimulus*.jpg')
random.shuffle(images)  

win = visual.Window(
    size=(1080, 720), color='Black', 
    fullscr=False,checkTiming=False)    

stopwatch = core.Clock()
rts = []
lion_rts = []
burrow_rts = []

# Functions
    
def msg(text): # Displaying text
    message = visual.TextStim(win, text=text, height=0.08)
    message.draw()
    win.flip()
    event.waitKeys()

def show_stim(image): # Displaying images
    img= visual.ImageStim(win, image=image)
    img.draw()
    win.flip()

# Experiment
msg('"Welcome to the experiment! Press any key to begin"\n\n'
    "You are the rabbit, and the lion is on the hunt!\n\n"
    "See a LION? Run the other way: press the OPPOSITE arrow.\n"
    "See a BURROW? Dive in: press the arrow on ITS side.\n\n"
    "Be quick, and be right. Press any key to start.")

for image in images:
    show_stim(image)
    stopwatch.reset()

    keys = event.waitKeys(keyList=['left', 'right',"escape"])
    rt = stopwatch.getTime()
    rts.append(rt)
    key = keys[0]
    
    if 'lion' in image:
        trial_type = 'lion'
    else:
        trial_type = 'burrow'
    
    if key == 'escape': 
        win.close(); core.quit()
    else:
        if image.endswith('_L.jpg'):
            correct_key = 'left'
        else:
            correct_key = 'right'
        
        if key == correct_key:
            feedback = visual.ImageStim(win, image='stimuli/success.jpg')
        else:
            feedback = visual.ImageStim(win, image='stimuli/failure.jpg')
            
        if key == correct_key:              
            if trial_type == 'lion':
                lion_rts.append(rt)
            else:
                burrow_rts.append(rt)
        feedback.draw()
        win.flip()
        core.wait(1)
        
        fixation = visual.TextStim(win, text="+", height=0.1)
        fixation.draw()
        win.flip()
        core.wait(0.5)

msg(f'Burrow trials: {sum(burrow_rts) / len(burrow_rts):.2f} s on average.\n'
    f'Lion trials: {sum(lion_rts) / len(lion_rts):.2f} s on average.\n\n'
    'Thank you! Press any key to close.')


win.close()
core.quit()