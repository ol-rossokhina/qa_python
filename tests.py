import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        # исправлена ошибка в тесте: метод get_books_rating заменила на get_books_genre
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    # Добавленные тесты финального проекта:

    # 1. add_new_book — параметризация: добавление книг с разными названиями
    @pytest.mark.parametrize('name', ['Гарри Поттер', 'Мастер и Маргарита', 'Война и мир'])
    def test_add_new_book_adds_book_to_dict(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    # 2. add_new_book — книга с названием больше 40 символов не добавляется
    def test_add_new_book_name_more_than_40_symbols_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('А' * 41)
        assert len(collector.get_books_genre()) == 0

    # 3. add_new_book — у добавленной книги нет жанра
    def test_add_new_book_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        assert collector.get_book_genre('Дюна') == ''

    # 4. add_new_book — одну книгу нельзя добавить дважды
    def test_add_new_book_same_book_added_once(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.get_books_genre()) == 1

    # 5. set_book_genre — жанр устанавливается корректно
    def test_set_book_genre_sets_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    # 6. get_books_with_specific_genre — возвращает книги нужного жанра
    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        books = [
            ('Дюна', 'Фантастика'),
            ('Марсианин', 'Фантастика'),
            ('Оно', 'Ужасы'),
            ('Сияние', 'Ужасы'),
            ('Шерлок Холмс', 'Детективы'),
            ('Десять негритят', 'Детективы'),
            ('Том и Джерри', 'Мультфильмы'),
            ('Бриджит Джонс', 'Комедии'),
        ]
        for name, genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна', 'Марсианин']
        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно', 'Сияние']
        assert collector.get_books_with_specific_genre('Детективы') == ['Шерлок Холмс', 'Десять негритят']
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Том и Джерри']
        assert collector.get_books_with_specific_genre('Комедии') == ['Бриджит Джонс']

    # 7. get_books_for_children — книги с возрастным рейтингом отсутствуют
    def test_get_books_for_children_excludes_age_rated_books(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        children_books = collector.get_books_for_children()
        assert 'Оно' not in children_books and 'Дюна' in children_books

    # 8. add_book_in_favorites — книга добавляется в избранное
    def test_add_book_in_favorites_adds_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert 'Дюна' in collector.get_list_of_favorites_books()

    # 9. delete_book_from_favorites — книга удаляется из избранного
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert 'Дюна' not in collector.get_list_of_favorites_books()

    # 10. get_list_of_favorites_books — возвращает корректный список избранного
    def test_get_list_of_favorites_books_returns_correct_list(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == ['Дюна', 'Гарри Поттер']

    # 11. get_books_genre — возвращает текущий словарь books_genre
    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_genre() == {'Дюна': 'Фантастика'}

    # 12. get_book_genre — возвращает жанр книги по названию
    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'    