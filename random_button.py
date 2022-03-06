from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line, Color



class WorkPlace(FloatLayout):


    def printer(self):
        return "akhf"

    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 0, 0)
            if self.ids.paint.collide_point(touch.x, touch.y):
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=7)
            return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.ids.paint.collide_point(touch.x, touch.y):
            touch.ud['line'].points += [touch.x, touch.y]
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.ids.paint.collide_point(touch.x, touch.y):
            pass
            # print(self.)
        return super().on_touch_move(touch)



class CalculatorApp(App):

    def build(self):
        return WorkPlace()

buttonapp = CalculatorApp()
buttonapp.run()