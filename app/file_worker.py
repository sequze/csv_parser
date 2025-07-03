import csv


def read_file(filename: str) -> list[list[str]]:
    rows = []
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
        return rows


def typify_rows(rows: list[list[str]]):
    for i in range(len(rows[0])):
        try:
            if "." in rows[0][i]:
                for j in range(len(rows)):
                    rows[j][i] = float(rows[j][i])
            else:
                for j in range(len(rows)):
                    rows[j][i] = int(rows[j][i])
        except ValueError:
            # Если какое-то значение колонки - строка,
            # значит вся колонка содержит строки
            for k in range(0, j):
                rows[k][i] = str(rows[k][i])
