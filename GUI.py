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

def linear_dataset(linearwin, function):
  linear = LINEAR()
  for widget in linearwin.winfo_children():
    if isinstance(widget, tk.Canvas):
      widget.destroy()
  if function == "plot_light_curve":
    fig, ax = linear.plot_light_curve()
    chart_type = FigureCanvasTkAgg(fig, linearwin)
    chart_type.get_tk_widget().pack()
  elif function == "plot_atocorrelation_function":
    fig, ax = linear.plot_atocorrelation_function()
    chart_type = FigureCanvasTkAgg(fig, linearwin)
    chart_type.get_tk_widget().pack()
  elif function == "plot_lomb_scargle":
    fig, ax = linear.plot_lomb_scargle()
    chart_type = FigureCanvasTkAgg(fig, linearwin)
    chart_type.get_tk_widget().pack()

## When clicked on LINEAR it opens a new window for LINEAR Functions
def linear_new_window():
  linearwin = tk.Toplevel(window)
  button3 = tk.Button(linearwin, width=16, height=2, text="Plot Liight Curve", command=lambda: linear_dataset(linearwin, "plot_light_curve"))
  button4 = tk.Button(linearwin, width=28, height=2, text="Plot Autocorrelation function", command=lambda: linear_dataset(linearwin, "plot_atocorrelation_function"))
  button5 = tk.Button(linearwin, width=22, height=2, text="Plot Lomb Scargle", command=lambda: linear_dataset(linearwin, "plot_lomb_scargle"))
  button3.pack(anchor=tk.W)
  button4.pack(anchor=tk.W)
  button5.pack(anchor=tk.W)

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
  elif function == "plot_arima":
    fig, ax = ligo.arima(10,0,0)
    chart_type = FigureCanvasTkAgg(fig, legowin)
    chart_type.get_tk_widget().pack()
  elif function == "plot_arima_kde":
    fig, ax = ligo.arima_kde(10,0,0)
    chart_type = FigureCanvasTkAgg(fig, legowin)
    chart_type.get_tk_widget().pack()
  elif function == "plot_seasonality_trends":
    fig, ax = ligo.plot_seasonality_trends()
    chart_type = FigureCanvasTkAgg(fig, legowin)
    chart_type.get_tk_widget().pack()

## When clicked on LIGO it opens a new window for LIGO Functions
def ligo_new_window():
  legowin = tk.Toplevel(window)
  button3 = tk.Button(legowin, width=16, height=2, text="Plot Data plot", command=lambda: ligo_dataset(legowin, "plot_data"))
  button4 = tk.Button(legowin, width=15, height=2, text="Plot FFT Plot", command=lambda: ligo_dataset(legowin, "plot_fft"))
  button5 = tk.Button(legowin, width=25, height=2, text="Plot Welch Periodogram", command=lambda: ligo_dataset(legowin, "plot_Welch_Periodogram"))
  button6 = tk.Button(legowin, width=25, height=2, text="Plot Lomb Scargle Periodogram", command=lambda: ligo_dataset(legowin, "plot_Lomb_Scargle_Periodogram"))
  button7 = tk.Button(legowin, width=16, height=2, text="Plot ACF", command=lambda: ligo_dataset(legowin, "calculate_ACF"))
  button8 = tk.Button(legowin, width=15, height=2, text="Plot PACF", command=lambda: ligo_dataset(legowin, "calculate_PACF"))
  button9 = tk.Button(legowin, width=16, height=2, text="Plot Arima", command=lambda: ligo_dataset(legowin, "plot_arima"))
  # button10 = tk.Button(legowin, width=15, height=2, text="Plot Seasonality Trend", command=lambda: ligo_dataset(legowin, "plot_seasonality_trends"))
  button11 = tk.Button(legowin, width=16, height=2, text="Plot Arima KDE", command=lambda: ligo_dataset(legowin, "plot_arima_kde"))
  button3.pack(anchor=tk.W)
  button4.pack(anchor=tk.W)
  button5.pack(anchor=tk.W)
  button6.pack(anchor=tk.W)
  button7.pack(anchor=tk.W)
  button8.pack(anchor=tk.W)
  button9.pack(anchor=tk.W)
  # button10.pack(anchor=tk.W)
  button11.pack(anchor=tk.W)

# Placing the widgets
w = tk.Label(frame, text="Time Series Analysis", font=("Helvetica", 40), height=2)
heading = tk.Label(frame, text="Please choose a dataset for the expermentation", font=("Helvetica", 20), height=2)
button1 = tk.Button(frame, width=20, height=3, text="LIGO", command=ligo_new_window)
button2 = tk.Button(frame, width=20, height=3, text="LINEAR", command=linear_new_window)

w.pack()
heading.pack()
button1.pack()
button2.pack()

window.mainloop() 
