from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line, Color
import cv2
from contours_copy2 import Pieces
from mathematical_operations import Priner
from mathematical_operations import MathematicalOperations


class WorkPlace(FloatLayout):

    prediction = []
    text =""
    printer = Priner()

    def clear(self):
        self.prediction = []
        self.ids.mathematical_operations.text = self.printer.circs(self.prediction)

    def undo(self):
        try: self.prediction.remove(" ")
        except:  ValueError
        self.prediction = self.prediction[:len(self.prediction)-1]
        self.ids.mathematical_operations.text = self.printer.circs(self.prediction)


    def on_touch_down(self, touch):

        with self.ids.paint.canvas:
            Color(0, 0, 0)
            if self.ids.paint.collide_point(touch.x, touch.y):
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=7)
            return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.ids.paint.collide_point(touch.x, touch.y):
            touch.ud['line'].points += [touch.x, touch.y]
        return super().on_touch_move(touch)

    licznik = 0
    def on_touch_up(self, touch):
        self.licznik += 1
        if self.ids.paint.collide_point(touch.x, touch.y):
            self.export_to_png("digit.png")

            img = cv2.imread("digit.png")
            img = img[300:600, 0:350]

            self.pieces = Pieces(img)
            self.pieces.cutting_out()

            self.prediction.append(self.pieces.prediction[0])
            self.ids.mathematical_operations.text = self.printer.circs(self.prediction)


        #     try:
        #         self.prediction.remove(" ")
        #     except:
        #         ValueError
        #
        #     for i in self.prediction:
        #         if isinstance(i, float):
        #             i = int(i)
        #         self.text += str(i)
        #
        #
        #     self.ids.mathematical_operations.text = self.text
        #     self.text = ""
        #
            self.ids.paint.canvas.clear()
        return super().on_touch_move(touch)

    # def printer(self):
    #     return str(self.licznik)


class CalculatorApp(App):

    def build(self):
        return WorkPlace()


buttonapp = CalculatorApp()
buttonapp.run()



