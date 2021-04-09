import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

class LocalizationPlot(FigureCanvas):
    def __init__(self,  widget):
        self.widget = widget
        self.fig = Figure(figsize=(200, 100), dpi=100)
        super(LocalizationPlot, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)
        self.axes.set(title="Localization")
        self.mlp_bar = NavigationToolbar(self,self.widget)
        self.mlp_bar.hide()
        self.mpl_connect("button_press_event", self.mlp_bar.pan())
        self.mpl_connect("scroll_event", self.zoom)
        self.draw()




    # We only want the latest 80 plot
    # update and cancel the previous one
    def update_plot(self, data):

        xs = []
        ys = []

        for i in range(len(data)):
            xs.append(data[i][0])
            ys.append(data[i][1])
        self.axes.cla()
        self.axes.set(xlabel='x Axis (m)', ylabel='y Axis (m)')

        # # Update the right label
        for i in range(len(xs)):
            self.axes.plot(xs[i], ys[i], '.', color='#00BFFF')
        self.axes.set_xlim([0,1])
        self.axes.set_ylim([0, 1])
        self.draw()



    def zoom(self,event):
        self.ran = [self.axes.get_xlim()[0], self.axes.get_xlim()[1],
                    self.axes.get_ylim()[0], self.axes.get_ylim()[1]]
        if event.button == "up":
            self.ran[0] += 5
            self.ran[1] -= 5
            self.ran[2] += 5
            self.ran[3] -= 5
            self.axes.set_xlim(self.ran[0], self.ran[1])
            self.axes.set_ylim(self.ran[2], self.ran[3])
        else:
            self.ran[0] -= 5
            self.ran[1] += 5
            self.ran[2] -= 5
            self.ran[3] += 5
            self.axes.set_xlim(self.ran[0], self.ran[1])
            self.axes.set_ylim(self.ran[2], self.ran[3])
        self.draw()
    def getrange(self):
        return self.ran






#