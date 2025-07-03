from app.file_worker import read_file
import csv


def test_read_file(tmp_path):
    path = tmp_path / "test.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Kirill", "22"])
        writer.writerow(["Alexander", "19"])

    rows = read_file(str(path))
    assert rows == [["Name", "Age"], ["Kirill", "22"], ["Alexander", "19"]]
