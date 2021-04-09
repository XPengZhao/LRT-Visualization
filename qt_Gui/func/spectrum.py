
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns



class SpectrumPlot(FigureCanvas):
    def __init__(self, widget):
        self.widget = widget
        self.fig = Figure(figsize=(200, 400), dpi=100)
        super(SpectrumPlot, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(121)
        self.axes.set(title="Spectrum")
        self.draw()

    def updata_plot(self, data,time):
        self.axes.cla()
        self.axes.set(title=time[0:19])
        sns.heatmap(data, ax=self.axes, fmt=".3f",xticklabels=100, yticklabels=False,cbar=False, center=0.5, vmax=1, vmin=0, cmap="gray", annot=False)

        self.draw()
        print(1111)
