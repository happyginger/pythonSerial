# -*- coding: utf-8 -*-
'''
Created on 2014��10��30��

@author: Winter
'''
from PyQt4 import QtGui,QtCore
from MyCOM_UiHandler import MyCOM_UiHandler
import Util

class MainWidget(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = MyCOM_UiHandler()
        self.flags = {"__isopen__": False, "__datatype__": "ascii"}
        self.ui.setupUi(self)

    def __setupSignal(self):
        self.ui.openPortButton.clicked.connect(self.__onOpenPort)
        self.ui.SendDataButton.clicked.connect(self.__onSendData)
        self.ui.ClearReceiveButton.clicked.connect(self.__onClearReceiveData)
        self.ui.ClearSendButton.clicked.connect(self.__onClearSendData)
        self.ui.recountButton.clicked.connect(self.__onReCount)
        
    def __openPort(self, settings=None):
#         print settings
        if not settings:
            settings = self.ui.getPortSettings()
#             print settings
            ret, msg = Util.formatPortSettins(settings)
            if not ret:
                return False, msg
                
        if not settings["port"]:
            return False, u"错误的串口号"
            
        self.serial = MySerial()
        self.connect(self.serial.qtobj, QtCore.SIGNAL("NewData"), self.ui.onRecvData)
        ret, msg = self.serial.open(settings)
        
        return ret, msg