import os
import json
import random

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import animation
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import numpy as np

class Viewer:
    def __init__(self, tk_root, new_tags, command):
        self.root = tk_root
        self.root.wm_title('Demo Interface')
        self.root.iconphoto(True, tk.PhotoImage(file='icon.png'))
        self.root.protocol('WM_DELETE_WINDOW', self.root.quit)
        self.image = tk.PhotoImage(file='Liu/button2.png')
        self.selectimage = tk.PhotoImage(file='Liu/button2_red.png')
        
        self.setup_ui(new_tags, command)
        
    def setup_ui(self, new_tags, command):
        self.filter_frame = tk.LabelFrame(self.root, 
                                          text='Tag Filter', bg='white', bd=0,
                                     font=('Times New Roman', 12, 'bold'), labelanchor='n')
        self.filter_frame.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.tag_var = tk.IntVar()
        # button-tags
        for tag in sorted(new_tags):
            button = tk.Radiobutton(self.filter_frame,
                                    text=tag,
                                    variable=self.tag_var,
                                    value=int(tag[-1]),
                                    indicatoron=False,
                                    width=100,
                                    height=30,
                                    compound=tk.CENTER,
                                    image=self.image,
                                    selectimage=self.selectimage,
                                    bg="#AEDDF2",
                                    bd=0,
                                    font=('Times New Roman', 12, 'bold'),
                                    command=command)
            button.pack(anchor='w', fill=tk.BOTH)
        # fig_frame
        self.fig = Figure(figsize=(5, 5), tight_layout=True)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_axis_off()
        self.ax.set_facecolor("white")
        self.canvas = FigureCanvasTkAgg(self.fig, self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.init_fig(range(16))

    def add_tag(self, tag, command):
        button = tk.Radiobutton(self.filter_frame,
                                text=tag,
                                variable=self.tag_var,
                                value=int(tag[-1]),
                                indicatoron=False,
                                width=100,
                                height=30,
                                compound=tk.CENTER,
                                image=self.image,
                                selectimage=self.selectimage,
                                bg="#AEDDF2",
                                bd=0,
                                font=('Times New Roman', 12, 'bold'),
                                command=command)
        button.pack(anchor='w', fill=tk.BOTH)
        
    def init_fig(self, num):
        self.spots = []
        self.spots_text_num = []
        h_interval = 0.2
        v_interval = 0.2

        for i in range(16):
            x = 0.05 + int(i % 4) * h_interval
            y = 0.65 - int(i // 4) * v_interval
            s = mpatches.FancyBboxPatch([x, y],
                                        0.1,
                                        0.1,
                                        facecolor="white",
                                        boxstyle=mpatches.BoxStyle("Round",
                                                                   pad=0.02))

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

    def update_fig(self, data):
        if len(data) != 0:
            f_colors = []
            e_colors = []
            for i in range(16):
                self.spots_text_num[i].set_text('{:.1f}'.format(data[1][i]))
                if data[1][i] >= 1:
                    f_colors.append((1.0, 0, 0, 0.1))
                    e_colors.append((1.0, 0, 0, 0.8))
                else:
                    f_colors.append((0.0, 1.0, 0, 0.1))
                    e_colors.append((0.0, 1.0, 0, 0.8))

            self.spots.set_facecolors(f_colors)
            self.spots.set_edgecolors(e_colors)

class Controller:
    def __init__(self, root):
        # data structure {'tag1':[[rss],[rss],...],
        #                 'tag2':[[rss],[rss],...],
        #                  ...
        #                }
        self.data = {}
        self.file_index = 550

        self.view = Viewer(root, self.data.keys(), self.change_tag)
        # animation
        self.fig_animation = animation.FuncAnimation(self.view.fig,
                                                     self.view.update_fig,
                                                     self.yield_fig_data,
                                                     interval=500,
                                                     blit=False)
        self.current_index = 0
        self.selected_tag = 0
        self.view.tag_var.set(1)
        
    def yield_fig_data(self):
        self.file_index += 1
        try:
            # print('json/t%d.json' % (self.file_index))
            with open('json/t%d.json' % (self.file_index)) as f:
                temp = json.load(f)
            tag = 'tag{}'.format(temp['tag'])
            if tag in self.data.keys():
                self.data[tag].append(temp['rss'])
            else:
                # add new tag button
                self.view.add_tag(tag, self.change_tag)
                # add new key to data
                self.data.update({tag:[temp['rss']]})
        except:
            self.file_index -= 1
            yield []
        
        k = list(self.data.keys())[self.selected_tag]
        if self.current_index >= len(self.data[k]):
            self.current_index = 0
            yield []
        else:
            yield [k, self.data[k][self.current_index]]
            self.current_index += 1
    
    def change_tag(self):
        self.current_index = 0 
        self.selected_tag = self.view.tag_var.get() - 1
            
if __name__ == "__main__":
    gui = tk.Tk()
    ctl = Controller(gui)
    gui.mainloop()