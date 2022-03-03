import cv2
import imutils
import numpy as np

#########################################################cv2.boundingRect################################################


class Pieces:

    def single_numbers(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(img, 200, 254, cv2.THRESH_BINARY)[1]
        contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)


        list = []
        for k in range(0, len(hierarchy)):
            for i in range(0, len(hierarchy[0])):
                j = hierarchy[0][i][3]
                if j == 0:
                    list.append(contours[i])


        dict_x = {}
        dict_y = {}
        dict_xw = {}
        dict_yh = {}

        for i in range(0, len(list)):
            if cv2.arcLength(list[i], True) < 20:
                continue


            x, y, w, h = cv2.boundingRect(list[i])

            # posortowne kontury od lewej do prawej
            if x != 0:
                dict_x.update({i:x})
                dict_y.update({i:y})
                dict_xw.update({i:x+w})
                dict_yh.update({i:y+h})


        dict_x = sorted(dict_x.items(), key=lambda x: x[1])
        dict_y = sorted(dict_y.items(), key=lambda x: x[1])
        dict_xw = sorted(dict_xw.items(), key=lambda x: x[1])
        dict_yh = sorted(dict_yh.items(), key=lambda x: x[1])


        space = []
        for i in range(0, len(dict_x)):

            img1 = img[dict_y[i][1]:dict_yh[i][1], dict_x[i][1]:dict_xw[i][1]]


            together = False
            if i == 0:
                pass
            
            elif i != 0 and i != len(dict_x)  and abs(dict_x[i][1] - dict_xw[i-1][1]) < 50:
                together = True

            space.append(together)


            img1 = cv2.copyMakeBorder(img1, 25, 25, 25, 25, cv2.BORDER_CONSTANT, value=255)


            if len(img1) != 0:
                img1 = cv2.resize(img1, (28, 28))
                img1 = cv2.bitwise_not(img1)
                img1 = np.array([img1])
                img1 = img1.reshape(img1.shape[0], -1)


                import predictions
                object = predictions.Img_here()
                object.predictions(img_1x784=img1)

        import printer
        printer.Printer().text(space=space)









