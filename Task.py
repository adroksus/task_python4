"""
Напишите функцию read_last(lines, file),
которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим,
что задано положительное целое число).
Протестируем функцию на файле «article.txt» со следующим содержимым:
"""

def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
        else:
            print('Количество строк может быть только целым положительным')

# Тесты 
read_last(5, 'article.txt')
read_last(-5, 'article.txt')

"""
Требуется реализовать функцию longest_words(file), которая записывает в файл result.txt слово,
имеющее максимальную длину (или список слов, если таковых несколько).
"""
def longest_words(file):
    with open(file, encoding='utf-8') as text:
        words = text.read().split()
        max_length = len(max(words, key=len))
        sought_words = [word for word in words if len(word) == max_length]
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words
 
 
print(longest_words('article.txt'))