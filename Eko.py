class Responder:
    def __init__(self,name):
        self._name=name

    def response(self,text):
        return "君は{}が得意なフレンズなんだね!!".format(text)

    @property
    def name(self):
        return self._name

class Kiseki:
    """人工無脳コアクラス
    プロパティ:
    name -- コアの名前
    responderName -- 現在応答中の応答クラスの名前
    """
    def __init__(self,name=None):
        self._name=name
        self._responder=Responder("Friends")

    def reply(self,text):
        """入力を受け取り、Responderに処理させた結果を返す"""
        return self._responder.response(text)

    @property
    def name(self):
        return self._name

    @property
    def responderName(self):
        return self._responder.name

if __name__=="__main__":
    eko=Kiseki("eko")
    while True:
        text=input("> ")
        response=eko.reply(text)
        print(response)
