import subprocess
import sys
import threading
from pynput import keyboard

__version__ = "1.1.0"

DEFAULT_INTERVAL = 3600  # seconds


def ring_laptop():
    # This command uses the 'afplay' utility to play a sound on macOS.
    try:
        subprocess.run(['afplay', '/System/Library/Sounds/Ping.aiff'], check=False)
    except Exception:
        pass  # Silently handle any errors playing the sound


def wait_for_keypress():
    """Block until spacebar or esc is pressed. Returns True to continue, False to exit."""
    result = threading.Event()
    should_exit = threading.Event()

    def on_press(key):
        if key == keyboard.Key.space:
            result.set()
            return False  # Stop listener
        elif key == keyboard.Key.esc:
            should_exit.set()
            return False  # Stop listener

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    return not should_exit.is_set()


def get_interval():
    if len(sys.argv) > 1:
        # Check for --version or -v flag
        if sys.argv[1] in ('--version', '-v'):
            print(f"ring-timer version {__version__}")
            sys.exit(0)

        try:
            return int(sys.argv[1])
        except ValueError:
            print(f"Invalid argument. Using the default value of {DEFAULT_INTERVAL} seconds.")
            return DEFAULT_INTERVAL

    try:
        print(f"Enter the time interval in seconds to ring the laptop (default: {DEFAULT_INTERVAL} seconds):")
        return int(input())
    except (ValueError, EOFError):
        print(f"Invalid input. Using the default value of {DEFAULT_INTERVAL} seconds.")
        return DEFAULT_INTERVAL


def main():
    print("Starting the program...")
    interval = get_interval()
    loop_counter = 0

    try:
        while True:
            print(f"(current loop: {loop_counter})  Waiting for {interval} seconds...")
            threading.Event().wait(interval)

            print("Ringing the laptop...")
            sound_thread = threading.Thread(target=ring_laptop)
            sound_thread.start()

            print("Press 'spacebar' to continue or 'esc' to exit.")
            should_continue = wait_for_keypress()

            sound_thread.join()

            if not should_continue:
                print("Escape pressed. Exiting the program.")
                break

            print("Spacebar pressed. Restarting the loop.")
            loop_counter += 1

    except KeyboardInterrupt:
        print("\nInterrupted. Exiting the program.")


if __name__ == "__main__":
    main()
