from __future__ import division, unicode_literals
import cssutils
import glob
import sys
from bs4 import BeautifulSoup
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQt5.QtCore import QUrl
# import urllib.request

# class Client(QWebEngineView):

#     def __init__(self, url):
#         self.app = QApplication(sys.argv)
#         QWebEngineView.__init__(self)
#         self.loadFinished.connect(self.on_page_load)
#         self.mainFrame().load(QUrl(url))
#         self.app.exec_()

#     def on_page_load(self):
#         self.app.quit()

# url = 'https://pythonprogramming.net/parsememcparseface/'

with open('out.txt','w') as outfile:
    for file in glob.glob("C:\\My Web Sites\\ssense\\www.ssense.com\\en-us\\men\\product\\acne-studios\\*\\*.html"):
        with open(file, 'r') as webpage:
                soup = BeautifulSoup(webpage, 'lxml')
                # Parse the html webpage
                descriptions = soup.find_all('meta', property="og:description")
                titles = soup.find_all('meta', property="og:title")
                prices = soup.find_all('meta', property="product:price:amount")

                for description in descriptions:
                    print(description["content"])
                    outfile.write(description["content"]+"\n")
                # for title in titles:
                #     print(title["content"])
                # for price in prices:
                #     print(price["content"])
