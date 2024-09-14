# Section header field lengths
SH_NAME_LEN = 4
SH_TYPE_LEN = 4
SH_FLAGS_32_BIT_LEN = 4
SH_FLAGS_64_BIT_LEN = 8
SH_ADDR_32_BIT_LEN = 4
SH_ADDR_64_BIT_LEN = 8
SH_OFFSET_32_BIT_LEN = 4
SH_OFFSET_64_BIT_LEN = 8
SH_SIZE_32_BIT_LEN = 4
SH_SIZE_64_BIT_LEN = 8
SH_LINK_LEN = 4
SH_INFO_LEN = 4
SH_ADDRALIGN_32_BIT_LEN = 4
SH_ADDRALIGN_64_BIT_LEN = 8
SH_ENTSIZE_32_BIT_LEN = 4
SH_ENTSIZE_64_BIT_LEN = 8

# Section header flags
SHF_WRITE = 0x00000001
SHF_ALLOC = 0x00000002
SHF_EXECINSTR = 0x00000004
SHF_MERGE = 0x00000010
SHF_STRINGS = 0x00000020
SHF_INFO_LINK = 0x00000040
SHF_LINK_ORDER = 0x00000080
SHF_OS_NONCONFORMING = 0x00000100
SHF_GROUP = 0x00000200
SHF_TLS = 0x00000400
SHF_MASKOS = 0x0FF00000
SHF_MASKPROC = 0xF0000000
SHF_ORDERED = 0x04000000
SHF_EXCLUDE = 0x08000000

# Stringified header values
TYPE_VALUES = {
    0x00000000: "SHT_NULL - entry is unused",
    0x00000001: "SHT_PROGBITS - program data",
    0x00000002: "SHT_SYMTAB - symbol table",
    0x00000003: "SHT_STRTAB - string table",
    0x00000004: "SHT_RELA - relocation entries with addends",
    0x00000005: "SHT_HASH - symbol hash table",
    0x00000006: "SHT_DYNAMIC - dynamic linking information",
    0x00000007: "SHT_NOTE - notes",
    0x00000008: "SHT_NOBITS - program space with no data (bss)",
    0x00000009: "SHT_REL - relocation entries, no addends",
    0x0000000A: "SHT_SHLIB - reserved",
    0x0000000B: "SHT_DYNSYM - dynamic linker symbol table",
    0x0000000E: "SHT_INIT_ARRAY - array of constructors",
    0x0000000F: "SHT_FINI_ARRAY - array of destructors",
    0x00000010: "SHT_PREINIT_ARRAY - array of pre-constructors",
    0x00000011: "SHT_GROUP - section group",
    0x00000012: "SHT_SYMTAB_SHNDX - extended section indices",
    0x00000013: "SHT_RELR - RELR relative relocations",
    # note: values 0x60000000 to 0x6FFFFFFF are OS specific
}
