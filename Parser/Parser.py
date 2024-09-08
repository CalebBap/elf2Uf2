from typing import BinaryIO
from typing import Callable
from typing import List

def get_field(file: BinaryIO, file_size: int, field_length: int) -> bytes:
    if file_size < (file.tell() + field_length):
        print(f"Error: invalid ELF file size - {file_size} bytes")
        return None

    return file.read(field_length)

def stringify(value: bytes, stringified_values: dict) -> str:
    return stringified_values[value] if value in stringified_values else value.hex()

class ValueString:
    def __init__(self, title: str, value: bytes | str, formatter: Callable = None, unit: str = ""):
        self.title = title
        self.value = value
        self.unit = unit
        self.formatter = formatter if formatter is not None else lambda str: str

def dump_values(header: str, values: List[ValueString]):
    if values:
        title_length = max(len(value.title) for value in values)

    print(f"{header}:\n")
    for value in values:
        title_value_spacing = ' ' * (title_length - len(value.title))
        print(f"\t{value.title}:{title_value_spacing}\t{value.formatter(value.value)} {value.unit}")
    print("\n")
