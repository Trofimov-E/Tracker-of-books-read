import json
import os
from collections import Counter

BOOKS_FILE = "books.json"

def clear_screen():
    """Очистака консоля"""
    os.system('cls' if os.name == 'nt' else 'clear') #Определяем ОС и посылаем команду очистки консоля

def load_books():
    """Загрузка книг из файла"""
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_books(books):
    """Сохранение книг в файл"""
    with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def main():
    """Главная функция программы"""
    books = load_books()
    while True:
        print("\n" + "=" * 50)
        print("ТРЕКЕР ПРОЧИТАННЫХ КНИГ")
        print("=" * 50)
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        print("-" * 50)

        choice = input("Выберите действие (1-6): ").strip() #Вводим команду и удаляем пробел

        if choice == '1':
            add_book(books) #Функция добавления книги
        elif choice == '2':
            display_books(books) #Функция отображения всех книг
        elif choice == '3':
            average_rating_books(books) #Функция показа средней оценки по всем книгам
        elif choice == '4':
            sat_author(books) #Функция вывода статистики по автору
        elif choice == '5':
            delete_book(books) #Функция удаления книги
        elif choice == '6':
            break #Выход из программы
        else:
            print('Нет такой команды') #Вывод на экран сообщения, если введена некорректная команда

# Код запуска
if __name__ == "__main__":
    main()
