from Eko import Kiseki

eko = Kiseki("eko")
with open("input.txt","a") as fd:
    while True:
        text = input("> ")
        #fd.write(text+"\n")
        response = eko.reply(text)
        print(response)
