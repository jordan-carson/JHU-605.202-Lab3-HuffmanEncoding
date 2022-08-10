from enum import Enum


class Constants(str, Enum):
    FREQUENCIES = "FreqTable.txt"
    ENCODED = "Encoded.txt"
    INPUT_TEXT = "ClearText.txt"


FREQUENCIES = Constants.FREQUENCIES
ENCODED = Constants.ENCODED
INPUT_TEXT = Constants.INPUT_TEXT
