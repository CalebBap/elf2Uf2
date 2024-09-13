# Program header field lengths
P_TYPE_LEN = 4
P_FLAGS_LEN = 4
P_OFFSET_32_BIT_LEN = 4
P_OFFSET_64_BIT_LEN = 8
P_VADDR_32_BIT_LEN = 4
P_VADDR_64_BIT_LEN = 8
P_PADDR_32_BIT_LEN = 4
P_PADDR_64_BIT_LEN = 8
P_FILESZ_32_BIT_LEN = 4
P_FILESZ_64_BIT_LEN = 8
P_MEMSZ_32_BIT_LEN = 4
P_MEMSZ_64_BIT_LEN = 8
P_ALIGN_32_BIT_LEN = 4
P_ALIGN_64_BIT_LEN = 8

# Segment flags
PF_X = 0x01
PF_W = 0x02
PF_R = 0x04

# Stringified header values
TYPE_VALUES = {
    0x00000000: "PT_NULL - unused",
    0x00000001: "PT_LOAD - loadable segment",
    0x00000002: "PT_DYNAMIC - dynamic linking information",
    0x00000003: "PT_INTERP - interpreter information",
    0x00000004: "PT_NOTE - auxiliary information",
    0x00000005: "PT_SHLIB - reserved",
    0x00000006: "PT_PHDR - segment contains program header table",
    0x00000007: "PT_TLS - thread-local storage template",
    0x60000000: "PT_LOOS - reserved, OS specific",
    0x6FFFFFFF: "PT_HIOS - reserved, OS specific",
    0x70000000: "PT_LOPROC - reserved, processor specific",
    0x7FFFFFFF: "PT_HIPROC - reserved, processor specific"
}
