from Constants.Constants import Endianess

from typing import BinaryIO
from typing import Dict
from typing import List
from typing import Type

class ValueStr:
    def __init__(self, title: str, value: str, unit: str = ""):
        self.title = title
        self.value = value
        self.unit = unit

class ValueUnicode(ValueStr):
    def __init__(self, title: str, value: bytes, unit: str = ""):
        value = value.decode()
        ValueStr.__init__(self, title, value, unit)

class ValueInt(ValueStr):
    def __init__(self, title: str, value: bytes, endianess: Endianess, unit: str = ""):
        value = bytes_to_int(value, endianess)
        ValueStr.__init__(self, title, value, unit)

class ValueHex(ValueStr):
    def __init__(self, title: str, value: bytes, endianess: Endianess, unit: str = ""):
        value = hex(bytes_to_int(value, endianess))
        ValueStr.__init__(self, title, value, unit)

class ValueDict(ValueStr):
    def __init__(self, title: str, value: bytes, endianess: Endianess, stringified_values: Dict[int, str], unit: str = ""):
        value = stringify(value, endianess, stringified_values)
        ValueStr.__init__(self, title, value, unit)

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

def dump_values(header: str, values: List[Type[ValueStr]]):
    if values:
        title_length = max(len(value.title) for value in values)

    print(f"{header}:\n")

    for value in values:
        title_value_spacing = ' ' * (title_length - len(value.title))
        print(f"\t{value.title}:{title_value_spacing}\t{value.value} {value.unit}")

    print("\n")

def parse_string(input_path: str, offset: int) -> str:
    with open(input_path, 'rb') as file:
        file.seek(offset)

        str = ""
        chr = file.read(1)
        while chr != b'\x00':
            str += chr.decode()
            chr = file.read(1)

        return str
