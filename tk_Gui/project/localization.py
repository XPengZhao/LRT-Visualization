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
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
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
        self.ax.set(xlabel='x Axis (m)', ylabel='y Axis (m)',
                    title='Position Estimation Result')

        # # Update the right label
        ls = []
        # labels = []
        for i in range(len(xs)):
            l, = self.ax.plot(xs[i], ys[i], '.',   color='#00BFFF',
                              visible=self.tag_var.get())
            if l.get_visible():
                ls.append(l)
        self.ax.set_xlim(self.ran[0], self.ran[1])
        self.ax.set_ylim(self.ran[2], self.ran[3])
        self.canvas.draw()

    def input_Motionx_y(self,event):
        self.mid_x_1 = event.x
        self.mid_y_1 = event.y
    def output_Motionx_y(self,event):
        res_x = self.mid_x_1-event.x
        res_y = self.mid_y_1-event.y
        print(res_x,res_y)
        if abs(res_y)<=20 and abs(res_x)<=20:
            pass
        elif abs(res_x)<=20 and abs(res_y)>20:
            y_c = eval(str(self.ran[3])+"-"+str(self.ran[2]))/10
            self.ran[2] += (res_y/100)*y_c
            self.ran[3] += (res_y/100)*y_c
            self.ax.set_xlim(self.ran[0], self.ran[1])
            self.ax.set_ylim(self.ran[2], self.ran[3])
        elif abs(res_y)<=20 and abs(res_x)>20:
            x_c = eval(str(self.ran[1]) + "-" + str(self.ran[0])) / 10
            self.ran[0] += (res_x / 100) * x_c
            self.ran[1] += (res_x / 100) * x_c
            self.ax.set_xlim(self.ran[0], self.ran[1])
            self.ax.set_ylim(self.ran[2], self.ran[3])
        else:
            x_c = eval(str(self.ran[1]) + "-" + str(self.ran[0])) / 10
            self.ran[0] += (res_x / 100) * x_c
            self.ran[1] += (res_x / 100) * x_c
            y_c = eval(str(self.ran[3]) + "-" + str(self.ran[2])) / 10
            self.ran[2] += (res_y / 100) * y_c
            self.ran[3] += (res_y / 100) * y_c
            self.ax.set_xlim(self.ran[0], self.ran[1])
            self.ax.set_ylim(self.ran[2], self.ran[3])
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




#