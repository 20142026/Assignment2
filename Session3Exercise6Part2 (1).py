## Session 3: Exercise 6: Weigh your own decisions ##   Made by Rebecca

### Part 2: Choice reaction time ###
from psychopy import visual, event, core
import random

win = visual.Window(size=(1280, 720), fullscr=False,
                    color='black', checkTiming=False)

stopwatch = core.Clock()                    # Create the stopwatch



# Making a loop 
for number in range(5):                     # Range() makes sure the loop runs for 5 times
    waits = [0.5,1,1.5,2,2.5,3]              # The rabbit must surprise you: shuffled waiting times
    random.shuffle(waits)                    # Shuffling the "waits" list
    win.flip()                               # Just a black screen waiting
    core.wait(waits[0])                      # Wait for the first numeric in the shuffled order
    
    pic = visual.ImageStim(win, image='rabbit.jpg', size=0.5)
    positions = [(-0.5,0),(0.5,0)]           # Making position for the rabbit
    random.shuffle(positions)                # Shuffling the positions
    pic.pos = positions[0]                   # Choosing the winning position
    pic.draw()
    win.flip()                               # The rabbit appears: onset
    stopwatch.reset()                        # Zero the clock right after the flip
    
    keys = event.waitKeys(keyList = ['left', 'right']) # Waiting for key to be pressed
    rt = stopwatch.getTime()                           # Reading the clock
    key = keys[0]
    
    if pic.pos[0] <0:                         # Rabbit was on the left
        correct_key ='left'
    else:
        correct_key = 'right'

    print(f'Choice reaction: {rt:.3f} seconds, pressed {key}, correct was {correct_key}')

win.close()
core.quit()