from app.file_worker import read_file, typify_rows
from app.aggregation import aggregate
from app.filters import FilterProcessor
from app.models import Arguments


def process_request(args: Arguments):
    filter_parameter = args.where
    aggregate_parameter = args.aggregate
    rows = read_file(args.file)
    columns = rows[0]
    rows = rows[1:]
    typify_rows(rows)
    f = FilterProcessor()
    if args.where:
        rows = f.filter_file(rows, columns, filter_parameter)
    if args.aggregate:
        result = aggregate(rows, columns, aggregate_parameter)
        return result
    rows.insert(0, columns)
    return rows
