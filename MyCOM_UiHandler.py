# -*- coding: utf-8 -*-
'''
Created on 2014��10��30��

@author: Winter
'''
from time import ctime
from PyQt4.QtGui import QKeySequence, QIcon, QPixmap
from PyQt4.QtCore import Qt
from Ui_serial import Ui_Dialog as MyCOM_UIForm
import Util
import re

abbss=20

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
        p=re.compile(r'speed\s*=\s*(\d+)')
        speedre=p.search(data)
        speed=speedre.group(1)
        self.sendcount.display(speed)
        print speed
        if not self.radioButton.isChecked():
            data = Util.toVisualHex(data)
        else:
            data = data.replace('\n', '<br/>')
        self.ReceivetextBrowser.append('<b>Recv</b> @%s<br/><font color="black">%s</font><br/><br/>'
                                        % (ctime(), data))
        self.receivecount.display(self.receivecount.intValue() + bytes)
        
    def setPortCombo(self,i,value):
        self.port.addItem(value)
    def removePortItems(self,num):
        self.port.removeItem(num)
    
    def getDataAndType(self):
        return self.SendtextEdit.toPlainText().toUtf8().data(), self.radioButton.isChecked() and "ascii" or "hex"
    
    def onSendData(self, data=None, _type="ascii"):
        if not data: data = self.SendtextEdit.toPlainText()
        if _type == "hex":
            data = ''.join(data.split())
            data = ' '.join([data[i:i+2] for i in xrange(0, len(data), 2)]).upper()
        else:
            data = data.replace('\n', '<br/>')
#         self.chatTextBrowser.append('<b>Send</b> @%s<br/><font color="white">%s</font><br/><br/>'
#                                      % (ctime(), data))
#         self.sendTextEdit.clear()
        bytes = _type == "ascii" and len(data) or len(data) / 2
        self.sendcount.display(self.sendcount.intValue() + bytes)
        
    def clearReceiveHistory(self):
        self.ReceivetextBrowser.clear()
        
    def ClearSendHistory(self):
        self.SendtextEdit.clear()
        
    def clearLcdNumber(self):
        self.sendcount.display(0)
        self.receivecount.display(0)
        
    def returndata(self):
        return self.data
    
