from os import system


def encode_character(character: str, encode_number: int) -> str:
    """Encode a single character based on specified limits. 

    Args:
        character (str): a single character in the input the user entered
        encode_number (int): a custom number with which the input is encoded

    Returns:
        chr(character_ascii)(str): encoded character
    """
    if character.isupper():
        lower_limit = 65
        upper_limit = 90
    elif character.islower():
        lower_limit = 97
        upper_limit = 122
    elif character.isnumeric():
        lower_limit = 48
        upper_limit = 57
    else:
        lower_limit = 0
        upper_limit = 127

    characters_number = upper_limit - lower_limit + 1
    encode_number %= characters_number
    character_ascii = ord(character) + encode_number

    if character_ascii > upper_limit:
        character_ascii -= characters_number
    if character_ascii < lower_limit:
        character_ascii += characters_number

    return chr(character_ascii)


def encode_input(user_input: str, encode_number: int) -> str:
    """Encode the whole text the user entered. 

    Args:
        user_input (str): the text the user want to encode
        encode_number (int): a custom number with which the input is encoded

    Returns:
        encoded_input (str): encoded text
    """
    encoded_input = ""
    for character in user_input:
        encoded_character = encode_character(character, encode_number)
        encoded_input += encoded_character
    return encoded_input


def result(user_input: str, encoded_input: str, decoded_input: str) -> str:
    """Show results

    Args:
        user_input (str): the text the user entered
        encoded_input (str): encoded text
        decoded_input (str): decoded text

    Returns:
        result_dict (dict): results
    """
    result_dict = {"The text you entered": user_input,
                   "Encoded text": encoded_input, "Decoded text": decoded_input}
    return result_dict


while True:
    user_answer = input(
        "Do you want to encode or decode a text? 1. [E]ncode 2. [D]ecode \n\U0001F449 ")
    system("cls")
    user_answer = user_answer.upper()
    match user_answer:
        case "1" | "E":

            # region Get the text the user want to encode/ Get the encode number
            user_input = input("Enter what you want to encode?\n\U0001F449")
            system("cls")
            encode_number = int(
                input("Enter the number you want to encode your text by.\n\U0001F449 "))
            system("cls")
            # endregion

            # Encode the text the user entered
            encoded_input = encode_input(user_input, encode_number)

            decode_encoded_input = input(
                "Do you want to decode the encoded text? 1. [Y]es 2. [N]o \n\U0001F449 ")
            system("cls")
            decode_encoded_input = decode_encoded_input.upper()

            # region Ask user if he/she wants to decode the encoded text
            if decode_encoded_input in ("1", "Y"):
                decoded_input = encode_input(encoded_input, -encode_number)
            else:
                decoded_input = "Not wanted"

            # region Result
            for key, val in result(user_input, encoded_input, decoded_input).items():
                print(key, val, sep=":")
            # endregion

        case "2" | "D":

            # region Get the text the user want to decode/ Get the encode number that the text was encoded by
            user_input = input(
                "Enter the text you want to decode. \n\U0001F449 ")
            system("cls")
            encode_number = int(
                input("Enter the number that the text was encoded by. \n\U0001F449 "))
            system("cls")
            # endregion

            # Decode the text the user enter
            decoded_input = encode_input(user_input, -encode_number)

            # region result
            for key, val in result(user_input, encoded_input="Not wanted", decoded_input=decoded_input). items():
                print(key, val, sep=":")
            # endregion

    user_continue = input(
        "Do you want to encode/decode another text? 1. [Y]es 2. [N]o \n\U0001F449 ")
    system("cls")
    user_continue.upper()
    if user_continue not in ("1", "Y"):
        break
