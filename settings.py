import kivy
from kivy.config import Config
from kivy.uix.widget import Widget
#from kivy.uix.floatlayout import FloatLayout
#from kivy.properties import StringProperty
from kivy.core.window import Window
#from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider import Slider

#背景を白色に
#Window.clearcolor = (0, 0, 0, 1)

class Parameter():
    def __init__(self):
        self.size = 1
        self.speed_temp = 4
        self.qua = 50
        self.times = 4
        self.lag = 50
        self.speed = 16

PM = Parameter()

class Setting(Screen):
    def __init__(self, **kwargs):
        self.para = PM
        super(Setting, self).__init__(**kwargs)

    def btn(self):
        self.manager.current = 'menu'
        PM.qua = int(self.ids.qua_slider.value)
        PM.size = int(self.ids.size_slider.value)
        PM.speed = 2 ** self.ids.speed_slider.value
        PM.times = int(self.ids.times_slider.value)
        PM.lag = int(self.ids.lag_slider.value)