import pickle


class Img_here:
    lista = []
    def predictions(self, img_1x784):
        with open("classifiter_SVC_+.pkl", "rb") as f:
            clssifiter = pickle.load(f)
        predictions = clssifiter.predict(img_1x784)
        self.lista.append(predictions[0])

    def detected(self):
        return self.lista
