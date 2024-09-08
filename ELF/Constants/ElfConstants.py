from enum import Enum

class Architecture(Enum):
    ELF_32_BIT = 0,
    ELF_64_BIT = 1,
    UNKNOWN = 2

class Endianess(Enum):
    BIG_ENDIAN = 0,
    LITTLE_ENDIAN = 1,
    UNKNOWN = 2
