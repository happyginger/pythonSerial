# -*- coding: utf-8 -*-
'''
Created on 2014��10��30��

@author: Winter
'''
import sys
from PyQt4.QtGui import QApplication
from serialCom import MainWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Plastique")
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec_())
