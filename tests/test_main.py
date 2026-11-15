from main import add_numbers


def test_add_numbers():
    result = add_numbers(10, 20)

    assert result == 30