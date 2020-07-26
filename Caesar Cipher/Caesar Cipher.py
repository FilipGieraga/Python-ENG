print("If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the "
      "letters of the alphabet, that not a word could be made out.")

string="aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźżaąbc"
string1="abcdefghijklmnopqrstuvwxyzabc"
string2=" -.,"

def choice():
    choi = input("Would you like to try again?(y/n)\n")
    if choi == "y":
        choi1=input("Do you want to encrypt the message?(y/n)\n")
        if choi1=="y":
            cipher(string, string1, string2)
        else:
            decipher(string, string1, string2)
    else:
        print("Thank you for using this program.")


def cipher(string, string1, string2):
    zdanie=input("Enter a sentence to encrypt:\n")
    p = input("Would you like to include Polish characters?(y/n)\n")
    if p == "y":
        p = string
    else:
        p = string1
    zdanie=zdanie.lower()
    nowe_zdanie=""
    cipher=[]
    for element in zdanie:
        if element in p:
            x=p.find(element)
            l=x+3
            cipher.append(l)
            nowe_zdanie += p[l]
        elif element in string2:
            cipher.append(element)
            nowe_zdanie+=element
    nowe_zdanie=nowe_zdanie.upper()
    print(nowe_zdanie)
    choice()



def decipher(string,string1,string2):
    zdanie=input("Enter the sentence to be decoded:\n")
    p=input("Would you like to include Polish characters?(y/n)\n")
    if p=="y":
        p=string
    else:
        p=string1
    zdanie=zdanie.lower()
    p=p[::-1]
    print(p)
    nowe_zdanie=""
    cipher=[]
    for element in zdanie:
        if element in p:
            x=p.find(element)
            l=x+3
            cipher.append(l)
            nowe_zdanie += p[l]
        elif element in string2:
            cipher.append(element)
            nowe_zdanie+=element
    nowe_zdanie=nowe_zdanie.upper()
    print(nowe_zdanie)
    choice()
cipher(string,string1,string2)
