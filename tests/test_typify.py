from app.file_worker import typify_rows


def test_typify_rows():
    rows = [["1", "2.5", "hello"], ["3", "4.0", "world"]]
    typify_rows(rows)
    assert rows == [[1, 2.5, "hello"], [3, 4.0, "world"]]
    assert isinstance(rows[0][0], int)
    assert isinstance(rows[0][1], float)
    assert isinstance(rows[0][2], str)


def test_string_row():
    rows = [["1", "2.5", "hello"], ["world", "hello", "4"]]
    typify_rows(rows)
    assert rows == [["1", "2.5", "hello"], ["world", "hello", "4"]]