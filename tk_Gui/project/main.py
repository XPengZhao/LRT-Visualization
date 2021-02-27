import json
from tkinter import messagebox
from tkinter import Button

import localization as lz
import phase as ph
import rss as rs
import spectrum as sp
import tkinter as tk
import RangeFilter as rf

class CheckFilter:
    def __init__(self, frame, var):
        self.frame = frame
        self.var = var
        self.counter = 0
        self.image = tk.PhotoImage(file='../pic/button.png')
        self.selectimage = tk.PhotoImage(file='../pic/button2.png')

    def update_filter(self, tags):
        if self.counter == len(tags):
            return

        new_tags = tags[self.counter:]
        self.counter += len(new_tags)

        for num in new_tags:
            button = tk.Radiobutton(
                self.frame, text='Tag %d' % num, variable=self.var, value=num, indicatoron=False,
                width=100, height=30, compound=tk.CENTER,
                image=self.image, selectimage=self.selectimage,
                bg="#AEDDF2", bd=0,
                font=('Times New Roman', 12, 'bold')
                )

            button.pack(anchor='w', fill=tk.BOTH)
    def changeTag(self,data,num):
        data[num]["spec_chang"] = True

class Program:
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_title('Demo Interface')
        self.root.iconphoto(True, tk.PhotoImage(file='../pic/icon.png'))
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry('%sx%s' % (width, height))
        self.root.attributes("-topmost",True)


        self.file_index = 0
        self.data = {}

        self.lf_lz = tk.LabelFrame(self.root,text="Localization", labelanchor = "n")
        self.lf_lz.place(relx=0.2, rely=0, relwidth=0.4, relheight=0.5)
        self.lf_ph = tk.LabelFrame(self.root, text="Phase", labelanchor="n")
        self.lf_ph.place(relx=0.6, rely=0, relwidth=0.4, relheight=0.5)
        self.lf_rs = tk.LabelFrame(self.root, text="RSS", labelanchor="n")
        self.lf_rs.place(relx=0.6, rely=0.5, relwidth=0.4, relheight=0.5)
        self.lf_sp = tk.LabelFrame(self.root, text="SPECTRUM", labelanchor="n")
        self.lf_sp.place(relx=0.2, rely=0.5, relwidth=0.4, relheight=0.5)


        self.tag_var = tk.IntVar()

        filter_frame = tk.LabelFrame(self.root, text='Tag', labelanchor='n', bg="white")
        filter_frame.place(relx=0, rely=0, relwidth=0.08, relheight=0.5)
        self.tag_filter = CheckFilter(filter_frame, self.tag_var)

        self.ran = [-1, 1, -1, 1]
        Local_set = tk.LabelFrame(self.root, text='Local Set', labelanchor='n', bg="white")
        Local_set.place(relx=0, rely=0.5, relwidth=0.15, relheight=0.5)

        b1 = Button(Local_set, text='Zoom in', command=self.getuser).grid(row=5, column=1)
        b2 = Button(Local_set, text='Zoom out', command=self.backplot).grid(row=6, column=1)

        self.phase_plot = ph.PhasePlot(self.lf_ph, self.tag_filter, self.tag_var)
        self.localization_plot = lz.LocalizationPlot(self.lf_lz, self.tag_filter, self.tag_var)
        self.rss_plot = rs.Controller(self.lf_rs, self.tag_var)
        self.spectrum_plot = sp.SpectrumPlot(self.lf_sp, self.tag_var, self.tag_filter)
        self.local_set = rf.RangeFilter(Local_set)

    def backplot(self):
        self.ran = [-1, 1, -1, 1]
        self.local_set.e1.delete(0,'end')
        self.local_set.e2.delete(0,'end')
        self.local_set.e3.delete(0,'end')
        self.local_set.e4.delete(0,'end')

    def getuser(self):
        xlimL = self.inputCheck(self.local_set.e1.get())
        xlimR = self.inputCheck(self.local_set.e2.get())
        ylimL = self.inputCheck(self.local_set.e3.get())
        ylimR = self.inputCheck(self.local_set.e4.get())

        if xlimL == "bad_guy" or xlimR == "bad_guy":
            xlimL = -1
            xlimR = 1
        if ylimL == "bad_guy" or ylimR == "bad_guy":
            ylimL = -1
            ylimR = 1

        self.ran = [xlimL,xlimR, ylimL, ylimR]

    def inputCheck(self, word):
        valid_char = [str(i) for i in range(10)]
        valid_char.extend(['-', '.'])
        if not word:
            return "bad_guy"
        for c in word:
            if c not in valid_char:
                messagebox.showwarning('Warning', 'Please enter the real number!')
                break
            else:
                return word

    def load_data(self):
        self.file_index += 1
        try:
            with open('../data/t%d.json' % (self.file_index)) as f:
                raw_data = json.load(f)
        except:
            self.file_index -= 1
            return
        else:
            try:
                tag = self.data[raw_data['tag']]
            except:
                tag = {'phase': [[] for i in range(16)],
                       'pos': [[], []],
                       'rss':[[] for i in range(16)],
                       'spectrum': [[] for i in range(360)],
                       "spec_change": False
                       }

                self.data[raw_data['tag']] = tag


            for i in range(16):
                tag['phase'][i].append(raw_data['phase'][i])
                if len(tag['phase'][i]) > 400:
                    tag['phase'][i] = tag['phase'][i][1:]

            for i in range(2):
                tag['pos'][i].append(raw_data['pos'][i])
                if len(tag['pos'][i]) > 80:
                    tag['pos'][i] = tag['pos'][i][1:]

            tag['rss'] = [[] for j in range(16)]
            for i in range(16):
                tag['rss'][i] = raw_data['rss'][i]

            tag["spec_change"] = False
            if 'spectrum' in raw_data:
                tag["spectrum"] = [[]for i in range(360)]
                tag["spec_change"] = True
                for i in range(360):
                    for j in range(90):
                        tag['spectrum'][i].append(raw_data['spectrum'][i][j])

        finally:
            self.tag_filter.update_filter(list(self.data.keys()))
            self.tag_var.set(list(self.data.keys())[0])
            self.localization_plot.update_plot(self.data,self.ran)
            self.phase_plot.update_plot(self.data)
            self.spectrum_plot.update_plot(self.data)
            self.rss_plot.view.update_fig(self.data)




            self.root.after(1, self.load_data)

    def refresh(self):
        self.spectrum_plot.update_plot(self.data)

    def run(self):
        self.load_data()

        self.root.protocol('WM_DELETE_WINDOW', self.root.quit)
        self.root.mainloop()
if __name__ == '__main__':
    program = Program()
    program.run()
