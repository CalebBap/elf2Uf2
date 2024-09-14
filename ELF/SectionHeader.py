from Constants.Constants import *
from ELF.Constants.SectionHeaderConstants import *
from Utilities.FormatOutput import *
from Utilities.Utilities import *

import os
from typing import BinaryIO

class ElfSectionHeader:
    def __init__(self, input_path: str, size: int, offset: int, arch: Architecture, endianess: Endianess):
        self.INPUT_PATH = input_path
        self.FILE_SIZE = os.path.getsize(input_path)
        self.SIZE = size
        self.OFFSET = offset
        self.ARCH = arch
        self.endianess = endianess

        self.sh_name = None
        self.sh_type = None
        self.sh_flags = None
        self.sh_addr = None
        self.sh_offset = None
        self.sh_size = None
        self.sh_link = None
        self.sh_info = None
        self.sh_addralign = None
        self.sh_entsize = None

        if not self.__parse():
            raise Exception("Error: failed to parse ELF section header entry")

    def __parse_name(self, file: BinaryIO) -> bool:
        self.sh_name = get_field(file, self.FILE_SIZE, SH_NAME_LEN)
        return self.sh_name is not None

    def __parse_type(self, file: BinaryIO) -> bool:
        self.sh_type = get_field(file, self.FILE_SIZE, SH_TYPE_LEN)
        return self.sh_type is not None

    def __parse_flags(self, file: BinaryIO) -> bool:
        length = SH_FLAGS_32_BIT_LEN if self.ARCH == Architecture.ELF_32_BIT else SH_FLAGS_64_BIT_LEN
        self.sh_flags = get_field(file, self.FILE_SIZE, length)
        return self.sh_flags is not None

    def __parse_addr(self, file: BinaryIO) -> bool:
        length = SH_ADDR_32_BIT_LEN if self.ARCH == Architecture.ELF_32_BIT else SH_ADDR_64_BIT_LEN
        self.sh_addr = get_field(file, self.FILE_SIZE, length)
        return self.sh_addr is not None

    def __parse_offset(self, file: BinaryIO) -> bool:
        length = SH_OFFSET_32_BIT_LEN if self.ARCH == Architecture.ELF_32_BIT else SH_OFFSET_64_BIT_LEN
        self.sh_offset = get_field(file, self.FILE_SIZE, length)
        return self.sh_offset is not None

    def __parse_size(self, file: BinaryIO) -> bool:
        length = SH_SIZE_32_BIT_LEN if self.ARCH == Architecture.ELF_32_BIT else SH_SIZE_64_BIT_LEN
        self.sh_size = get_field(file, self.FILE_SIZE, length)
        return self.sh_size is not None

    def __parse_link(self, file: BinaryIO) -> bool:
        self.sh_link = get_field(file, self.FILE_SIZE, SH_LINK_LEN)
        return self.sh_link is not None

    def __parse_info(self, file: BinaryIO) -> bool:
        self.sh_info = get_field(file, self.FILE_SIZE, SH_INFO_LEN)
        return self.sh_info is not None

    def __parse_addralign(self, file: BinaryIO) -> bool:
        length = SH_ADDRALIGN_32_BIT_LEN if self.ARCH == Architecture.ELF_32_BIT else SH_ADDRALIGN_64_BIT_LEN
        self.sh_addralign = get_field(file, self.FILE_SIZE, length)
        return self.sh_addralign is not None

    def __parse_entsize(self, file: BinaryIO) -> bool:
        length = SH_ENTSIZE_32_BIT_LEN if self.ARCH == Architecture.ELF_32_BIT else SH_ENTSIZE_64_BIT_LEN
        self.sh_entsize = get_field(file, self.FILE_SIZE, length)
        return self.sh_entsize is not None

    def __section_name(self, string_table_offset: int):
        sh_name_offset = bytes_to_int(self.sh_name, self.endianess)
        total_offset = string_table_offset + sh_name_offset
        return parse_string(self.INPUT_PATH, total_offset)

    def dump_values(self, index: int, string_table_offset: int) -> str:
        values = [
            ValueStr("Name", self.__section_name(string_table_offset)),
            # TODO: ValueString("Type"),
            # TODO: ValueString("Flags"),
            # TODO: ValueString("Virtual address"),
            # TODO: ValueString("File image offset"),
            # TODO: ValueString("Size"),
            # TODO: ValueString("Associated section index"),
            # TODO: ValueString("Information"),
            # TODO: ValueString("Alignment"),
            # TODO: ValueString("Entry fixed-size"),
        ]

        dump_values(f"Section #{index}", values)

    def __parse(self) -> bool:
        with open(self.INPUT_PATH, 'rb') as elf_file:
            elf_file.seek(self.OFFSET)

            parse_funcs = [
                self.__parse_name,
                self.__parse_type,
                self.__parse_flags,
                self.__parse_addr,
                self.__parse_offset,
                self.__parse_size,
                self.__parse_link,
                self.__parse_info,
                self.__parse_addralign,
                self.__parse_entsize
            ]

            if not all(func(elf_file) for func in parse_funcs):
                return False

            entry_size = elf_file.tell() - self.OFFSET
            if entry_size != self.SIZE:
                print(f"Error: expected section header to be {self.SIZE} bytes, not {entry_size} bytes")
                return False

            return True

    def offset(self) -> int:
        return bytes_to_int(self.sh_offset, self.endianess)
