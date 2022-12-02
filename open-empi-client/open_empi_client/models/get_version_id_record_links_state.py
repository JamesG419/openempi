from enum import Enum


class GetVersionIdRecordLinksState(str, Enum):
    M = "M"
    P = "P"
    A = "A"

    def __str__(self) -> str:
        return str(self.value)
