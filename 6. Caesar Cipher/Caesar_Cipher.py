print("If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the "
      "letters of the alphabet, that not a word could be made out.")

string = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźżaąbc"
string1 = "abcdefghijklmnopqrstuvwxyzabc"
string2 = " -.,"


def choice():
    while True:
        try:
            decision = input("Would you like to try again?(y/n)\n")
            decision = decision.lower()
            if decision not in "yn":
                raise ValueError("Incomprehensible decision.")
        except Exception as error:
            print(error)
        else:
            break

    if decision == "y":
        while True:
            try:
                decision_2 = input("Do you want to encrypt the message?(y/n)\n")
                decision_2 = decision_2.lower()
                if decision_2 not in "yn":
                    raise ValueError("Incomprehensible decision.")
            except Exception as error:
                print(error)
            else:
                break

        if decision_2 == "y":
            cipher(string, string1, string2)
        else:
            decipher(string, string1, string2)
    else:
        print("Thank you for using this program.")


def cipher(string, string1, string2):
    sentence = input("Enter a sentence to encrypt:\n")
    while True:
        try:
            characters = input("Would you like to include Polish characters?(y/n)\n")
            characters = characters.lower()
            if characters not in "yn":
                raise ValueError("Incomprehensible decision.")
        except Exception as error:
            print(error)
        else:
            break
    if characters == "y":
        characters = string
    else:
        characters = string1
    sentence = sentence.lower()
    new_sentence = ""
    for element in sentence:
        if element in characters:
            x = characters.find(element)
            l = x + 3
            new_sentence += characters[l]
        elif element in string2:
            new_sentence += element
    new_sentence = new_sentence.upper()
    print(new_sentence)
    choice()


def decipher(string, string1, string2):
    sentence = input("Enter the sentence to be decoded:\n")
    while True:
        try:
            characters = input("Would you like to include Polish characters?(y/n)\n")
            characters = characters.lower()
            if characters not in "yn":
                raise ValueError("Incomprehensible decision.")
        except Exception as error:
            print(error)
        else:
            break
    if characters == "y":
        characters = string
    else:
        characters = string1
    sentence = sentence.lower()
    characters = characters[::-1]
    print(characters)
    new_sentence = ""
    for element in sentence:
        if element in characters:
            x = characters.find(element)
            l = x + 3
            new_sentence += characters[l]
        elif element in string2:
            new_sentence += element
    new_sentence = new_sentence.upper()
    print(new_sentence)
    choice()


if __name__ == '__main__':
    cipher(string, string1, string2)
