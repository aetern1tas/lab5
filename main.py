import re
import csv

with open('task1-en.txt', 'r', encoding='utf-8') as file:
    text = file.read()


words = re.findall(r'\b[a-zA-Z]{3,5}\b', text)
print("Слова от 3 до 5 букв:")
for word in words:
    print(word)
print("Нашлось слов:", len(words))


numbers = re.findall(r'\b[1-9]\d{3,}\b', text)
#numbers = re.findall(r'\b\d{4,}\b', text) (если число может начинаться с нуля)
print("Числа больше 3 знаков:")
for number in numbers:
    print(number)
print("Всего чисел:", len(numbers))


with open('task2.html', 'r', encoding='utf-8') as file:
    html_file = file.read()

all_tags = re.findall(r'<([a-zA-Z][a-zA-Z0-9]*)(?:\s+[^>]*)?(?<!\/)>', html_file)
unique_tags = []
for tag in all_tags:
    if tag not in unique_tags:
        unique_tags.append(tag)
print("Найденные уникальные открывающие тэги:", unique_tags, "\nВсего найдено тэгов:", len(unique_tags))


with open("task3.txt", "r", encoding='utf-8') as text:
    file_content = text.read()


search_ID = re.findall(r"\b\d{1,4}\b", file_content)
search_Surname = re.findall(r"\b[A-Z][a-z]+\b", file_content)
search_email = re.findall(r"\b\S+@\S+\.\S+\b", file_content)
search_date = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", file_content)
search_site = re.findall(r"\bhttps?://\S+\b", file_content)

min_length = min(len(search_ID), len(search_Surname), len(search_email), len(search_date), len(search_site))

with open('task3_table.txt', 'w', encoding='utf-8') as answer:
    for i in range(min_length):
        id_val = search_ID[i].strip()
        surname_val = search_Surname[i].strip()
        email_val = search_email[i].strip()
        date_val = search_date[i].strip()
        site_val = search_site[i].strip()
        
        table = "; ".join([id_val, surname_val, email_val, date_val, site_val])
        answer.write(table)
        answer.write('\n')


with open("task3_table.csv", 'w', encoding='utf-8', newline='') as csvfile:
    answercsv = csv.writer(csvfile, delimiter=';')
    
    answercsv.writerow(['ID', 'Фамилия', 'Email', 'Дата', 'Сайт'])
    
    for i in range(min_length):
        answercsv.writerow([
            search_ID[i].strip(),
            search_Surname[i].strip(),
            search_email[i].strip(),
            search_date[i].strip(),
            search_site[i].strip()
        ])
