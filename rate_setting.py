from PyQt5 import QtCore, QtWidgets
import globalvar

def getSteamRating(rate_num, percentage):
    if rate_num >= 500 and percentage >= 95:
        return "Overwhelmingly Positive"
    elif rate_num >= 50 and percentage >= 80:
        return "Very Positive"
    elif rate_num >= 10 and percentage >= 80:
        return "Positive"
    elif percentage >= 70:
        return "Mostly Positive"
    elif percentage >= 40:
        return "Mixed"
    elif percentage >= 20:
        return "Mostly Negative"
    elif percentage < 20 and rate_num >= 500:
        return "Overwhelmingly Negative"
    elif percentage < 20 and rate_num >= 50:
        return "Very Negative"
    elif percentage < 20 and rate_num >= 10:
        return "Negative"
    else:
        return "No Rating"

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(164, 133)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setMaximum(10000000)
        self.spinBox.setSingleStep(100)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_2.setMaximum(10000000)
        self.spinBox_2.setSingleStep(100)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame_4)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setRange(0, 100)
        self.verticalLayout_3.addWidget(self.horizontalSlider_2)
        self.verticalLayout.addWidget(self.frame_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.custom_setup(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Set Rating"))
        self.label.setText(_translate("Dialog", "Min Rating:"))
        self.label_3.setText(_translate("Dialog", "Max Rating:"))
        self.label_2.setText(_translate("Dialog", "Min User Rating:"))
        self.label_6.setText(_translate("Dialog", "%"))

    def custom_setup(self, Dialog):
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.buttonBox.accepted.connect(lambda: self.accept(Dialog))
        self.buttonBox.rejected.connect(Dialog.reject)
        self.horizontalSlider_2.valueChanged.connect(self.changeRatingNum)
        self.spinBox_2.valueChanged.connect(self.changeRatingNum)
    
        self.spinBox.setValue(globalvar.global_min_rating)
        self.spinBox_2.setValue(globalvar.global_max_rating)
        self.horizontalSlider_2.setValue(globalvar.global_user_rating)
        self.label_5.setText(str(globalvar.global_user_rating))
        self.label_4.setText(getSteamRating(globalvar.global_max_rating, globalvar.global_user_rating))

    def accept(self, Dialog):
        if self.spinBox.value() > self.spinBox_2.value():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Min Rating cannot be greater than Max Rating.")
            msg.setWindowTitle("Error")
            msg.exec_()
            return

        globalvar.global_min_rating = self.spinBox.value()
        globalvar.global_max_rating = self.spinBox_2.value()
        globalvar.global_user_rating = self.horizontalSlider_2.value()

        Dialog.close()

    def changeRatingNum(self):
        current_max_rating = self.spinBox_2.value()
        self.label_5.setText(str(self.horizontalSlider_2.value()))
        self.label_4.setText(getSteamRating(current_max_rating, self.horizontalSlider_2.value()))