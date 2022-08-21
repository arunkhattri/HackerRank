def capitalize(string):
    new_word = []
    word = string.split(" ")
    for w in word:
        if w == "":
            new_word.append(w)
        elif w[0].isdigit():
            new_word.append(w)
        else:
            new_word.append(w.capitalize())

    return(" ".join(new_word))

if __name__ == "__main__":
    in_word = ["132 456 Wq m e", "hello world", "hello   world  lol" ]
    out_word = ["132 456 Wq M E", "Hello World", "Hello   World  Lol"]
    for i in range(len(in_word)):
        if capitalize(in_word[i]) == out_word[i]:
            print("word: {}".format(in_word[i]))
            print("capitalize word: {}".format(capitalize(in_word[i])))
            print("for string: {}, Passed Test".format(in_word[i]))
        else:
            print("for string: {}, Failed Test".format(in_word[i]))
            print("word: {}".format(in_word[i]))
            print("capitalize word: {}".format(capitalize(in_word[i])))
