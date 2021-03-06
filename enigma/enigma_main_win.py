from PyQt5 import QtCore, QtWidgets
from enigma import EnigmaMachine
import pyperclip, os, sys, webbrowser

QtCore.QCoreApplication.setOrganizationName("Michael Hollingworth")
QtCore.QCoreApplication.setOrganizationDomain("michaelhollingworth.io")
QtCore.QCoreApplication.setApplicationName("Enigma")


class Ui_Enigma(object):
  def about():
    about = QtWidgets.QMessageBox()
    about.setIcon(QtWidgets.QMessageBox.Information)
    about.setWindowTitle("About Enigma")
    about.setText("Enigma is an encoding app based on the famous German machine by the same name.")
    about.setInformativeText("It also contains the ability to enable 'typex' mode, which is based of the later British model.")
    about.setStandardButtons(QtWidgets.QMessageBox.Ok)
    about.exec()

  def setupUi(self, Enigma):
    Enigma.setObjectName("Enigma")
    Enigma.resize(800, 600)

    self.Enigma = Enigma

    self.rotor_options = list(EnigmaMachine.rotors.keys())
    self.settings = QtCore.QSettings("Michael Hollingworth", "Enigma")

    print(self.settings.value("config_path"))
    
    self.centralwidget = QtWidgets.QWidget(Enigma)
    self.centralwidget.setObjectName("centralwidget")
    self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
    self.verticalLayout_5.setObjectName("verticalLayout_5")
    self.config_groupBox = QtWidgets.QGroupBox(self.centralwidget)
    self.config_groupBox.setObjectName("config_groupBox")
    self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.config_groupBox)
    self.verticalLayout_4.setObjectName("verticalLayout_4")
    self.config_verticalLayout = QtWidgets.QVBoxLayout()
    self.config_verticalLayout.setObjectName("config_verticalLayout")
    self.configHeader_horizontalLayout = QtWidgets.QHBoxLayout()
    self.configHeader_horizontalLayout.setObjectName("configHeader_horizontalLayout")
    self.typex_checkBox = QtWidgets.QCheckBox(self.config_groupBox)
    self.typex_checkBox.setObjectName("typex_checkBox")
    self.configHeader_horizontalLayout.addWidget(self.typex_checkBox)
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.configHeader_horizontalLayout.addItem(spacerItem)
    self.reload_pushButton = QtWidgets.QPushButton(self.config_groupBox)
    self.reload_pushButton.setObjectName("reload_pushButton")
    self.configHeader_horizontalLayout.addWidget(self.reload_pushButton)
    self.config_verticalLayout.addLayout(self.configHeader_horizontalLayout)
    self.line = QtWidgets.QFrame(self.config_groupBox)
    self.line.setFrameShape(QtWidgets.QFrame.HLine)
    self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.line.setObjectName("line")
    self.config_verticalLayout.addWidget(self.line)
    self.rotor_widget = QtWidgets.QWidget(self.config_groupBox)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.rotor_widget.sizePolicy().hasHeightForWidth())
    self.rotor_widget.setSizePolicy(sizePolicy)
    self.rotor_widget.setObjectName("rotor_widget")
    self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.rotor_widget)
    self.verticalLayout_3.setObjectName("verticalLayout_3")
    self.rotors_gridLayout = QtWidgets.QGridLayout()
    self.rotors_gridLayout.setObjectName("rotors_gridLayout")
    spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.rotors_gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
    self.rotor2_comboBox = QtWidgets.QComboBox(self.rotor_widget)
    self.rotor2_comboBox.setObjectName("rotor2_comboBox")
    self.rotor2_comboBox.addItems(self.rotor_options)
    self.rotors_gridLayout.addWidget(self.rotor2_comboBox, 1, 3, 1, 1)
    self.rotor2_spinBox = QtWidgets.QSpinBox(self.rotor_widget)
    self.rotor2_spinBox.setObjectName("rotor2_spinBox")
    self.rotors_gridLayout.addWidget(self.rotor2_spinBox, 2, 3, 1, 1)
    self.rotor5_spinBox = QtWidgets.QSpinBox(self.rotor_widget)
    self.rotor5_spinBox.setObjectName("rotor5_spinBox")
    self.rotors_gridLayout.addWidget(self.rotor5_spinBox, 2, 9, 1, 1)
    self.rotor3_label = QtWidgets.QLabel(self.rotor_widget)
    self.rotor3_label.setObjectName("rotor3_label")
    self.rotors_gridLayout.addWidget(self.rotor3_label, 0, 5, 1, 1)
    spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.rotors_gridLayout.addItem(spacerItem2, 0, 8, 1, 1)
    spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.rotors_gridLayout.addItem(spacerItem3, 0, 6, 1, 1)
    self.rotor5_label = QtWidgets.QLabel(self.rotor_widget)
    self.rotor5_label.setObjectName("rotor5_label")
    self.rotors_gridLayout.addWidget(self.rotor5_label, 0, 9, 1, 1)
    spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.rotors_gridLayout.addItem(spacerItem4, 0, 10, 1, 1)
    self.rotor4_comboBox = QtWidgets.QComboBox(self.rotor_widget)
    self.rotor4_comboBox.setObjectName("rotor4_comboBox")
    self.rotor4_comboBox.addItems(self.rotor_options)
    self.rotors_gridLayout.addWidget(self.rotor4_comboBox, 1, 7, 1, 1)
    self.rotor1_comboBox = QtWidgets.QComboBox(self.rotor_widget)
    self.rotor1_comboBox.setObjectName("rotor1_comboBox")
    self.rotor1_comboBox.addItems(self.rotor_options)
    self.rotors_gridLayout.addWidget(self.rotor1_comboBox, 1, 1, 1, 1)
    spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.rotors_gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
    self.rotor5_comboBox = QtWidgets.QComboBox(self.rotor_widget)
    self.rotor5_comboBox.setObjectName("rotor5_comboBox")
    self.rotor5_comboBox.addItems(self.rotor_options)
    self.rotors_gridLayout.addWidget(self.rotor5_comboBox, 1, 9, 1, 1)
    self.rotor4_label = QtWidgets.QLabel(self.rotor_widget)
    self.rotor4_label.setObjectName("rotor4_label")
    self.rotors_gridLayout.addWidget(self.rotor4_label, 0, 7, 1, 1)
    self.rotor3_spinBox = QtWidgets.QSpinBox(self.rotor_widget)
    self.rotor3_spinBox.setObjectName("rotor3_spinBox")
    self.rotors_gridLayout.addWidget(self.rotor3_spinBox, 2, 5, 1, 1)
    spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.rotors_gridLayout.addItem(spacerItem6, 0, 2, 1, 1)
    self.rotor1_label = QtWidgets.QLabel(self.rotor_widget)
    self.rotor1_label.setObjectName("rotor1_label")
    self.rotors_gridLayout.addWidget(self.rotor1_label, 0, 1, 1, 1)
    self.rotor4_spinBox = QtWidgets.QSpinBox(self.rotor_widget)
    self.rotor4_spinBox.setObjectName("rotor4_spinBox")
    self.rotors_gridLayout.addWidget(self.rotor4_spinBox, 2, 7, 1, 1)
    self.rotor3_comboBox = QtWidgets.QComboBox(self.rotor_widget)
    self.rotor3_comboBox.setObjectName("rotor3_comboBox")
    self.rotor3_comboBox.addItems(self.rotor_options)
    self.rotors_gridLayout.addWidget(self.rotor3_comboBox, 1, 5, 1, 1)
    self.rotor2_label = QtWidgets.QLabel(self.rotor_widget)
    self.rotor2_label.setObjectName("rotor2_label")
    self.rotors_gridLayout.addWidget(self.rotor2_label, 0, 3, 1, 1)
    self.rotor1_spinBox = QtWidgets.QSpinBox(self.rotor_widget)
    self.rotor1_spinBox.setObjectName("rotor1_spinBox")
    self.rotors_gridLayout.addWidget(self.rotor1_spinBox, 2, 1, 1, 1)
    self.verticalLayout_3.addLayout(self.rotors_gridLayout)
    self.config_verticalLayout.addWidget(self.rotor_widget)
    self.line_2 = QtWidgets.QFrame(self.config_groupBox)
    self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
    self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.line_2.setObjectName("line_2")
    self.config_verticalLayout.addWidget(self.line_2)
    self.plugboard_groupBox = QtWidgets.QGroupBox(self.config_groupBox)
    self.plugboard_groupBox.setObjectName("plugboard_groupBox")
    self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.plugboard_groupBox)
    self.verticalLayout_2.setObjectName("verticalLayout_2")
    self.plugboard_scrollArea = QtWidgets.QScrollArea(self.plugboard_groupBox)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.plugboard_scrollArea.sizePolicy().hasHeightForWidth())
    self.plugboard_scrollArea.setSizePolicy(sizePolicy)
    self.plugboard_scrollArea.setWidgetResizable(True)
    self.plugboard_scrollArea.setObjectName("plugboard_scrollArea")
    self.scrollAreaWidgetContents = QtWidgets.QWidget()
    self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 743, 238))
    self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
    self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
    self.formLayout.setObjectName("formLayout")
    self.wire1_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    self.wire1_label.setObjectName("wire1_label")
    self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.wire1_label)
    self.wire1_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
    self.wire1_lineEdit.setMaxLength(2)
    self.wire1_lineEdit.setObjectName("wire1_lineEdit")
    self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.wire1_lineEdit)
    self.wire2_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    self.wire2_label.setObjectName("wire2_label")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.wire2_label)
    self.wire2_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
    self.wire2_lineEdit.setMaxLength(2)
    self.wire2_lineEdit.setObjectName("wire2_lineEdit")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.wire2_lineEdit)
    self.wire3_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    self.wire3_label.setObjectName("wire3_label")
    self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.wire3_label)
    self.wire3_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
    self.wire3_lineEdit.setMaxLength(2)
    self.wire3_lineEdit.setObjectName("wire3_lineEdit")
    self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.wire3_lineEdit)
    self.wire4_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    self.wire4_label.setObjectName("wire4_label")
    self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.wire4_label)
    self.wire4_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
    self.wire4_lineEdit.setMaxLength(2)
    self.wire4_lineEdit.setObjectName("wire4_lineEdit")
    self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.wire4_lineEdit)
    self.wire5_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    self.wire5_label.setObjectName("wire5_label")
    self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.wire5_label)
    self.wire5_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
    self.wire5_lineEdit.setMaxLength(2)
    self.wire5_lineEdit.setObjectName("wire5_lineEdit")
    self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.wire5_lineEdit)
    self.wire6_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    self.wire6_label.setObjectName("wire6_label")
    self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.wire6_label)
    self.wire6_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
    self.wire6_lineEdit.setMaxLength(2)
    self.wire6_lineEdit.setObjectName("wire6_lineEdit")
    self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.wire6_lineEdit)
    self.wire7_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    self.wire7_label.setObjectName("wire7_label")
    self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.wire7_label)
    self.wire7_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
    self.wire7_lineEdit.setMaxLength(2)
    self.wire7_lineEdit.setObjectName("wire7_lineEdit")
    self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.wire7_lineEdit)
    self.wire8_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    self.wire8_label.setObjectName("wire8_label")
    self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.wire8_label)
    self.wire8_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
    self.wire8_lineEdit.setMaxLength(2)
    self.wire8_lineEdit.setObjectName("wire8_lineEdit")
    self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.wire8_lineEdit)
    self.wire9_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    self.wire9_label.setObjectName("wire9_label")
    self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.wire9_label)
    self.wire9_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
    self.wire9_lineEdit.setMaxLength(2)
    self.wire9_lineEdit.setObjectName("wire9_lineEdit")
    self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.wire9_lineEdit)
    self.wire10_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    self.wire10_label.setObjectName("wire10_label")
    self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.wire10_label)
    self.wire10_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
    self.wire10_lineEdit.setMaxLength(2)
    self.wire10_lineEdit.setObjectName("wire10_lineEdit")
    self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.wire10_lineEdit)
    self.plugboard_scrollArea.setWidget(self.scrollAreaWidgetContents)
    self.verticalLayout_2.addWidget(self.plugboard_scrollArea)
    self.config_verticalLayout.addWidget(self.plugboard_groupBox)
    self.verticalLayout_4.addLayout(self.config_verticalLayout)
    self.verticalLayout_5.addWidget(self.config_groupBox)
    self.input_groupBox = QtWidgets.QGroupBox(self.centralwidget)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.input_groupBox.sizePolicy().hasHeightForWidth())
    self.input_groupBox.setSizePolicy(sizePolicy)
    self.input_groupBox.setObjectName("input_groupBox")
    self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.input_groupBox)
    self.verticalLayout_6.setObjectName("verticalLayout_6")
    self.input_plainTextEdit = QtWidgets.QPlainTextEdit(self.input_groupBox)
    self.input_plainTextEdit.setObjectName("input_plainTextEdit")
    self.verticalLayout_6.addWidget(self.input_plainTextEdit)
    self.verticalLayout_5.addWidget(self.input_groupBox)
    self.output_groupBox = QtWidgets.QGroupBox(self.centralwidget)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.output_groupBox.sizePolicy().hasHeightForWidth())
    self.output_groupBox.setSizePolicy(sizePolicy)
    self.output_groupBox.setObjectName("output_groupBox")
    self.verticalLayout = QtWidgets.QVBoxLayout(self.output_groupBox)
    self.verticalLayout.setObjectName("verticalLayout")
    self.output_plainTextEdit = QtWidgets.QPlainTextEdit(self.output_groupBox)
    self.output_plainTextEdit.setReadOnly(True)
    self.output_plainTextEdit.setObjectName("output_plainTextEdit")
    self.verticalLayout.addWidget(self.output_plainTextEdit)
    self.horizontalLayout = QtWidgets.QHBoxLayout()
    self.horizontalLayout.setObjectName("horizontalLayout")
    spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout.addItem(spacerItem7)
    self.encode_pushButton = QtWidgets.QPushButton(self.output_groupBox)
    self.encode_pushButton.setObjectName("encode_pushButton")
    self.horizontalLayout.addWidget(self.encode_pushButton)
    self.copy_pushButton = QtWidgets.QPushButton(self.output_groupBox)
    self.copy_pushButton.setObjectName("copy_pushButton")
    self.horizontalLayout.addWidget(self.copy_pushButton)
    self.verticalLayout.addLayout(self.horizontalLayout)
    self.verticalLayout_5.addWidget(self.output_groupBox)
    Enigma.setCentralWidget(self.centralwidget)
    self.menubar = QtWidgets.QMenuBar(Enigma)
    self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
    self.menubar.setObjectName("menubar")
    self.menuFile = QtWidgets.QMenu(self.menubar)
    self.menuFile.setObjectName("menuFile")
    self.menuHelp = QtWidgets.QMenu(self.menubar)
    self.menuHelp.setObjectName("menuHelp")
    self.menuEdit = QtWidgets.QMenu(self.menubar)
    self.menuEdit.setObjectName("menuEdit")
    Enigma.setMenuBar(self.menubar)
    self.statusbar = QtWidgets.QStatusBar(Enigma)
    self.statusbar.setObjectName("statusbar")
    Enigma.setStatusBar(self.statusbar)
    self.actionOpen_Config = QtWidgets.QAction(Enigma)
    self.actionOpen_Config.setObjectName("actionOpen_Config")
    self.actionPaste_Message = QtWidgets.QAction(Enigma)
    self.actionPaste_Message.setObjectName("actionPaste_Message")
    self.actionCopy_Output = QtWidgets.QAction(Enigma)
    self.actionCopy_Output.setObjectName("actionCopy_Output")
    self.actionExit = QtWidgets.QAction(Enigma)
    self.actionExit.setObjectName("actionExit")
    self.actionEnigma_Help = QtWidgets.QAction(Enigma)
    self.actionEnigma_Help.setObjectName("actionEnigma_Help")
    self.actionAbout_Enigma = QtWidgets.QAction(Enigma)
    self.actionAbout_Enigma.setObjectName("actionAbout_Enigma")
    self.actionEncode_Input = QtWidgets.QAction(Enigma)
    self.actionEncode_Input.setObjectName("actionEncode_Input")
    self.menuFile.addAction(self.actionEncode_Input)
    self.menuFile.addSeparator()
    self.menuFile.addAction(self.actionOpen_Config)
    self.menuFile.addSeparator()
    self.menuFile.addAction(self.actionExit)
    self.menuHelp.addAction(self.actionEnigma_Help)
    self.menuHelp.addSeparator()
    self.menuHelp.addAction(self.actionAbout_Enigma)
    self.menuEdit.addAction(self.actionPaste_Message)
    self.menuEdit.addAction(self.actionCopy_Output)
    self.menubar.addAction(self.menuFile.menuAction())
    self.menubar.addAction(self.menuEdit.menuAction())
    self.menubar.addAction(self.menuHelp.menuAction())

    # Collect elements
    self.combo_boxes =[self.rotor1_comboBox, self.rotor2_comboBox, self.rotor3_comboBox, self.rotor4_comboBox, self.rotor5_comboBox] 
    self.spin_boxes = [self.rotor1_spinBox, self.rotor2_spinBox, self.rotor3_spinBox, self.rotor4_spinBox, self.rotor5_spinBox]
    self.line_edits = [self.wire1_lineEdit, self.wire2_lineEdit, self.wire3_lineEdit, self.wire4_lineEdit, self.wire5_lineEdit, self.wire6_lineEdit, self.wire7_lineEdit, self.wire8_lineEdit, self.wire9_lineEdit, self.wire10_lineEdit]

    attempts = 0

    while True:
      attempts += 1

      try:
        self.enigmaMachine = EnigmaMachine(self.settings.value("config_path"))
        break
      except FileNotFoundError:
        if attempts > 5: break

        documents = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DocumentsLocation)
        config_path = f"{documents}/Enigma/enigma.ini"

        if not os.path.exists(f"{documents}/Enigma"):
          os.makedirs(f"{documents}/Enigma")
        
        with open(config_path, "w") as f:
          f.write("""
          [rotors]
          first = a
          second = b
          third = c
          fourth = d
          fifth = e

          [rotor positions]
          first_pos = 0
          second_pos = 0
          third_pos = 0
          fourth_pos = 0
          fifth_pos = 0

          [plugboard]
          wire0 = ak
          wire1 = bl
          wire2 = cm
          wire3 = dn
          wire4 = eo
          wire5 = fp
          wire6 = gq
          wire7 = hr
          wire8 = is
          wire9 = jt

          [typex]
          enable_typex = 0
          """[1:-1])
        self.settings.setValue("config_path", config_path)

    self.retranslateUi(Enigma)
    QtCore.QMetaObject.connectSlotsByName(Enigma)
    self.preloadUi()
    self.configureElements()
    self.makeConnections()

  def retranslateUi(self, Enigma):
    _translate = QtCore.QCoreApplication.translate
    Enigma.setWindowTitle(_translate("Enigma", "Enigma"))
    self.config_groupBox.setTitle(_translate("Enigma", "Config"))
    self.typex_checkBox.setText(_translate("Enigma", "Typex"))
    self.reload_pushButton.setText(_translate("Enigma", "Reload from File"))
    self.rotor3_label.setText(_translate("Enigma", "Rotor 3"))
    self.rotor5_label.setText(_translate("Enigma", "Rotor 5"))
    self.rotor4_label.setText(_translate("Enigma", "Rotor 4"))
    self.rotor1_label.setText(_translate("Enigma", "Rotor 1"))
    self.rotor2_label.setText(_translate("Enigma", "Rotor 2"))
    self.plugboard_groupBox.setTitle(_translate("Enigma", "Plugboard"))
    self.wire1_label.setText(_translate("Enigma", "Wire 1"))
    self.wire2_label.setText(_translate("Enigma", "Wire 2"))
    self.wire3_label.setText(_translate("Enigma", "Wire 3"))
    self.wire4_label.setText(_translate("Enigma", "Wire 4"))
    self.wire5_label.setText(_translate("Enigma", "Wire 5"))
    self.wire6_label.setText(_translate("Enigma", "Wire 6"))
    self.wire7_label.setText(_translate("Enigma", "Wire 7"))
    self.wire8_label.setText(_translate("Enigma", "Wire 8"))
    self.wire9_label.setText(_translate("Enigma", "Wire 9"))
    self.wire10_label.setText(_translate("Enigma", "Wire 10"))
    self.input_groupBox.setTitle(_translate("Enigma", "Input"))
    self.output_groupBox.setTitle(_translate("Enigma", "Output"))
    self.encode_pushButton.setText(_translate("Enigma", "Encode"))
    self.copy_pushButton.setText(_translate("Enigma", "Copy"))
    self.menuFile.setTitle(_translate("Enigma", "File"))
    self.menuHelp.setTitle(_translate("Enigma", "Help"))
    self.menuEdit.setTitle(_translate("Enigma", "Edit"))
    self.actionOpen_Config.setText(_translate("Enigma", "Open Config"))
    self.actionOpen_Config.setShortcut(_translate("Enigma", "Ctrl+,"))
    self.actionPaste_Message.setText(_translate("Enigma", "Paste Message"))
    self.actionPaste_Message.setShortcut(_translate("Enigma", "Ctrl+Shift+V"))
    self.actionCopy_Output.setText(_translate("Enigma", "Copy Output"))
    self.actionCopy_Output.setShortcut(_translate("Enigma", "Ctrl+Shift+C"))
    self.actionExit.setText(_translate("Enigma", "Exit"))
    self.actionExit.setShortcut(_translate("Enigma", "Ctrl+Q"))
    self.actionEnigma_Help.setText(_translate("Enigma", "Enigma Help"))
    self.actionEnigma_Help.setShortcut(_translate("Enigma", "Ctrl+Shift+/"))
    self.actionAbout_Enigma.setText(_translate("Enigma", "About Enigma"))
    self.actionEncode_Input.setText(_translate("Enigma", "Encode Input"))
    self.actionEncode_Input.setShortcut(_translate("Enigma", "Ctrl+E"))

  # Load the UI with values from the config
  def preloadUi(self):
    # Preload typex
    self.typex_checkBox.setChecked(self.enigmaMachine.typex)

    # Preload combo boxes
    for i in range(len(self.combo_boxes)):
      self.combo_boxes[i].setCurrentIndex(self.rotor_options.index(
        self.enigmaMachine.rotors[i]
      ))

    # Preload spin boxes
    for i in range(len(self.spin_boxes)):
      self.spin_boxes[i].setValue(self.enigmaMachine.rotor_positions[i])

    # Preload line edits
    for i in range(len(self.line_edits)):
      self.line_edits[i].setText(self.enigmaMachine.wires[i])

    # Enable/disable rotors
    self.rotor4_comboBox.setEnabled(self.enigmaMachine.typex)
    self.rotor4_spinBox.setEnabled(self.enigmaMachine.typex)
    self.rotor5_comboBox.setEnabled(self.enigmaMachine.typex)
    self.rotor5_spinBox.setEnabled(self.enigmaMachine.typex)

  # Configure the spin boxes
  def configureElements(self):
    # Configure spin boxes
    for spin_box in self.spin_boxes:
      spin_box.setWrapping(True)
      spin_box.setRange(0, len(EnigmaMachine.alphabet) - 1)

  # Connect all the elements to their handler methods
  def makeConnections(self):
    # Connect check box
    self.typex_checkBox.stateChanged.connect(self.check_box_state_changed)
    
    # Connect combo boxes
    for i in range(len(self.combo_boxes)):
      self.combo_boxes[i].currentTextChanged.connect(
        lambda val, i=i : self.combo_box_current_text_changed(i, val)
      )
    
    # Connect spin boxes
    for i in range(len(self.spin_boxes)):
      self.spin_boxes[i].valueChanged.connect(
        lambda val, i=i : self.spin_box_value_changed(i, val)
      )

    # Connect line edits
    for i in range(len(self.line_edits)):
      self.line_edits[i].textChanged.connect(
        lambda val, i=i : self.line_edit_text_changed(i, val)
      )

    # Connect buttons
    self.encode_pushButton.clicked.connect(self.encode)
    self.copy_pushButton.clicked.connect(self.copy)

    # Connect actions
    self.actionEncode_Input.triggered.connect(self.encode)
    self.actionOpen_Config.triggered.connect(self.open_config)
    self.actionCopy_Output.triggered.connect(self.copy)
    self.actionPaste_Message.triggered.connect(self.paste)
    self.actionExit.triggered.connect(sys.exit)
    self.actionAbout_Enigma.triggered.connect(Ui_Enigma.about)
    self.actionEnigma_Help.triggered.connect(lambda : webbrowser.open("https://github.com/M3L6H/secret-codes/tree/main/enigma"))

  # Enable/disable typex rotors
  def check_box_state_changed(self, val):
    self.enigmaMachine.typex = val
    self.enigmaMachine.write("typex", "enable_typex", str(val))

    self.rotor4_comboBox.setEnabled(val)
    self.rotor4_spinBox.setEnabled(val)
    self.rotor5_comboBox.setEnabled(val)
    self.rotor5_spinBox.setEnabled(val)

  # Update the currently picked rotors when the combo box is changed
  def combo_box_current_text_changed(self, i, val):
    other = None

    for j in range(len(self.combo_boxes)):
      if i == j: continue
      if self.combo_boxes[j].currentText() == val:
        other = self.combo_boxes[j]

    if other != None: other.setCurrentText(self.enigmaMachine.rotors[i])
    self.enigmaMachine.rotors[i] = val

    keys = ["first", "second", "third", "fourth", "fifth"]
    self.enigmaMachine.write("rotors", keys[i], str(val))

  # Update the positions of the rotors based on the spin boxes
  def spin_box_value_changed(self, i, val):
    keys = ["first_pos", "second_pos", "third_pos", "fourth_pos", "fifth_pos"]
    self.enigmaMachine.rotor_positions[i] = val
    self.enigmaMachine.write("rotor positions", keys[i], str(val))

  # Update the wire connections when they change
  def line_edit_text_changed(self, i, val):
    wire = self.enigmaMachine.wires[i]
    keys = ["wire0", "wire1", "wire2", "wire3", "wire4", "wire5", "wire6", "wire7", "wire8", "wire9"]
    
    # We just deleted a character and haven't updated the wires yet
    if len(val) == 1 and len(wire) == 2:
      # So remove the corresponding connection
      del self.enigmaMachine.plugboard[wire[0]]
      del self.enigmaMachine.plugboard[wire[1]]
      self.enigmaMachine.wires[i] = ""
    # We just added a new wire
    elif len(val) == 2:
      # This wire already exists, so we revert our change
      if val[0] in self.enigmaMachine.plugboard or val[1] in self.enigmaMachine.plugboard:
        self.line_edits[i].setText(val[0])
      # Otherwise we create the new connection and save it to our config
      else:
        if len(wire) == 2:
          del self.enigmaMachine.plugboard[wire[0]]
          del self.enigmaMachine.plugboard[wire[1]]
        self.enigmaMachine.wires[i] = val
        self.enigmaMachine.plugboard[val[0]] = val[1]
        self.enigmaMachine.plugboard[val[1]] = val[0]
        self.enigmaMachine.write("plugboard", keys[i], val)

  # Select a config file
  def open_config(self):
    config, _ = QtWidgets.QFileDialog.getOpenFileName(self.Enigma, "Open Config", self.settings.value("config_path"), "Config files (*.ini)")
    print(config)
    self.enigmaMachine.config = config
    self.settings.setValue("config_path", config)
    self.enigmaMachine.load()
    self.preloadUi()

  # Run a message through the machine
  def encode(self):
    self.enigmaMachine.load()
    self.preloadUi()
    msg = self.input_plainTextEdit.toPlainText()
    encoded = self.enigmaMachine.encode(msg)
    self.output_plainTextEdit.setPlainText(encoded)

  # Copy text from the output box
  def copy(self):
    pyperclip.copy(self.output_plainTextEdit.toPlainText())

  # Paste text into the input box
  def paste(self):
    self.input_plainTextEdit.setPlainText(pyperclip.paste())


if __name__ == "__main__":
  import sys
  app = QtWidgets.QApplication(sys.argv)
  Enigma = QtWidgets.QMainWindow()
  ui = Ui_Enigma()
  ui.setupUi(Enigma)
  Enigma.showMaximized()
  sys.exit(app.exec_())
