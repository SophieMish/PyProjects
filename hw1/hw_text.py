import re

# text_ru.txt
# text_en.txt

print("""Задание №1.
1. Взять текстовый файл с каким-нибудь достаточно большим текстом.
* Посчитать количество слов
* Найти топ-10 самых часто повторящихся слов
* Создать новый текст, в котором все предложения идут задом наперёд. (Имеются ввиду слова) Мама мыла
раму -> раму мыла Мама. Знаки препинания можно не учитывать или учитывать как захочется. Конец
предложения - это точка, вопросительный знак, восклицательный знак, многоточие.""")


def count_words(text):
    print("\nПункт №1")
    print("Количество слов в тексте:", len(text.split()))


def find_frequency(text):
    print("\nПункт №2")
    frequency = {}
    words = text.split()
    dict = set(words)
    for word in dict:
        frequency.update({word: words.count(word)})
    max_value = max(frequency.values())
    min_value = min(frequency.values())
    final_dict_max = {k: v for k, v in frequency.items() if v == max_value}
    final_dict_min = {k: v for k, v in frequency.items() if v == min_value}
    print("Максимально используемое слово", final_dict_max)
    print("Минимально используемое(ые) слово(a)", final_dict_min)


def reverse_words(text):
    print("\nПункт №3")
    # t = reversed(text.split())
    text = " ".join(reversed(text.split(" ")))
    # print("Текст, в котором слова поставены наоборот:", text)
    print("Текст, в котором слова поставены наоборот:", text)
    file = open("text_ru1.txt", "w", encoding='utf-8')
    text = text.replace("\n", "")
    file.write(text)


file = open('text_ru.txt', 'r', encoding='utf-8')
text = file.read()
print("\nТекст из файла: ", text)

sep = [',', '.', '!', '?!', '-', '(', ')','1','2','3','4','"']
for i in sep:
    text = text.replace(i, ' ')
print("\nТекст без разделителей: ", text)
count_words(text)
find_frequency(text)
reverse_words(text)
