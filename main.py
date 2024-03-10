import tkinter as tk

# Creating the window
window = tk.Tk()
window.title("Clock In")
window.geometry("300x300")

# Creating the timer label
timer = tk.Label(window, text="0.00", font=("Arial", 30))
timer.pack(pady=20)

# Creating pause functionality
is_paused = [True]

def pause():
    if not is_paused[0]:
        is_paused[0] = True
        main_button['text'] = "Start"
    else:
        is_paused[0] = False
        main_button['text'] = "Stop"
        update_timer()

# Main function that runs the timer
def update_timer():
    if is_paused[0]:
        return
    
    time = float(timer['text'])
    time += 0.05
    timer['text'] = f"{time:.2f}"
    window.after(50, update_timer)

# Main button
main_button = tk.Button(
    text="Start",
    command=(pause),
    font=("Arial", 15)
)
main_button.pack()

window.mainloop()

# TO DO:
# Display timer in the correct format
# Basic styling