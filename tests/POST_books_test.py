from services.books.requests import POST


def test_books_POST():
    response = POST.add_user()
    assert response.status_code == 200
    print(response.content)
