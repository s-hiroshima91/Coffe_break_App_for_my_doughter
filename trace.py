#ライブラリのインポート
import kivy
#import numpy as np
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.clock import Clock

import common
from settings import PM

#背景を白色に
Window.clearcolor = (1, 1, 1, 1)

#ウインドウの幅と高さの設定
Config.set('graphics', 'width', 1080)
Config.set('graphics', 'height', 1920)
#1でサイズ変更可、0はサイズ変更不可
Config.set('graphics', 'resizable', 1)

#表示する画像の管理
class ImageManage(common.SuperImageManage):
    def __init__(self):
        super().__init__()

#表示する画像のオブジェクト名を
        self.wname = 'move_widgbt'
        self.delayx = [0] * 100
        self.delayy = [0] * 100
        self.pre = - PM.lag
        self.flag = 0

#タップ時に画像を表示する
class BaseLayout(common.SuperBaseLayout):
    def __init__(self, **kwargs):
        self.DL = DrowLayout()
        super().__init__(**kwargs)
        
    def btn(self):
        self.DLtemp = DrowLayout()
        IM.count = 0
        super().btn()
        IM.flag = 0

#タップ時に画像を表示するインスタンス
class DrowLayout(Widget):
    def on_touch_down(self, touch):
        if (IM.flag == 0):
            self.tempx = touch.pos[0]
            self.tempy = touch.pos[1]

            IM.flag = 1
            IM.count = 0
            IM.pre = - PM.lag - 1
#タップした場所に新たなオブジェクトを生成
            IM.wname = DrowImg(self.tempx, self.tempy)
            self.add_widget(IM.wname)
            Clock.schedule_once(self.delay, 0)

    def on_touch_move(self, touch):
        self.tempx = touch.pos[0]
        self.tempy = touch.pos[1]

    def delay(self, dt):
        IM.delayx[IM.count] = self.tempx
        IM.delayy[IM.count] = self.tempy
        
        if (IM.flag > 0):
            Clock.schedule_once(self.delay, 0.01)
            
#            if (IM.pre < 0):
#                IM.pre += 1

            if (IM.flag >= 2):
                IM.flag += 1
                
                if (IM.flag == PM.lag + 2):
                    IM.flag = 0

            if (IM.pre < 0):
                IM.pre +=1
            else:
                IM.wname.x_img_pos = IM.delayx[(IM.count + 100 - PM.lag) % 100 ] / 100
                IM.wname.y_img_pos = IM.delayy[(IM.count + 100 - PM.lag) % 100] / 100

            IM.count = (IM.count +1)% 100

        else:
            self.remove_widget(IM.wname)

    def on_touch_up(self, touch):
        if (IM.flag == 1):
                IM.flag = 2
#                IM.pre = 0
                
#        Clock.schedule_once(self.elase, 2)

    def elase(self, dt):
#        IM.flag = 1
        self.remove_widget(IM.wname)

#画像のオブジェクトを生成する
class DrowImg(common.SuperDrowImg):
    img_name = StringProperty('')
 
    def __init__(self, x, y):
        img = super().__init__(x, y, IM.length)
        self.img_name = IM.name[img] 

#表示する画像を管理するオブジェクトを生成
IM = ImageManage()