import MeCab

class MeCabResult:
    def __init__(self,result):
        result=result.split("\t")
        self.表層形=result[0]
        data=result[1].split(",")
        self.品詞細分類1=data[0]
        self.品詞細分類2=data[1]
        self.品詞細分類3=data[2]
        self.活用型=data[3]
        self.活用形=data[4]
        self.原形=data[5]
        self.読み=data[6]
        self.発音=data[7]

    def __repr__(self):
        return self.表層系
