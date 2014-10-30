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

        