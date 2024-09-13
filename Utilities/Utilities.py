from ELF.Constants.ElfConstants import Endianess

from typing import BinaryIO
from typing import Dict
from typing import List

class ValueString:
    def __init__(self, title: str, value: str, unit: str = ""):
        self.title = title
        self.value = value
        self.unit = unit

def get_field(file: BinaryIO, file_size: int, field_length: int) -> bytes:
    if file_size < (file.tell() + field_length):
        print(f"Error: invalid ELF file size - {file_size} bytes")
        return None

    return file.read(field_length)

def bytes_to_int(value: bytes, endianess: Endianess) -> int:
    endianess = 'big' if endianess == Endianess.BIG_ENDIAN else 'little'
    return int.from_bytes(value, endianess)

def stringify(value: bytes, endianess: Endianess, stringified_values: Dict[int, str]) -> str:
    value = bytes_to_int(value, endianess)
    return stringified_values[value] if value in stringified_values else hex(value)

def dump_values(header: str, values: List[ValueString]):
    if values:
        title_length = max(len(value.title) for value in values)

    print(f"{header}:\n")

    for value in values:
        title_value_spacing = ' ' * (title_length - len(value.title))
        print(f"\t{value.title}:{title_value_spacing}\t{value.value} {value.unit}")

    print("\n")
