import pyperclip
import time

def save_to_notepad_uppercase(filepath="clipboard_history.txt"):
    """Continuously monitors the clipboard and saves new content in uppercase to a text file."""
    previous_clipboard_content = None

    print(f"Monitoring clipboard. New copies in uppercase will be saved to '{filepath}'. Press Ctrl+C to stop.")

    try:
        while True:
            current_clipboard_content = pyperclip.paste()

            if current_clipboard_content != previous_clipboard_content:
                if current_clipboard_content:
                    uppercase_content = current_clipboard_content.upper()
                    with open(filepath, "a") as f:
                        f.write(uppercase_content + "\n")
                    print(f"Saved (uppercase): '{uppercase_content[:20]}...'")
                    previous_clipboard_content = current_clipboard_content

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nClipboard monitoring stopped.")
    except pyperclip.PyperclipException as e:
        print(f"Error accessing the clipboard: {e}")
        print("Make sure you have the necessary clipboard tools installed.")

if __name__ == "__main__":
    save_to_notepad_uppercase()
