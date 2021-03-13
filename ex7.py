# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func(a):
    my_separate = a.split(' ')
    my_words = []
    for i in my_separate:
        letter_elements = str(i)
        first_letter = letter_elements[:1].upper()
        word = first_letter + letter_elements[1:]
        my_words.append(word)
    return my_words


print(int_func("abra kadabra abra kadabra"))