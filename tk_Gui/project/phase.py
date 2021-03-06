import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CheckFilter:
    def __init__(self, frame, vars):
        self.frame = frame
        self.vars = vars
        self.counter = 0
        self.image = tk.PhotoImage(file='../pic/button.png')
        self.selectimage = tk.PhotoImage(file='../pic/button2.png')

    def update_filter(self, tags):
        if self.counter == len(tags):
            return

        new_tags = tags[self.counter:]
        self.counter += len(new_tags)

        for num in new_tags:
            button = tk.Checkbutton(
                self.frame, text='ANT %d' % (num + 1), variable=self.vars[num], indicatoron=False,
                # justify=tk.CENTER,
                width=10, height=1, compound=tk.CENTER,
                font=('Times New Roman', 8, 'bold'))
            button.pack(anchor='w', fill=tk.BOTH)


class PhasePlot:
    def __init__(self, frame, tag_filter, tag_var):

        self.tag_filter = tag_filter
        self.tag_var = tag_var

        filter_frame2 = tk.LabelFrame(frame, text='Phase Filter', bg='white', bd=0,
                                      font=('Times New Roman', 12, 'bold'), labelanchor='n')
        filter_frame2.pack(side=tk.LEFT, fill=tk.BOTH)
        self.phase_vars = [tk.IntVar() for i in range(16)]
        self.phase_filter = CheckFilter(filter_frame2, self.phase_vars)

        self.x_start = 0
        self.x_end = 400
        self.frame = frame

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)



        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.canvas.mpl_connect("scroll_event", self.zoom)
        self.canvas.mpl_connect("button_press_event", self.input_Motionx_y)
        self.canvas.mpl_connect("button_release_event", self.output_Motionx_y)

    def update_plot(self, data):

        self.phase_filter.update_filter([i for i in range(16)])

        self.ax.cla()
        self.ax.set(xlabel='sample (#)', ylabel='phase (rad)',
                    title='Phase Plot')
        ys = data[self.tag_var.get()]['phase']
        self.data_len = len(ys[0])
        if self.data_len > 400 and self.x_end == self.data_len-1:
            self.x_start +=1
            self.x_end += 1
        if self.x_end - self.x_start <400 and self.x_end == self.data_len-1:
            self.x_start += 1
            self.x_end += 1


        ls = []
        labels = []
        # print(self.tag_var.get())
        for i in range(16):
            l, = self.ax.plot(ys[i], label='antenna%d' % (i + 1),
                              visible=self.phase_vars[i].get())
            if l.get_visible():
                ls.append(l)
                labels.append(l.get_label())
        self.ax.set_ylim(-6, 6)
        self.ax.set_xlim(self.x_start, self.x_end)
        self.ax.legend(ls, labels, loc=1)




        self.canvas.draw()

    def zoom(self,event):
        if event.button == "up":
            if self.x_end-self.x_start >50:
                self.x_end -= 50
                self.ax.set_xlim(self.x_start, self.x_end)
        else:
            if self.x_end-self.x_start <400:
                if self.x_start <= 25:
                    mid = self.x_start
                    self.x_start = 0
                    self.x_end += 25+abs(mid)
                    self.ax.set_xlim(self.x_start, self.x_end)
                elif self.x_end >=400:
                    mid = self.x_end - 400
                    self.x_end = self.data_len - 1
                    self.x_start += 25 + mid
                    self.ax.set_xlim(self.x_start, self.x_end)
                else:
                    self.x_start -= 25
                    self.x_end += 25
                    self.ax.set_xlim(self.x_start, self.x_end)
            elif self.x_end-self.x_start >= 400:
                pass


    def input_Motionx_y(self,event):
        self.c_list_x = []
        self.c_list_y = []
        self.c_list_x.append(event.x)
        self.c_list_y.append(event.y)
        self.move_f = self.canvas.mpl_connect("motion_notify_event", self.moveon)

    def output_Motionx_y(self,event):
        self.canvas.mpl_disconnect(self.move_f)

    def moveon(self,event):
        self.c_list_x.append(event.x)

        if self.c_list_x[-1]-self.c_list_x[-2] >0:
            if self.x_start >= 0:
                self.x_start -= 1
                self.x_end -= 1
            if self.x_start <= 0:
                mid = self.x_start
                self.x_start =0
                self.x_end += abs(mid)

        else:
            if self.data_len > self.x_end:
                self.x_start += 1
                self.x_end += 1

        self.ax.set_xlim(self.x_start, self.x_end)


