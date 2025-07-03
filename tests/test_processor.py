from app.processor import process_request
from app.models import Arguments


def test_full_pipeline():
    args = Arguments(
        file="tests/sample.csv",
        where="Score>80",
        aggregate="Score=avg"
    )
    result = process_request(args)
    assert result[0] == "avg"
    assert result[1] == 90

def test_without_aggregate():
    args = Arguments(
        file="tests/sample.csv",
        where="Score<90"
    )
    result = process_request(args)
    assert result[0] == ["Name","Score"]
    assert result[1] == ["Alexey",85]
