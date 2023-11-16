def reverse_string(word):
    if word is None or len(word) == 0:
        return ""

    list_words = word.split(" ")
    final_list = []
    for i in range(0, len(list_words)):
        if i % 2 != 0:
            final_list.append(list_words[i][::-1])
        else:
            final_list.append(list_words[i])

    reversed_string = ""
    for i in range(0, len(final_list)):
        if i == len(final_list) - 1:
            reversed_string = reversed_string + final_list[i]
        else:
            reversed_string = reversed_string + final_list[i] + " "

    return reversed_string

word = "the quick brown fox jumps over"
print (reverse_string(word))