import tkinter as tk
import matplotlib.pyplot as plt
from ligo import LIGO
from linear import LINEAR

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

def linear_dataset():
  linear = LINEAR()
  linear.plot_light_curve()
  linear.plot_atocorrelation_function()
  linear.plot_lomb_scargle()
  plt.show()

def ligo_dataset():
  ligo = LIGO()
  ligo.plot_data()
  ligo.plot_FFT()
  ligo.plot_Welch_Periodogram()
  ligo.plot_Lomb_Scargle_Periodogram()
  ligo.calculate_ACF()
  ligo.calculate_PACF()
  plt.show()

# Placing the widgets
w = tk.Label(frame, text="Time Series Analysis", font=("Helvetica", 40), height=2)
heading = tk.Label(frame, text="Please choose a dataset for the expermentation", font=("Helvetica", 20), height=2)
button1 = tk.Button(frame, width=20, height=3, text="LIGO", command=ligo_dataset)
button2 = tk.Button(frame, width=20, height=3, text="Linear", command=linear_dataset)

w.pack()
heading.pack()
button1.pack()
button2.pack()

window.mainloop() 

# popupMenu = tk.OptionMenu(window, dropdown_var, *OPTIONS, command=dropdown_change)
