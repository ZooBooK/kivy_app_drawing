from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from kivy.core.window import Window
from kivy.graphics import (Color, Ellipse, Rectangle, Line)

class PainterWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 1, 0, 1)
            rad = 30
            self.ellipse = Ellipse(pos=(touch.x - rad/2, touch.y - rad/2,),size = (rad, rad))
            touch.ud['line'] = Line(points = (touch.x, touch.y), width = 15)#Словарь пользователя

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x,touch.y)

class PaintApp(App):

    def build(self):
        parent = Widget()
        self.painter = PainterWidget()
        parent.add_widget(self.painter)

        parent.add_widget(Button(text = 'Clear', on_press = self.clear_canvas, size = (100,50)))
        parent.add_widget(Button(text='Save', on_press=self.save, size=(100, 50), pos = (100,0)))

        return parent

    def clear_canvas(self, instance):
        self.painter.canvas.clear()

    def save(self, instance):
        self.painter.size = (Window.size[0], Window.size[1])
        self.painter.export_to_png('image.png')


if __name__ == '__main__':
    PaintApp().run()