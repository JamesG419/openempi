from enum import Enum


class GetVersionIdRecordLinksRecordRecordIdDirect(str, Enum):
    Y = "Y"

    def __str__(self) -> str:
        return str(self.value)
