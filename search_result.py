from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot, QVariant
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
import bs4
import main
import html
from sql_op import SqlOp

html_dir = './page.html'

current_page = 0

class GameData:
    def __init__(self, app_id, title, price, historically_low, rating, image_src):
        self.app_id = app_id
        self.title = title
        self.price = price
        self.historically_low = historically_low
        self.rating = rating
        self.image_src = image_src

    def toHtmlElement(self):
        HL = ''
        if self.historically_low:
            HL = r'<div class="historically-low">HL</div>'
        result = f'''
        <div class="game-card" style="animation-delay: 0s;">
            <img src="{self.image_src}" onclick="handleClick({self.app_id})">
            <div class="game-details">
                <div class="game-title" onclick="handleClick({self.app_id})">{self.title}</div>
                <div class="game-price">
                    ${self.price}
                    {HL}
                </div>
            </div>
        </div>
        '''
        return result

# https://stackoverflow.com/questions/58210400/how-to-receive-data-from-python-to-js-using-qwebchannel
class Backend(QtCore.QObject):
    @QtCore.pyqtSlot(int)
    def getRef(self, x):
        if x < 0:
            print("This is index", -x)
        else:
            print("This is item", x)


    # @QtCore.pyqtSlot(int)
    # def printRef(self, ref):
    #     print("inside printRef", ref)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 383)
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
        self.channel = QWebChannel()
        self.browser.page().setWebChannel(self.channel)
        self.channel.registerObject("backend", self.backend)

        sql_operation = SqlOp()
        search_name = main.getSearchName()
        data_lst = sql_operation.getGameByName("Team Fortress 2")
        game_lst = []
        for data in data_lst:
            rate_percentage = data[3] / data[2] * 100
            image_src = f'https://steamcdn-a.akamaihd.net/steam/apps/{data[4]}'
            game_lst.append(GameData(data[0], data[1], 20, True, rate_percentage, image_src))
            
        self.loadPage(game_lst)

    def loadPage(self, game_lst):
        html_result = ''
        content = ''
        
        with open(html_dir, 'r', encoding='utf-8-sig') as file:
            html_result = file.read()
        for data in game_lst:
            content += data.toHtmlElement()
        soup = bs4.BeautifulSoup(html_result, 'html.parser')
        soup.find('div', {'id': 'content'}).append(content)
        html_result = soup.prettify()
        html_result = str(soup)
        html_result = html.unescape(html_result)
        self.browser.setHtml(html_result)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
