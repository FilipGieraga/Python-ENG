import string

class Message:
    alphabet = string.ascii_uppercase + "ABC"
    alphabet_d = alphabet[::-1]
    def __init__(self, message):
        self.message = message
        self.encrypted = ""
        self.decrypted = ""

    def cipher(self):
        message = self.message.upper()
        for element in message:
            if element in Message.alphabet:
                x = Message.alphabet.find(element)
                l = x + 3
                self.encrypted += Message.alphabet[l]
            else:
                self.encrypted += element
        print(self.encrypted)

    def decipher(self):
        message = self.message.upper()
        for element in message:
            if element in Message.alphabet_d:
                x = Message.alphabet_d.find(element)
                l = x + 3
                self.decrypted += Message.alphabet_d[l]
            else:
                self.decrypted += element
        print(self.decrypted)

message1 = Message("But believe me, my dear boy, there is nothing stronger than those two: patience and time, "
                   "they will do it all.")
message1.cipher()
# print(message1.encrypted)

message2 = Message("EXW EHOLHYH PH, PB GHDU ERB, WKHUH LV QRWKLQJ VWURQJHU WKDQ WKRVH WZR: SDWLHQFH DQG WLPH, "
                   "WKHB ZLOO GR LW DOO.")
message2.decipher()
# print(message2.decrypted)