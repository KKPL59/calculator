import cv2
import numpy as np

#########################################################cv2.boundingRect################################################


class Pieces:

    def __init__(self, img):
        """Z wcześniejszego pliku paint przyjmuje parametr img,
        instancja znbajduje się w pliku main"""

        self.img = img


    def img_contours_preapare(self):
        """Przygotowuje zdjęcie do wykrycia konturów, i hierarhizuje je, zapisując do zminnej
                        list tylko te najbardziej zewnętrzne."""


        self.img2 = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.thresh = cv2.threshold(self.img2, 200, 254, cv2.THRESH_BINARY)[1]
        self.contours, self.hierarchy = cv2.findContours(image=self.thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

        self.list = []
        for k in range(0, len(self.hierarchy)):
            for i in range(0, len(self.hierarchy[0])):
                self.j = self.hierarchy[0][i][3]
                if self.j == 0:
                    self.list.append(self.contours[i])

        return self.list



    def sorting(self, value):
        """korzystając z wcześniej przygotowanej listy, przygotowuje prostokąt wokół każdego wykrytego
                    konturu i sortuje(prostokąty) od lewej do prawej"""

        self.list = self.img_contours_preapare()
        self.dict = {}

        for i in range(0, len(self.list)):
            if cv2.arcLength(self.list[i], True) < 20:
                continue


            self.x, self.y, self.w, self.h = cv2.boundingRect(self.list[i])
            if value == "x":
                self.value = self.x

            elif value == "y":
                self.value = self.y

            elif value == "xw":
                self.value = self.x + self.w

            elif value == "yh":
                self.value = self.y + self.h


            # posortowne kontury od lewej do prawej
            if self.x != 0:
                self.dict.update({i:self.value})

        self.dict = sorted(self.dict.items(), key=lambda x: x[1])

        return self.dict

    def cutting_out(self):
        self.dict_x = self.sorting("x")
        self.dict_y = self.sorting("y")
        self.dict_xw = self.sorting("xw")
        self.dict_yh = self.sorting("yh")


        self.space = []
        for i in range(0, len(self.dict_x)):

            self.img1 = self.img2[self.dict_y[i][1]:self.dict_yh[i][1], self.dict_x[i][1]:self.dict_xw[i][1]]


            self.together = False
            if i == 0:
                pass
            
            elif i != 0 and i != len(self.dict_x)  and abs(self.dict_x[i][1] - self.dict_xw[i-1][1]) < 50:
                self.together = True

            self.space.append(self.together)


            self.img1 = cv2.copyMakeBorder(self.img1, 35, 35, 35, 35, cv2.BORDER_CONSTANT, value=255)


            if len(self.img1) != 0:
                self.img1 = cv2.resize(self.img1, (28, 28))
                self.img1 = cv2.bitwise_not(self.img1)

                # cv2.imshow("JD", self.img1)
                # cv2.waitKey(0)
                # # print(self.img1.shape)

                self.img1 = np.array([self.img1])
                self.img1 = self.img1.reshape(self.img1.shape[0], -1)


                import predictions
                object = predictions.Img_here()
                object.predictions(img_1x784=self.img1)

        import printer
        printer.Printer().text(space=self.space)


    def temporaty_starter(self):
        pass








