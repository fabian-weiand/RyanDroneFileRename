import os
import re
import tkinter as tk
from tkinter import INSERT, ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo

def main_window():
    
    # root window
    root = tk.Tk()
    # Set window size and position
    window_width = 400
    window_height = 150
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.resizable(0, 0)
    # Set window title and icon
    root.title('Drone Image File Mover App')
    root.iconbitmap('./assets/Checkbox.ico')
    #root.config(background='#84BF04')
    # windows only (remove the minimize/maximize button)
    #root.attributes('-toolwindow', True)

    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    main_window.input_frame = input_frame(root)
    main_window.input_frame.grid(column=0, row=0)

    main_window.button_frame = button_frame(root)
    main_window.button_frame.grid(column=1, row=0)

    root.mainloop()

def input_frame(container):
    
    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Origin folder
    ttk.Label(frame, text='Origin:').grid(column=0, row=0, sticky=tk.W)
    input_frame.origin = ttk.Entry(frame, width=30)
    input_frame.origin.focus()
    input_frame.origin.grid(column=1, row=0, sticky=tk.W)

    # Destination folder
    ttk.Label(frame, text='Destination:').grid(column=0, row=1, sticky=tk.W)
    input_frame.destination = ttk.Entry(frame, width=30)
    input_frame.destination.grid(column=1, row=1, sticky=tk.W)

    # Regex keyword
    ttk.Label(frame, text='Regex pattern:').grid(column=0, row=2, sticky=tk.W)
    input_frame.regex_keyword = ttk.Entry(frame, text=".*_R.JPG", width=30)
    input_frame.regex_keyword.grid(column=1, row=2, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)

    return frame 

def button_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    button_frame.origin_folder = ttk.Button(frame, text='Browse', command=set_origin).grid(column=0, row=0)

    button_frame.destination_folder = ttk.Button(frame, text='Browse', command=set_destination).grid(column=0, row=1)

    button_frame.move_files = ttk.Button(frame, text='Move Files', comman=change_file_names).grid(column=0, row=2)

    button_frame.quit_button = ttk.Button(frame, text='Cancel', command=container.destroy).grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=3)

    return frame

def set_origin():
    filename = filedialog.askdirectory()
    
    # Change label contents
    input_frame.origin.insert(INSERT, filename)

def set_destination():
    filename = filedialog.askdirectory()
    
    # Change label contents
    input_frame.destination.insert(INSERT, filename)

def change_file_names():
    # Inititalize path variables
    orig_path = input_frame.origin.get()
    while not os.path.exists(orig_path):
        showinfo(
            title='Error',
            message="Invalid file path"
        )
    
    dest_path = input_frame.destination.get()
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    # Create list of files at origin
    files = os.listdir(orig_path)

    # Inititalize counter
    count = 0

    # Change filename of files that ends with "_R.JPG"
    for file in files:
        if re.search(input_frame.regex_keyword.get(), file):
            os.rename(os.path.join(orig_path,file), 
                os.path.join(dest_path,file))
            count += 1

    # Print confirmation of files renamed
    showinfo(
        title='Success',
        message=f"%d files renamed and moved" %count
    )

if __name__ == "__main__":
    main_window()