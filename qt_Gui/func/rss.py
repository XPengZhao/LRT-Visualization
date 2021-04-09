import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import seaborn as sns
from matplotlib.figure import Figure

class RssPlot(FigureCanvas):
    def __init__(self, widget):
        self.widget = widget
        self.fig = Figure(figsize=(200, 400), dpi=100)
        super(RssPlot, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)
        self.axes.set(title="Rss")
        self.draw()
    def updata_plot(self,data):
        self.axes.cla()
        self.axes.set(title='Rss')
        sns.heatmap(data, ax=self.axes,fmt=".3f",cbar=False,vmin=-90,vmax=-50,center=-70,cmap="rainbow_r", annot=True, annot_kws={'size':9,'weight':'bold', 'color':'black'})
        self.draw()