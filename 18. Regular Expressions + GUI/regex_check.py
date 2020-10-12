import re


def is_valid_time(input):
    '''Checks the string for time values where it follows correct format
    Hours can be between 0-23 and minutes between 00-59'''
    output = []
    matches = re.findall(r'\b(0?[0-9]|1[0-9]|2[0-3]):([0-5][0-9])\b', input)
    if matches:
        for match in matches:
            match = ",".join(match).replace(",", ":")
            print(match)
            output.append(match)
        return output
    return "No matches found"


def is_valid_nip(input):
    '''Checks the string for NIP numbers where it follows correct format
    XXX-XX-XX-XXX or XXXXXXXXXX and returns it without dashes(-)'''
    output = []
    matches = re.findall(r'\b(\d{3}-\d{2}-\d{2}-\d{3}|\d{10})\b', input)
    if matches:
        for match in matches:
            match = match.replace("-", "")
            print(match)
            output.append(match)
        return output
    return "No matches found"


def is_valid_phone(input):
    '''Looks for valid phone nr with a variety of possible inputs  '''
    output = []
    matches = re.findall(r'\b\+?(\d{2})?\s?(\d{3})\-?(\d{3})\-?(\d{3})\b', input)
    if matches:
        for match in matches:
            if match[0] != None:
                area_code = match[0]
            phone_number = ",".join(match[-3:]).replace(",", "")
            if area_code:
                output.append(f"Area code: {area_code} Phone: {phone_number}")
            else:
                output.append(f"Phone: {phone_number}")
        return output
    return "No matches found"


def is_valid_id(input):
    '''Checks the string for IDs where it follows correct format
    3 capital letters and 6 digits'''
    output = []
    matches = re.findall(r'\b[A-Z]{3}[0-9]{6}\b', input)
    if matches:
        for match in matches:
            print(match)
            output.append(match)
        return output
    return "No matches found"


def is_valid_pesel(input):
    '''Checks the string for pesel where it follows correct format - 11 digits'''
    output = []
    matches = re.findall(r'\b\d{11}\b', input)
    if matches:
        for match in matches:
            print(match)
            output.append(match)
        return output
    return "No matches found"

# is_valid_time("12:15 --> Correct,  2:07 --> Correct, 2:7 --> Incorrect, 22:41 --> Correct, 24:00 --> Incorrect, 23:59 --> Correct")
# is_valid_nip("931-37-42-089 --> Correct,  9313742089 --> Correct, 931-31-42123 --> Incorrect, 38922959385 --> Incorrect")
# is_valid_phone("45 121-973-002  --> Correct, 693283213 --> Correct"
#                "+35 324-985-345 --> Correct, +35+324-985-345 --> Semi-Correct,"
#                "121-973-002  --> Correct, 86-48397-49  --> Incorrect,"
#                "8648397492  --> Incorrect")
# is_valid_id("QKD256422 --> Correct, QkD256422 --> Incorrect, QKOL213222 --> Incorrect, ASR125476 --> Correct")
# is_valid_pesel("45121973002@!#!@# 123 123 12324234 2432434354325 234532452435 3453453428573429572495429534 35324485345")
