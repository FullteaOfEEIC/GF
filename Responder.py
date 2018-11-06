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
    def __init__(self,name):
        super().__init__(name)
        self._responses=[]
        with open("random.txt") as f:
            for line in f:
                if line:
                    line=line.strip()
                    self._responses.append(line)
    def response(self,_):
        #入力は(受け取るけど)利用しない
        return random.choice(self._responses)
