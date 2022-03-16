import pickle


class ImgHere:
    """Przy pomocy pliku z klasyfikatorem dokonuje predykcji z dostarczonego
    zdjęcia z pliku contours copy. Następnie zwraca tę predykcję"""

    # otwiera plik z klasyfikatorem
    lista = []
    classifiter = open("classifiter_SVC_thresh.pkl", "rb")
    clssifiter = pickle.load(classifiter)

    def __init__(self, img_1x784):
        """Doknuje predykcji na podtawie otrzymanego zdjęcia."""

        self.predictions = self.clssifiter.predict(img_1x784)

    def predictions_append(self):
        """Zwraca predykcje"""

        return self.predictions
