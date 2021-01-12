import random


class CYGNO:

    def __init__(self):
        pass

    def guys(self):
        return 'Kosterin,Mishukova,Papko,Yuzhakov'

    def utility(self):
        val = 0
        for k in self.enemy_suggestion.keys():
            val += self.my_value[k] * self.enemy_suggestion[k]
        return val

    def turn(self):
        if self.round == 0:
            if self.me_first:
                self.suggestion = {
                    "Book": 1,
                    "Hat": 2,
                    "Ball": 3,
                }
            else:
                max_util = self.my_value['Book'] * 1 + self.my_value['Hat'] * 2 + self.my_value['Ball'] * 3
                if self.utility() < max_util / 2:
                    self.suggestion = {
                            "Book": random.randint(0,1),
                            "Hat": 1,
                            "Ball": 3,
                    }
                else:
                    self.suggestion = 'OK'

        else:
            if self.me_first:
                self.suggestion = {
                    "Book": 1,
                    "Hat": 2,
                    "Ball": 3,
                }
            else:
                if self.utility() > 0:
                    self.suggestion = {
                        "Book": random.randint(0, 1),
                        "Hat": 1,
                        "Ball": 3,
                    }
                else:
                    self.suggestion = 'OK'


Haggler = CYGNO()


