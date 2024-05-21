from PyQt5 import QtCore, QtGui, QtWidgets
import main

class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(160, 108)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(10000)
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setMaximum(10000)
        self.gridLayout.addWidget(self.spinBox_2, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(2, 1, 2, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.custom_setup(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Set Price"))
        self.label.setText(_translate("Dialog", "Min Price:"))
        self.label_2.setText(_translate("Dialog", "Max Price:"))
        self.checkBox.setText(_translate("Dialog", "Historical Low Only"))
        self.checkBox_2.setText(_translate("Dialog", "Hide Subscription"))

    def custom_setup(self, Dialog):
        self.buttonBox.accepted.connect(lambda: self.accept(Dialog))
        self.buttonBox.rejected.connect(Dialog.reject)

        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.spinBox.setValue(main.global_min_price)
        self.spinBox_2.setValue(main.global_max_price)
        self.checkBox.setChecked(main.global_historical_low)
        self.checkBox_2.setChecked(main.global_hide_subscription)

    def accept(self, Dialog):

        if self.spinBox.value() > self.spinBox_2.value():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Min price should be less than max price.")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        main.global_min_price = self.spinBox.value()
        main.global_max_price = self.spinBox_2.value()
        main.global_historical_low = self.checkBox.isChecked()
        main.global_hide_subscription = self.checkBox_2.isChecked()
        Dialog.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
