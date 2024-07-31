from PyQt5 import QtCore, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(153, 145)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)

        self.custom_setup(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)

    def custom_setup(self, Dialog):
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget.itemDoubleClicked.connect(self.change_discount)
        self.listWidget.customContextMenuRequested.connect(self.delete_game)
        self.buttonBox.accepted.connect(lambda: self.accept(Dialog))
        self.buttonBox.rejected.connect(Dialog.reject)

        self.deleted_games = []

        from globalvar import global_sql_op, global_your_user_id
            
        wishlist = global_sql_op.getWishlist(global_your_user_id)
        self.list_wishlist(wishlist)

    def list_wishlist(self, wishlist):
        for game in wishlist:
            self.add_game(game[0], game[1], game[2])

    def add_game(self, app_id, game_name, discount):
        item = QtWidgets.QListWidgetItem()
        item.setText(game_name)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        item.value_changed = False
        item.app_id = app_id
        item.game_name = game_name
        item.discount = discount
        self.listWidget.addItem(item)

    def delete_game(self, pos):
        item_index = self.listWidget.indexAt(pos).row()
        item = self.listWidget.item(item_index)
        if item is None:
            return
        from PyQt5.QtWidgets import QMessageBox
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Are you sure you want to delete this game from your wishlist?")
        msg.setWindowTitle("Delete Game")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.Yes)
        ret = msg.exec()

        if ret == QMessageBox.Yes:
            self.deleted_games.append(item.app_id)
            self.listWidget.takeItem(item_index)
    
    def change_discount(self, item):
        from set_wishlist import Ui_Dialog as set_wishlist_UI
        self.set_wishlist_diag = QtWidgets.QDialog()
        self.set_wishlist_ui = set_wishlist_UI()
        self.set_wishlist_ui.setupUi(self.set_wishlist_diag, item.discount)
        self.set_wishlist_diag.exec()

        if self.set_wishlist_diag.success:
            item.discount = self.set_wishlist_ui.horizontalSlider.value()
            item.value_changed = True

    def accept(self, Dialog):
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if item.value_changed:
                from globalvar import global_sql_op, global_your_user_id
                global_sql_op.updateWishlist(global_your_user_id, item.app_id, item.discount)
        for app_id in self.deleted_games:
            from globalvar import global_sql_op, global_your_user_id
            global_sql_op.deleteWishlist(global_your_user_id, app_id)
        Dialog.accept()
