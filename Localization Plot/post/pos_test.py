import json
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# the class set for the filter
# the input is nothing
# the output is show the filter and the button
class CheckFilter:
    # Initialization and get the button picture
    def __init__(self, frame, vars):
        self.frame = frame
        self.vars = vars
        self.counter = 0
        self.image = tk.PhotoImage(file='button.png')
        self.selectimage = tk.PhotoImage(file='button2.png')
    # Update the filter
    # In the tkinter instead of matplotlib

    def update_filter(self, tags):
        if self.counter == len(tags):
            return

        new_tags = tags[self.counter:]
        self.counter += len(new_tags)

        for num in new_tags:
            var = tk.IntVar()
            var.set(1)
            self.vars.append(var)
            # Set the attribute for the button
            button = tk.Checkbutton(
                self.frame, text='Tag %d' % num, variable=self.vars[self.counter-1], indicatoron=False,
                width=120, height=30, compound=tk.CENTER,
                image=self.image, selectimage=self.selectimage,
                bg='white', bd=0,
                font=('Times New Roman', 12, 'bold'))
            button.pack(anchor='w', fill=tk.BOTH)

# print out the point
class LocalizationPlot:
    def __init__(self, frame):
        filter_frame = tk.LabelFrame(frame, text='Tag Filter', bg='white', bd=0,
                                     font=('Times New Roman', 12, 'bold'), labelanchor='n')
        filter_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        self.tag_vars = []
        self.tag_filter = CheckFilter(filter_frame, self.tag_vars)

        self.frame = frame

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        # Hollow out
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    # We only want the latest 80 plot
    # update and cancel the previous one
    def update_plot(self, data):
        self.tag_filter.update_filter(list(data.keys()))

        xs = []
        ys = []
        for i in range(self.tag_filter.counter):
            xs.append(data[list(data.keys())[i]]['pos'][0])
            ys.append(data[list(data.keys())[i]]['pos'][1])

        self.ax.cla()
        self.ax.set(xlabel='x Axis (m)', ylabel='y Axis (m)',
                    title='Position Estimation Result')
        self.ax.axis([-1, 1, -1, 1])
        # Update the right label
        ls = []
        labels = []
        for i in range(len(xs)):
            l, = self.ax.plot(xs[i], ys[i], 'o',  # color='#00BFFF',
                              markerfacecolor='none', label=('Tag % d' % (i+1)),
                              visible=self.tag_vars[i].get())
            if l.get_visible():
                ls.append(l)
                labels.append(l.get_label())
        self.ax.legend(ls, labels, loc=1)
        self.canvas.draw()

# translate the matplotlib to tkinter
class Program:
    def __init__(self):
        # Inout polyu's picture
        self.root = tk.Tk()
        self.root.wm_title('Demo Interface')
        self.root.iconphoto(True, tk.PhotoImage(file='icon.png'))

        self.file_index = 0
        self.data = {}

        self.localization_plot = LocalizationPlot(self.root)
    # get the data from json one by one in time
    # But should change when use RabbitMQ
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
                tag = {'pos': [[],[]]}
                self.data[raw_data['tag']] = tag
            # print out the tag and the point at the same time
            for i in range(2):
                tag['pos'][i].append(raw_data['pos'][i])
                if len(tag['pos'][i]) > 80:
                    tag['pos'][i] = tag['pos'][i][1:]

        finally:
            self.localization_plot.update_plot(self.data)
            self.root.after(20, self.load_data)

    def run(self):
        self.load_data()
        self.root.protocol('WM_DELETE_WINDOW', self.root.quit)
        self.root.mainloop()

#the main entrance
def main():
    #get the value result from the class
    program = Program()
    #run the program
    program.run()


if __name__ == '__main__':
    main()
