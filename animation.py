import time
import sys

# Characters used for the loading animation
spinner = ['\\', '/', '-', '|']

def loading_animation(duration=5, delay=0.1):
    """Display a loading animation for a given duration."""
    end_time = time.time() + duration
    idx = 0

    while time.time() < end_time:
        sys.stdout.write('\rLoading ' + spinner[idx % len(spinner)])
        sys.stdout.flush()
        time.sleep(delay)
        idx += 1

    sys.stdout.write('\rDone!       \n')

# Run the animation
loading_animation()
