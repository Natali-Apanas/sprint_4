# qa_python_4_sprint

Список тестов в финальном проекте 4 спринта:

1. `test_add_new_book_with_empty_title_does_not_add` - метод `add_new_book()` не добавляет книгу с названием в виде пустой строки
2. `test_add_new_book_add_book_in_list` - метод `add_new_book()` успешно добавляет книгу в список книг
3. `test_set_book_genre_in_list_correct` - метод `set_book_genre()` успешно задаёт книге жанр из поддерживаемого списка
4. `test_get_book_genre_returns_correct_genre` - метод `get_book_genre()` успешно возвращает жанр ранее добавленной книги
5. `test_get_books_with_specific_genre_returns_right_books_list` - метод `get_books_with_specific_genre()` выводит по заданному жанру все имеющиеся книги
6. `test_get_books_genre_returns_correct_dict` - метод `get_books_genre()` возвращает корректный словарь с ранее добавленными книгами
7. `test_get_books_for_children_returns_correct_books_for_children` - метод `get_books_for_children()` возвращает список детских книг (книг тех жанров, которые разрешены детям)
8. `test_add_book_in_favorites_correct_add_book_in_favorites` - метод `add_book_in_favorites()` успешно добавляет в избранное ранее добавленную книгу
9. `test_add_book_in_favorites_not_add_unkown_book_in_favorites` - метод `add_book_in_favorites()` не добавляет в избранное неизвестную книгу
10. `test_delete_book_from_favorites_delete_only_one_book_from_favorites` - метод `delete_book_from_favorite()` удаляет только одну указанную книгу из списка
11. `test_get_list_of_favorites_books_returns_correct_list` - метод `get_list_of_favorites_books()` возвращает корректный список с ранее добавленными в избранное книгами

Для запуска тестов, находясь в папке с проектом, можно выполнить или `python tests.py`, или `pytest -v tests.py`.
