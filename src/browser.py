#-*- encoding: utf-8 -*-
# Um navegador em poucas linhas de código

from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit
import sys

app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()

Form.resize(719, 547)
webView = QtWebKit.QWebView(Form)
webView.setGeometry(0, 0, 719, 547)
webView.setUrl(QtCore.QUrl("http://www.google.com.br/"))
    
Form.show()
sys.exit(app.exec_())
