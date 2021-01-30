import os
import json
import random

import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import animation
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
from matplotlib import cm
import numpy as np

class Viewer:
    def __init__(self, tk_root):
        self.root = tk_root
        self.setup_ui()

    def setup_ui(self):
        # button-tag1
        self.btn_t1 = tk.Button(self.root, text="Tag 1", width=25, height=2,
                                bg="#AEDDF2", font=('Times New Roman', 12, 'bold'))
        self.btn_t1.grid(row=0, column=0, pady=[5,5], padx=[5,5])
        # button-tag2
        self.btn_t2 = tk.Button(self.root, text="Tag 2", width=25, height=2,
                                bg='#F2B0AE', font=('Times New Roman', 12, 'bold'))
        self.btn_t2.grid(row=0, column=1, pady=[5,5], padx=[5,5])
        # fig_frame
        self.fig = Figure(figsize=(5, 5), tight_layout=True)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_axis_off()
        self.ax.set_facecolor("white")
        self.canvas = FigureCanvasTkAgg(self.fig, self.root)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)
        self.init_fig(range(16))

    def init_fig(self, num):
        self.spots = []
        self.spots_text_num = []
        h_interval = 0.2
        v_interval = 0.2

        for i in range(16):
            x = 0.05 + int(i % 4) * h_interval
            y = 0.65 - int(i // 4)* v_interval
            s = mpatches.FancyBboxPatch([x, y],
                                        0.1, 0.1, facecolor="white",
                                        boxstyle=mpatches.BoxStyle("Round",
                                                                   pad=0.02))

            self.spots.append(s)
            t = self.ax.text(x + 0.02, y + 0.04, str(num[i]),
                             fontsize=14, fontweight="bold")
            self.spots_text_num.append(t)

        self.ax.set_xlim(0, 0.8)
        self.ax.set_ylim(0, 0.8)
        collection = PatchCollection(self.spots)
        self.spots = self.ax.add_collection(collection)
        self.spots.set_facecolors('white')
        self.spots.set_edgecolors('gray')

    def update_fig(self, data):
        if len(data) != 0:
            f_colors = []
            e_colors = []
            for i in range(16):
                self.spots_text_num[i].set_text('{:.1f}'.format(data[1][1][i]))
                if data[1][1][i] <= 1:
                    f_colors.append((1.0,0,0,0.1))                
                    e_colors.append((1.0,0,0,0.8))
                else:
                    f_colors.append((0.0,1.0,0,0.1))                
                    e_colors.append((0.0,1.0,0,0.8))               

            self.spots.set_facecolors(f_colors)
            self.spots.set_edgecolors(e_colors)



class Controller:
    def __init__(self, root):
        self.view = Viewer(root)
        # prepare data
        data_tag1 = {}
        data_tag2 = {}
        for f in os.listdir(os.getcwd() + '\\' + "json"):
            with open("json" + '/' + f) as fp:
                temp = json.load(fp)
                if temp['tag'] == 1:
                    data_tag1.update({temp['time']:temp['rss']})
                if temp['tag'] == 2:
                    data_tag2.update({temp['time']:temp['rss']})
        self.sorted_data1 = sorted(data_tag1.items(), key=lambda x:x[0])
        self.sorted_data2 = sorted(data_tag2.items(), key=lambda x:x[0])

        # control parameters
        self.tag1_play = False
        self.tag1_current_index = 0
        self.tag2_play = False
        self.tag2_current_index = 0

        # animation
        self.fig_animation = animation.FuncAnimation(self.view.fig,
                                                     self.view.update_fig,
                                                     self.yield_fig_data,
                                                     interval=500,
                                                     blit=False)

        # bound button handling
        self.view.btn_t1.config(command=self.tag1_pressed)
        self.view.btn_t2.config(command=self.tag2_pressed)

    def yield_fig_data(self):
        if self.tag1_play:
            if self.tag1_current_index == len(self.sorted_data1):
                self.tag1_current_index = 0
                self.tag1_play = False
                yield []
            else:
                yield ['tag1', self.sorted_data1[self.tag1_current_index]]
                self.tag1_current_index += 1

        elif self.tag2_play:
            if self.tag2_current_index == len(self.sorted_data2):
                self.tag2_current_index = 0
                self.tag2_play = False
                yield []
            else:
                yield ['tag2', self.sorted_data2[self.tag2_current_index]]
                self.tag2_current_index += 1
        else:
            yield []

    def tag1_pressed(self):
        self.tag1_play = True
        self.tag2_play = False

    def tag2_pressed(self):
        self.tag1_play = False
        self.tag2_play = True



if __name__ == "__main__":
    gui = tk.Tk()
    ctl = Controller(gui)
    gui.mainloop()
