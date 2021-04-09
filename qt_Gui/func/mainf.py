# -*- coding: utf-8 -*-

import json
import time

import pandas as pd
import os

from PyQt5.QtCore import Qt

from mainwindow import Ui_MainWindow as mw
from loading import Ui_Dialog as ld
import localization
import phase
import rss
import spectrum
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QFileDialog, QDialog, QSlider, QHBoxLayout, \
    QVBoxLayout, QCheckBox


class processingWindow(QDialog,ld):
    def __init__(self):
        super(processingWindow, self).__init__()
        self.setupUi(self)



class MyWindow(QMainWindow, mw):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.data = {}
        self.ant_check = []
        self.tag = -1


        self.load_button.clicked.connect(self.loaddata)
        self.loading = processingWindow()
        self.loading.pushButton.clicked.connect(self.close_loading)
        self.tag_box.currentIndexChanged.connect(self.listen_tag_box)
        self.time_slider.sliderMoved.connect(self.timechange)
        self.time_slider.sliderReleased.connect(self.timechange_Rel)

        self.connect_button.clicked.connect(self.checkgoupbox)


        self.localization_layout = QVBoxLayout(self.localization_widget)
        self.localization_fig = localization.LocalizationPlot(self.localization_widget)
        self.localization_layout.addWidget(self.localization_fig)

        self.phase_layout = QVBoxLayout(self.phase_widget)
        self.phase_fig = phase.PhasePlot(self.phase_widget)
        self.phase_layout.addWidget(self.phase_fig)

        self.rss_layout = QVBoxLayout(self.rss_widget)
        self.rss_fig = rss.RssPlot(self.rss_widget)
        self.rss_layout.addWidget(self.rss_fig)

        self.spectrum_layout = QVBoxLayout(self.spectrum_widget)
        self.spectrum_fig = spectrum.SpectrumPlot(self.spectrum_widget)
        self.spectrum_layout.addWidget(self.spectrum_fig)



    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(int(newLeft), int(newTop))

    def changePnum(self):
        num_p = int(self.num_p_input.text())
        if num_p>len(list(self.data[self.tag]["Time"])):
            pass
        else:
            time_num = self.time_slider.value()
            self.localization_fig.update_plot(list(self.data[self.tag]["pos"])
                                                  [time_num:time_num + num_p])


    def listen_tag_box(self):
        self.tag = int(self.tag_box.currentText()[4:])
        self.time_start_label.setText(str(list(self.data[self.tag]["Time"])[0]))
        self.time_end_label.setText(str(list(self.data[self.tag]["Time"])[-1]))
        self.time_show_label.setText(str(list(self.data[self.tag]["Time"])[0]))
        self.time_slider.setMaximum(len(list(self.data[self.tag]["Time"])))
        self.time_slider.setMinimum(0)

    def timechange(self):
        if self.tag != -1:
            self.time_show_label.setText(list(self.data[self.tag]["Time"])[self.time_slider.value()-1])
            num_p = int(self.num_p_input.text())
            time_num = self.time_slider.value()
            self.localization_fig.update_plot(list(self.data[self.tag]["pos"])
                                                  [time_num:time_num + num_p])
            self.checkgoupbox()
            self.update_rss_data()

    def timechange_Rel(self):
        if self.tag != -1:
            self.time_show_label.setText(list(self.data[self.tag]["Time"])[self.time_slider.value() - 1])
            num_p = int(self.num_p_input.text())
            time_num = self.time_slider.value()
            self.localization_fig.update_plot(list(self.data[self.tag]["pos"])
                                              [time_num:time_num + num_p])
            self.checkgoupbox()
            self.update_rss_data()
            self.update_spectrum_data()

    def lisencheckbox(self):
        for checkbox in self.ant_box.findChildren(QCheckBox):
            checkbox.toggled.connect(self.checkgoupbox)

    def checkgoupbox(self):
        time_num = self.time_slider.value()
        self.ant_check = []
        for checkbox in self.ant_box.findChildren(QCheckBox):
            if checkbox.isChecked():
                self.ant_check.append(1)
            else:
                self.ant_check.append(0)
        self.phase_fig.update_plot(self.tag, time_num, self.ant_check)

    def give_data_to_phase(self):
        phase_data = {}
        phase_tag = [[] for i in range(16)]
        for tag in self.data:
            phase = list(self.data[tag]["phase"])
            for i in range(len(phase)):
                for j in range(16):
                    phase_tag[j].append(phase[i][j])
            phase_data[tag] = phase_tag
        self.phase_fig.get_data(phase_data)
        del phase_data,phase_tag

    def update_rss_data(self):
        time_num = int(self.time_slider.value())
        rss_data = list(self.data[self.tag]["rss"])[time_num]
        pre_data = pd.DataFrame([rss_data[0:4], rss_data[4:8], rss_data[8:12], rss_data[12:]])
        self.rss_fig.updata_plot(pre_data)

    def update_spectrum_data(self):
        time_num = int(self.time_slider.value())
        for i in range(30):
            if list(self.data[self.tag]["spectrum"])[i] !=0 :
                spectrum_data = list(self.data[self.tag]["spectrum"])[i]
                pre_data = pd.DataFrame(spectrum_data)
                self.spectrum_fig.updata_plot(pre_data, list(self.data[self.tag]["Time"])[time_num + i])
                del pre_data, spectrum_data
                break





    def show_loading(self):
        self.loading.show()

    def close_loading(self):
        self.loading.close()
        self.num_p_input.setText("1")
        for tag in self.data:
            self.tag_box.addItem("Tag "+str(tag))
        num_p = int(self.num_p_input.text())
        time_num = int(self.time_slider.value())
        self.checkgoupbox()
        self.localization_fig.update_plot(list(self.data[self.tag]["pos"])
                                               [time_num:time_num+num_p])
        self.update_rss_data()
        self.update_spectrum_data()





    def loaddata(self):
        data_file = QFileDialog.getExistingDirectory(self,
                  "Please select the experiment you want to view",
                  "../data")
        self.file_name_label.setText(str(data_file)[-10:])
        if data_file:
            files = os.listdir(data_file)
            self.show_loading()
            for file in files:
                path = data_file + "/" + file
                with open(path) as f:
                    load_dict = json.load(f)
                    try:
                        tag = self.data[load_dict['tagid']]
                    except:
                        tag = []
                    mid = list()
                    timeArray = time.strptime(load_dict["Time"][0:19], "%Y-%m-%d %H:%M:%S")
                    timeStamp = int(time.mktime(timeArray) + int(load_dict["Time"][20:24]))
                    mid.append(timeStamp)
                    mid.append(load_dict["Time"])
                    mid.append(load_dict["tagid"])
                    mid.append(load_dict["phase"])
                    mid.append(load_dict["rss"])
                    if "spectrum" in load_dict:
                        mid.append(load_dict["spectrum"])
                    else:
                        mid.append(0)
                    mid.append([load_dict["pos"][0]/1000,load_dict["pos"][1]/1000])
                    tag.append(mid)
                    self.data[load_dict['tagid']] = tag
            for tag in self.data.keys():
                self.data[tag] = pd.DataFrame(self.data[tag], columns=["TimeStamp","Time", "tagid", "phase", "rss", "spectrum", "pos"])
                self.data[tag].sort_values("TimeStamp",inplace=True)
                del load_dict, files
            self.give_data_to_phase()
            self.lisencheckbox()
            self.num_p_button.clicked.connect(self.changePnum)
            print(len(self.data[1]))


        else:
            pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow=MyWindow()
    myshow.center()
    myshow.show()
    sys.exit(app.exec_())


