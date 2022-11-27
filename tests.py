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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Тестирование метода __init__
    # Рейтинг книг по умолчанию является пустым словарем
    def test_default_rating_is_empty_dict(self, books_collector):
        assert books_collector.books_rating == {}

    # Избранные книги по умолчанию являются пустым списком
    def test_default_favorites_is_empty_list(self, books_collector):
        assert books_collector.favorites == []

    # Метод add_new_book добавляет книгу в словарь с рейтингом по умолчанию 1
    def test_add_new_book_add_book_true(self, books_collector):
        books_collector.add_new_book("Гарри Поттер")
        assert books_collector.books_rating == {"Гарри Поттер": 1}

    # Книга добавляется только один раз
    def test_add_new_book_adding_exist_book_false(self, books_collector):
        books_collector.add_new_book("Гарри Поттер и принц полукровка")
        books_collector.add_new_book('Гарри Поттер и принц полукровка')
        book_names = books_collector.books_rating.keys()
        assert len(book_names) == 1 and "Гарри Поттер и принц полукровка" in book_names

    # Метод set_book_rating может устанавливать новый рейтинг от 1 до 10 для книги из словаря books_rating
    def test_set_book_rating_set_from_1_to_10_true(self, books_collector):
        books_collector.add_new_book("Вторая жизнь Уве")
        for rating in range(1, 11):
            books_collector.set_book_rating("Вторая жизнь Уве", rating)
            assert books_collector.books_rating.get("Вторая жизнь Уве") == rating

    # Нельзя установить новый рейтинг меньше 1 для книги из словаря
    def test_set_book_rating_set_less_than_1_false(self, books_collector):
        books_collector.add_new_book("Вторая жизнь Уве")
        for rating in range(-1, 1):
            books_collector.set_book_rating("Вторая жизнь Уве", rating)
            assert books_collector.books_rating.get("Вторая жизнь Уве") == 1

    # Нельзя установить новый рейтинг, если книги в словаре нет
    def test_set_book_rating_set_for_missing_false(self, books_collector):
        assert books_collector.set_book_rating("Дети из камеры хранения", 3) is None

    # Метод get_book_rating выводит рейтинг книги из словаря по её имени
    def test_get_book_rating_for_exist_name_true(self, books_collector):
        books_collector.add_new_book("Как тестируют в Google")
        books_collector.set_book_rating("Как тестируют в Google", 10)
        assert books_collector.get_book_rating("Как тестируют в Google") == 10

    # Отсутстует рейтинг книги не из словаря
    def test_get_book_rating_for_not_exist_name_false(self, books_collector):
        assert books_collector.get_book_rating("Как тестируют в Avito") is None

    # Метод get_books_with_specific_rating выводит список книг с указанным рейтингом от 1 до 10
    def test_get_books_with_specific_rating_equal_10_for_book_in_dict_true(self, books_collector):
        books_with_raiting = {
            "Как тестируют в Google": 10,
            "Как тестируют в Avito": 10,
            "Вторая жизнь Уве": 3
            }
        for key, value in books_with_raiting.items():
            books_collector.add_new_book(key)
            books_collector.set_book_rating(key, value)
        sorted_book_list_by_10 = books_collector.get_books_with_specific_rating(10)
        assert len(sorted_book_list_by_10) == 2 and "Вторая жизнь Уве" not in sorted_book_list_by_10

    # Метод get_books_rating выводит текущий словарь books_rating
    def test_get_books_rating_only_1_book_true(self, books_collector):
        books_collector.add_new_book("Alice in Wonderland")
        books_collector.set_book_rating("Alice in Wonderland", 8)
        assert books_collector.get_books_rating() == {"Alice in Wonderland": 8}

    # Метод add_book_in_favorites добавляет книгу из словаря в избранное
    def test_add_book_in_favorites_for_book_from_dict_true(self, books_collector):
        list_books = ["Как тестируют в Google", "Alice in Wonderland", "Как тестируют в Avito"]
        for book in list_books:
            books_collector.add_new_book(book)
        books_collector.add_book_in_favorites("Как тестируют в Avito")
        assert books_collector.favorites == ["Как тестируют в Avito"]

    # Метод delete_book_from_favorites удаляет книгу из избранного, если она там есть
    def test_delete_book_from_favorites_delete_1_book_from_list_true(self, books_collector):
        books_collector.favorites.append("Цветы для Элджернона")
        books_collector.favorites.append("Чистый код")
        books_collector.favorites.append("The Minds of Billy Milligan")
        books_collector.delete_book_from_favorites("Чистый код")
        assert len(books_collector.favorites) == 2 and "Чистый код" not in books_collector.favorites

    # Метод get_list_of_favorites_books получает список избранных книг
    def test_get_list_of_favorites_books_list_with_3_books_true(self, books_collector):
        books_collector.favorites.append("Цветы для Элджернона")
        books_collector.favorites.append("Чистый код")
        books_collector.favorites.append("The Minds of Billy Milligan")
        list_of_favorites_books = books_collector.get_list_of_favorites_books()
        assert list_of_favorites_books == ["Цветы для Элджернона", "Чистый код", "The Minds of Billy Milligan"]
