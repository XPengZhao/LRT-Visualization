import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
from matplotlib.gridspec import GridSpec


class Viewer:
    def __init__(self, tk_root,tag_var):
        self.root = tk_root
        self.tag_var = tag_var
        self.setup_ui()

    def setup_ui(self):

        self.fig = Figure(figsize=(5, 5), tight_layout=True)

        gs = GridSpec(3, 4, figure=self.fig)
        self.ax = self.fig.add_subplot(gs[0:3,1:3])
        self.ax.set_axis_off()
        self.ax.set_facecolor("white")
        self.canvas = FigureCanvasTkAgg(self.fig, self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.init_fig(range(16))


    def init_fig(self, num):
        self.spots = []
        self.spots_text_num = []
        h_interval = 0.2
        v_interval = 0.2

        for i in range(16):
            x = 0.03 + int(i % 4) * h_interval
            y = 0.64 - int(i // 4) * v_interval
            s = mpatches.FancyBboxPatch([x, y],
                                        0.15,
                                        0.15,
                                        facecolor="white",
                                        boxstyle=mpatches.BoxStyle("square",
                                                                   pad=0.01))

            self.spots.append(s)
            t = self.ax.text(x + 0.02,
                             y + 0.04,
                             str(num[i]),
                             fontsize=14,
                             fontweight="bold")
            self.spots_text_num.append(t)

        self.ax.set_xlim(0, 0.8)
        self.ax.set_ylim(0, 0.8)
        collection = PatchCollection(self.spots)
        self.spots = self.ax.add_collection(collection)
        self.spots.set_facecolors('white')
        self.spots.set_edgecolors('gray')


    def update_fig(self,data):
        self.ax.cla()
        self.ax.set_axis_off()
        self.ax.set_facecolor("white")
        self.init_fig(range(16))
        f_colors = []
        e_colors = []
        for i in range(16):
            self.spots_text_num[i].set_text('{:.1f}'.format(data[self.tag_var.get()]['rss'][i]))
            if data[self.tag_var.get()]['rss'][i] >= 1:
                f_colors.append((1.0, 0, 0, 0.1))
                e_colors.append((1.0, 0, 0, 0.8))
            else:
                f_colors.append((0.0, 1.0, 0, 0.1))
                e_colors.append((0.0, 1.0, 0, 0.8))

        self.spots.set_facecolors(f_colors)
        self.spots.set_edgecolors(e_colors)
        self.canvas.draw()


class Controller:
    def __init__(self, root,tag_var):

        self.view = Viewer(root,tag_var)
