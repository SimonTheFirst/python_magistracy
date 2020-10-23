def super_reduced_string(word: str):
    if len(word) == 0:
        return "Empty String"
    word_list = list(word)
    for i, v in enumerate(word_list):
        try:
            if word_list[i+1] == v:
                word_list.pop(i + 1)
                word_list.pop(i)
                return super_reduced_string("".join(word_list))
        except IndexError:
            return word


if __name__ == "__main__":
    print(super_reduced_string("aaabccddd"))
    print(super_reduced_string("cccxllyyy"))
    print(super_reduced_string("aa"))
    print(super_reduced_string("fghiiijkllmnnno"))
    print(super_reduced_string("baab"))
