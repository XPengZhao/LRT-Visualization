
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# the class set for the filter
# the input is nothing
# the output is show the filter and the button
# class CheckFilter:
#     # Initialization and get the button picture
#     def __init__(self, frame, vars):
#         self.frame = frame
#         self.vars = vars
#         self.counter = 0
#         self.image = tk.PhotoImage(file='../pic/button.png')
#         self.selectimage = tk.PhotoImage(file='../pic/button2.png')
#
#     # Update the filter
#     # In the tkinter instead of matplotlib
#
#     def update_filter(self, tags):
#         if self.counter == len(tags):
#             return
#
#         new_tags = tags[self.counter:]
#         self.counter += len(new_tags)
#
#         for num in new_tags:
#             var = tk.IntVar()
#             var.set(1)
#             self.vars.append(var)
#             # Set the attribute for the button
#             button = tk.Checkbutton(
#                 self.frame, text='Tag %d' % num, variable=self.vars[num - 1], indicatoron=False,
#                 width=120, height=30, compound=tk.CENTER,
#                 image=self.image, selectimage=self.selectimage,
#                 bg='white', bd=0,
#                 font=('Times New Roman', 12, 'bold'))
#             button.pack(anchor='w', fill=tk.BOTH)


class SpectrumPlot:
    def __init__(self, frame, tag_var, tag_filter):
        # filter_frame = tk.LabelFrame(frame, text='Tag Filter', bg='white', bd=0,
        #                              font=('Times New Roman', 12, 'bold'), labelanchor='n')
        # filter_frame.pack(side=tk.LEFT, fill=tk.BOTH)
        #
        # self.tag_vars = []
        # self.tag_filter = CheckFilter(filter_frame, self.tag_vars)

        self.frame = frame
        self.tag_var = tag_var
        self.tag_filter = tag_filter

        self.signal = tk.IntVar()

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_plot(self, data):
        # self.tag_filter.update_filter(list(data.keys()))
        # print(data[self.tag_var.get()]["spectrum"][0])
        if self.signal != self.tag_var.get():
            self.signal = self.tag_var.get()
            self.update_plot_change(data)
        else:
            if data[self.tag_var.get()]["spectrum"][0]:
                if data[self.tag_var.get()]["spec_change"]:
                    xs = []
                    ys = []
                    zs = []
                    for i in range(self.tag_filter.counter):
                        for j in range(360):
                            for z in range(90):
                                xs.append(j)
                                ys.append(z)
                                zs.append(data[self.tag_var.get()]['spectrum'][j][z])

                    self.ax.cla()
                    self.ax.set(xlabel='x Axis', ylabel='y Axis', zlabel='z Axis',
                                title='Spectrum Plot Tag%d' % (self.tag_var.get()))
                    self.ax.scatter(xs, ys, zs, c=zs, marker='.', cmap='rainbow')
                    self.canvas.draw()
    def update_plot_change(self,data):
        if data[self.tag_var.get()]["spectrum"][0]:
            xs = []
            ys = []
            zs = []
            for i in range(self.tag_filter.counter):
                for j in range(360):
                    for z in range(90):
                        xs.append(j)
                        ys.append(z)
                        zs.append(data[self.tag_var.get()]['spectrum'][j][z])

            self.ax.cla()
            self.ax.set(xlabel='x Axis', ylabel='y Axis', zlabel='z Axis',
                        title='Spectrum Plot Tag%d' % (self.tag_var.get()))
            self.ax.scatter(xs, ys, zs, c=zs, marker='.', cmap='rainbow')
            self.canvas.draw()


# class Program:
#     def __init__(self):
#         # Inout polyu's picture
#         self.root = tk.Tk()
#         self.root.wm_title('Demo Interface')
#         self.root.iconphoto(True, tk.PhotoImage(file='../pic/icon.png'))
#
#         self.file_index = 0
#         self.data = {}
#         self.spectrum_plot = SpectrumPlot(self.root)
#         self.signal = False
#
#     # get the data from json one by one in time
#     # But should change when use RabbitMQ
#     def load_data(self):
#         self.file_index += 1
#         try:
#             with open('../data/t%d.json' % self.file_index) as f:
#                 raw_data = json.load(f)
#         except:
#             self.file_index -= 1
#             return
#         else:
#             try:
#                 tag = self.data[raw_data['tag']]
#             except:
#                 tag = {'spectrum': [[] for i in range(360)]}
#                 self.data[raw_data['tag']] = tag
#
#
#             if 'spectrum' in raw_data:
#                 tag = {'spectrum': [[] for i in range(360)]}
#                 self.signal = True
#                 for i in range(360):
#                     for j in range(90):
#                         tag['spectrum'][i].append(raw_data['spectrum'][i][j])
#
#         finally:
#             # self.localization_plot.update_plot(self.data)
#             # print(raw_data['spectrum'])
#             if self.signal:
#                 self.spectrum_plot.update_plot(self.data)
#             self.root.after(100, self.load_data)
#
#
#     def run(self):
#         self.load_data()
#         self.root.protocol('WM_DELETE_WINDOW', self.root.quit)
#         self.root.mainloop()
#
#
# # the main entrance
# def main():
#     program = Program()
#     program.run()


if __name__ == '__main__':
    main()
