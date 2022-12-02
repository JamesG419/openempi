from enum import Enum


class PutVersionIdPixpdqServiceStateUpdownUpdown(str, Enum):
    UP = "up"
    DOWN = "down"

    def __str__(self) -> str:
        return str(self.value)
