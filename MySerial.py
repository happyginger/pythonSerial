#-*- coding: utf-8 -*-
'''
Created on 2014��10��31��

@author: Winter
'''
import threading
from time import sleep
from PyQt4.QtCore import QObject, SIGNAL
from serial import Serial
class MySerial(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.qtobj = QObject()
        self.__terminate = False
        
    def open(self, settings):
        try:
            self.serial = Serial(settings["port"], settings["baund"], settings["bytesize"],
                    settings["parity"], settings["stopbits"], settings["timeout"])
            self.serial.flushInput()
            self.serial.flushOutput()
        except Exception, msg:
            return False, msg.message.decode("gbk")
        
        return True, "success"
    
    def terminate(self):
        self.__terminate = True
        
    def send(self, data, _type):
        self.serial.write(data)
        
    def __recv(self):
        data, quit = None, False
        while 1:
            if self.__terminate:
                break
            data = self.serial.read(1)
            if data == '':
                continue
            while 1:
                n = self.serial.inWaiting()
                if n > 0:
                    data = "%s%s" % (data, self.serial.read(n))
                    sleep(0.02) # data is this interval will be merged
                else:
                    quit = True
                    break
            if quit:
                break

        return data
    
    def close(self):
        if self.serial.isOpen():
            self.serial.close()
    
    def run(self):
        while 1:
            data = self.__recv()
            if not data:
                break
            self.qtobj.emit(SIGNAL("NewData"), data)

        self.serial.close()