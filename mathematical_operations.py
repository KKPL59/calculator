
class Priner:


    def circs(self, operation):
        self.text = ""
        for i in enumerate(operation):
            if i[1] == "10":
                operation[i[0]] = "+"

        for i in operation:
            if i != " ":

                i = str(i)
                self.text += i

        return self.text


    def operations(self):
        self.text = ""


class MathematicalOperations(Priner):
    pass
