import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
from matplotlib.widgets import RadioButtons

xs = []
y1 = []
y2 = []

for i in range(0, 400, 2):
    xs.append(i)
    y1.append(np.random.uniform(0, 6))
    y2.append(np.random.uniform(-5, 1))

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.3)


axcolor = 'lightgoldenrodyellow'
rax = plt.axes([0.05, 0.7, 0.15, 0.15], facecolor=axcolor)
labels = ['test1', 'test2']
check = CheckButtons(rax, labels)
visible = {'test1': False, 'test2': False}


def func(label):
    visible[label] = not visible[label]


check.on_clicked(func)


while True:
    y1 = y1[1:]
    y2 = y2[1:]
    y1.append(np.random.uniform(0, 6))
    y2.append(np.random.uniform(-5, 1))
    ax.cla()
    ax.set_xlim(0, 400)
    ax.set_ylim(-6, 6)
    l0, = ax.plot(xs, y1, label='test1', visible=visible['test1'])
    l1, = ax.plot(xs, y2, label='test2', visible=visible['test2'])
    labels = []
    if l0.get_visible():
        labels.append(l0.get_label())
    if l1.get_visible():
        labels.append(l1.get_label())
    ax.legend(labels, loc=1)
    plt.pause(0.02)
