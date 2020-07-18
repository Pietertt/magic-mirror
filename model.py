import time

class Model:
    def __init__(self):
        self.days = ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag"]
        self.months = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]

    def get_current_second(self):
        t = time.time()
        local = time.localtime(t)
        return local.tm_sec

    def get_current_date(self):
        t = time.time()
        local = time.localtime(t)
        return self.days[local.tm_wday] + ", " + str(local.tm_mday) + " " + self.months[local.tm_mon - 1] + " " + str(local.tm_year)

    def get_current_time(self):
        t = time.time()
        local = time.localtime(t)
        return str(local.tm_hour) + ":" + str(local.tm_min)

    # def calculate(self, caption):
    #     if(caption == "C"):            
    #         self.previous_value = ""
    #         self.value = ""
    #         self.operator = ""

    #     elif caption == "+/-":
    #         self.value = self.value[1:] if self.value[0] == "-" else "-" + self.value
        
    #     elif caption == "%":
    #         pass

    #     elif caption == "=":
    #         self.value = str(self._evaluate())

    #     elif caption == ".":
    #         if not caption in self.value:
    #             self.value += caption

    #     elif isinstance(caption, int):
    #         self.value += str(caption)

    #     else:
    #         if self.value:
    #             self.operator = caption
    #             self.previous_value = self.value
    #             self.value = ""

    #     return self.value

    # def _evaluate(self):
    #     return eval(self.previous_value + self.operator + self.value)