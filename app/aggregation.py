from argparse import ArgumentTypeError


def average(arr: list):
    return sum(arr) / len(arr)


aggregates = {
    "min": min,
    "max": max,
    "avg": average,
}


def aggregate(rows: list[list[str]], columns: list[str], aggregate_parameter: str):
    # валидация
    if "=" not in aggregate_parameter:
        raise ArgumentTypeError('Аргумент --aggregate должен содержать разделитель "="')
    params = aggregate_parameter.split("=")
    if params[0] not in columns:
        raise ArgumentTypeError(
            "Аргумент --aggregate должен содержать существующую колонку"
        )
    column_id = columns.index(params[0])
    if params[1] not in aggregates.keys():
        raise ArgumentTypeError(f"--aggregate: Неизвестная операция {params[1]}")
    func = aggregates[params[1]]
    result = func([i[column_id] for i in rows])
    return [params[1], result]
