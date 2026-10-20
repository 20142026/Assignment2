## Session 2: The fleeing rabbit ## Made by Johannes

import glob
import random
from psychopy import visual, event, core

images = glob.glob('stimuli/stimulus*.jpg')
random.shuffle(images)

win = visual.Window(size=(1080, 720), color='black',
                    fullscr=False, checkTiming=False)

# Functions
def msg(text):
    message = visual.TextStim(win, text=text, height=0.08)
    message.draw()
    win.flip()
    event.waitKeys()

def show_stim(image):
    img = visual.ImageStim(win, image=image)
    img.draw()
    win.flip()
    
msg("Welcome to the experiment!\nPress any key to continue.")
msg("Lion means press the opposite arrow, burrow means press its side.\nPress any key to begin.")

counter_success = 0
counter_fail = 0 

for image in images:
    show_stim(image)
    
    keys = event.waitKeys(keyList=['left', 'right', 'escape'])
    key = keys[0]
    if key == 'escape' :
        win.close()
        core.quit()
    
    if image.endswith('_L.jpg'):
        correct_key = 'left'
    else:
        correct_key = 'right'
    if key == correct_key:
        show_stim('stimuli/success.jpg')
        core.wait(2.0)
        counter_success += 1
    else:
       show_stim('stimuli/failure.jpg')
       core.wait(2.0)
       counter_fail += 1
    fixation = visual.TextStim(win, text="+", height=0.1)
    fixation.draw()
    win.flip()
    core.wait(0.5)

msg(f'Your total amount of saving the rabbit is {counter_success} and your total ammount of killing the rabbit is {counter_fail}.')

win.close()      # Close the window
core.quit()      # End the session cleanly