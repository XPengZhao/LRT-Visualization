import json
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class LocalizationPlot:
    def __init__(self, frame, tag_filter, tag_var,ran):

        self.frame = frame
        self.tag_filter = tag_filter
        self.tag_var = tag_var
        self.ran = ran

        self.fig = plt.figure()



        self.ax = self.fig.add_subplot(111)



        # Hollow out
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)
        self.canvas.mpl_connect("button_press_event", self.input_Motionx_y)
        self.canvas.mpl_connect("button_release_event", self.output_Motionx_y)
        self.canvas.mpl_connect("scroll_event", self.zoom)



    # We only want the latest 80 plot
    # update and cancel the previous one
    def update_plot(self, data):

        xs = []
        ys = []
        for i in range(self.tag_filter.counter):
            xs.append(data[self.tag_var.get()]['pos'][0])
            ys.append(data[self.tag_var.get()]['pos'][1])

        self.ax.cla()
        self.ax.set(xlabel='x Axis (m)', ylabel='y Axis (m)')

        # # Update the right label
        for i in range(len(xs)):
            self.ax.plot(xs[i], ys[i], '.',   color='#00BFFF',
                              visible=self.tag_var.get())

        self.ax.set_xlim(self.ran[0], self.ran[1])
        self.ax.set_ylim(self.ran[2], self.ran[3])
        self.canvas.draw()

    def input_Motionx_y(self,event):
        self.mid_x_1 = event.x
        self.mid_y_1 = event.y
        self.move_f = self.canvas.mpl_connect("motion_notify_event", self.moveon)

    def output_Motionx_y(self,event):
        self.canvas.mpl_disconnect(self.move_f)
        self.mid_y_1 = 0
        self.mid_x_1 = 0

    def zoom(self,event):
        if event.button == "up":
            self.ran[0] += 0.05
            self.ran[1] -= 0.05
            self.ran[2] += 0.05
            self.ran[3] -= 0.05
            self.ax.set_xlim(self.ran[0], self.ran[1])
            self.ax.set_ylim(self.ran[2], self.ran[3])
        else:
            self.ran[0] -= 0.05
            self.ran[1] += 0.05
            self.ran[2] -= 0.05
            self.ran[3] += 0.05
            self.ax.set_xlim(self.ran[0], self.ran[1])
            self.ax.set_ylim(self.ran[2], self.ran[3])
    def getrange(self):
        return self.ran

    def moveon(self,event):
        if event.x > self.mid_x_1:
            res_x = event.xdata
            x_c = eval(str(self.ran[1]) + "-" + str(self.ran[0])) / 200
            self.ran[0] -= (res_x) * x_c
            self.ran[1] -= (res_x) * x_c
        else:
            res_x = event.xdata
            x_c = eval(str(self.ran[1]) + "-" + str(self.ran[0])) / 200
            self.ran[0] -= (res_x) * x_c
            self.ran[1] -= (res_x) * x_c
        if event.ydata>0.75:
            res_y = event.ydata
            y_c = eval(str(self.ran[3]) + "-" + str(self.ran[2])) / 200
            self.ran[2] -= (res_y) * y_c
            self.ran[3] -= (res_y) * y_c
            self.ax.set_xlim(self.ran[0], self.ran[1])
            self.ax.set_ylim(self.ran[2], self.ran[3])
        elif event.ydata<0.5:
            res_y = event.ydata
            y_c = eval(str(self.ran[3]) + "-" + str(self.ran[2])) / 80
            self.ran[2] += (res_y) * y_c
            self.ran[3] += (res_y) * y_c
            self.ax.set_xlim(self.ran[0], self.ran[1])
            self.ax.set_ylim(self.ran[2], self.ran[3])




#