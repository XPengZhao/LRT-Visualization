import json
import localization as lz
import phase as ph
import rss as rs
import spectrum as sp
import tkinter as tk
import threading
# import RangeFilter as rf

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
    def __init__(self,ran,p_num):
        self.root = tk.Tk()
        self.root.wm_title('Demo Interface')
        self.root.iconphoto(True, tk.PhotoImage(file='../pic/icon.png'))
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry('%sx%s' % (width, height))
        self.root.attributes("-topmost",True)
        self.var_NumP = tk.StringVar()


        self.file_index = 0
        self.data = {}

        menubar = tk.Menu(self.root)
        setMenu = tk.Menu(menubar,tearoff = False)
        menubar.add_cascade(label="Setting",menu=setMenu)
        setMenu.add_command(label="Num of Point",command=self.setPointNum)
        setMenu.add_command(label="Time")
        processMenu = tk.Menu(menubar, tearoff = False)
        menubar.add_cascade(label="Process",menu=processMenu)
        processMenu.add_command(label="Pause")
        processMenu.add_command(label="Start")
        self.root.config(menu=menubar)

        self.ran = ran
        self.p_num = p_num

        self.var_NumP.set("Number: "+str(self.p_num))

        self.num_lab = tk.Label(self.root,textvariable=self.var_NumP)
        self.num_lab.place(relx=0.1, rely=0,relwidth=0.4, relheight=0.01)
        self.lf_lz = tk.LabelFrame(self.root,text="Localization", labelanchor = "n",cursor="hand2")
        self.lf_lz.place(relx=0.1, rely=0.02, relwidth=0.4, relheight=0.48)
        self.lf_ph = tk.LabelFrame(self.root, text="Phase", labelanchor="n")
        self.lf_ph.place(relx=0.5, rely=0.02, relwidth=0.4, relheight=0.48)
        self.lf_rs = tk.LabelFrame(self.root, text="RSS", labelanchor="n")
        self.lf_rs.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.4)
        self.lf_sp = tk.LabelFrame(self.root, text="SPECTRUM", labelanchor="n")
        self.lf_sp.place(relx=0.1, rely=0.5, relwidth=0.4, relheight=0.4)




        self.tag_var = tk.IntVar()

        filter_frame = tk.LabelFrame(self.root, text='Tag', labelanchor='n', bg="white")
        filter_frame.place(relx=0, rely=0.05, relwidth=0.08, relheight=0.5)
        self.tag_filter = CheckFilter(filter_frame, self.tag_var)

        self.phase_plot = ph.PhasePlot(self.lf_ph, self.tag_filter, self.tag_var)
        self.localization_plot = lz.LocalizationPlot(self.lf_lz, self.tag_filter, self.tag_var, self.ran)
        self.rss_plot = rs.Controller(self.lf_rs, self.tag_var)
        self.spectrum_plot = sp.SpectrumPlot(self.lf_sp, self.tag_var, self.tag_filter)

    def setPointNum(self):
        self.p_num = int(tk.simpledialog.askstring(title = 'Set Number',
                                                   prompt='Number：',
                                                   initialvalue = str(self.p_num)))
        self.var_NumP.set("Number: "+str(self.p_num))


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
                if len(tag['pos'][i]) > self.p_num:
                    tag['pos'][i] = tag['pos'][i][1:]
                    #动态设置数量

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

            self.root.after(500, self.load_data)

    def refresh(self):
        self.spectrum_plot.update_plot(self.data)

    def run(self):
        self.load_data()
        self.root.protocol('WM_DELETE_WINDOW', self.savedata)
        self.root.mainloop()


    def savedata(self):
        f = open("../user_data/lrtdata.txt","r+")
        f.seek(0)
        f.truncate()
        ran = self.localization_plot.getrange()
        word = ''
        for i in range(3):
            word += str(ran[i])+","
        word += str(ran[3])+"\n"+str(self.p_num)
        f.write(word)
        f.close()
        self.root.quit()


def readata():
    f = open("../user_data/lrtdata.txt","r+")
    data = f.readlines()
    ran = data[0].replace('\n','').split(",")
    for i in range(4):
        ran[i] = float(ran[i])
    p_num = int(data[1])
    return ran,p_num



if __name__ == '__main__':
    ran ,p_num = readata()
    program = Program(ran,p_num)
    program.run()


