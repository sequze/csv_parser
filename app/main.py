from argparse import ArgumentTypeError
from app.processor import process_request
from app.parser import parse
from tabulate import tabulate


def main():
    try:
        table = process_request(parse())
        head = table[0]
        rows = table[1:]
        if isinstance(head, str):
            head = [head]
            rows = [rows]
        print(tabulate(rows, head, tablefmt="grid"))
    except ArgumentTypeError as e:
        print(f"Ошибка: {e}")


main()
