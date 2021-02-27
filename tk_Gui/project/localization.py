import json
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

    # We only want the latest 80 plot
    # update and cancel the previous one
    def update_plot(self, data, ran):

        xs = []
        ys = []
        for i in range(self.tag_filter.counter):
            xs.append(data[self.tag_var.get()]['pos'][0])
            ys.append(data[self.tag_var.get()]['pos'][1])

        self.ax.cla()
        self.ax.set(xlabel='x Axis (m)', ylabel='y Axis (m)',
                    title='Position Estimation Result')

        # # Update the right label
        ls = []
        # labels = []
        for i in range(len(xs)):
            l, = self.ax.plot(xs[i], ys[i], 'o',   color='#00BFFF',
                              markerfacecolor='none',
                              visible=self.tag_var.get())
            if l.get_visible():
                ls.append(l)
        self.ax.set_xlim(ran[0], ran[1])
        self.ax.set_ylim(ran[2], ran[3])
        # self.ax.set_yticks((ran[3] - ran[2]) / 20)
        self.canvas.draw()

#