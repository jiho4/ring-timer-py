import time
import os
import sys
import threading
from pynput import keyboard

# second
interval_sleep_time = 3600

continue_loop = False
exit_program = False
loop_counter = 0


# TODO: change sleep to listening, and space pressed before ring then start again
# TODO: consider to change it to React, running on browser and show realtime info like time left to ring
def ring_laptop():
    # This command uses the 'afplay' utility to play a sound on macOS.
    os.system('afplay /System/Library/Sounds/Ping.aiff')


def ring_laptop_thread():
    thread = threading.Thread(target=ring_laptop)
    thread.start()


def on_press(key):
    global continue_loop
    global exit_program

    if key == keyboard.Key.space:
        continue_loop = True
        return False  # Stop listener
    elif key == keyboard.Key.esc:
        exit_program = True
        return False  # Stop listener


def main():
    global interval_sleep_time
    global continue_loop
    global exit_program
    global loop_counter

    print("Starting the program...")

    try:
        if len(sys.argv) > 1:
            # if parameter is passed, use it as interval time to sleep
            interval_sleep_time = int(sys.argv[1])
        else:
            # get input for interval time to sleep
            print(f"Enter the time interval in seconds to ring the laptop (default: {interval_sleep_time}seconds):")
            interval_sleep_time = int(input())
    except ValueError:
        print(f"Invalid input. Using the default value of {interval_sleep_time}seconds.")

    while True:
        print(f"(current loop: {loop_counter})  Waiting for {interval_sleep_time} seconds...")
        time.sleep(interval_sleep_time)

        print("Ringing the laptop...")
        ring_laptop_thread()

        print("Press 'spacebar' to continue or 'esc' to exit.")
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

        if exit_program:
            print("Escape pressed. Exiting the program.")
            break

        if continue_loop:
            print("Spacebar pressed. Restarting the loop.")
            loop_counter += 1
            continue_loop = False


if __name__ == "__main__":
    main()
