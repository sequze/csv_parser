from argparse import ArgumentTypeError
from typing import Callable


def bigger(b) -> Callable:
    def filter_bigger(a):
        return a > b

    return filter_bigger


def equals(b) -> Callable:
    def filter_equals(a):
        return a == b

    return filter_equals


def smaller(b) -> Callable:
    def filter_smaller(a):
        return a < b

    return filter_smaller


filters = {
    ">": bigger,
    "<": smaller,
    "=": equals,
}


class FilterProcessor:
    filter_function: Callable
    column_id: int

    def validate_filter(
        self, rows: list[list[str]], columns: list[str], filter_parameter: str
    ):
        # Проверка на операторы
        if sum(filter_parameter.count(i) for i in filters.keys()) != 1:
            raise ArgumentTypeError("Аргумент --where должен иметь 1 оператор >,=,<")
        for i in filters.keys():
            if i in filter_parameter:
                filter_args = filter_parameter.split(i)
                # Проверка на существование колонки
                if not (filter_args[0] in columns):
                    raise ArgumentTypeError(
                        "Аргумент --where должен содержать существующую колонку"
                    )
                filter_column_id = columns.index(filter_args[0])
                val = filter_args[1]
                if isinstance(rows[0][filter_column_id], (int, float)):
                    try:
                        val = float(val) if "." in val else int(val)
                    except ValueError:
                        pass
                self.filter_function = filters[i](val)
                self.column_id = filter_column_id
                break

    def filter_file(
        self, rows: list[list[str]], columns: list[str], filter_parameter: str
    ):
        self.validate_filter(rows, columns, filter_parameter)
        filtered_rows = []
        for i in rows:
            if self.filter_function(i[self.column_id]):
                filtered_rows.append(i)
        return filtered_rows
