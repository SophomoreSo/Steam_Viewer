from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(160, 176)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        self.custom_setup(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Parameters"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))

    def custom_setup(self, Dialog):
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.listWidget.itemDoubleClicked.connect(self.change_param)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget.customContextMenuRequested.connect(self.delete_param)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.clicked.connect(lambda: self.accept(Dialog))
        self.pushButton_2.clicked.connect(lambda: self.reject(Dialog))

        self.deleted_params = []

        self.initialize()

    def initialize(self):
        import globalvar
        user_id = globalvar.global_your_user_id
        params = globalvar.global_sql_op.getSavedParameter(user_id)
        for param in params:
            search_id = param[0]
            name = param[1]
            keyword = param[2]
            min_price = param[3]
            max_price = param[4]
            min_review = param[5]
            max_review = param[6]
            min_rating = param[7]
            hl_only = param[8]
            self.add_item(search_id, name, keyword, min_price, max_price, min_review, max_review, min_rating, hl_only)
    
    def add_item(self, _search_id, _name, _keyword, _min_price, _max_price, _min_review, _max_review, _min_rating, _hl_only):
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        item.setText(_name)
        item.search_id = _search_id
        item.name = _name
        item.keyword = _keyword
        item.min_price = _min_price
        item.max_price = _max_price
        item.min_review = _min_review
        item.max_review = _max_review
        item.min_rating = _min_rating
        item.hl_only = _hl_only
        self.listWidget.addItem(item)
    
    def delete_param(self, pos):
        item_index = self.listWidget.indexAt(pos).row()
        item = self.listWidget.item(item_index)

        if item is None:
            return
        
        from PyQt5.QtWidgets import QMessageBox
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Are you sure you want to delete this parameter?")
        msg.setWindowTitle("Delete Parameter")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.Yes)
        ret = msg.exec()

        if ret == QMessageBox.Yes:
            self.deleted_params.append(item.search_id)
            self.listWidget.takeItem(item_index)
        
    def change_param(self, item):
        from set_parameter import Ui_Dialog as set_parameter_UI
        self.set_parameter_diag = QtWidgets.QDialog()
        self.set_parameter_ui = set_parameter_UI()
        self.set_parameter_ui.setupUi(self.set_parameter_diag)
        self.set_parameter_ui.lineEdit.setText(item.name)
        self.set_parameter_ui.lineEdit.setReadOnly(True)
        self.set_parameter_ui.lineEdit.setDisabled(True)
        self.set_parameter_diag.exec()

    def accept(self, Dialog):
        import globalvar

        item = self.listWidget.currentItem()
        if item is None:
            Dialog.success = False
        else:        
            globalvar.global_search_lineEdit.setText(item.keyword)
            globalvar.global_min_price = int(item.min_price)
            globalvar.global_max_price = int(item.max_price)
            globalvar.global_min_rating = item.min_review
            globalvar.global_max_rating = item.max_review
            globalvar.global_user_rating = int(item.min_rating)
            globalvar.global_historical_low = item.hl_only
            Dialog.success = True

        user_id = globalvar.global_your_user_id
        for search_id in self.deleted_params:
            globalvar.global_sql_op.deleteParameter(user_id, search_id)
        
        if Dialog.success:
            Dialog.accept()
        else:
            Dialog.reject()

    def reject(self, Dialog):
        import globalvar
        user_id = globalvar.global_your_user_id
        for search_id in self.deleted_params:
            globalvar.global_sql_op.deleteParameter(user_id, search_id)

        Dialog.success = False
        Dialog.reject()