#ライブラリのインポート
import kivy
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.core.window import Window

#from kivy.uix.screenmanager import ScreenManager, Screen

import common
from settings import PM

#背景を白色に
Window.clearcolor = (1, 1, 1, 1)

#ウインドウの幅と高さの設定
Config.set('graphics', 'width', 1080)
Config.set('graphics', 'height', 1920)
#1でサイズ変更可、0はサイズ変更不可
Config.set('graphics', 'resizable', 1)
        
class ImageManage(common.SuperImageManage):
    def __init__(self):
        super().__init__()
        self.wname = []
#表示する画像のオブジェクト名を動的に生成
#50個まで表示できるようにする
        for i in range(100):
            self.wname.append(['tet' + str(i)])

#タップ時に画像を表示する
class BaseLayout(common.SuperBaseLayout):
    def __init__(self, **kwargs):
        self.DL = DrowLayout()
        super().__init__(**kwargs)
        
    def btn(self):
        self.DLtemp = DrowLayout()
        super().btn()

class DrowLayout(Widget):
    def on_touch_down(self, touch):
#画像が50個を越えたら最初に戻す
        num = IM.count % PM.qua
#元々あった画像を削除する
        try:
            self.remove_widget(IM.wname[num])
        except AttributeError:
            pass
#タップした場所を取得
        x = touch.pos[0]
        y = touch.pos[1]
#タップした場所に新たなオブジェクトを生成
        IM.wname[num] = DrowImg(x, y)
        self.add_widget(IM.wname[num])
        IM.count = num + 1

#画像のオブジェクトを生成する
class DrowImg(common.SuperDrowImg):
    img_name = StringProperty('')
 
    def __init__(self, x, y):
        img = super().__init__(x, y, IM.length)
        self.img_name = IM.name[img] 

#表示する画像を管理するオブジェクトを生成
IM = ImageManage()