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
        self.ax.set(xlabel='x Axis (m)', ylabel='y Axis (m)')

        # # Update the right label
        for i in range(len(xs)):
            self.ax.plot(xs[i], ys[i], '.',   color='#00BFFF',
                              visible=self.tag_var.get())

        self.ax.set_xlim(self.ran[0], self.ran[1])
        self.ax.set_ylim(self.ran[2], self.ran[3])
        self.canvas.draw()

    def input_Motionx_y(self,event):
        self.c_list_x = []
        self.c_list_y = []
        self.c_list_x.append(event.x)
        self.c_list_y.append(event.y)
        self.move_f = self.canvas.mpl_connect("motion_notify_event", self.moveon)

    def output_Motionx_y(self,event):
        self.canvas.mpl_disconnect(self.move_f)

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
        self.c_list_x.append(event.x)
        self.c_list_y.append(event.y)
        try:
            if self.c_list_x[-1]-self.c_list_x[-2] >0:
                res_x = event.xdata
                x_c = eval(str(self.ran[1]) + "-" + str(self.ran[0])) / 50
                self.ran[0] -= (res_x) * x_c
                self.ran[1] -= (res_x) * x_c
            else:
                res_x = event.xdata
                x_c = eval(str(self.ran[1]) + "-" + str(self.ran[0])) / 50
                self.ran[0] -= (res_x) * x_c
                self.ran[1] -= (res_x) * x_c

            if self.c_list_y[-1]-self.c_list_y[-2] >0:
                res_y = event.ydata
                y_c = eval(str(self.ran[3]) + "-" + str(self.ran[2]))/5
                self.ran[2] -= (res_y) * y_c
                self.ran[3] -= (res_y) * y_c
                self.ax.set_xlim(self.ran[0], self.ran[1])
                self.ax.set_ylim(self.ran[2], self.ran[3])

            elif self.c_list_y[-1]-self.c_list_y[-2] == 0:
                pass
            else:
                res_y = event.ydata
                y_c = eval(str(self.ran[3]) + "-" + str(self.ran[2]))/10
                self.ran[2] -= (res_y) * y_c
                self.ran[3] -= (res_y) * y_c
                self.ax.set_xlim(self.ran[0], self.ran[1])
                self.ax.set_ylim(self.ran[2], self.ran[3])
        except:
            pass




#