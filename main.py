from Eko import Kiseki

eko = Kiseki("eko")
while True:
    text = input("> ")
    response = eko.reply(text)
    print(response)
