from tkinter import *
import tkinter as tk

def change_color_confirm(confirmBtn):
    confirmBtn.config(bg='red')

def change_color_cancel(cancelBtn):
    cancelBtn.config(bg='red')

# Reset buttons
def clear_buttons(confirmBtn, cancelBtn):
    confirmBtn.config(bg='SystemButtonFace', state=NORMAL)
    cancelBtn.config(bg='SystemButtonFace', state=NORMAL)

# Create field for user to enter commands
def commandField(root, confirmBtn, cancelBtn):
    # Prompt the user
    l = tk.Label(root, text="Enter Commands here:", font=("Tahoma", 20)) 
    l.pack()

    t = Text(root, padx=15, height=5, width=60, font=("Tahoma", 20)) # Customise font style and padding
    t.pack(padx=10)
    # Handle commands starting from the first character of the first word, strip and make lower case. 
    # Commands available are simply typing to names of the buttons then hitting enter. 
    def handle_command(event=None):
        command = t.get("1.0", END).strip().lower()
        t.delete("1.0", END)
        # Get commands user is expected to say
        if command in ("ok", "confirm", "yes", "y", "yeah"):
            confirmBtn.invoke()
        elif command in ("cancel", "no", "n"):
            cancelBtn.invoke()
        elif command in ("clear", "reset"):
            clear_buttons(confirmBtn, cancelBtn)
        else:
            print(f"Unknown command: {command}") # Throws an error if unrecognised command

        return "break"

    t.bind("<Return>", handle_command)
# Draw the window
def open_new_window():
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Hello World")

    label = tk.Label(root, text="Hello, World!")
    label.pack(padx=20, pady=20)

    # Add button logic to invoke events
    confirmBtn = Button(root, padx=20, text="OK",
                        command=lambda: change_color_confirm(confirmBtn))
    cancelBtn = Button(root, padx=20, text="Cancel",
                       command=lambda: change_color_cancel(cancelBtn))
    # Pack buttons so they appear
    confirmBtn.pack()
    cancelBtn.pack()

    commandField(root, confirmBtn, cancelBtn)

    root.mainloop()

open_new_window()

