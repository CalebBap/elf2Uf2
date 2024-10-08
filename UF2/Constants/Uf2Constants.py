from enum import IntEnum

class Uf2Flags(IntEnum):
    NONE = 0x00000000,
    NOT_MAIN_FLASH = 0x00000001,
    FILE_CONTAINER = 0x00001000,
    FAMILY_ID_PRESENT = 0x00002000,
    MD5_CHECKSUM_PRESENT = 0x00004000,
    EXTENSION_TAGS_PRESENT = 0x00008000,

BLOCK_SIZE = 512
BLOCK_DATA_SIZE = 476
BLOCK_FIELD_SIZE = 4
BLOCK_FIELD_MAX_VALUE = 0xFFFFFFFF
