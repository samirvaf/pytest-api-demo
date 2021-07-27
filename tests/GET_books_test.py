from services.books.requests import GET


def test_books_GET():
    response = GET.all_books()
    assert response.status_code == 200
    assert response.content is not None
