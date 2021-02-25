import json
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as tkagg

class LocalizationPlot:
    def __init__(self, frame, tag_filter, tag_var):

        self.frame = frame
        self.tag_filter = tag_filter
        self.tag_var = tag_var

        self.fig = plt.figure()


        self.ax = self.fig.add_subplot(111)


        # Hollow out
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = tkagg(self.canvas, self.frame)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.X, expand=1)



    # We only want the latest 80 plot
    # update and cancel the previous one
    def update_plot(self, data):

        xs = []
        ys = []
        try:
            for i in range(self.tag_filter.counter):
                xs.append(data[self.tag_var.get()]['pos'][0])
                ys.append(data[self.tag_var.get()]['pos'][1])
        except:
            self.tag_var.set(list(data.keys())[0])
            for i in range(self.tag_filter.counter):
                xs.append(data[self.tag_var.get()]['pos'][0])
                ys.append(data[self.tag_var.get()]['pos'][1])

        self.ax.cla()
        self.ax.set(xlabel='x Axis (m)', ylabel='y Axis (m)',
                    title='Position Estimation Result')
        self.ax.axis([-1, 1, -1, 1])
        # # Update the right label
        ls = []
        # labels = []
        for i in range(len(xs)):
            l, = self.ax.plot(xs[i], ys[i], 'o',   color='#00BFFF',
                              markerfacecolor='none',
                              visible=self.tag_var.get())
            if l.get_visible():
                ls.append(l)
        self.canvas.draw()

#