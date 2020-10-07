def encode_str(string):
    vowel_encode_dict = {
        "a": "0",
        "e": "1",
        "i": "2",
        "o": "2",
        "u": "3"
    }
    for key in vowel_encode_dict.keys():
        string = string.replace(key, vowel_encode_dict[key])
    return str(string[::-1] + "aca")


if __name__ == "__main__":
    print("Enter a string:", end=" ")
    enc_string = input()
    print(encode_str(enc_string))
