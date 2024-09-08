from ELF.ElfHeaderConstants import *
from Parser.Parser import *

import os
from typing import BinaryIO

class ElfHeader:
    def __init__(self, input_path) -> None:
        self.INPUT_PATH = input_path
        self.FILE_SIZE = os.path.getsize(input_path)
        self.ei_mag = None
        self.ei_class = None
        self.ei_data = None
        self.ei_version = None
        self.ei_osabi = None
        self.ei_abiversion = None
        self.e_type = None
        self.e_machine = None
        self.e_version = None
        self.e_entry = None
        self.e_phoff = None
        self.e_shoff = None
        self.e_flags = None
        self.e_ehsize = None
        self.e_phentsize = None
        self.e_phnum = None
        self.e_shentsize = None
        self.e_shnum = None
        self.e_shstrndx = None

    def __parse_magic(self, file: BinaryIO) -> bool:
        self.ei_mag = get_field(file, self.FILE_SIZE, EI_MAG_LEN)
        return self.ei_mag is not None

    def __parse_format(self, file: BinaryIO) -> bool:
        self.ei_class = get_field(file, self.FILE_SIZE, EI_CLASS_LEN)
        return self.ei_class is not None

    def __parse_endianness(self, file: BinaryIO) -> bool:
        self.ei_data = get_field(file, self.FILE_SIZE, EI_DATA_LEN)
        return self.ei_data is not None

    def __parse_version(self, file: BinaryIO) -> bool:
        self.ei_version = get_field(file, self.FILE_SIZE, EI_VERSION_LEN)
        return self.ei_version is not None

    def __parse_abi(self, file: BinaryIO) -> bool:
        self.ei_osabi = get_field(file, self.FILE_SIZE, EI_OSABI_LEN)
        return self.ei_osabi is not None

    def __parse_abi_version(self, file: BinaryIO) -> bool:
        self.ei_abiversion = get_field(file, self.FILE_SIZE, EI_ABIVERSION_LEN)
        return self.ei_abiversion is not None

    def __parse_padding(self, file: BinaryIO) -> bool:
        padding = get_field(file, self.FILE_SIZE, EI_PAD_LEN)
        return padding is not None

    def __parse_type(self, file: BinaryIO) -> bool:
        self.e_type = get_field(file, self.FILE_SIZE, E_TYPE_LEN)
        return self.e_type is not None

    def __parse_machine(self, file: BinaryIO) -> bool:
        self.e_machine = get_field(file, self.FILE_SIZE, E_MACHINE_LEN)
        return self.e_machine is not None

    def __parse_version_2(self, file: BinaryIO) -> bool:
        self.e_version = get_field(file, self.FILE_SIZE, E_VERSION_LEN)
        return self.e_version is not None

    def __parse_entry_addr(self, file: BinaryIO) -> bool:
        e_entry_len = E_ENTRY_LEN_32_BIT if self.ei_class == EI_CLASS_32_BIT else E_ENTRY_LEN_64_BIT
        self.e_entry = get_field(file, self.FILE_SIZE, e_entry_len)
        return self.e_entry is not None

    def __parse_ph_offset(self, file: BinaryIO) -> bool:
        e_phoff_len = E_PHOFF_LEN_32_BIT if self.ei_class == EI_CLASS_32_BIT else E_PHOFF_LEN_64_BIT
        self.e_phoff = get_field(file, self.FILE_SIZE, e_phoff_len)
        return self.e_phoff is not None

    def __parse_sh_offset(self, file: BinaryIO) -> bool:
        e_shoff_len = E_SHOFF_LEN_32_BIT if self.ei_class == EI_CLASS_32_BIT else E_SHOFF_LEN_64_BIT
        self.e_shoff = get_field(file, self.FILE_SIZE, e_shoff_len)
        return self.e_shoff is not None

    def __parse_flags(self, file: BinaryIO) -> bool:
        self.e_flags = get_field(file, self.FILE_SIZE, E_FLAGS_LEN)
        return self.e_flags is not None

    def __parse_eh_size(self, file: BinaryIO) -> bool:
        self.e_ehsize = get_field(file, self.FILE_SIZE, E_EHSIZE_LEN)
        return self.e_ehsize is not None

    def __parse_phent_size(self, file: BinaryIO) -> bool:
        self.e_phentsize = get_field(file, self.FILE_SIZE, E_PHENTSIZE_LEN)
        return self.e_phentsize is not None

    def __parse_ph_num(self, file: BinaryIO) -> bool:
        self.e_phnum = get_field(file, self.FILE_SIZE, E_PHNUM_LEN)
        return self.e_phnum is not None

    def __parse_shent_size(self, file: BinaryIO) -> bool:
        self.e_shentsize = get_field(file, self.FILE_SIZE, E_SHENTSIZE_LEN)
        return self.e_shentsize is not None

    def __parse_sh_num(self, file: BinaryIO) -> bool:
        self.e_shnum = get_field(file, self.FILE_SIZE, E_SHNUM_LEN)
        return self.e_shnum is not None

    def __parse_shstrndx(self, file: BinaryIO) -> bool:
        self.e_shstrndx = get_field(file, self.FILE_SIZE, E_SHSTRNDX_LEN)
        return self.e_shstrndx is not None

    def __bytes_to_int(self, value: bytes) -> int:
        endianess = 'little' if self.ei_data == EI_DATA_LITTLE else 'big'
        return int.from_bytes(value, endianess)

    def __arm_eabi_unknown_flags(self, flags: int) -> str:
        str = ", GNU EABI"

        if flags & EF_ARM_INTERWORK:
          flags &= ~EF_ARM_INTERWORK
          str += ", interworking enabled"

        if flags & EF_ARM_APCS_26:
          flags &= ~EF_ARM_APCS_26
          str += ", uses APCS/26"

        if flags & EF_ARM_APCS_FLOAT:
          flags &= ~EF_ARM_APCS_FLOAT
          str += ", uses APCS/float"

        if flags & EF_ARM_PIC:
          flags &= ~EF_ARM_PIC
          str += ", position independent"

        if flags & EF_ARM_ALIGN8:
          flags &= ~EF_ARM_ALIGN8
          str += ", 8 bit structure alignment"

        if flags & EF_ARM_NEW_ABI:
          flags &= ~EF_ARM_NEW_ABI
          str += ", uses new ABI"

        if flags & EF_ARM_OLD_ABI:
          flags &= ~EF_ARM_OLD_ABI
          str += ", uses old ABI"

        if flags & EF_ARM_SOFT_FLOAT:
          flags &= ~EF_ARM_SOFT_FLOAT
          str += ", software FP"

        if flags & EF_ARM_VFP_FLOAT:
          flags &= ~EF_ARM_VFP_FLOAT
          str += ", VFP"

        return (str, flags)

    def __arm_eabi_v1_flags(self, flags: int) -> str:
        str = ", Version1 EABI"

        if flags & EF_ARM_SYMSARESORTED:
            flags &= ~EF_ARM_SYMSARESORTED
            str += ", sorted symbol tables"

        return (str, flags)

    def __arm_eabi_v2_flags(self, flags: int) -> str:
        str = ", Version2 EABI"

        if flags & EF_ARM_DYNSYMSUSESEGIDX:
            flags &= ~EF_ARM_DYNSYMSUSESEGIDX
            str += ", dynamic symbols use segment index"

        if flags & EF_ARM_MAPSYMSFIRST:
            flags &= ~EF_ARM_MAPSYMSFIRST
            str += ", mapping symbols precede others"

        return (str, flags)

    def __arm_eabi_v3_flags(self, flags: int) -> str:
        str = ", Version3 EABI"

        return (str, flags)

    def __arm_eabi_v4_flags(self, flags: int) -> str:
        str = ", Version4 EABI"

        if flags & EF_ARM_BE8:
            flags &= ~EF_ARM_BE8
            str += ", BE8"

        if flags & EF_ARM_LE8:
            flags &= ~EF_ARM_LE8
            str += ", LE8"

        return (str, flags)

    def __arm_eabi_v5_flags(self, flags: int) -> str:
        str = ", Version5 EABI"

        if flags & EF_ARM_BE8:
            flags &= ~EF_ARM_BE8
            str += ", BE8"

        if flags & EF_ARM_LE8:
            flags &= ~EF_ARM_LE8
            str += ", LE8"

        if flags & EF_ARM_ABI_FLOAT_SOFT:
            flags &= ~EF_ARM_ABI_FLOAT_SOFT
            str += ", soft-float ABI"

        if flags & EF_ARM_ABI_FLOAT_HARD:
            flags &= ~EF_ARM_ABI_FLOAT_HARD
            str += ", hard-float ABI"

        return (str, flags)

    def __arm_flags_str(self) -> str:
        flags = self.__bytes_to_int(self.e_flags)
        str = hex(flags)

        # currently, only stringification of ARM flags is supported
        if self.e_machine != ARM_MACHINE:
            return str

        # flags processed as per binutils-gdb/binutils/readelf.c
        if flags & EF_ARM_RELEXEC:
            flags &= ~EF_ARM_RELEXEC
            str += ", relocatable executable"

        if flags & EF_ARM_PIC:
            flags &= ~EF_ARM_PIC
            str += ", position independent"

        eabi_ver = flags & EF_ARM_EABIMASK
        flags &= ~EF_ARM_EABIMASK

        EABI_VERSION_STR = {
            EF_ARM_EABI_UNKNOWN: self.__arm_eabi_unknown_flags(flags),
            EF_ARM_EABI_VER1: self.__arm_eabi_v1_flags(flags),
            EF_ARM_EABI_VER2: self.__arm_eabi_v2_flags(flags),
            EF_ARM_EABI_VER3: self.__arm_eabi_v3_flags(flags),
            EF_ARM_EABI_VER4: self.__arm_eabi_v4_flags(flags),
            EF_ARM_EABI_VER5: self.__arm_eabi_v5_flags(flags),
        }

        if eabi_ver in EABI_VERSION_STR:
            eabi_ver_str = EABI_VERSION_STR[eabi_ver]
        else:
            eabi_ver_str = (", <unrecognized EABI>", flags)

        str += eabi_ver_str[0]
        flags = eabi_ver_str[1]

        if flags != 0:
            str += f", <unknown - {hex(flags)}>"

        return str

    def dump_values(self):
        values = [
            ValueString("Magic", self.ei_mag, lambda bytes: bytes.decode()),
            ValueString("Class", self.ei_class, lambda bytes: stringify(bytes, CLASS_VALUES)),
            ValueString("Endianess", self.ei_data, lambda bytes: stringify(bytes, DATA_VALUES)),
            ValueString("Version", self.ei_version, self.__bytes_to_int),
            ValueString("OS ABI", self.ei_osabi, lambda bytes: stringify(bytes, ABI_VALUES)),
            ValueString("ABI version", self.ei_abiversion, self.__bytes_to_int),
            ValueString("Object file type", stringify(self.e_type, OBJECT_FILE_TYPES)),
            ValueString("ISA", stringify(self.e_machine, MACHINE_TYPES)),
            ValueString("Entry point", self.e_entry, lambda bytes: hex(self.__bytes_to_int(bytes))),
            ValueString("Program header offset", self.e_phoff, lambda bytes: hex(self.__bytes_to_int(bytes))),
            ValueString("Section header offset", self.e_shoff, lambda bytes: hex(self.__bytes_to_int(bytes))),
            ValueString("Flags", self.__arm_flags_str()),
            ValueString("ELF header size", self.e_ehsize, self.__bytes_to_int, "bytes"),
            ValueString("Program header entry size", self.e_phentsize, self.__bytes_to_int, "bytes"),
            ValueString("Program header entry count", self.e_phnum, self.__bytes_to_int),
            ValueString("Section header entry size", self.e_shentsize, self.__bytes_to_int, "bytes"),
            ValueString("Section header entry count", self.e_shnum, self.__bytes_to_int),
            ValueString("Section name index", self.e_shstrndx, self.__bytes_to_int)
        ]

        dump_values("ELF Header values", values)

    def parse(self) -> bool:
        with open(self.INPUT_PATH, 'rb') as elf_file:
            parse_funcs = [
                self.__parse_magic,
                self.__parse_format,
                self.__parse_endianness,
                self.__parse_version,
                self.__parse_abi,
                self.__parse_abi_version,
                self.__parse_padding,
                self.__parse_type,
                self.__parse_machine,
                self.__parse_version_2,
                self.__parse_entry_addr,
                self.__parse_ph_offset,
                self.__parse_sh_offset,
                self.__parse_flags,
                self.__parse_eh_size,
                self.__parse_phent_size,
                self.__parse_ph_num,
                self.__parse_shent_size,
                self.__parse_sh_num,
                self.__parse_shstrndx
            ]

            return all(func(elf_file) for func in parse_funcs)

    def ph_table_offset(self) -> int:
        return self.__bytes_to_int(self.e_phoff)

    def ph_entry_size(self) -> int:
        return self.__bytes_to_int(self.e_phentsize)

    def ph_table_entry_count(self) -> int:
        return self.__bytes_to_int(self.e_phnum)
