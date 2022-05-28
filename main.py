#ライブラリのインポート
import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen

import increase
import move

# Declare both screens
class MenuScreen(Screen):
    pass

#ウインドウの幅と高さの設定
Config.set('graphics', 'width', 1080)
Config.set('graphics', 'height', 1920)
#1でサイズ変更可、0はサイズ変更不可
Config.set('graphics', 'resizable', 1)

class TapApp(App):
    def build(self):
        self.title = "window"
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(increase.BaseLayout(name='increase'))
        sm.add_widget(move.BaseLayout(name='move'))
        
        return sm

if __name__ == '__main__':
    TapApp().run()