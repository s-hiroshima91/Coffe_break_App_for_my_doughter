#ライブラリのインポート
import kivy
import numpy as np
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.clock import Clock

import common

#背景を白色に
Window.clearcolor = (1, 1, 1, 1)

#ウインドウの幅と高さの設定
Config.set('graphics', 'width', 1080)
Config.set('graphics', 'height', 1920)
#1でサイズ変更可、0はサイズ変更不可
Config.set('graphics', 'resizable', 1)

def move_func(dt):
    d = IM.VE.length
    int_d = int(d / 100)
    if (IM.flag <= int_d + 1):
        Clock.schedule_once(move_func, 0.01)
        pos = IM.VE.equation(IM.flag * 100)
        IM.wname.x_img_pos = float(pos[0])
        IM.wname.y_img_pos = float(pos[1])
        IM.flag += 1
    else:
        IM.flag = 0

class vector_equation():
    def __init__(self, x1, y1, x2, y2):
        pos1 = np.array([x1, y1])
        pos2 = np.array([x2, y2])
        deltapos = pos2 - pos1
        self.init_pos = pos1
        self.length = np.linalg.norm(deltapos)
        if (self.length == 0):
            IM.flag = 0
        else:
            self.direct_vector = deltapos / self.length

    def equation(self, t):
        current_pos = (self.direct_vector * t + self.init_pos) / 100
        return current_pos

#表示する画像の管理
class ImageManage(common.SuperImageManage):
    def __init__(self):
        super().__init__()
        self.wname = 'move_widget'
#表示する画像のオブジェクト名を
        self.VE = 'VE'

#タップ時に画像を表示する
class BaseLayout(common.SuperBaseLayout):
    def __init__(self, **kwargs):
        self.DL = DrowLayout()
        super().__init__(**kwargs)
        
    def btn(self):
        self.DLtemp = DrowLayout()
        IM.count = 0
        super().btn()

#タップ時に画像を表示するインスタンス
class DrowLayout(Widget):
    def on_touch_down(self, touch):
#画像が50個を越えたら最初に戻す
        num = IM.count % 4

#タップした場所を取得
        x = touch.pos[0]
        y = touch.pos[1]
        if (IM.flag == 0):
        
            if (num == 0):
#元々あった画像を削除する
                try:
                    self.remove_widget(IM.wname)
                except AttributeError:
                    pass
#タップした場所に新たなオブジェクトを生成
                IM.wname = DrowImg(x, y)
                self.add_widget(IM.wname)
            else:
                IM.flag = 1
                IM.VE = vector_equation(IM.wname.x_img_pos * 100, IM.wname.y_img_pos * 100, x, y)
                Clock.schedule_once(move_func, 0.01)
            IM.count = num + 1

#画像のオブジェクトを生成する
class DrowImg(common.SuperDrowImg):
    img_name = StringProperty('')
 
    def __init__(self, x, y):
        img = super().__init__(x, y, IM.length)
        self.img_name = IM.name[img] 

#表示する画像を管理するオブジェクトを生成
IM = ImageManage()