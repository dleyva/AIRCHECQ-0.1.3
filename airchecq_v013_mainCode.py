# -*- AIRCHECQ v 0.1.3 DLeyvaPernia 2018/11/05 -*-

import sys
from PyQt5 import QtWidgets as QW
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
import numpy as np
import pandas as pd
from airchecq_v013_layout import Ui_AIRCHECQv013
from functionsRiskThresholds import (risk_threshold1, risk_threshold2, risk_threshold3, risk_threshold4)
from functionsShortTimeVariation import (shortvariation1)
from functionsIAQindexes import iaq_general1
from functionPlot import plotGraph1, plotGraph2, plotGraph3, plotGraph5
import matplotlib.dates as mdates
from functionDataMining import outLayers


class AirchecqGui013Program(Ui_AIRCHECQv013):
    def __init__(self, dialog):
        Ui_AIRCHECQv013.__init__(self)
        self.setupUi(dialog)

        # Implement "login dialog"
        #self.lineEdit.setFocus()
        #self.lineEdit_2.setEchoMode(QW.QLineEdit.Password)
        #self.lineEdit.returnPressed.connect(self.pushButton.click)
        #self.lineEdit_2.returnPressed.connect(self.pushButton.click)
        self.pushButton.clicked.connect(self.handleLogin)

        # Load environmental data from file
        self.pushButton_2.clicked.connect(lambda: self.loadFile())

        # Selecting Material from list
        self.comboBox_7.currentIndexChanged.connect(lambda: self.selectMaterial(self.comboBox_7),
                                                    self.comboBox_7.currentIndex())

        # Selecting Colormap from list
        self.comboBox_9.currentIndexChanged.connect(lambda: self.plotIAQindexVisual(),
                                                    self.comboBox_9.currentIndex())

        # Selecting Env. parameters from list
        self.comboBox_4.currentIndexChanged.connect(lambda: self.selectParam(), self.comboBox_4.currentIndex())
        self.comboBox_5.currentIndexChanged.connect(lambda: self.selectParam(), self.comboBox_5.currentIndex())

        # Selecting Env. parameters from checkbox
        self.checkBox.stateChanged.connect(lambda: self.dataMining())
        self.checkBox_2.stateChanged.connect(lambda: self.dataMining())
        self.checkBox_3.stateChanged.connect(lambda: self.dataMining())
        self.checkBox_4.stateChanged.connect(lambda: self.dataMining())
        self.checkBox_5.stateChanged.connect(lambda: self.dataMining())
        self.checkBox_6.stateChanged.connect(lambda: self.dataMining())
        self.checkBox_7.stateChanged.connect(lambda: self.dataMining())

        # Selecting IAQ  from checkbox
        self.checkBox_70.stateChanged.connect(lambda: self.plotIAQindexVisual())
        self.checkBox_71.stateChanged.connect(lambda: self.plotIAQindexVisual())
        self.checkBox_711.stateChanged.connect(lambda: self.plotIAQindexVisual())
        self.checkBox_72.stateChanged.connect(lambda: self.plotIAQindexVisual())
        self.checkBox_721.stateChanged.connect(lambda: self.plotIAQindexVisual())
        self.checkBox_73.stateChanged.connect(lambda: self.plotIAQindexVisual())
        self.checkBox_74.stateChanged.connect(lambda: self.plotIAQindexVisual())
        self.checkBox_75.stateChanged.connect(lambda: self.plotIAQindexVisual())
        self.checkBox_76.stateChanged.connect(lambda: self.plotIAQindexVisual())
        self.checkBox_77.stateChanged.connect(lambda: self.plotIAQindexVisual())

        # Export file
        self.pushButton_3.clicked.connect(lambda: self.exportIAQ(self.graphicsView_4))

    def handleLogin(self):
        #if (self.lineEdit.text() == '' and self.lineEdit_2.text() == ''):
        #if (self.lineEdit.text() == 'airchecq' and self.lineEdit_2.text() == 'airchecq2018'):
        self.stackedWidget.setCurrentIndex(1)
        #else:
        #    m = QW.QMessageBox()
        #    m.setWindowTitle("Error")
        #    m.setText("Wrong user or password!")
        #    m.setIcon(QW.QMessageBox.Critical)
        #    m.setStandardButtons(QW.QMessageBox.Ok)
        #    m.exec_()

    def loadFile(self):
        self.directory, _filter = QFileDialog.getOpenFileName(None, "Open " + " Data File", '.', "(*.xlsx)")

        if self.directory:
            self.label_7.setText(self.directory)
            self.tabWidget.setEnabled(True)
            self.fillTable()
            self.loadParametersX()
            self.loadParametersY()
            self.plotEnvParam()
            self.loadMaterials()
            self.loadTypesOfThresholds()
            self.loadGraphOptions()
            self.loadDataMining()
            self.window.showMaximized()

    def fillTable(self):
            data_0 = pd.read_excel(self.directory, sheet_name=0, index_col=None, na_values=[np.nan])
            data = data_0.values
            self.t = data[:, 0]
            self.tmp = data[:, 1]
            self.rh = data[:, 2]
            self.lux = data[:, 3]
            self.uv = data[:, 4]
            self.pm = data[:, 5]
            self.no2 = data[:, 6]
            self.o3 = data[:, 7]
            self.ncol = len(data_0.columns)
            self.nrow = len(data_0.index)

            # Setting the variable t in a time format
            self.mtime = [mdates.date2num(x) for x in self.t]

            # Grouping the environmental data
            self.param = [self.mtime, self.tmp, self.rh, self.lux, self.uv, self.pm, self.no2, self.o3]

            self.tableWidget.setColumnCount(self.ncol)
            self.tableWidget.setRowCount(self.nrow)

            self.envParamNames = list(data_0)

            self.label_19.setText(min(self.t).strftime("%Y-%m-%d %H:%M"))
            self.label_21.setText(max(self.t).strftime("%Y-%m-%d %H:%M"))
            self.label_26.setText(str(self.nrow))

            # Time lapse between measurements (minutes)
            self.tLapse = self.t[1] - self.t[0]
            self.tLapse = (self.tLapse.days * 24 * 3600 + self.tLapse.seconds)/60

            self.label_25.setText(str(self.tLapse))

            # Time interval for short time fluctuations (hours)
            t_shortFluctuation = 24

            # Number of inputs inside the time window set for short time fluctuation.
            self.timeWindow = int(t_shortFluctuation * 60 / self.tLapse)

            self.tableWidget.setHorizontalHeaderLabels(self.envParamNames)
            for i in range(0, self.ncol):
                self.tableWidget.horizontalHeaderItem(i).setTextAlignment(QtCore.Qt.AlignLeft)

            for i in range(0, self.nrow):
                for j in range(0, self.ncol):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(data_0.iat[i, j])))

    def loadParametersX(self):
        self.comboBox_5.clear()
        self.comboBox_5.addItems(self.envParamNames)
        for i in range(0, 8):
            if np.isnan(min(self.param[i])):
                self.comboBox_5.model().item(i).setEnabled(False)

    def loadParametersY(self):
        self.comboBox_4.clear()
        for i in range(1, 8):
            self.comboBox_4.addItem(self.envParamNames[i])
            if np.isnan(min(self.param[i])):
                self.comboBox_4.model().item(i-1).setEnabled(False)

    def selectParam(self):
        self.xParamIndex = self.comboBox_5.currentIndex()
        self.yParamIndex = self.comboBox_4.currentIndex()
        self.plotEnvParam()

    def plotEnvParam(self):
        self.colors = ['#d9541a', '#0073bd', '#ffd600', '#bf00bf', '#78ab30', '#d9b3ff', '#4dbfed']

        if self.comboBox_5.currentIndex() == 0:
            try:
                for i in range(0, 7):
                    if self.comboBox_4.currentIndex() == i:
                        if ~np.isnan(min(self.param[i+1])):
                            plotGraph2(self.graphicsView_2, self.figure_2, self.mtime, self.param[i+1],
                                       self.comboBox_4.currentText(), self.colors[i])
                        else:
                            self.graphicsView_2.clear()
            except Exception as e:
                print(e)
        else:
            for i in range(0, 7):
                if self.comboBox_4.currentIndex() == i:
                    for j in range(1, 8):
                        if self.comboBox_5.currentIndex() == j:
                            if ~np.isnan(min(self.param[i+1])) and ~np.isnan(min(self.param[j])):
                                plotGraph1(self.graphicsView_2, self.figure_2, self.param[j],
                                           self.comboBox_5.currentText(), self.param[i+1],
                                           self.comboBox_4.currentText())
                            else:
                                self.graphicsView_2.clear()

    def loadMaterials(self):
        dataWF = {
            'RH too high (<75%)': [0.75, 0.75, 0.75, 0.5, 0.75, 1, 0.75, 0.75, 0.75, 0.25, 0.5, 0.5, 0.5, 0.75, 0.25,
                                   0.05, 0.5, 0.25, 1, 0.75, 0.75, 0.25, 0.75, 0.05, 0.05, 0.25, 0.75, 0.5, 0.25, 0.5,
                                   0.75, 0.75, 0.75, 0.75, 0.5],
            'RH too high (>75%)': [1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.05, 0.5, 0.25, 1, 1, 1, 0.25, 0.75,
                                   0.05, 0.05, 0.25, 0.75, 0.5, 0.25, 1, 1, 1, 1, 1, 0.75],
            'RH too low': [0.5, 0.5, 0.25, 0.05, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.05,
                           0.05, 0.05, 0.05, 0.5, 0.25, 0.05, 0.25, 0.05, 0.05, 0.05, 0.25, 0.05, 0.05, 0.25, 0.5, 0.25,
                           0.25, 0.25, 0.05],
            'RH too low (<25%)': [0.75, 1, 0.75, 0.05, 0.5, 0.75, 0.5, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.05,
                                  0.05, 0.05, 0.05, 0.75, 0.5, 0.05, 0.25, 0.05, 0.05, 0.05, 0.5, 0.05, 0.05, 0.5, 0.75,
                                  0.5, 0.5, 0.5, 0.25],
            'RH fluctuations': [0.75, 0.75, 0.5, 0.05, 0.5, 0.5, 0.5, 1, 0.25, 0.5, 0.5, 0.5, 1, 0.75, 0.5, 0.05, 0.05,
                                0.05, 0.05, 1, 0.75, 0.25, 0.75, 0.75, 0.25, 0.5, 0.05, 0.05, 0.05, 1, 0.5, 0.5, 0.75,
                                0.75, 0.05],
            'T too high': [0.25, 0.25, 0.5, 0.05, 1, 1, 1, 0.05, 0.05, 0.75, 0.75, 0.75, 0.75, 1, 0.75, 0.05, 0.05,
                           0.05, 0.05, 1, 1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.5, 1, 1, 1, 1, 0.75],
            'T too low': [0.05, 0.25, 0.25, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
                          0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
                          0.25, 0.05, 0.05, 0.05, 0.25],
            'T fluctuations': [0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25,
                               0.05, 0.05, 0.05, 0.05, 0.25, 0.25, 0.05, 0.25, 0.25, 0.25, 0.25, 0.05, 0.05, 0.25, 0.75,
                               0.25, 0.25, 0.25, 0.25, 0.05],
            'Visible light': [0.5, 0.5, 0.5, 0.5, 0.75, 1, 0.75, 0.5, 0.5, 0.75, 0.75, 0.75, 0.75, 1, 0.75, 0.05, 0.05,
                              0.05, 0.05, 0.75, 0.75, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.5, 0.75, 1, 1,
                              1, 1],
            'UV': [0.25, 0.75, 0.75, 0.75, 1, 1, 1, 0.75, 0.75, 1, 1, 1, 1, 1, 1, 0.05, 0.05, 0.05, 0.05, 1, 1, 0.05,
                   0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.75, 1, 1, 1, 1, 1],
            'O3/NOx/SO2': [0.25, 0.5, 0.5, 0.5, 0.75, 0.75, 0.75, 0.25, 0.25, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5,
                           0.25, 0.05, 0.5, 0.75, 0.75, 0.05, 0.25, 0.05, 0.05, 0.5, 0.05, 0.05, 0.5, 0.25, 0.75, 0.5,
                           0.5, 0.5, 1],
            'Gaseous organic pollutants': [0.25, 0.05, 0.5, 0.05, 0.5, 0.5, 0.5, 0.05, 0.05, 0.5, 0.5, 0.5, 0.5, 0.5,
                                           0.5, 0.05, 0.25, 1, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.05, 0.25, 0.05, 0.05,
                                           0.25, 0.25, 0.5, 0.25, 0.5, 0.5, 0.5],
            'H2S/OCS': [0.25, 0.05, 0.05, 0.25, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 1,
                        0.5, 0.25, 0.25, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 1,
                        0.05, 0.05, 0.05],
            'Particles/dust': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                               0.5, 0.5, 0.5, 0.25, 0.25, 0.05, 0.05, 0.25, 0.05, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25,
                               0.25, 0.25, 0.25, 0.25]}
        materials = {
            'Materials': ['General Collection', 'Paintings   |   Wood', 'Paintings   |   Canvas',
                          'Paintings   |   Copper',
                          'Paper   |   Cotton and Rag Paper', 'Paper   |   Groundwood Containing Paper',
                          'Paper   |   Lignin-free Paper', 'Wood   |   Restrained', 'Wood   |   Unrestrained',
                          'Textile   |   Vegetable Fibers', 'Textile   |   Wool/Hair',
                          'Textile   |   Unrestrained Silk',
                          'Textile   |   Restrained Silk', 'Textile   |   Weighted Silk',
                          'Textile   |   Synthetic Fibers',
                          'Metal   |   Silver', 'Metal   |   Copper', 'Metal   |   Lead', 'Metal   |   Iron',
                          'Leather and Parchment   |   Restrained', 'Leather and Parchment   |   Unrestrained',
                          'Glass   |   General', 'Glass   |   Crizzling', 'Ceramic   |   Terracotta/Earthenware',
                          'Ceramic   |   Stoneware/Porcelain', 'Stone   |   Limestone', 'Stone   |   Gypsum',
                          'Stone   |   Alabaster', 'Stone   |   Marble', 'Ivory/Bone/Antler/Horn',
                          'Feather/Insects/Stuffed Animals', 'Visual Media   |   Albumen',
                          'Visual Media   |   Collodion',
                          'Visual Media   |   Gelatin', 'Plastic   |   Malignant and Benign']}
        self.mat_df = pd.DataFrame(materials)
        self.wf_0 = pd.DataFrame(dataWF)
        self.wf_0 = self.wf_0.set_index(self.mat_df['Materials'])
        self.comboBox_7.clear()
        self.comboBox_7.addItems(self.wf_0.index)

    def selectMaterial(self, matIndex_1):
        self.material = matIndex_1.currentIndex()
        self.loadThresholds()
        self.loadWeighingFactors()
        self.calculateRisk()
        self.calculateIAQindex()
        self.plotIAQindexVisual()
        print(self.material)

    def loadTypesOfThresholds(self):
        self.comboBox_8.clear()
        self.comboBox_8.addItem('AIRCHECQ Weighted Thresholds')

    def loadThresholds(self):
        RhThTl_data = {
            'point 1': [25, 20, 20, 20, 25, 25, 25, 30, 10, 25, 25, 25, 25, 25, 25, 0, 0, 0, 0, 40, 25, 10, 35, 30, 10,
                        25, 20, 25, 25, 25, 30, 30, 30, 30, 30],
            'point 2': [40, 45, 40, 30, 40, 40, 40, 40, 30, 40, 40, 40, 40, 40, 40, 0, 0, 0, 0, 50, 30, 40, 41, 40, 40,
                        40, 35, 40, 40, 45, 45, 45, 45, 45, 45],
            'point 3': [60, 55, 60, 50, 60, 60, 60, 60, 70, 55, 55, 55, 55, 55, 55, 35, 35, 35, 35, 60, 40, 60, 43, 45,
                        60, 60, 45, 60, 60, 55, 55, 55, 55, 55, 55],
            'point 4': [75, 75, 75, 65, 70, 70, 70, 75, 75, 70, 70, 70, 70, 70, 70, 75, 75, 75, 75, 65, 60, 80, 50, 55,
                        80, 75, 60, 75, 75, 70, 70, 70, 70, 70, 70]}

        RhThTl = pd.DataFrame(RhThTl_data)


        RhThTl_0 = RhThTl.set_index(self.mat_df['Materials'])

        self.RhThTl = RhThTl_0.iloc[[self.material]]

        RhFluct_data = {
            'point 2': [30, 15, 30, 45, 30, 30, 30, 30, 45, 30, 30, 30, 15, 30, 30, 60, 60, 60, 60, 15, 30, 45, 15, 15,
                        30, 30, 30, 30, 30, 15, 15, 15, 15, 15, 30],
            'point 1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0]}

        RhFluct = pd.DataFrame(RhFluct_data)
        RhFluct_0 = RhFluct.set_index(self.mat_df['Materials'])

        self.RhFluct = RhFluct_0.iloc[[self.material]]

        TmpThTl_data = {
            'point 1': [7, 7, 7, 7, 5, 5, 5, 10, 0, 5, 5, 5, 5, 5, 5, -10, -10, -10, -10, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0,
                        10, 5, 0, -30, -30, 13],
            'point 2': [15, 10, 10, 10, 16, 16, 16, 15, 15, 16, 16, 16, 16, 16, 16, 0, 0, 0, 0, 10, 10, 10, 10, 15, 10,
                        15, 13, 15, 15, 16, 15, 15, 15, 15, 15],
            'point 3': [25, 25, 25, 25, 20, 20, 20, 25, 25, 18, 18, 18, 18, 18, 18, 25, 25, 25, 25, 18, 18, 25, 25, 22,
                        25, 25, 18, 25, 25, 20, 20, 20, 20, 20, 20],
            'point 4': [30, 30, 30, 30, 25, 25, 25, 30, 30, 25, 25, 25, 25, 25, 25, 35, 35, 35, 35, 25, 25, 30, 30, 30,
                        35, 30, 30, 30, 30, 25, 25, 25, 25, 25, 25]}

        TmpThTl = pd.DataFrame(TmpThTl_data)
        TmpThTl_0 = TmpThTl.set_index(self.mat_df['Materials'])

        self.TmpThTl = TmpThTl_0.iloc[[self.material]]

        TmpFluct_data = {'point 2': [15, 9, 9, 15, 6, 6, 6, 6, 15, 9, 9, 9, 9, 9, 9, 15, 15, 15, 15, 6, 15, 15, 15, 15, 15, 15, 15, 15, 15, 6, 6, 6, 6, 6, 6],
                          'point 1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

        TmpFluct = pd.DataFrame(TmpFluct_data)
        TmpFluct_0 = TmpFluct.set_index(self.mat_df['Materials'])

        self.TmpFluct = TmpFluct_0.iloc[[self.material]]

        Illum_data = {
            'point 1': [150, 150, 150, 150, 50, 50, 50, 150, 150, 50, 50, 50, 50, 50, 50, 250, 250, 250, 250, 50, 50,
                        250, 250, 250, 250, 150, 150, 150, 150, 150, 50, 50, 50, 50, 50],
            'point 2': [600, 600, 600, 600, 200, 200, 200, 600, 600, 200, 200, 200, 200, 200, 200, 1000, 1000, 1000,
                        1000, 200, 200, 1000, 1000, 1000, 1000, 600, 600, 600, 600, 600, 200, 200, 200, 200, 200]}

        Illum_0 = pd.DataFrame(Illum_data)
        Illum_0 = Illum_0.set_index(self.mat_df['Materials'])

        self.Illum = Illum_0.iloc[[self.material]]

        UltV_data = {
            'point 1': [10, 10, 10, 10, 0.01, 0.01, 0.01, 10, 10, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 10, 10, 10, 10, 0.01, 0.01, 10, 10, 10, 10, 10, 10,
                        10, 10, 10, 0.01, 0.01, 0.01, 0.01, 0.01],
            'point 2': [75, 75, 75, 75, 30, 30, 30, 75, 75, 30, 30, 30, 30, 30, 30, 75, 75, 75, 75, 30, 30, 75, 75, 75,
                        75, 75, 75, 75, 75, 75, 30, 30, 30, 30, 30]}

        UltV_0 = pd.DataFrame(UltV_data)
        UltV_0 = UltV_0.set_index(self.mat_df['Materials'])

        self.UltV = UltV_0.iloc[[self.material]]

        PM25_data = {
            'point 1': [1, 1, 1, 1, 0.1, 0.1, 0.1, 1, 1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 1,
                        0.1, 1, 1, 0.1, 0.1, 1, 1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
            'point 2': [10, 10, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 10, 10, 5, 5, 10,
                        10, 5, 5, 5, 5, 5, 5]}

        PM25_0 = pd.DataFrame(PM25_data)
        PM25_0 = PM25_0.set_index(self.mat_df['Materials'])

        self.PM25 = PM25_0.iloc[[self.material]]

        NO2_data = {
            'point 1a': [2, 2, 2, 2, 0.05, 0.05, 0.05, 2, 2, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 2, 0.16, 24, 2, 0.05,
                         0.05, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0.05],
            'point 1b': [10, 10, 10, 10, 0.26, 0.26, 0.26, 10, 10, 2.6, 2.6, 2.6, 2.6, 2.6, 2.6, 10, np.nan, np.nan, 10,
                         2.6, 2.6, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 2.6],
            'point 2a': [np.nan, np.nan, np.nan, np.nan, 26, 26, 26, np.nan, np.nan, 26, 26, 26, 26, 26, 26, np.nan, 26,
                         np.nan, np.nan, 26, 26, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
                         np.nan, np.nan, np.nan, np.nan, 26],
            'point 2b': [260, 260, 260, 260, 104, 104, 104, 260, 260, 104, 104, 104, 104, 104, 104, 260, 104, 260, 260,
                         104, 104, 260, 260, 260, 260, 260, 260, 260, 260, 260, 260, 260, 260, 260, 104]}

        NO2_0 = pd.DataFrame(NO2_data)
        NO2_0 = NO2_0.set_index(self.mat_df['Materials'])

        self.NO2 = NO2_0.iloc[[self.material]]

        O3_data = {
            'point 1a': [0.5, 0.5, 0.5, 0.5, 0.05, 0.05, 0.05, 0.5, 0.5, 0.015, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.5,
                         22.5, 0.5, 0.05, 0.05, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.05],
            'point 1b': [5, 5, 5, 5, np.nan, np.nan, np.nan, 5, 5, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
                         np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, np.nan],
            'point 2a': [75, 75, 75, 75, 25, 25, 25, 75, 75, 25, 25, 25, 25, 25, 25, 25, 75, np.nan, 75, 25, 25, 75, 75,
                         75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 25],
            'point 2b': [250, 250, 250, 250, 60, 60, 60, 250, 250, 60, 60, 60, 60, 60, 60, 60, 250, 250, 250, 60, 60,
                         250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 60]}

        O3_0 = pd.DataFrame(O3_data)
        O3_0 = O3_0.set_index(self.mat_df['Materials'])

        self.O3 = O3_0.iloc[[self.material]]

    def loadWeighingFactors(self):
        self.wf = np.empty(14)
        self.wf = self.wf_0.iloc[[self.material]]

    def calculateRisk(self):
        # Time window for short time fluctuation (hours)
        self.tShortFluct = 24

        # Calculating temperature related risk
        self.TmpThTlValues = self.TmpThTl.values
        self.riskTmp = risk_threshold1(self.tmp, self.TmpThTlValues[0, 0], self.TmpThTlValues[0, 1],
                                       self.TmpThTlValues[0, 2], self.TmpThTlValues[0, 3])

        # Calculating relative humidity related risk
        self.RhThTlValues = self.RhThTl.values
        self.riskRh = risk_threshold1(self.rh, self.RhThTlValues[0, 0], self.RhThTlValues[0, 1], self.RhThTlValues[0, 2]
                                      , self.RhThTlValues[0, 3])

        # Calculating temperature variation related risk
        self.tmp_flu = shortvariation1(self.tShortFluct, self.tLapse, self.tmp)
        self.TmpFluctValues = self.TmpFluct.values
        self.riskTmp_flu = risk_threshold2(self.tmp_flu, self.TmpFluctValues[0, 1], self.TmpFluctValues[0, 0])

        # Calculating relative humidity variation related risk
        self.rh_flu = shortvariation1(self.tShortFluct, self.tLapse, self.rh)
        self.RhFluctValues = self.RhFluct.values
        self.riskRh_flu = risk_threshold2(self.rh_flu, self.RhFluctValues[0, 1], self.RhFluctValues[0, 0])

        # Calculating PM2.5 related risk
        self.PM25Values = self.PM25.values
        self.riskPm = risk_threshold2(self.pm, self.PM25Values[0, 0], self.PM25Values[0, 1])

        # Calculating Illuminance related risk
        self.IllumValues = self.Illum.values
        self.riskLux = risk_threshold3(self.lux, self.IllumValues[0, 0], self.IllumValues[0, 1], 0.05)

        # Calculating UV related risk
        self.UltVValues = self.UltV.values
        self.riskUv = risk_threshold3(self.uv, self.UltVValues[0, 0], self.UltVValues[0, 1], 0.05)

        # Calculating NO2 related risk
        self.NO2Values = self.NO2.values
        self.riskNo2 = risk_threshold4(self.no2, self.NO2Values[0, 0], self.NO2Values[0, 1], self.NO2Values[0, 2],
                                       self.NO2Values[0, 3], 0.1, 0.9)

        # Calculating O3 related risk
        self.O3Values = self.O3.values
        self.riskO3 = risk_threshold4(self.o3, self.O3Values[0, 0], self.O3Values[0, 1], self.O3Values[0, 2],
                                      self.O3Values[0, 3], 0.1, 0.9)

    def calculateIAQindex(self):
        self.IAQ = np.empty(self.nrow)
        self.IAQ = iaq_general1(self.wf.values, self.RhThTl.values, self.TmpThTl.values, self.riskTmp, self.riskTmp_flu,
                                self.riskRh, self.riskRh_flu, self.riskLux, self.riskUv, self.riskPm, self.riskNo2,
                                self.riskO3, self.tmp, self.rh, self.nrow)

        self.iaqType = [self.IAQ, 1-self.riskRh, 1-self.riskRh_flu, 1-self.riskTmp, 1-self.riskTmp_flu, 1-self.riskLux,
                        1 - self.riskUv, 1-self.riskPm, 1-self.riskNo2,  1-self.riskO3]
        self.iaqName = ['General IAQ-index', 'RH IAQ-index', '$\Delta$RH IAQ-index', 'Temp. IAQ-index',
                        '$\Delta$Temp. IAQ-index',
                        'Illuminance IAQ-index', 'UV IAQ-index', 'PM IAQ-index', 'NO2 IAQ-index', 'O3 IAQ-index']

    def loadGraphOptions(self):
        self.checkBox_70.setChecked(True)

        if ~np.isnan(min(self.param[1])):
            self.checkBox_71.setDisabled(False)
            self.checkBox_71.setChecked(True)
            self.checkBox_711.setDisabled(False)
            self.checkBox_711.setChecked(True)
        else:
            self.checkBox_71.setDisabled(True)
            self.checkBox_71.setChecked(False)
            self.checkBox_711.setDisabled(True)
            self.checkBox_711.setChecked(False)

        if ~np.isnan(min(self.param[2])):
            self.checkBox_72.setDisabled(False)
            self.checkBox_72.setChecked(True)
            self.checkBox_721.setDisabled(False)
            self.checkBox_721.setChecked(True)
        else:
            self.checkBox_72.setDisabled(True)
            self.checkBox_72.setChecked(False)
            self.checkBox_721.setDisabled(True)
            self.checkBox_721.setChecked(False)

        if ~np.isnan(min(self.param[3])):
            self.checkBox_73.setDisabled(False)
            self.checkBox_73.setChecked(True)
        else:
            self.checkBox_73.setDisabled(True)
            self.checkBox_73.setChecked(False)

        if ~np.isnan(min(self.param[4])):
            self.checkBox_74.setDisabled(False)
            self.checkBox_74.setChecked(True)
        else:
            self.checkBox_74.setDisabled(True)
            self.checkBox_74.setChecked(False)

        if ~np.isnan(min(self.param[5])):
            self.checkBox_75.setDisabled(False)
            self.checkBox_75.setChecked(True)
        else:
            self.checkBox_75.setDisabled(True)
            self.checkBox_75.setChecked(False)

        if ~np.isnan(min(self.param[6])):
            self.checkBox_76.setDisabled(False)
            self.checkBox_76.setChecked(True)
        else:
            self.checkBox_76.setDisabled(True)
            self.checkBox_76.setChecked(False)

        if ~np.isnan(min(self.param[7])):
            self.checkBox_77.setDisabled(False)
            self.checkBox_77.setChecked(True)
        else:
            self.checkBox_77.setDisabled(True)
            self.checkBox_77.setChecked(False)

        self.comboBox_9.clear()
        self.comboBox_9.addItems(['Jet (Reversed)', 'Red-Yellow-Green', 'Viridis', 'Hot', 'Gray'])

    def plotIAQindexVisual(self):
        self.IAQselected = [self.checkBox_70.isChecked(), self.checkBox_71.isChecked(), self.checkBox_711.isChecked(),
                       self.checkBox_72.isChecked(), self.checkBox_721.isChecked(), self.checkBox_73.isChecked(),
                       self.checkBox_74.isChecked(), self.checkBox_75.isChecked(), self.checkBox_76.isChecked(),
                       self.checkBox_77.isChecked()]

        self.IAQtoPlot = np.empty(shape=[0, len(self.iaqType[0])])
        for i in range(0, 10):
            if self.IAQselected[i] is True:
                 self.IAQtoPlot = np.append(self.IAQtoPlot, [self.iaqType[i]], axis=0)

        self.IAQnameToPlot = ['']*len(self.IAQtoPlot)
        a = 0
        for i in range(0, 10):
            if self.IAQselected[i] is True:
                self.IAQnameToPlot[a] = self.iaqName[i]
                a += 1

        print('iaq to plot: ', self.IAQtoPlot)
        print(self.IAQnameToPlot)

        colormaps = ['jet_r',  'RdYlGn', 'viridis', 'hot', 'gray']
        colormap = 'jet_r'
        for i in range(0, 5):
            if self.comboBox_9.currentIndex() == i:
                colormap = colormaps[i]

        print(len(self.IAQtoPlot))

        plotGraph5(self.graphicsView_3, self.figure_3, self.IAQtoPlot, self.mtime, colormap,
                   ('IAQ-index,   Material: '+self.comboBox_7.currentText()), self.IAQnameToPlot)

    def plotIAQindexVisual_onChange(self):
        self.plotIAQindexVisual()

    def loadDataMining(self):
        if ~np.isnan(min(self.param[1])):
            self.checkBox.setDisabled(False)
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setDisabled(True)
            self.checkBox.setChecked(False)

        if ~np.isnan(min(self.param[2])):
            self.checkBox_2.setDisabled(False)
            self.checkBox_2.setChecked(True)
        else:
            self.checkBox_2.setDisabled(True)
            self.checkBox_2.setChecked(False)

        if ~np.isnan(min(self.param[3])):
            self.checkBox_3.setDisabled(False)
            self.checkBox_3.setChecked(True)
        else:
            self.checkBox_3.setDisabled(True)
            self.checkBox_3.setChecked(False)

        if ~np.isnan(min(self.param[4])):
            self.checkBox_4.setDisabled(False)
            self.checkBox_4.setChecked(True)
        else:
            self.checkBox_4.setDisabled(True)
            self.checkBox_4.setChecked(False)

        if ~np.isnan(min(self.param[5])):
            self.checkBox_5.setDisabled(False)
            self.checkBox_5.setChecked(True)
        else:
            self.checkBox_5.setDisabled(True)
            self.checkBox_5.setChecked(False)

        if ~np.isnan(min(self.param[6])):
            self.checkBox_6.setDisabled(False)
            self.checkBox_6.setChecked(True)
        else:
            self.checkBox_6.setDisabled(True)
            self.checkBox_6.setChecked(False)

        if ~np.isnan(min(self.param[7])):
            self.checkBox_7.setDisabled(False)
            self.checkBox_7.setChecked(True)
        else:
            self.checkBox_7.setDisabled(True)
            self.checkBox_7.setChecked(False)

        self.dataMining()

    def dataMining(self):
        self.outLayersEval = [np.zeros(len(self.tmp)), np.zeros(len(self.rh)), np.zeros(len(self.lux)),
                              np.zeros(len(self.uv)), np.zeros(len(self.pm)), np.zeros(len(self.no2)),
                              np.zeros(len(self.o3))]
        self.names = ['Temperature', 'Rel. Humidity', 'Illuminance', 'UV', 'PM2.5', 'NO2', 'O3']

        self.selectedParmeters = [self.checkBox.isChecked(), self.checkBox_2.isChecked(),
                                  self.checkBox_3.isChecked(), self.checkBox_4.isChecked(),
                                  self.checkBox_5.isChecked(), self.checkBox_6.isChecked(),
                                  self.checkBox_7.isChecked()]

        self.figure_4.clear()

        for i in range(0, 7):
            self.outLayersEval[i] = outLayers(self.param[i+1], self.timeWindow)
            if self.selectedParmeters[i] is True:
                plotGraph3(self.graphicsView_4, self.figure_4, self.mtime, self.outLayersEval[i], self.colors[i],
                           self.names[i])

    def exportIAQ(self, element):
        fileName, _ = QFileDialog.getSaveFileName(element, "QFileDialog.getSaveFileName()", "",
                                                  "(.csv)")
        df = pd.DataFrame(self.t, columns=['Timestamp'])

        for i in range(0, 9):
            df[self.iaqName[i]] = pd.DataFrame(self.iaqType[i])
            
        df.to_csv(str(fileName)+'.csv')

        if fileName:
            print('File exported:', fileName+'.csv')


if __name__ == '__main__':
    app = QW.QApplication(sys.argv)
    dialog = QW.QDialog()

    mainCode = AirchecqGui013Program(dialog)

    dialog.show()
    sys.exit(app.exec_())