import predictions


class Printer:

    def text(self, space):
        prediction = predictions.Img_here().detected()
        lista = []
        lista2 = []

        licznik = -1

        for i in prediction:
            i = int(i)
            lista2.append(i)




        for i, j in  zip(lista2, space):
            i = str(i)
            licznik += 1
            if j == False:
                lista.append("")
                lista.append(i)

            elif j == True:
                lista.append(i)

            else:
                print("JD")
        print(lista)

        działanie = ""
        for i in enumerate(lista):


            if i[0] == 0:
                pass


            elif i[1] == "10":
                działanie += "+"


            elif i[1] == "11":
                działanie += "-"


            elif i[1] != "":
                działanie += i[1]


            elif i[1] == "":
                działanie += " "
        print(działanie)


        print(eval(działanie))

#trochę zmieniona wersja
