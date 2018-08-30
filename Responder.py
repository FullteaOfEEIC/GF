import random

class _Responder:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

class defaultResponder(_Responder):
    def response(self, text):
        return "君は{}が得意なフレンズなんだね!!".format(text)

class randomResponder(_Responder):
    responses=["わーい！","たーのしー！","すごいね、魔法みたい！"]
    def response(self,_):
        return random.choice(randomResponder.responses)
