import tkinter as tk 

# Initializing Object
window = tk.Tk()
window.title('Time Series Analysis | Sem 6 Project')
window.geometry("800x600")

frame = tk.Frame(window)
frame.pack()

# Dictionary with options
OPTIONS = ["LIGO", "Linear"]
dropdown_var = tk.StringVar(frame)
dropdown_var.set(OPTIONS[0])
  
def buttonClicked(button):
  print(button)

# Placing the widgets
w = tk.Label(frame, text="Time Series Analysis", font=("Helvetica", 40), height=2)
w.pack()
heading = tk.Label(frame, text="Please choose a dataset for the expermentation", font=("Helvetica", 20), height=2)
heading.pack()
button = tk.Button(frame, text="LIGO", bg="black", fg="white")
button.pack()

window.mainloop() 

# popupMenu = tk.OptionMenu(window, dropdown_var, *OPTIONS, command=dropdown_change)
