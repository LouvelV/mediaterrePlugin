"""
/***************************************************************************
Name			 	 : mediaterre Plugin
Description          : Zooms to issues
Date                 : 25/May/16 
copyright            : (C) 2016 by Vincent Louvel
email                : louvel.vincent9@gmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4 import QtCore, QtGui 
from Ui_mediaterreConseil import Ui_mediaterreConseil
# create the dialog for mediaterreConseil
class mediaterreConseilDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_mediaterreConseil ()
    self.ui.setupUi(self)