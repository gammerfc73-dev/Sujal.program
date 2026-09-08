import tkinter as tk
from time import strftime

window = tk.Tk()
window.title("Digital Clock")
window.geometry("400x200")
window.configure(bg="black")

clock = tk.Label(
    window,
    font=("Arial", 50, "bold"),
    background="black",
    foreground="cyan"
)
clock.pack(expand=True)

def update_clock():
    current_time = strftime("%H:%M:%S")
    clock.config(text=current_time)
    window.after(1000, update_clock)

update_clock()

window.mainloop()
