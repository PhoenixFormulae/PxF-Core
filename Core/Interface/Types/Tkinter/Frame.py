## System Imports
from typing import List, Type


## Application Imports
from Core.Interface.Frame import FrameBase
from Core.Interface.View.Control import discovery
from Core.Interface.data import BaseWindowConfiguration
from Core.Interface.View.interfaces import ViewInterface
from Core.Interface.Types.Tkinter.Window import TkinterWindow
from Core.Interface.Frame.interfaces import FrameWindowInterface
from Core.Interface.View.Control.interfaces import ControlInterface
from Core.Interface.View.UserControl.interfaces import UserControlInterface


## Library Imports
from Content.Interface.Types.Tkinter import Controls


class TkinterFrame(FrameBase):
	
	Type: str = "Tkinter"
	SingleWindow: bool = False
	
	@property
	def views(self) -> List[ViewInterface]:
		return self.__views
	
	@property
	def windows(self) -> List[FrameWindowInterface]:
		return self.__windows
	
	@property
	def control_types(self) -> List[ControlInterface]:
		return self.__controls
	
	@property
	def user_control_types(self) -> List[UserControlInterface]:
		return self.__user_controls
	
	@property
	def window_type(self) -> type(FrameWindowInterface):
		return self.__window_type
	
	def __init__(self):
		super().__init__()
		
		self.__views: List[ViewInterface] = []
		self.__window_configuration = BaseWindowConfiguration()
		self.__windows: List[TkinterWindow] = []
		
		self.__controls: List[ControlInterface] = []
		self.__user_controls: List[UserControlInterface] = []
		
		self.__window_type: Type[FrameWindowInterface] = TkinterWindow
	
	def Initialize(self):
		self.__controls = discovery.get_controls(Controls.__path__)
		self.__windows.append(TkinterWindow(self, self.__window_configuration))
	
	def Loop(self):
		if len(self.__windows) > 0:
			self.__windows[0].Loop()
