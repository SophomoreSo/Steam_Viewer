from PyQt5 import QtCore, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(206, 254)
        Dialog.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(6, 2, 6, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(5)
        self.horizontalLayout_3.addWidget(self.spinBox)
        self.verticalLayout.addWidget(self.frame_4)
        
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout.addWidget(self.frame)
        
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.verticalLayout.addWidget(self.frame_2)
        
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addWidget(self.frame_3)
        
        self.retranslateUi(Dialog)
        self.custom_setup(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Setting"))
        self.checkBox.setText(_translate("Dialog", "Search Autocomplete"))
        self.label.setText(_translate("Dialog", "Limit # of Result:"))
        self.pushButton_2.setText(_translate("Dialog", "Save Current Parameter"))
        self.pushButton.setText(_translate("Dialog", "Saved Parameters"))
        self.pushButton_4.setText(_translate("Dialog", "Manage Wishlist"))
        self.pushButton_5.setText(_translate("Dialog", "Check Wishlist Discounts"))
        self.label_3.setText(_translate("Dialog", "Last Updated:"))
        self.label_4.setText(_translate("Dialog", "2024-06-17"))
        self.pushButton_3.setText(_translate("Dialog", "Update DB"))
        self.label_5.setText(_translate("Dialog", "Log:"))
        self.label_6.setText(_translate("Dialog", "2024-06-17"))

    def custom_setup(self, Dialog):
        self.hideProgressBar()
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.pushButton_2.clicked.connect(self.saveParameter)
        self.pushButton.clicked.connect(self.savedParameter)
        self.pushButton_4.clicked.connect(self.manageWishlist)
        self.pushButton_5.clicked.connect(self.checkWishlistDiscounts)
        self.pushButton_3.clicked.connect(self.updateDB)

    def saveParameter(self):
        from set_parameter import Ui_Dialog as set_parameter_UI
        self.set_parameter_diag = QtWidgets.QDialog()
        self.set_parameter_ui = set_parameter_UI()
        self.set_parameter_ui.setupUi(self.set_parameter_diag)
        self.set_parameter_diag.exec()

        success = self.set_parameter_diag.success
        saved_name = self.set_parameter_diag.name

        if success:
            import globalvar
            user_id = globalvar.global_your_user_id
            keyword = globalvar.global_search_lineEdit.text()
            min_price = globalvar.global_min_price
            max_price = globalvar.global_max_price
            min_review = globalvar.global_min_rating
            max_review = globalvar.global_max_rating
            min_rating = globalvar.global_user_rating
            hl_only = globalvar.global_historical_low

            globalvar.global_sql_op.saveParameter(user_id, saved_name, keyword, min_price, max_price, min_review, max_review, min_rating, hl_only)

            from PyQt5.QtWidgets import QMessageBox
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Parameter saved successfully!")
            msg.setWindowTitle("Success")
            msg.exec()
        
    def savedParameter(self):
        from parameters import Ui_Dialog as parameters_UI
        self.parameters_diag = QtWidgets.QDialog()
        self.parameters_ui = parameters_UI()
        self.parameters_ui.setupUi(self.parameters_diag)
        self.parameters_diag.exec()

    def manageWishlist(self):
        from wishlist import Ui_Dialog as wishlist_UI
        self.wishlist_diag = QtWidgets.QDialog()
        self.wishlist_ui = wishlist_UI()
        self.wishlist_ui.setupUi(self.wishlist_diag)
        self.wishlist_diag.exec()

    def checkWishlistDiscounts(self):
        pass

    def hideProgressBar(self):
        self.frame_2.hide()
        self.frame_3.hide()

    def showProgressBar(self):
        self.frame_2.show()
        self.frame_3.show()

    def updateDB(self):
        self.showProgressBar()