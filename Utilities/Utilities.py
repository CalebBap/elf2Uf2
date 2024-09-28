from Constants.Constants import Endianess

from typing import BinaryIO
from typing import Dict

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

def parse_string(input_path: str, offset: int) -> str:
    with open(input_path, 'rb') as file:
        file.seek(offset)

        str = ""
        chr = file.read(1)
        while chr != b'\x00':
            str += chr.decode()
            chr = file.read(1)

        return str

def zero_pad_data(data: bytes, padded_size: int) -> bytes:
    data_size = len(data)

    if data_size > padded_size:
        raise Exception(f"Error: data size of {data_size} bytes exceeds {padded_size} bytes")

    if data_size != padded_size:
        data += b'\x00' * (padded_size - data_size)

    return data
