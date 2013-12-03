# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import tank

from tank.platform.qt import QtCore, QtGui
from ..ui.list_widget import Ui_ListWidget

class ListWidget(QtGui.QWidget):
    """
    List widget
    """
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)

        # make sure this widget isn't shown
        self.setVisible(False)
        
        # set up the UI
        self.ui = Ui_ListWidget() 
        self.ui.setupUi(self)
        
        # make the background groupbox transparent for events so that
        # the select detection in the base class will work
        self.ui.box.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
            
    def set_selected(self, selected):
        """
        Adjust the style sheet to indicate selection or not
        """
        p = QtGui.QPalette()
        highlight_col = p.color(QtGui.QPalette.Active, QtGui.QPalette.Highlight)
        
        transp_highlight_str = "rgba(%s, %s, %s, 25%%)" % (highlight_col.red(), highlight_col.green(), highlight_col.blue())
        highlight_str = "rgb(%s, %s, %s)" % (highlight_col.red(), highlight_col.green(), highlight_col.blue())
        
        if selected:
            self.ui.box.setStyleSheet("""QGroupBox {border-width: 2px; 
                                                    border-color: %s; 
                                                    border-style: solid; 
                                                    background-color: %s}
                                      """ % (highlight_str, transp_highlight_str))
        else:
            self.ui.box.setStyleSheet("")
    
    def set_thumbnail(self, pixmap):
        """
        Set a thumbnail given the current pixmap.
        The pixmap must be 512x400 or it will appear squeezed
        """
        self.ui.thumbnail.setPixmap(pixmap)
    
    def set_text(self, line1, line2, line3):
        """
        Populate three lines of text in the widget
        """
        self.ui.label.setText("<b>%s</b><br>%s<br>%s" % (line1, line2, line3))        

    @staticmethod
    def calculate_size():
        """
        Calculates and returns a suitable size for this widget.
        """        
        return QtCore.QSize(200, 100)
