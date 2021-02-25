import json

import localization as lz
import phase as ph
import rss as rs
import spectrum as sp
import tkinter as tk
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
        self.lf_lz.place(relx=0.1, rely=0, relwidth=0.4, relheight=0.5)
        self.lf_ph = tk.LabelFrame(self.root, text="Phase", labelanchor="n")
        self.lf_ph.place(relx=0.51, rely=0, relwidth=0.4, relheight=0.5)
        self.lf_rs = tk.LabelFrame(self.root, text="RSS", labelanchor="n")
        self.lf_rs.place(relx=0.51, rely=0.5, relwidth=0.4, relheight=0.5)
        self.lf_sp = tk.LabelFrame(self.root, text="SPECTRUM", labelanchor="n")
        self.lf_sp.place(relx=0.1, rely=0.5, relwidth=0.4, relheight=0.5)


        self.tag_var = tk.IntVar()

        filter_frame = tk.LabelFrame(self.root, text='Tag', labelanchor='n', bg="white")
        filter_frame.place(relx=0, rely=0, relwidth=0.08, relheight=0.92)
        self.tag_filter = CheckFilter(filter_frame, self.tag_var)

        self.phase_plot = ph.PhasePlot(self.lf_ph, self.tag_filter, self.tag_var)
        self.localization_plot = lz.LocalizationPlot(self.lf_lz, self.tag_filter, self.tag_var)
        self.rss_plot = rs.Controller(self.lf_rs, self.tag_var)
        self.spectrum_plot = sp.SpectrumPlot(self.lf_sp, self.tag_var, self.tag_filter)


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
            self.localization_plot.update_plot(self.data)
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
