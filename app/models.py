from dataclasses import dataclass


@dataclass
class Arguments:
    file: str
    where: str | None = None
    aggregate: str | None = None
