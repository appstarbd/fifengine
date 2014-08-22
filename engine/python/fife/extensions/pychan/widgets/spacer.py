# -*- coding: utf-8 -*-

# ####################################################################
#  Copyright (C) 2005-2013 by the FIFE team
#  http://www.fifengine.net
#  This file is part of FIFE.
#
#  FIFE is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the
#  Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
# ####################################################################

from fife import fifechan

from widget import Widget
from fife.extensions.pychan.attrs import PointAttr

class Spacer(Widget):
	"""
	A spacer represents expandable or fixed 'whitespace' in the GUI.

	In a XML file you can get this by adding a <Spacer /> inside a VBox or
	HBox element (Windows implicitly are VBox elements).
	"""

	ATTRIBUTES = Widget.ATTRIBUTES + [ PointAttr('fixed_size'),
									   ]
	
	DEFAULT_HEXPAND = 1
	DEFAULT_VEXPAND = 1
	
	def __init__(self, 
				 parent = None, 
				 name = None,
				 size = None,
				 min_size = None, 
				 max_size = None, 
				 helptext = None, 
				 position = None, 
				 style = None, 
				 hexpand = None,
				 vexpand = None,
				 font = None,
				 base_color = None,
				 background_color = None,
				 foreground_color = None,
				 selection_color = None,
				 border_size = None,
				 position_technique = None,
				 is_focusable = None,
				 comment = None):
				 
		self.real_widget = fifechan.Spacer()
		super(Spacer,self).__init__(parent=parent, 
								  name=name, 
								  size=size, 
								  min_size=min_size, 
								  max_size=max_size,
								  helptext=helptext, 
								  position=position,
								  style=style, 
								  hexpand=hexpand, 
								  vexpand=vexpand,
								  font=font,
								  base_color=base_color,
								  background_color=background_color,
								  foreground_color=foreground_color,
								  selection_color=selection_color,
								  border_size=border_size,
								  position_technique=position_technique,
								  is_focusable=is_focusable,
								  comment=comment)
		if hexpand is not None: 
			self.hexpand = hexpand
		else:
			self.hexpand = self.DEFAULT_HEXPAND
		if vexpand is not None: 
			self.vexpand = vexpand
		else:
			self.vexpand = self.DEFAULT_VEXPAND

	def clone(self, prefix):
		spacerClone = Spacer(None,
				self._createNameWithPrefix(prefix),
				self.size,
				self.min_size, 
				self.max_size, 
				self.helptext, 
				self.position, 
				self.style, 
				self.hexpand,
				self.vexpand,
				self.font,
				self.base_color,
				self.background_color,
				self.foreground_color,
				self.selection_color,
				self.border_size,
				self.position_technique,
				self.is_focusable,
				self.comment)
				 
		return spacerClone
	