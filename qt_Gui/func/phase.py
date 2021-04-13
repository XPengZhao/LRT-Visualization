import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class PhasePlot(FigureCanvas):
    def __init__(self,widget):
        self.widget = widget
        self.fig = Figure(figsize=(200,400))

        super(PhasePlot, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)
        self.axes.set(title="Phase")
        self.mlp_bar = NavigationToolbar(self, self.widget)
        self.mlp_bar.hide()
        self.mpl_connect("scroll_event", self.zoom)
        self.mpl_connect("button_press_event", self.input_Motionx_y)
        self.mpl_connect("button_release_event", self.output_Motionx_y)
        self.ran = 400
        self.draw()

    def get_data(self, data):
        self.data = data
        self.xs = {}
        for tag in self.data:
            length = len(self.data[tag][0])
            self.xs[tag] = [ i for i in range(length)]






    def update_plot(self, tag, time_num, ant):

        self.tag = tag
        self.time_num = time_num
        self.x_start = time_num
        self.x_end = time_num+self.ran


        self.axes.cla()
        self.axes.set(xlabel='sample (#)', ylabel='phase (rad)',
                    title='Phase Plot')
        ls = []
        labels = []
        x_len = len(self.xs[tag])
        for i in range(16):
            if len(self.xs[tag][time_num:])>400:
                l, = self.axes.plot(self.xs[tag][time_num:time_num+400],self.data[tag][i][time_num:time_num+400], visible=ant[i])
            else:
                l, = self.axes.plot(self.xs[tag][-400:-1], self.data[tag][i][-400:-1],visible=ant[i])

            if int(ant[i]) == 1:
                ls.append(l)
                labels.append('ant%d' % (i + 1))

        self.axes.set_ylim(-6, 6)
        self.axes.legend(ls, labels,loc=1)
        if len(self.xs[tag][time_num:]) > 400:
            self.axes.set_xlim([time_num,time_num+self.ran])
        else:
            self.axes.set_xlim([x_len-400, x_len])
        del l
        self.draw()





    def zoom(self,event):

        if event.button == "up":
            if self.x_end-self.x_start >50:
                self.x_end -= 10
                self.axes.set_xlim(self.x_start, self.x_end)
        else:
            if self.x_end <self.time_num+400:
                self.x_end += 10
                self.axes.set_xlim(self.x_start, self.x_end)
            else:
                self.x_end = self.time_num+400
                self.axes.set_xlim(self.x_start, self.x_end)
        self.ran = abs(self.x_start-self.x_end)
        self.draw()

    def input_Motionx_y(self,event):
        self.c_list_x = []
        self.c_list_x.append(event.x)
        self.move_f = self.mpl_connect("motion_notify_event", self.moveon)

    def output_Motionx_y(self,event):
        self.mpl_disconnect(self.move_f)

    def moveon(self,event):
        self.c_list_x.append(event.x)

        if self.c_list_x[-1]-self.c_list_x[-2] >0:
            if self.x_start >= self.time_num:
                if self.x_end - self.x_start > 100:
                    self.x_start -= 10
                    self.x_end -= 10
                else:
                    self.x_start -= 5
                    self.x_end -= 5
            if self.x_start <= self.time_num:
                mid = self.x_start-self.x_end
                self.x_start =self.time_num
                self.x_end = abs(mid)+self.time_num

        else:
            if self.time_num+self.ran > self.x_end:
                if self.x_end-self.x_start>100:
                    self.x_start += 10
                    self.x_end += 10
                else:
                    self.x_start += 5
                    self.x_end += 5

        self.axes.set_xlim(self.x_start, self.x_end)
        self.ran = abs(self.x_start-self.x_end)
        self.draw()





