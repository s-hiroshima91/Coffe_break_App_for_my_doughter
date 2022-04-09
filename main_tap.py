#ライブラリのインポート
import kivy
import random
import os
from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.core.window import Window

#背景を白色に
Window.clearcolor = (1, 1, 1, 1)

#ウインドウの幅と高さの設定
Config.set('graphics', 'width', 1080)
Config.set('graphics', 'height', 1920)
#1でサイズ変更可、0はサイズ変更不可
Config.set('graphics', 'resizable', 1)

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
        self.wname = []
#表示する画像のオブジェクト名を動的に生成
#50個まで表示できるようにする
        for i in range(50):
            self.wname.append(['tet' + str(i)])

        self.count = 0
        self.flag = 0

#タップ時に画像を表示するインスタンス
class MyLayout(Widget):
    def on_touch_down(self, touch):
#画像が50個を越えたら最初に戻す
        num = IM.count % 50
#元々あった画像を削除する
        self.remove_widget(IM.wname[num])
#タップした場所を取得
        x = touch.pos[0]
        y = touch.pos[1]
#タップした場所に新たなオブジェクトを生成
        IM.wname[num]= DrowImg(x, y)
        self.add_widget(IM.wname[num])
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