#ライブラリのインポート
import kivy
import random
import os
import numpy as np

from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.clock import Clock

#背景を白色に
Window.clearcolor = (1, 1, 1, 1)

#ウインドウの幅と高さの設定
Config.set('graphics', 'width', 1080)
Config.set('graphics', 'height', 1920)
#1でサイズ変更可、0はサイズ変更不可
Config.set('graphics', 'resizable', 1)

def move_func(dt):
    d = IM.VE.length
    int_d = int(d / 20)
    if (IM.flag <= int_d + 1):
        Clock.schedule_once(move_func, 0.01)
        pos = IM.VE.equation(IM.flag * 20)
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
#        self.direct_vector =np.array([0, 0])
        if (self.length == 0):
            IM.flag = 0
        else:
            self.direct_vector = deltapos / self.length

    def equation(self, t):
        current_pos = (self.direct_vector * t + self.init_pos) / 100
        return current_pos

#表示する画像の管理
class ImageManage():
    def __init__(self):
        files = list(os.listdir(".images")) #フォルダ内のファイル名を取得
        length = len(files)
        self.name = []
        for i in range(length): #jpgとpngだけリストから抽出
            if (files[i].endswith('.jpg') | files[i].endswith('.png')):
                self.name.append('.images/' + files[i]) #相対パス化
        self.length = len(self.name)
        self.wname = 'move_widget'
#表示する画像のオブジェクト名を
        self.VE = 'VE'
        self.count = 0
        self.flag = 0

#タップ時に画像を表示するインスタンス
class MyLayout(Widget):
    def on_touch_down(self, touch):
#画像が50個を越えたら最初に戻す
        num = IM.count % 4


#タップした場所を取得
        x = touch.pos[0]
        y = touch.pos[1]
        if (IM.flag == 0):
        
            if (num == 0):
#元々あった画像を削除する
                self.remove_widget(IM.wname)
#タップした場所に新たなオブジェクトを生成
                IM.wname = DrowImg(x, y)
                self.add_widget(IM.wname)
            else:
                IM.flag = 1
                IM.VE = vector_equation(IM.wname.x_img_pos * 100, IM.wname.y_img_pos * 100, x, y)
                Clock.schedule_once(move_func, 0.01)
            IM.count = num + 1
                
#画像のオブジェクトを生成するインスタンス
class DrowImg(Widget):
    x_img_pos = NumericProperty(3)
    y_img_pos = NumericProperty(3)
    img_name = StringProperty('')
 
    def __init__(self, x, y, **kwargs):
        img = random.randint(0, IM.length - 1)
        super(DrowImg, self).__init__(**kwargs)
        self.img_name = IM.name[img]
        self.x_img_pos = x / 100
        self.y_img_pos = y/ 100 

class TapApp(App):
    def build(self):
        self.title = "window"
        root = MyLayout()
        return root

#表示する画像を管理するオブジェクトを生成
IM = ImageManage()

if __name__ == '__main__':
    TapApp().run()