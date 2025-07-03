from app.filters import FilterProcessor


def test_filter_greater_than():
    rows = [[25], [30], [15], [40]]
    columns = ["Age"]
    processor = FilterProcessor()
    result = processor.filter_file(rows, columns, "Age>20")
    assert result == [[25], [30], [40]]


def test_filter_equal():
    rows = [[1, "Artur"], [2, "Alexey"], [3, "Maxim"]]
    columns = ["ID", "Name"]
    processor = FilterProcessor()
    result = processor.filter_file(rows, columns, "Name=Maxim")
    assert result == [[3, "Maxim"]]

def test_filter_less_than():
    rows = [[12],[24],[45],[-120]]
    columns = ["Balance"]
    processor = FilterProcessor()
    result = processor.filter_file(rows, columns, "Balance<20")
    assert result == [[12], [-120]]


processor = FilterProcessor()
def test_filter_with_float():
    rows = [[4.45], [4.2], [1.2], [3.0], [5.0]]
    columns = ["Score"]
    result = processor.filter_file(rows, columns, "Score>4.2")
    assert result == [[4.45],[5.0]]