# qa_python
# BooksCollector — тесты

## Описание проекта

Автотесты для класса `BooksCollector` — приложения для управления коллекцией книг и избранным.

---


## Описание тестов

### Добавление книг — `add_new_book`

| Тест | Описание |
|------|----------|
| `test_add_new_book_adds_book_to_dict` | Параметризованный тест. Проверяет, что книги с разными названиями успешно добавляются в словарь `books_genre` |
| `test_add_new_book_name_more_than_40_symbols_not_added` | Проверяет, что книга с названием длиннее 40 символов не добавляется |
| `test_add_new_book_has_no_genre` | Проверяет, что у новой книги жанр по умолчанию пустой |
| `test_add_new_book_same_book_added_once` | Проверяет, что одну и ту же книгу нельзя добавить дважды |

### Установка жанра — `set_book_genre`, `get_book_genre`

| Тест | Описание |
|------|----------|
| `test_set_book_genre_sets_correct_genre` | Проверяет, что жанр книги устанавливается и возвращается корректно |

### Книги по жанру — `get_books_with_specific_genre`

| Тест | Описание |
|------|----------|
| `test_get_books_with_specific_genre_returns_correct_books` | Параметризованный тест. Проверяет, что метод возвращает книги нужного жанра для Фантастики, Ужасов и Детективов |

### Книги для детей — `get_books_for_children`

| Тест | Описание |
|------|----------|
| `test_get_books_for_children_excludes_age_rated_books` | Проверяет, что книги с возрастным рейтингом (Ужасы, Детективы) отсутствуют в списке книг для детей |

### Избранное — `add_book_in_favorites`, `delete_book_from_favorites`, `get_list_of_favorites_books`

| Тест | Описание |
|------|----------|
| `test_add_book_in_favorites_adds_book` | Проверяет, что книга успешно добавляется в избранное |
| `test_delete_book_from_favorites_removes_book` | Проверяет, что книга успешно удаляется из избранного |
| `test_get_list_of_favorites_books_returns_correct_list` | Проверяет, что метод возвращает корректный список избранных книг |

---

## Структура проекта

```
├── main.py       # Основной класс BooksCollector
├── tests.py  # Автотесты
└── README.md                # Описание проекта
```