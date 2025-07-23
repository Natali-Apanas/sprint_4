import os
import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:
    # 1
    def test_add_new_book_with_empty_title_does_not_add(self, collector):
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    # 2
    def test_add_new_book_add_book_in_list(self, collector):
        collector.add_new_book('Война и мир')
        books = collector.get_books_genre()
        assert len(books) == 1
        assert 'Война и мир' in books

    # 3
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Кладбище домашних животных', 'Ужасы'],
            ['Лето в Простоквашино', 'Мультфильмы'],
            ['Снежная королева', 'Мультфильмы']
        ]
    )
    def test_set_book_genre_in_list_correct(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    # 4
    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Кладбище домашних животных', 'Ужасы'),
            ('Лето в Простоквашино', 'Мультфильмы'),
            ('Снежная королева', 'Мультфильмы')
        ]
    )
    def test_get_book_genre_returns_correct_genre(self, collector, name, genre):
        collector.books_genre[name] = genre
        assert collector.get_book_genre(name) == genre

    # 5
    @pytest.mark.parametrize(
        'books, genre',
        [
            [['Кладбище домашних животных', 'Страшный сон разработчика'], 'Ужасы'],
            [['Лето в Простоквашино', 'Лило и Стич', 'Моана'], 'Мультфильмы'],
            [['Чумовая пятница'], 'Комедии']
        ]
    )
    def test_get_books_with_specific_genre_returns_right_books_list(self, collector, books, genre):
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert sorted(collector.get_books_with_specific_genre(genre)) == sorted(books)

    # 6
    @pytest.mark.parametrize(
        'books_dict',
        [
            {
                'Кладбище домашних животных': 'Ужасы',
                'Страшный сон разработчика': 'Ужасы'
            },
            {
                'Лето в Простоквашино': 'Мультфильмы',
                'Лило и Стич': 'Мультфильмы',
                'Моана': 'Мультфильмы'
            }
        ]
    )
    def test_get_books_genre_returns_correct_dict(self, collector, books_dict):
        for book, genre in books_dict.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert collector.get_books_genre() == books_dict

    # 7
    def test_get_books_for_children_returns_correct_books_for_children(self, collector):
        collector.add_new_book('Клуб убийств по четвергам')
        collector.set_book_genre('Клуб убийств по четвергам', 'Детективы')
        collector.add_new_book('Лето в Простоквашино')
        collector.set_book_genre('Лето в Простоквашино', 'Мультфильмы')
        assert len(collector.get_books_for_children()) == 1

    # 8
    def test_add_book_in_favorites_correct_add_book_in_favorites(self, collector):
        book_name = 'Кладбище моих нервных клеток'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Ужасы')
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == [book_name]

    # 9
    def test_add_book_in_favorites_not_add_unkown_book_in_favorites(self, collector):
        collector.add_book_in_favorites('Кладбище домашних животных')
        assert len(collector.get_list_of_favorites_books()) == 0

    # 10
    def test_delete_book_from_favorites_delete_only_one_book_from_favorites(self, collector):
        collector.add_new_book('Поющие в терновнике')
        collector.add_new_book('Унесенные ветром')
        collector.add_book_in_favorites('Поющие в терновнике')
        collector.add_book_in_favorites('Унесенные ветром')
        collector.delete_book_from_favorites('Унесенные ветром')
        assert len(collector.get_list_of_favorites_books()) == 1

    # 11
    def test_get_list_of_favorites_books_returns_correct_list(self, collector):
        books = ['Лето в Простоквашино', 'Лило и Стич', 'Моана', 'Черный обелиск']
        for book in books:
            collector.add_new_book(book)
        collector.add_book_in_favorites(books[1])
        collector.add_book_in_favorites(books[3])
        assert collector.get_list_of_favorites_books() == [books[1], books[3]]


if __name__ == '__main__':
    print(pytest.main([os.path.basename(__file__)]))
