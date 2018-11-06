from Responder import *
import random
class Kiseki:
    """人工無脳コアクラス
    プロパティ:
    name -- コアの名前
    responderName -- 現在応答中の応答クラスの名前
    """
    def __init__(self,name=None):
        self._responders={"default":defaultResponder("Default"),"random":randomResponder("Random")}


        self._name=name
        self._responder=self._responders["random"]

    def reply(self,text):
        """入力を受け取り、Responderに処理させた結果を返す。その際、Responderをランダムに切り替える"""
        key=random.choice(list(self._responders.keys()))
        self._responder=self._responders[key]
        return self._responder.response(text)

    @property
    def name(self):
        return self._name

    @property
    def responderName(self):
        return self._responder.name
