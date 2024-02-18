import tkinter as tk
from datetime import datetime
import time

def get_time_format():
    return time.strftime('%I') != ''

def update_time_and_date():
    try:
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%d/%m/%Y")
        is_12_hour_format = get_time_format()
        time_format = "%I:%M:%S %p" if is_12_hour_format else "%H:%M:%S"
        formatted_time = current_datetime.strftime(time_format)
        time_label.config(text=formatted_time)
        date_label.config(text=formatted_date)

    except Exception as e:
        print(f"Error updating time and date: {e}")
    time_label.place(relx=0.5, rely=0.3, anchor="center")
    date_label.place(relx=0.5, rely=0.6, anchor="center")
    window.after(500, update_time_and_date)

def on_window_resize(event):
    font_size = int(window.winfo_width() / 20)
    time_label.config(font=("Helvetica", font_size))
    date_label.config(font=("Helvetica", font_size // 2))

def toggle_fullscreen(event=None):
    window.attributes("-fullscreen", not window.attributes("-fullscreen"))

def exit_fullscreen(event):
    if window.attributes("-fullscreen"):
        window.attributes("-fullscreen", False)

def on_key(event):
    if event.keysym == "F11":
        toggle_fullscreen()

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

window = tk.Tk()
window.title("Simple Time Display")
window.geometry("580x200")
window.eval('tk::PlaceWindow . center')

time_label = tk.Label(window, font=("Helvetica", 24), pady=10)
time_label.pack()

date_label = tk.Label(window, font=("Helvetica", 12), justify="center", wraplength=500)
date_label.pack()

update_time_and_date()
window.bind("<Configure>", on_window_resize)
window.bind("<Escape>", exit_fullscreen)
window.bind("<F11>", toggle_fullscreen)
window.bind("<Key>", on_key)

context_menu = tk.Menu(window, tearoff=0)
context_menu.add_command(label="Toggle Fullscreen", command=toggle_fullscreen)
window.bind("<Button-3>", show_context_menu)

window.mainloop()
