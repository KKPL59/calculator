import pickle


class ImgHere:

    def __init__(self, img_1x784):
        self.predictions = self.clssifiter.predict(img_1x784)

    lista = []
    classifiter = open("classifiter_SVC_+.pkl", "rb")
    clssifiter = pickle.load(classifiter)

    def predictions_append(self):
        self.lista.append(self.predictions[0])

    def detected(self):
        print(self.lista)
        self.classifiter.close()
