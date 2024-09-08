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
    b'\x00\x00\x00\x00': "PT_NULL - unused",
    b'\x01\x00\x00\x00': "PT_LOAD - loadable segment",
    b'\x02\x00\x00\x00': "PT_DYNAMIC - dynamic linking information",
    b'\x03\x00\x00\x00': "PT_INTERP - interpreter information",
    b'\x04\x00\x00\x00': "PT_NOTE - auxiliary information",
    b'\x05\x00\x00\x00': "PT_SHLIB - reserved",
    b'\x06\x00\x00\x00': "PT_PHDR - segment contains program header table",
    b'\x07\x00\x00\x00': "PT_TLS - thread-local storage template",
    b'\x00\x00\x00\x60': "PT_LOOS - reserved, OS specific",
    b'\xFF\xFF\xFF\x6F': "PT_HIOS - reserved, OS specific",
    b'\x00\x00\x00\x70': "PT_LOPROC - reserved, processor specific",
    b'\xFF\xFF\xFF\x7F': "PT_HIPROC - reserved, processor specific"
}
