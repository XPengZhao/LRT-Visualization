import json
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Filter:
    def __init__(self, frame, var):
        self.frame = frame
        self.var = var
        self.counter = 0

    def update_filter(self, tags):
        if self.counter == len(tags):
            return

        new_tags = tags[self.counter:]
        self.counter += len(new_tags)

        for num in new_tags:
            button = tk.Radiobutton(
                self.frame, text='Tag ' + str(num), variable=self.var, value=num)
            button.pack(anchor='w')


class PhasePlot:
    def __init__(self, frame):
        # tk.Label(frame, text='Phase Plot', font=('times', 20)).pack()

        filter_frame = tk.LabelFrame(frame, text='Tag Filter',
                                     font=('times', 12), labelanchor='n')
        filter_frame.pack(side=tk.LEFT)

        self.tag_var = tk.IntVar()
        self.tag_var.set(1)
        self.tag_filter = Filter(filter_frame, self.tag_var)

        self.frame = frame

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_plot(self, data):
        self.tag_filter.update_filter(list(data.keys()))

        y = data[self.tag_var.get()]['phase'][0]

        self.ax.cla()
        self.ax.set(xlabel='time (s)', ylabel='phase (cm)',
                    title='Phase Plot')
        self.ax.set_xlim(0, 400)
        self.ax.set_ylim(-6, 6)
        l, = self.ax.plot(y, label='test1')
        self.ax.legend([l.get_label()], loc=1)
        self.canvas.draw()

        # self.frame.after(20, self.update_plot)


class Program:
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_title('Demo Interface')

        self.file_index = 0
        self.data = {}

        self.phase_plot = PhasePlot(self.root)

    def load_data(self):
        self.file_index += 1
        with open('json/t%d.json' % (self.file_index)) as f:
            raw_data = json.load(f)

            try:
                tag = self.data[raw_data['tag']]
            except:
                tag = {'phase': [[] for i in range(16)]}
                self.data[raw_data['tag']] = tag

            for i in range(16):
                tag['phase'][i].append(raw_data['phase'][i])
                if len(tag['phase'][i]) > 400:
                    tag['phase'][i] = tag['phase'][i][1:]

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
