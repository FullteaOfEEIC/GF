from Responder import *
class Kiseki:
    """人工無脳コアクラス
    プロパティ:
    name -- コアの名前
    responderName -- 現在応答中の応答クラスの名前
    """
    def __init__(self,name=None):
        self._name=name
        self._responder=randomResponder("Random")

    def reply(self,text):
        """入力を受け取り、Responderに処理させた結果を返す"""
        return self._responder.response(text)

    @property
    def name(self):
        return self._name

    @property
    def responderName(self):
        return self._responder.name
