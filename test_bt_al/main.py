import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.carousel import Carousel
from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.effects.kinetic import KineticEffect
from kivy.base import runTouchApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from  kivy.uix.screenmanager import ScreenManager, Screen


Window.size = (375, 700)


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('AlfaBt.kv')


class AlfaBtApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    AlfaBtApp().run()