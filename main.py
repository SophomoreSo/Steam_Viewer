from PyQt5 import QtCore, QtWidgets
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

import globalvar

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(233, 70)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setFocusPolicy(QtCore.Qt.TabFocus)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setMaxLength(100)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_5.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 5))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.custom_setup(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Game Search"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Search Name Here!"))
        self.pushButton_5.setText(_translate("Dialog", "Search"))
        self.pushButton.setText(_translate("Dialog", "Price ▼"))
        self.pushButton_2.setText(_translate("Dialog", "Rating ▼"))
        self.pushButton_4.setText(_translate("Dialog", "Setting"))
    
    def custom_setup(self, Dialog):
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.pushButton_5.clicked.connect(self.search)
        self.pushButton.clicked.connect(self.price_setting)
        self.pushButton_2.clicked.connect(self.rate_setting)
        self.pushButton_4.clicked.connect(self.setting_setting)
    
    def price_setting(self):
        from price_setting import Ui_Dialog as price_UI
        self.price_diag = QtWidgets.QDialog()
        self.price_ui = price_UI()
        self.price_ui.setupUi(self.price_diag)
        self.price_diag.show()

    def rate_setting(self):
        from rate_setting import Ui_Dialog as rate_UI
        self.rate_diag = QtWidgets.QDialog()
        self.rate_ui = rate_UI()
        self.rate_ui.setupUi(self.rate_diag)
        self.rate_diag.show()

    def setting_setting(self):
        from setting_setting import Ui_Dialog as setting_UI
        self.setting_diag = QtWidgets.QDialog()
        self.setting_ui = setting_UI()
        self.setting_ui.setupUi(self.setting_diag)
        self.setting_diag.show()
    
    def search(self):
        from search_result import Ui_Dialog as search_UI
        if not globalvar.global_has_session:
            from login_setting import Ui_Dialog as setting_UI
            self.setting_diag = QtWidgets.QDialog()
            self.setting_ui = setting_UI()
            self.setting_ui.setupUi(self.setting_diag)
            self.setting_diag.exec()
            if not globalvar.global_has_session:
                return
        search_name = self.lineEdit.text()
        self.search_diag = QtWidgets.QDialog()
        self.search_ui = search_UI(search_name)
        self.search_ui.setupUi(self.search_diag)
        self.search_diag.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
