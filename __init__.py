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
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "mediaterre Plugin" 
def description():
  return "Zooms to issues"
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "1.0"
def classFactory(iface): 
  # load mediaterreConseil class from file mediaterreConseil
  from mediaterreConseil import mediaterreConseil 
  return mediaterreConseil(iface)
