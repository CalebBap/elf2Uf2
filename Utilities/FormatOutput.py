from Constants.Constants import Endianess
from Utilities.Utilities import *

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

def dump_values(header: str, values: List[Type[ValueStr]]):
    if values:
        title_length = max(len(value.title) for value in values)

    print(f"{header}:\n")

    for value in values:
        title_value_spacing = ' ' * (title_length - len(value.title))
        print(f"\t{value.title}:{title_value_spacing}\t{value.value} {value.unit}")

    print("\n")
