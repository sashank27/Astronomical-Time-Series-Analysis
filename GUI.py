import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ligo import LIGO
from linear import LINEAR

# Initializing Object
window = tk.Tk()
window.title('Time Series Analysis | Sem 6 Project')
window.geometry("1500x900")

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

def ligo_dataset(legowin, function):
  ligo = LIGO()
  for widget in legowin.winfo_children():
    if isinstance(widget, tk.Canvas):
      widget.destroy()
  if function == "plot_data":
    fig, ax = ligo.plot_data()
    chart_type = FigureCanvasTkAgg(fig, legowin)
    chart_type.get_tk_widget().pack()
  elif function == "plot_fft":
    fig, ax = ligo.plot_FFT()
    chart_type = FigureCanvasTkAgg(fig, legowin)
    chart_type.get_tk_widget().pack()
  elif function == "plot_Welch_Periodogram":
    fig, ax = ligo.plot_Welch_Periodogram()
    chart_type = FigureCanvasTkAgg(fig, legowin)
    chart_type.get_tk_widget().pack()
  elif function == "plot_Lomb_Scargle_Periodogram":
    fig, ax = ligo.plot_Lomb_Scargle_Periodogram()
    chart_type = FigureCanvasTkAgg(fig, legowin)
    chart_type.get_tk_widget().pack()
  elif function == "calculate_ACF":
    fig, ax = ligo.calculate_ACF()
    chart_type = FigureCanvasTkAgg(fig, legowin)
    chart_type.get_tk_widget().pack()
  elif function == "calculate_PACF":
    fig, ax = ligo.calculate_PACF()
    chart_type = FigureCanvasTkAgg(fig, legowin)
    chart_type.get_tk_widget().pack()

## When clicked on LIGO it opens a new window for LIGO Functions
def ligo_new_window():
  legowin = tk.Toplevel(window)
  button3 = tk.Button(legowin, width=16, height=3, text="Plot Data plot", command=lambda: ligo_dataset(legowin, "plot_data"))
  button4 = tk.Button(legowin, width=15, height=3, text="Plot FFT Plot", command=lambda: ligo_dataset(legowin, "plot_fft"))
  button5 = tk.Button(legowin, width=25, height=3, text="Plot Welch Periodogram", command=lambda: ligo_dataset(legowin, "plot_Welch_Periodogram"))
  button6 = tk.Button(legowin, width=25, height=3, text="Plot Lomb Scargle Periodogram", command=lambda: ligo_dataset(legowin, "plot_Lomb_Scargle_Periodogram"))
  button7 = tk.Button(legowin, width=16, height=3, text="Plot ACF", command=lambda: ligo_dataset(legowin, "calculate_ACF"))
  button8 = tk.Button(legowin, width=15, height=3, text="Plot PACF", command=lambda: ligo_dataset(legowin, "calculate_PACF"))
  button3.pack(anchor=tk.W)
  button4.pack(anchor=tk.W)
  button5.pack(anchor=tk.W)
  button6.pack(anchor=tk.W)
  button7.pack(anchor=tk.W)
  button8.pack(anchor=tk.W)

# def ligo_dataset():
  # newwin = Toplevel(root)
  # ligo = LIGO()
  # fig, ax = ligo.plot_data()
  # chart_type = FigureCanvasTkAgg(fig, window)
  # chart_type.get_tk_widget().pack()
  # fig, ax = ligo.plot_FFT()
  # chart_type = FigureCanvasTkAgg(fig, window)
  # chart_type.get_tk_widget().pack()
  # ligo.plot_FFT()
  # ligo.plot_Welch_Periodogram()
  # ligo.plot_Lomb_Scargle_Periodogram()
  # ligo.calculate_ACF()
  # ligo.calculate_PACF()

# Placing the widgets
w = tk.Label(frame, text="Time Series Analysis", font=("Helvetica", 40), height=2)
heading = tk.Label(frame, text="Please choose a dataset for the expermentation", font=("Helvetica", 20), height=2)
button1 = tk.Button(frame, width=20, height=3, text="LIGO", command=ligo_new_window)
button2 = tk.Button(frame, width=20, height=3, text="LINEAR", command=linear_dataset)

w.pack()
heading.pack()
button1.pack()
button2.pack()

window.mainloop() 
