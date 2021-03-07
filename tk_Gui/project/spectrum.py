
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.gridspec import GridSpec
from mpl_toolkits.mplot3d import Axes3D



class SpectrumPlot:
    def __init__(self, frame, tag_var, tag_filter):

        self.frame = frame
        self.tag_var = tag_var
        self.tag_filter = tag_filter

        self.signal = tk.IntVar()

        self.fig = plt.figure()
        gs = GridSpec(3, 5, figure=self.fig)
        self.ax = self.fig.add_subplot(gs[0:3, 1:4], projection='3d')
        # self.ax = self.fig.add_subplot(111, projection='3d')

        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_plot(self, data):
        if self.signal != self.tag_var.get():
            self.signal = self.tag_var.get()
            self.update_plot_change(data)
        else:
            if data[self.tag_var.get()]["spectrum"][0]:
                if data[self.tag_var.get()]["spec_change"]:
                    xs = []
                    ys = []
                    zs = []
                    for i in range(self.tag_filter.counter):
                        for j in range(360):
                            for z in range(90):
                                xs.append(j)
                                ys.append(z)
                                zs.append(data[self.tag_var.get()]['spectrum'][j][z])

                    self.ax.cla()
                    self.ax.set(xlabel='x Axis', ylabel='y Axis', zlabel='z Axis',
                                title='Spectrum Plot Tag%d' % (self.tag_var.get()))
                    self.ax.scatter(xs, ys, zs, c=zs, marker='.', cmap='rainbow')
                    self.canvas.draw()
    def update_plot_change(self,data):
        if data[self.tag_var.get()]["spectrum"][0]:
            xs = []
            ys = []
            zs = []
            for i in range(self.tag_filter.counter):
                for j in range(360):
                    for z in range(90):
                        xs.append(j)
                        ys.append(z)
                        zs.append(data[self.tag_var.get()]['spectrum'][j][z])

            self.ax.cla()
            self.ax.set(xlabel='x Axis', ylabel='y Axis', zlabel='z Axis',
                        title='Spectrum Plot Tag%d' % (self.tag_var.get()))
            self.ax.scatter(xs, ys, zs, c=zs, marker='.', cmap='rainbow')
            self.canvas.draw()
