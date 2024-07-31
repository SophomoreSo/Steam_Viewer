from PyQt5 import QtCore, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(258, 69)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.custom_setup(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Challenge"))
        self.label.setText(_translate("Dialog", "Password:"))

    def custom_setup(self, Dialog):
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.buttonBox.accepted.connect(lambda: self.accept(Dialog))
        self.buttonBox.rejected.connect(Dialog.reject)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setPlaceholderText("Enter Password Here!")

    def accept(self, Dialog):
        import sql_op
        import globalvar

        current_password = self.lineEdit.text()
        try:
            connector = sql_op.SqlOp(current_password)
            if connector is None:
                raise Exception("Server not connected.")
            globalvar.global_sql_op = connector
            globalvar.global_password = current_password
            globalvar.global_has_session = True
            Dialog.accept()

        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(str(e))
            msg.setWindowTitle("Error")
            msg.exec_()
            Dialog.reject()