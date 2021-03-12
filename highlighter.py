from PyQt5 import QtCore, QtGui


class Highlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent):
        super(Highlighter, self).__init__(parent)
        self.isOddNumberRow=False
        self.oddRowFormat = QtGui.QTextCharFormat()
        self.oddRowFormat.setForeground(QtCore.Qt.blue)
        #self.oddRowFormat.setBackground(QtCore.Qt.red)
        
        self.evenRowFormat = QtGui.QTextCharFormat()
        self.evenRowFormat.setForeground(QtCore.Qt.red)
        #self.evenRowFormat.setBackground(QtCore.Qt.blue)

    def highlightBlock(self, text):
        if self.isOddNumberRow:
            self.setFormat(0, len(text), self.oddRowFormat)
        else:
            self.setFormat(0, len(text), self.evenRowFormat)
        self.isOddNumberRow = not self.isOddNumberRow