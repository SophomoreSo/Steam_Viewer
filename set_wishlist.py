from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog, discount=0):
        Dialog.setObjectName("Dialog")
        Dialog.resize(174, 75)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.label_2.setText(str(discount))
        self.horizontalSlider.setValue(discount)

        self.retranslateUi(Dialog)
        self.custom_setup(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Set Wishlist"))
        Dialog.success = False
        self.label.setText(_translate("Dialog", "Desired Discount:"))
        self.label_3.setText(_translate("Dialog", "%"))

    def custom_setup(self, Dialog):
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.valueChanged.connect(self.updateDiscount)
        self.buttonBox.accepted.connect(lambda: self.accept(Dialog))
        self.buttonBox.rejected.connect(Dialog.reject)

    def updateDiscount(self):
        self.label_2.setText(str(self.horizontalSlider.value()))

    def accept(self, Dialog):
        Dialog.discount = self.horizontalSlider.value()
        Dialog.success = True
        Dialog.accept()