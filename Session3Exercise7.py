## Exercise 7 ##   Made by Josefine
from psychopy import visual, event, core, gui, data
import glob
import random
import os
import pandas as pd

#---participant---
box = gui.Dlg(title='The Fleeing Rabbit')
box.addField('Native language')
box.addField('Handedness', choices=['Right-handed', 'Left-handed'])
box.show()

if box.OK:
    language = box.data['Native language']               # the key is the label, exactly
    handedness = box.data['Handedness']
else:
    core.quit()                                      # cancel means stop, politely

participant_id = f'P{random.randint(10000, 99999)}'     # a code nobody chooses


# --- setup ---
os.makedirs('logfiles', exist_ok=True)            # the folder the save relies on
date = data.getDateStr()
logfile_name = f'logfiles/logfile_{participant_id}_{date}.csv'   # what makes it unique?

rows = []                                   # where the trials will pile up

images = glob.glob('stimuli/stimulus*.jpg')
random.shuffle(images)                                  # a fresh order, no assignment!

win = visual.Window(size=(1280, 720), fullscr=False,
                    color='black', checkTiming=False)

stopwatch= core.Clock()

def msg(text):
    message = visual.TextStim(win, text=text, height=0.08, color='pink')
    message.draw()
    win.flip()
    event.waitKeys(10)
    
msg("Welcome to the experiment! Press any key to begin.")

score=0

def show_stim(image):
    stim = visual.ImageStim(win, image=image) # prepare an image stimulus
    stim.draw()                           # paint it backstage
    win.flip()                           # curtain up
msg('The Fleeing Rabbit\n\n'
    'You are the rabbit, and the lion is on the hunt!\n\n'
    'See a LION? Run the other way: press the OPPOSITE arrow.\n'
    'See a BURROW? Dive in: press the arrow on ITS side.\n\n'
    'A right answer gives you 1 point, a wrong one gives you -1 point.\n\n'
    'Be quick, and be right. Press any key to start.')    
    
for image in images:
    show_stim(image) 
    stopwatch.reset()
    keys = event.waitKeys(keyList=['left', 'right', 'escape'])
    rt = stopwatch.getTime()
    key = keys[0]
    
    if image.endswith('_L.jpg'):
        correct_key = 'left'
    else:
        correct_key = 'right'
    if key == correct_key:
        feedback = visual.ImageStim(win, image='stimuli/success.jpg')
        score+=1
    else:
        feedback = visual.ImageStim(win, image='stimuli/failure.jpg')
        score-=1
    
    if key == 'escape':
        win.close()
        core.quit()

    feedback.draw()
    win.flip()
    core.wait(2)
    msg(f'{key} pressed, correct was {correct_key}, reaction time {rt:.2f} s.\nYour score is {score}\n\nPress any key to continue')

     # one trial, one dictionary
    rows.append({'id': participant_id,
                 'language': language,
                 'handedness': handedness,
                 'stimulus': image,
                 'key': key,
                 'correct_key': correct_key,
                 'rt': rt})

# --- save, then goodbye ---
logfile = pd.DataFrame(rows)                          # list of dictionaries in, table out
logfile.to_csv(logfile_name, index=False)

if score <= 6:
    msg(f"You have now completed the mission-your score is {score} -You have bad survival instincs")
else: 
    msg(f"You have now completed the mission-your score is {score} -You are the survival of the fittest")  

win.close()
core.quit()