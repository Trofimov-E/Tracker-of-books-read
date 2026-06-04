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

def add_book(books):
    """Добавление новой книги"""
    clear_screen()  # Функция очистки экрана
    while True:
        try:
            author = input('Введите автора: ')
            if author.strip() != '':  # проверяем на пустоту ввода, если не пусто то переходим к следующему вводу
                break
            print('Автор не может быть пустым!')
        except ValueError:
            print('Введите автора!')
    while True:
        try:
            title = input('Введите название книги: ')
            if title.strip() != '':  # проверяем на пустоту ввода, если не пусто то переходим к следующему вводу
                break
            print('Название книги не может быть пустым!')
        except ValueError:
            print('Введите название книги!')
    for book in books: # проверка есть ли введенная книга в списке прочитанных, если есть то выходим из функции добавления
        if book['author'] == author.lower() and book['title'] == title.lower():
            print('Такая книга уже прочитана.')
            return
    while True:
        try:
            rating = int(input('Введите оценку (1-5): '))
            if 1 <= rating <= 5:
                break
            print('Введите число от 1 до 5')
        except ValueError:
            print('Введите число.')
    date = input('Дата прочтения: ')
    new_book = {'author': author.lower(), 'title': title.lower(), 'rating': rating, 'date': date}
    books.append(new_book)
    save_books(books)
    print('Книга добавлена!')

def display_books(books):
    """Отображение списка книг"""
    clear_screen()  # Функция очистки экрана
    if not books: #проверка на пустоту списка книг, если список пустой выходим из функции
        print('Список книг пуст!')
        return
    print('\nСписок книг:')
    print(f'\n{'№':<3} {'Автор':<20} {'Название книги':<40} {'Оценка книги':<15} {'Дата прочтения':<15}')
    print('=' * 96)
    for i, book in enumerate(books, 1):  # перебираем весь список книг и выводим на экран
        print(f'{i:<3} {book['author']:<20} {book['title']:<40} {book['rating']:<15} {book['date']:<15}')

def average_rating_books(books):
    """Отображение средней оценки по всем прочитанным книгам"""
    clear_screen()  # Функция очистки экрана
    if not books:
        print('Список книг пуст!')
        return
    avg = sum(book["rating"] for book in books) / len(books)

    print(f'Средняя оценка прочитанных книг: {avg:.2f}')

def sat_author(books):
    """Отображение статистики по автору (сколько прочитано книг)"""
    clear_screen()  # Функция очистки экрана
    if not books:
        print('Список книг пуст!')
        return
    authors = [book["author"] for book in books]
    stats = Counter(authors)
    print('\nСтатистика по авторам:')
    for author, count in stats.items():
        if count == 1:
            print(f'{author}: {count} книга')
        elif 2 <= count <= 4:
            print(f'{author}: {count} книги')
        else:
            print(f'{author}: {count} книг')
            
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
