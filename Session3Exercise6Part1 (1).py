## Session 3 Excercise 1 ## Made by Paula

### Part 1 ### 
from psychopy import visual, event, core
import random

win = visual.Window(size=(1280, 720), fullscr=False,
                    color='black', checkTiming=False)

stopwatch = core.Clock()                    # Create the stopwatch

waits = [1, 1.5, 2, 2.5, 3]                 # The rabbit must surprise you: shuffled waiting times, first one wins
random.shuffle(waits)                       # How would we shuffle a list of durations?

win.flip()                                  # Black screen: get ready...
core.wait(waits[0])                         # Wait for the winning duration

pic = visual.ImageStim(win, image='rabbit.jpg', size=0.5)
pic.draw()
win.flip()                                  # The rabbit appears: onset
stopwatch.reset()                           # Zero the clock, exactly here. Why here?

event.waitKeys()
rt = stopwatch.getTime()                    # Read the clock: seconds since the reset
print(f'Simple reaction: {rt:.3f} seconds')


win.close()
core.quit()