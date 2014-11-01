# -*- coding: utf-8 -*-
'''
Created on 2014��10��30��

@author: Winter
'''
from time import ctime
from PyQt4.QtGui import QKeySequence, QIcon, QPixmap
from PyQt4.QtCore import Qt
from Ui_serial import Ui_Dialog as MyCOM_UIForm


class MyCOM_UiHandler(MyCOM_UIForm):
    def __init__(self, parent=None):
        MyCOM_UIForm.__init__(self)

        
    def getPortSettings(self):
        settings = {
            "port": None, "baund": 9600, "bytesize": 8,
            "parity": "no", "stopbits": 1, "timeout": 1}
        settings['port']=self.port.currentText().toUtf8().data()
        settings['baund']=self.baund.currentText().toUtf8().data()
        settings['bytesize']=self.bytesize.currentText().toUtf8().data()
        settings['stopbits']=self.stopbits.currentText().toUtf8().data()
        settings['parity']=self.parity.currentText().toUtf8().data()
        print settings
        
#         fieldmap = ("port", "baund", "bytesize", "parity", "stopbits")
#         settings_line = self.setComboBox.currentText().toUtf8().data()
#         fields = settings_line.split(':')
#         for i in xrange(len(fields)):
#             settings[fieldmap[i]] = fields[i]

        return settings
    
    def onPortClosed(self):
        self.openPortButton.setText(u"打开串口")
        
    def onPortOpened(self):
        self.openPortButton.setText(u"关闭串口")
        
    def onRecvData(self, data):
        bytes = len(data)
#         if not self.radioButton.isChecked():
#             data = Util.toVisualHex(data)
#         else:
        data = data.replace('\n', '<br/>')
        self.ReceivetextBrowser.append('<b>Recv</b> @%s<br/><font color="yellow">%s</font><br/><br/>'
                                    % (ctime(), data))
        self.receivecount.display(self.receivecount.intValue() + bytes)
        
    def setPortCombo(self,i,value):
        self.port.addItem(value)
    def removePortItems(self,num):
        self.port.removeItem(num)