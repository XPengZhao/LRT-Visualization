import json
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

TAGS = [("Test 1", 0), ("Test 2", 1), ("Test 3", 2), ("Test 4", 3),
        ("Test 5", 4), ("Test 6", 5), ("Test 7", 6), ("Test 8", 7),
        ("Test 9", 8), ("Test 10", 9), ("Test 11", 10), ("Test 12", 11),
        ("Test 13", 12), ("Test 14", 13), ("Test 15", 14), ("Test 16", 15)]


class Filter:
    def __init__(self, frame, v):
        for lang, num in TAGS:
            button = tk.Radiobutton(frame, text=lang, variable=v, value=num)
            button.pack(anchor='w')


class PhasePlot:
    def __init__(self, frame):
        # tk.Label(frame, text='Phase Plot', font=('times', 20)).pack()
        filter_frame = tk.LabelFrame(frame, text='Tag Filter',
                                     font=('times', 20), labelanchor='n')
        filter_frame.pack(side=tk.LEFT)

        self.v = tk.IntVar()
        self.v_value = 1
        self.v.set(1)
        self.filter = Filter(filter_frame, self.v)

        self.frame = frame
        self.i = 0  # index
        self.y = []  # list of show point
        self.K = 400  # max length of list

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def load_data(self):
        if self.v_value != self.v.get():
            self.v_value = self.v.get()
            self.i = 0
        while True:
            self.i += 1
            with open('json/t%d.json' % (self.i)) as f:
                data = json.load(f)
            if data['tag'] == 1:
                break
        return data

    def update_plot(self):
        data = self.load_data()
        if len(self.y) > self.K:
            self.y = self.y[1:]
        self.y.append(data['phase'][self.v_value])

        self.ax.cla()
        self.ax.set(xlabel='time (s)', ylabel='phase (cm)',
                    title='Phase Plot')
        self.ax.set_xlim(0, 400)
        self.ax.set_ylim(-6, 6)
        l, = self.ax.plot(self.y, label='test1')
        self.ax.legend([l.get_label()], loc=1)
        self.canvas.draw()
        self.frame.after(20, self.update_plot)

    def run(self):
        self.update_plot()


def main():
    root = tk.Tk()
    frame = tk.LabelFrame(root, text='Phase Plot',
                          font=('times', 20), labelanchor='n')
    frame.pack()

    root.wm_title('Demo Interface')
    # root.geometry('500x550')

    phase_plot = PhasePlot(frame)
    phase_plot.run()

    root.protocol('WM_DELETE_WINDOW', root.quit)
    tk.mainloop()


if __name__ == '__main__':
    main()
