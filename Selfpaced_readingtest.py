## Excercise 8: Self-paced reading test ##
## Made by Paula, Magnus, Johannes, Josefine, Rebecca

## Made by Magnus (until the next '## Made by ...' note appears
from psychopy import visual, event, core, gui, data, os # Importing necessary packages
import random
import glob
import pandas as pd

# Create a consent dialogue  
consent = gui.Dlg(
    title='Study information',
    labelButtonOK='OK',
    labelButtonCancel='Cancel' # Button for declining to participate. 
)

consent.addText(
    'Reading experiment\n'
    'Reading a short story word by word\n\n'
 
    'INTRODUCTION\n'
    'You are being invited to take part in a research study. Please read this\n'
    'information carefully before deciding whether to participate. The study\n'
    'investigates how people read a short story presented one word at a time.\n'
    'You can take part if you are at least 18 years old and can read English\n'
    'comfortably, with normal or corrected-to-normal vision. If you need more\n'
    'information, please contact the researchers.\n\n'
 
    'PRINCIPAL INVESTIGATOR AND CONTACT\n'
    'Magnus Zippor Kirkegaard, Magnuszk@hotmail.com\n\n'
 
    'PURPOSE OF THE RESEARCH\n'
    'We are interested in how readers process words as they read, and how\n'
    'quickly they move through a text.\n\n'
 
    'STUDY PROCEDURE\n'
    'You will read one short story of about 180 words on the screen, one word\n'
    'at a time, pressing the SPACE bar to see the next word. The study takes\n'
    'about 5 minutes and there is no compensation. Participation is voluntary,\n'
    'and you can stop at any time, without giving a reason, by pressing Escape.\n\n'
 
    'BENEFITS AND RISKS\n'
    'There are no direct benefits to you. There are no risks other than those\n'
    'you meet in daily life.\n\n'
 
    'CONFIDENTIALITY AND DATA HANDLING\n'
    'We do not collect your name or any other identifying information. We\n'
    'record only your age, and your native language and your reading times, stored\n'
    'under a randomly generated participant ID. The data are anonymous, are\n'
    'stored securely by the researchers for 1 year, and may be shared in\n'
    'anonymised form for research purposes. Because the data are anonymous,\n'
    'they cannot be identified and withdrawn after data collection has ended.\n\n'
 
    'SIGNATURE AND DATE\n'
    'By clicking OK, I confirm that I understand the information above and that\n'
    'I can withdraw my consent at any time without personal consequences. I\n'
    'give my consent to participate in the research and for my data to be used\n'
    'as described in this document. Click Cancel if you do not wish to take part.')
consent.show()

# Quit experiment if participant withdraws consent. 
if not consent.OK:
    core.quit()

# Creating ID
participant_id = f'P{random.randint(10000, 99999)}'

# Participant
box = gui.Dlg(title='Self-paced reading test')
box.addField('Native language')
box.addField('Age')
box.show()

if box.OK:
    language = box.data['Native language']
    age = box.data['Age']
else:
    core.quit()
    
# Setup ## Made by Paula
os.makedirs('logfiles2', exist_ok=True)
date = data.getDateStr()
logfile_name = f'logfiles2/logfile_{participant_id}_{date}.csv'

story = """Once upon a time, a lonely princess lived in a stone castle, kept hidden away from the world by her mean stepmother. 
She had been held captive there for eighteen long years, waiting day and night for a brave soul to rescue her. 
One rainy afternoon, the ground trembled beneath her feet as a loud roar echoed through the valley. 
As tension filled the air, the princess ran to look out the window. 
Her heart pounded as she noticed a handsome knight battling a furious dragon outside the castle walls. 
A final, gut-wrenching scream put an end to the battle, leaving behind a heavy silence. 
Moments later, footsteps climbed the stone staircase toward her chamber. 
The door swung open, revealing the most magnificent knight she had ever seen. 
Without hesitation, he lifted her as though she weighed nothing and carried her down to his horse, 
which had been patiently waiting for its master’s return. Together they rode into the glowing sunset, 
leaving the dark castle behind, and from that day forward, they lived happily ever after."""

# Turning the story into a list of words; making a copy of our story

# control condition is unaltered story.
control_cond = story.split() # this makes a list where each item is a word in the story.
# surprise condition is initially just copy of control story.
surprise_cond = control_cond.copy() 

# Replacing a control word with a suprise word in the surprise condition
control_target = 'dragon'
surprise_target = 'pepperoni'

# Get index to target word in control story
target_i = control_cond.index(control_target)
# Now replace that index with the surprise word. 
surprise_cond[target_i] = surprise_target

# Write a for loop that goes through every index in control_cond and prints both the index and the word at that position.

for word_index in range(len(control_cond)):
    print(word_index, control_cond[word_index])
    
# Shuffling randomly between the control and surprise condition 
conditions = ['control', 'surprise'] ## Made by Rebecca
random.shuffle(conditions)
conditions[0]

if conditions[0] == 'control':
    text_cond = control_cond
else:
    text_cond = surprise_cond

# Make a window
win = visual.Window(
    size=(1000, 700), units='pix', color='black', fullscr=False
)
# Make a text object
text = visual.TextStim(win, text='+', color='white', height=48, units='pix')

# Define a helper to display text in the window ## Made by Johannes
def show(message):
    text.text = message
    text.draw()
    win.flip()

# Initialize the clock from the core module 
clock = core.Clock()

# Clear key press events (just in case)
event.clearEvents()


word_index = 0 # first control word in story 
text.text = text_cond[word_index]

results = []

# Instructions
show('You will read one story, one word at a time.\n'
    'Press Space for the next word.\n'
    'Press Escape to stop.\n\n'
    'Press any key to begin.')

# Wait for keypress 
event.waitKeys()

# fixation cross 
show('+')

# Display cross for .8s
core.wait(0.8)

for word in text_cond: ## Made by Josefine
    event.clearEvents()
    # Draw your text 
    text.text = word
    text.draw()

    # Reset the clock when the window is flipped and the word appears
    win.callOnFlip(clock.reset)

    # Flip your window
    win.flip()

    # Record keypresses (either space or escape)
    keys = event.waitKeys(
        keyList=['space', 'escape'],
        timeStamped=clock)

    # Store keys (which contains key pressed and response time) in two variables: key & reaction_time 
    key, reaction_time = keys[0]    

    if key == 'escape':
        pd.DataFrame(results).to_csv(logfile_name, index=False)
        win.close()
        core.quit()
        

    
    # Inside the trial loop, after the feedback
    results.append({'id': participant_id,
                 'condition': conditions[0],
                 'word index': word_index,
                 'word': word,
                 'language': language,
                 'age': age,
#                 'key': key, # I don't think it is necessary, as the instructions ask to use space!
                 'reaction time in ms': round(reaction_time*1000, 2)})

    word_index += 1
 
 # After the loop 
logfile = pd.DataFrame(results)
logfile.to_csv(logfile_name, index=False) 
  
show('Thanks for participating! The programme will close automatically.')
core.wait(3)

win.close()
core.quit()

  



