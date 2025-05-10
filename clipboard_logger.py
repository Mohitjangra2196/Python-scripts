import pyperclip
import time

def save_to_notepad(filepath="clipboard_history.txt"):
    """Continuously monitors the clipboard and saves new content to a text file."""
    previous_clipboard_content = None

    print(f"Monitoring clipboard. New copies will be saved to '{filepath}'. Press Ctrl+C to stop.")

    try:
        while True:
            current_clipboard_content = pyperclip.paste()

            if current_clipboard_content != previous_clipboard_content:
                if current_clipboard_content:  # Avoid saving empty clipboard
                    with open(filepath, "a") as f:
                        f.write(current_clipboard_content + "\n")
                    print(f"Saved: '{current_clipboard_content[:20]}...'")  # Print a snippet of what was saved
                    previous_clipboard_content = current_clipboard_content

            time.sleep(1)  # Check the clipboard every 1 second (adjust as needed)

    except KeyboardInterrupt:
        print("\nClipboard monitoring stopped.")
    except pyperclip.PyperclipException as e:
        print(f"Error accessing the clipboard: {e}")
        print("Make sure you have the necessary clipboard tools installed.")

if __name__ == "__main__":
    save_to_notepad()