from Constants.Constants import *
from ELF.Constants.ProgramHeaderConstants import *
from Utilities.FormatOutput import *
from Utilities.Utilities import *

import os
from typing import BinaryIO

class ElfProgramHeader:
    def __init__(self, input_path: str, size: int, offset: int, arch: Architecture, endianess: Endianess) -> None:
        self.INPUT_PATH = input_path
        self.FILE_SIZE = os.path.getsize(input_path)
        self.SIZE = size
        self.OFFSET = offset
        self.ARCH = arch
        self.endianess = endianess

        self.p_type = None
        self.p_flags = None
        self.p_offset = None
        self.p_vaddr = None
        self.p_paddr = None
        self.p_filesz = None
        self.p_memsz = None
        self.p_flags = None
        self.p_align = None

        if not self.__parse():
            raise Exception("Error: failed to parse ELF program header entry")

    def __parse_type(self, file: BinaryIO) -> bool:
        self.p_type = get_field(file, self.FILE_SIZE, P_TYPE_LEN)
        return self.p_type is not None

    def __parse_flags(self, file: BinaryIO) -> bool:
        self.p_flags = get_field(file, self.FILE_SIZE, P_FLAGS_LEN)
        return self.p_flags is not None

    def __parse_offset(self, file: BinaryIO) -> bool:
        length = P_OFFSET_32_BIT_LEN if self.ARCH == Architecture.ELF_32_BIT else P_OFFSET_64_BIT_LEN
        self.p_offset = get_field(file, self.FILE_SIZE, length)
        return self.p_offset is not None

    def __parse_vaddr(self, file: BinaryIO) -> bool:
        length = P_VADDR_32_BIT_LEN if self.ARCH == Architecture.ELF_32_BIT else P_VADDR_64_BIT_LEN
        self.p_vaddr = get_field(file, self.FILE_SIZE, length)
        return self.p_vaddr is not None

    def __parse_paddr(self, file: BinaryIO) -> bool:
        length = P_PADDR_32_BIT_LEN if self.ARCH == Architecture.ELF_32_BIT else P_PADDR_64_BIT_LEN
        self.p_paddr = get_field(file, self.FILE_SIZE, length)
        return self.p_paddr is not None

    def __parse_filesz(self, file: BinaryIO) -> bool:
        length = P_FILESZ_32_BIT_LEN if self.ARCH == Architecture.ELF_32_BIT else P_FILESZ_64_BIT_LEN
        self.p_filesz = get_field(file, self.FILE_SIZE, length)
        return self.p_filesz is not None

    def __parse_memsz(self, file: BinaryIO) -> bool:
        length = P_MEMSZ_32_BIT_LEN if self.ARCH == Architecture.ELF_32_BIT else P_MEMSZ_64_BIT_LEN
        self.p_memsz = get_field(file, self.FILE_SIZE, length)
        return self.p_memsz is not None

    def __parse_align(self, file: BinaryIO) -> bool:
        length = P_ALIGN_32_BIT_LEN if self.ARCH == Architecture.ELF_32_BIT else P_ALIGN_64_BIT_LEN
        self.p_align = get_field(file, self.FILE_SIZE, length)
        return self.p_align is not None

    def __flags_str(self) -> str:
        flags = bytes_to_int(self.p_flags, self.endianess)

        flags_str = ""
        flags_str += "R" if flags & PF_R else ""
        flags_str += "W" if flags & PF_W else ""
        flags_str += "X" if flags & PF_X else ""

        return flags_str

    def __alignment_str(self) -> str:
        alignment = bytes_to_int(self.p_align, self.endianess)
        alignment_str = hex(alignment)

        if alignment in [0, 1]:
            alignment_str += " (no alignment)"

        return alignment_str

    def dump_values(self, index: int) -> str:
        values = [
            ValueDict("Type", self.p_type, self.endianess, TYPE_VALUES),
            ValueStr("Flags", self.__flags_str()),
            ValueHex("Offset", self.p_offset, self.endianess),
            ValueHex("Virtual address", self.p_vaddr, self.endianess),
            ValueHex("Physical address", self.p_paddr, self.endianess),
            ValueInt("File image size", self.p_filesz, self.endianess, "bytes"),
            ValueInt("Memory size", self.p_memsz, self.endianess, "bytes"),
            ValueStr("Alignment", self.__alignment_str()),
        ]

        dump_values(f"Segment #{index}", values)

    def __parse(self) -> bool:
        with open(self.INPUT_PATH, 'rb') as elf_file:
            elf_file.seek(self.OFFSET)

            parse_funcs = [
                self.__parse_type,
                self.__parse_offset,
                self.__parse_vaddr,
                self.__parse_paddr,
                self.__parse_filesz,
                self.__parse_memsz,
                self.__parse_align,
            ]

            FLAGS_POSITION = 6 if self.ARCH == Architecture.ELF_32_BIT else 1
            parse_funcs.insert(FLAGS_POSITION, self.__parse_flags)

            if not all(func(elf_file) for func in parse_funcs):
                return False

            entry_size = elf_file.tell() - self.OFFSET
            if entry_size != self.SIZE:
                print(f"Error: expected program header to be {self.SIZE} bytes, not {entry_size} bytes")
                return False

            return True
