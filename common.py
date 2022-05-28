#ライブラリのインポート
import kivy
import random
import os
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
#from kivy.core.window import Window

from kivy.uix.screenmanager import ScreenManager, Screen


#表示する画像の管理
class SuperImageManage():
    def __init__(self):
        files = list(os.listdir(".images")) #フォルダ内のファイル名を取得
        length = len(files)
        self.name = []
        for i in range(length): #jpgとpngだけリストから抽出
            if (files[i].endswith('.jpg') | files[i].endswith('.png')):
                self.name.append('.images/' + files[i]) #相対パス化
        self.length = len(self.name)
        
        self.count = 0
        self.flag = 0

#タップ時に画像を表示するインスタンス
class SuperBaseLayout(Screen):
    def __init__(self, **kwargs):
        super(SuperBaseLayout, self).__init__(**kwargs)
        self.add_widget(self.DL)
        
    def btn(self):
        self.remove_widget(self.DL)
        del self.DL
        self.DL = self.DLtemp
        del self.DLtemp
        self.manager.current = 'menu'
        self.add_widget(self.DL)

#画像のオブジェクトを生成する
class SuperDrowImg(Widget):
    x_img_pos = NumericProperty(3)
    y_img_pos = NumericProperty(3)
 
    def __init__(self, x, y, num, **kwargs):
        img = random.randint(0, num - 1)
        super(SuperDrowImg, self).__init__(**kwargs)
        self.x_img_pos = x / 100
        self.y_img_pos = y/ 100 
        return img