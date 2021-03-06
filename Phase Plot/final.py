import json
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CheckFilter:
    def __init__(self, frame, vars):
        self.frame = frame
        self.vars = vars
        self.counter = 0
        self.image = tk.PhotoImage(file='Liu/button2.png')
        self.selectimage = tk.PhotoImage(file='Liu/button2_red.png')

    def update_filter(self, tags):
        if self.counter == len(tags):
            return

        new_tags = tags[self.counter:]
        self.counter += len(new_tags)

        for num in new_tags:
            button = tk.Checkbutton(
                self.frame, text='Antenna %d' % (num + 1), variable=self.vars[num], indicatoron=False,
                # justify=tk.CENTER,
                width=100, height=24, compound=tk.CENTER,
                image=self.image, selectimage=self.selectimage,
                bg='white', bd=0,
                font=('Times New Roman', 12, 'bold'))
            button.pack(anchor='w', fill=tk.BOTH)


class RadioFilter:
    def __init__(self, frame, var):
        self.frame = frame
        self.var = var
        self.counter = 0
        self.image = tk.PhotoImage(file='Liu/button2.png')
        self.selectimage = tk.PhotoImage(file='Liu/button2_red.png')

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
                font=('Times New Roman', 12, 'bold'))
            button.pack(anchor='w', fill=tk.BOTH)


class PhasePlot:
    def __init__(self, frame):
        # tk.Label(frame, text='Phase Plot', font=('times', 20)).pack()

        filter_frame = tk.LabelFrame(frame, text='Tag Filter', bg='white', bd=0,
                                     font=('Times New Roman', 12, 'bold'), labelanchor='n')
        filter_frame.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tag_var = tk.IntVar()
        self.tag_filter = RadioFilter(filter_frame, self.tag_var)

        filter_frame2 = tk.LabelFrame(frame, text='Phase Filter', bg='white', bd=0,
                                      font=('Times New Roman', 12, 'bold'), labelanchor='n')
        filter_frame2.pack(side=tk.LEFT, fill=tk.BOTH)
        self.phase_vars = [tk.IntVar() for i in range(16)]
        self.phase_filter = CheckFilter(filter_frame2, self.phase_vars)

        self.frame = frame

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_plot(self, data):
        self.phase_filter.update_filter([i for i in range(16)])
        self.tag_filter.update_filter(list(data.keys()))

        self.ax.cla()
        self.ax.set(xlabel='time (s)', ylabel='phase (cm)',
                    title='Phase Plot')
        self.ax.axis([0, 400, -6, 6])
        #self.ax.set_xlim(0, 400)
        #self.ax.set_ylim(-6, 6)

        try:
            ys = data[self.tag_var.get()]['phase']
        except:
            self.tag_var.set(list(data.keys())[0])
            ys = data[self.tag_var.get()]['phase']

        ls = []
        labels = []
        for i in range(16):
            l, = self.ax.plot(ys[i], label='antenna%d' % (i + 1),
                              visible=self.phase_vars[i].get())
            if l.get_visible():
                ls.append(l)
                labels.append(l.get_label())
        self.ax.legend(ls, labels, loc=1)
        self.canvas.draw()

        # self.frame.after(20, self.update_plot)


class Program:
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_title('Demo Interface')
        self.root.iconphoto(True, tk.PhotoImage(file='Liu/icon.png'))

        self.file_index = 0
        self.data = {}

        self.phase_plot = PhasePlot(self.root)

    def load_data(self):
        self.file_index += 1
        try:
            with open('json/t%d.json' % (self.file_index)) as f:
                raw_data = json.load(f)
        except:
            self.file_index -= 1
            return
        else:
            try:
                tag = self.data[raw_data['tag']]
            except:
                tag = {'phase': [[] for i in range(16)]}
                self.data[raw_data['tag']] = tag

            for i in range(16):
                tag['phase'][i].append(raw_data['phase'][i])
                if len(tag['phase'][i]) > 400:
                    tag['phase'][i] = tag['phase'][i][1:]
        finally:
            self.phase_plot.update_plot(self.data)
            self.root.after(1, self.load_data)

    def run(self):
        self.load_data()

        self.root.protocol('WM_DELETE_WINDOW', self.root.quit)
        self.root.mainloop()


def main():
    program = Program()
    program.run()


if __name__ == '__main__':
    main()
