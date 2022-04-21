from kivy.app import App
from kivy.graphics import Line, Color
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from mathematical_operations import Priner
import predictions_api

class Results(Screen):
    Window.size = 280, 520
    text = ""
    printer = Priner()


    def results(self):
        """powinno zwrócić wynik predycji"""
        self.ids.result.text = Photo.wynik



    def results_printer(self):
        """wywołuje funkcje z wynikiem predykcji XD"""
        self.results()



class Photo(Screen):
    Window.size = 280, 520
    licznik = 0
    wynik = ""
    prediction = []
    printer = Priner()

    def take_p(self):
        """robi zrzut ekranu, podaje go do predictions_api, gdzie wysyłane jest żądanie i odbiera wynik predykcji"""

        Photo.licznik += 1

        self.export_to_png(f"digit.png")
        self.url = "http://127.0.0.1:5000/photo"

        # podaje obraz do funkcji predictions_api
        self.imghere = predictions_api.ImgHere(1)
        self.prediction_api = self.imghere.get_prediction_photo()
        print("taking...")

        self.prediction_api = str(self.prediction_api)

        # przetwarza wynik
        self.prediction.append(self.prediction_api)
        print(self.prediction)
        Photo.wynik = self.printer.circs(self.prediction)





class WorkPlace(Screen):
    """tutaj wywoływane są wszystkie funkcje, obierany jest narysowany obraz"""

    prediction = []
    text = ""
    printer = Priner()
    Window.size = 280, 520
    # Window.size = 1080, 2145


    def clear(self):
        """służy do czyszczenia płótna"""

        self.prediction = []
        self.ids.mathematical_operations.text = self.printer.circs(self.prediction)

    def undo(self):
        """usuwa po jednym znaku z płótna"""

        # po usunięciu, a następnie dodaniu jednej cyfry pojawiało się " " więc jest usuwane
        try:
            self.prediction.remove(" ")
        except ValueError:
            print(ValueError)

        # wypisuje się lista o 1 krótsza niż przed zmianą
        self.prediction = self.prediction[:len(self.prediction) - 1]
        self.ids.mathematical_operations.text = self.printer.circs(self.prediction)

    def on_touch_down(self, touch):
        """rysuje linie i jest odpowiedzialna za wykrywanie dotyku"""

        # wużywa płótna o id canvas
        with self.ids.paint.canvas:
            Color(0, 0, 0)
            if self.ids.paint.collide_point(touch.x, touch.y):
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=4) # 7 test 5 jest dobrze
            return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        """rysuje linie"""

        if self.ids.paint.collide_point(touch.x, touch.y):
            touch.ud['line'].points += [touch.x, touch.y]
        return super().on_touch_move(touch)

    licznik = 0

    def on_touch_up(self, touch):
        """po uniesieniu palca zapisuje zdjęcie płótna i dokonuje predykcji"""

        # rozbi screena płotana
        self.licznik += 1
        if self.ids.paint.collide_point(touch.x, touch.y):
            # self.ids.paint.export_to_png(r"C:\Users\lukas\PycharmProjects\img_to_string\test\digit.png")
            print(App().user_data_dir)
            self.export_to_png(f"{App().user_data_dir}/digit.png")

            self.url = "https://imgpred.herokuapp.com/digit"
            self.imghere = predictions_api.ImgHere(1)

            print("getting prediction...")
            self.prediction_api = self.imghere.get_prediction_digit()
            print(self.prediction)

            self.prediction.append(self.prediction_api[0])
            self.ids.mathematical_operations.text = self.printer.circs(self.prediction)

            self.ids.paint.canvas.clear()

            print(Window.size)

        return super().on_touch_move(touch)


class CalculatorApp(App):

    def build(self):
        self.menager = ScreenManager()
        self.menager.add_widget(WorkPlace(name="workplace"))
        self.menager.add_widget(Photo(name="photo"))
        self.menager.add_widget(Results(name="results"))


        return self.menager



buttonapp = CalculatorApp()
if __name__ == "__main__":
    buttonapp.run()
