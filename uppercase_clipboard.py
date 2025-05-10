import pyperclip
import time

def force_uppercase_clipboard():
    """Continuously monitors the clipboard and forces new content to be uppercase."""
    previous_clipboard_content = None

    print("Monitoring clipboard. New copies will be forced to uppercase. Press Ctrl+C to stop.")

    try:
        while True:
            current_clipboard_content = pyperclip.paste()

            if current_clipboard_content != previous_clipboard_content:
                if current_clipboard_content:
                    uppercase_content = current_clipboard_content.upper()
                    pyperclip.copy(uppercase_content)
                    print(f"Converted to uppercase: '{uppercase_content[:20]}...'")
                    previous_clipboard_content = uppercase_content  # Update with the uppercase version
                else:
                    previous_clipboard_content = current_clipboard_content # Keep track of empty clipboard

            time.sleep(0.1) # Check more frequently for a smoother experience

    except KeyboardInterrupt:
        print("\nClipboard monitoring stopped.")
    except pyperclip.PyperclipException as e:
        print(f"Error accessing the clipboard: {e}")
        print("Make sure you have the necessary clipboard tools installed.")

if __name__ == "__main__":
    force_uppercase_clipboard()