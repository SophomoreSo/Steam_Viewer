from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
import game_data

# imports 3rd party javascript modules
# https://www.pythonguis.com/tutorials/qresource-system/
import js_files

# https://stackoverflow.com/questions/58210400/how-to-receive-data-from-python-to-js-using-qwebchannel
class Backend(QtCore.QObject):
    @QtCore.pyqtSlot(int)
    def getRef(self, x):
        if x < 0:
            import globalvar
            globalvar.global_current_page = -x
            self.pageUI.loadPage()
        else:
            self.pageUI.loadGamePage(x)
    @QtCore.pyqtSlot(int)
    def getSort(self, attribute):
        import globalvar
        # 1: sort by price
        # 2: sort by rating
        # 3: sort by name
        if attribute == 1:
            globalvar.global_sort_by = 'price'
        elif attribute == 2:
            globalvar.global_sort_by = 'rate_num'
        elif attribute == 3:
            globalvar.global_sort_by = 'game_name'
        self.pageUI.loadPage()

    @QtCore.pyqtSlot(bool)
    def getAscend(self, is_ascend):
        import globalvar
        globalvar.global_is_ascend = is_ascend
        self.pageUI.loadPage()

    @QtCore.pyqtSlot()
    def wishlist(self):
        import globalvar
        user_id = globalvar.global_your_user_id
        app_id = globalvar.global_viewing_app_id
        is_duplicate = globalvar.global_sql_op.isDuplicateWishlist(user_id, app_id)
        
        if is_duplicate:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Wishlist already added!")
            msg.setWindowTitle("Warning")
            msg.exec_()
            return

        from set_wishlist import Ui_Dialog as set_wishlist_UI
        self.set_wishlist_diag = QtWidgets.QDialog()
        self.set_wishlist_ui = set_wishlist_UI()
        self.set_wishlist_ui.setupUi(self.set_wishlist_diag)
        self.set_wishlist_diag.exec()

        if self.set_wishlist_diag.success:
            discount = self.set_wishlist_diag.discount
            globalvar.global_sql_op.addWishlist(user_id, app_id, discount)
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Wishlist added successfully!")
            msg.setWindowTitle("Success")
            msg.exec_()

    @QtCore.pyqtSlot()
    def findStreamer(self):
        import globalvar
        app_id = globalvar.global_viewing_app_id
        self.pageUI.loadStreamListPage(app_id)

    @QtCore.pyqtSlot()
    def findDLCs(self):
        import globalvar
        app_id = globalvar.global_viewing_app_id
        self.pageUI.saveDLCResultToView(app_id)
        self.pageUI.loadPage()

    @QtCore.pyqtSlot(str)
    def openLink(self, link):
        import webbrowser
        webbrowser.open(link)

        
class Ui_Dialog(object):
    def __init__(self, search_name):
        self.search_name = search_name

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 700)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.SearchResult = QtWidgets.QWidget()
        self.SearchResult.setObjectName("SearchResult")
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.SearchResult)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.browser = QWebEngineView(self.SearchResult)
        
        self.browser.setObjectName("webBrowser")
        self.gridLayout_2.addWidget(self.browser, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.SearchResult)
        self.GamePage = QtWidgets.QWidget()
        self.GamePage.setObjectName("GamePage")
        self.stackedWidget.addWidget(self.GamePage)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.custom_setup(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Results"))
        
    def custom_setup(self, Dialog):
        self.backend = Backend()
        self.backend.pageUI = self
        self.channel = QWebChannel()
        self.browser.page().setWebChannel(self.channel)
        self.channel.registerObject("backend", self.backend)
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.saveResultToView()
        self.loadPage()

    def saveResultToView(self):
        import globalvar
        if globalvar.global_historical_low:
            globalvar.global_sql_op.advancedSearchWithHL(self.search_name,
                                                        globalvar.global_min_price, 
                                                        globalvar.global_max_price, 
                                                        globalvar.global_min_rating, 
                                                        globalvar.global_max_rating, 
                                                        globalvar.global_user_rating)
        else:
            globalvar.global_sql_op.advancedSearch(self.search_name, 
                                                    globalvar.global_min_price, 
                                                    globalvar.global_max_price, 
                                                    globalvar.global_min_rating, 
                                                    globalvar.global_max_rating, 
                                                    globalvar.global_user_rating)
        globalvar.global_search_count = globalvar.global_sql_op.getCountFromSearchResult()[0][0]
        globalvar.global_total_page = globalvar.global_search_count // globalvar.global_search_limit + 1
        globalvar.global_current_page = 1
        
    def loadPage(self):
        import globalvar
        import html_builder
        data_lst = globalvar.global_sql_op.getSearchResult(globalvar.global_search_limit,
                                                            globalvar.global_current_page,
                                                            globalvar.global_sort_by, 
                                                            globalvar.global_is_ascend)
        
        game_lst = []
        for data in data_lst:
            if data[5] is None:
                historical_low = False
            else:
                historical_low = data[5] > data[2]
            game = game_data.GamePageData(data[0], data[1], data[2], data[3], data[4], historical_low)
            game_lst.append(game)

        builder = html_builder.IndexPage()
        builder.setGameList(game_lst)
        builder.setSortOption(globalvar.global_sort_by)
        builder.setAscending(globalvar.global_is_ascend)
        builder.setNavigator(globalvar.global_total_page, globalvar.global_current_page)
        builder.setSearchResultCount(globalvar.global_search_count)
        html_result = builder.build()

        self.browser.setHtml(html_result)
    
    def loadGamePage(self, app_id):
        import globalvar
        import html_builder
        data = globalvar.global_sql_op.getGameById(app_id)[0]
        price = globalvar.global_sql_op.getPriceById(app_id)[0][0]
        description = globalvar.global_sql_op.getDescriptionById(app_id)
        description = description[0][0] if description else ''
        genres = globalvar.global_sql_op.getGameGenresById(app_id)
        price_history = globalvar.global_sql_op.getPriceHistoryById(app_id)
        reviews = globalvar.global_sql_op.getReviewByAppId(app_id)
        globalvar.global_viewing_app_id = app_id
        image_src = f'https://cdn.akamai.steamstatic.com/steam/apps/{data[0]}/header.jpg'
        builder = html_builder.GamePage()
        builder.setGameImage(image_src)
        builder.setGameName(data[1])
        builder.setGamePrice(price)
        builder.setGameDescription(description)
        builder.setGameGenre(genres)
        builder.setPriceHistory(price_history)
        builder.setReview(reviews)
        html_result = builder.build()
        self.browser.setHtml(html_result)

    def loadStreamListPage(self, app_id):
        import globalvar
        import html_builder
        streamer_tuple = globalvar.global_sql_op.getStreamerList(app_id)
        
        # set derived attribute "link" for each streamers
        # https://www.twitchmetrics.net/c/{streamer_id}-{streamer_name.lower()}
        streamer_dict = []
        for streamer in streamer_tuple:
            streamer_dict.append({'name': streamer[1], 
                                  'followers': streamer[2], 
                                  'link': f'https://www.twitchmetrics.net/c/{streamer[0]}-{streamer[1].lower()}'})
        builder = html_builder.StreamerPage()
        builder.setStreamers(streamer_dict)
        html_result = builder.build()
        self.browser.setHtml(html_result)

    def saveDLCResultToView(self, app_id):
        import globalvar
        globalvar.global_sql_op.searchDLCs(app_id)
        globalvar.global_search_count = globalvar.global_sql_op.getCountFromSearchResult()[0][0]
        globalvar.global_total_page = globalvar.global_search_count // globalvar.global_search_limit + 1
        globalvar.global_current_page = 1
        
        