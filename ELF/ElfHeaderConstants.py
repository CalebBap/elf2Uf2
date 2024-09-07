# ELF header field lengths
EI_MAG_LEN = 4
EI_CLASS_LEN = 1
EI_DATA_LEN = 1
EI_VERSION_LEN = 1
EI_OSABI_LEN = 1
EI_ABIVERSION_LEN = 1
EI_PAD_LEN = 7
E_TYPE_LEN = 2
E_MACHINE_LEN = 2
E_VERSION_LEN = 4
E_ENTRY_LEN_32_BIT = 4
E_ENTRY_LEN_64_BIT = 8
E_PHOFF_LEN_32_BIT = 4
E_PHOFF_LEN_64_BIT = 8
E_SHOFF_LEN_32_BIT = 4
E_SHOFF_LEN_64_BIT = 8
E_FLAGS_LEN = 4
E_EHSIZE_LEN = 2
E_PHENTSIZE_LEN = 2
E_PHNUM_LEN = 2
E_SHENTSIZE_LEN = 2
E_SHNUM_LEN = 2
E_SHSTRNDX_LEN = 2

# ELF header constants
EI_CLASS_32_BIT = b'\x01'
EI_CLASS_64_BIT = b'\x02'

EI_DATA_LITTLE = b'\x01'
EI_DATA_BIG = b'\x02'

ARM_MACHINE = b'\x28\x00'

# ARM ELF flags from binutils-gdb/include/elf/arm.h
EF_ARM_RELEXEC = 0x01
EF_ARM_INTERWORK = 0x04
EF_ARM_SYMSARESORTED = 0x04
EF_ARM_APCS_26 = 0x08
EF_ARM_DYNSYMSUSESEGIDX = 0x08
EF_ARM_APCS_FLOAT = 0x10
EF_ARM_MAPSYMSFIRST = 0x10
EF_ARM_PIC = 0x20
EF_ARM_ALIGN8 = 0x40
EF_ARM_NEW_ABI = 0x80
EF_ARM_OLD_ABI = 0x100
EF_ARM_SOFT_FLOAT = 0x200
EF_ARM_ABI_FLOAT_SOFT = 0x200
EF_ARM_ABI_FLOAT_HARD = 0x400
EF_ARM_VFP_FLOAT = 0x400
EF_ARM_LE8 = 0x400000
EF_ARM_BE8 = 0x800000

EF_ARM_EABIMASK = 0xFF000000
EF_ARM_EABI_UNKNOWN = 0x00000000
EF_ARM_EABI_VER1 = 0x01000000
EF_ARM_EABI_VER2 = 0x02000000
EF_ARM_EABI_VER3 = 0x03000000
EF_ARM_EABI_VER4 = 0x04000000
EF_ARM_EABI_VER5 = 0x05000000

# Stringified header values
CLASS_VALUES = {
    EI_CLASS_32_BIT: "32-bit",
    EI_CLASS_64_BIT: "64-bit"
}

DATA_VALUES = {
    EI_DATA_LITTLE: "little",
    EI_DATA_BIG: "big"
}

ABI_VALUES = {
    b'\x00': "System V",
    b'\x01': "HP-UX",
    b'\x02': "NetBSD",
    b'\x03': "Linux",
    b'\x04': "GNU Hurd",
    b'\x06': "Solaris",
    b'\x07': "AIX (Monterey)",
    b'\x08': "IRIX",
    b'\x09': "FreeBSD",
    b'\x0A': "Tru64",
    b'\x0B': "Novell Modesto",
    b'\x0C': "OpenBSD",
    b'\x0D': "OpenVMS",
    b'\x0E': "NonStop Kernel",
    b'\x0F': "AROS",
    b'\x10': "FenixOS",
    b'\x11': "Nuxi CloudABI",
    b'\x12': "Stratus Technologies OpenVOS",
}

OBJECT_FILE_TYPES = {
    b'\x00\x00': "ET_NONE (Unknown)",
    b'\x01\x00': "ET_REL (Relocatable file)",
    b'\x02\x00': "ET_EXEC (Executable file)",
    b'\x03\x00': "ET_DYN (Shared object)",
    b'\x04\x00': "ET_CORE (Core file)",
    b'\xFE\x00': "ET_LOOS",
    b'\xFE\xFF': "ET_HIOS",
    b'\xFF\x00': "ET_LOPROC",
    b'\xFF\xFF': "ET_HIPROC",
}

MACHINE_TYPES = {
    b'\x00\x00': "Unspecified",
    b'\x01\x00': "AT&T WE 32100",
    b'\x02\x00': "SPARC",
    b'\x03\x00': "x86",
    b'\x04\x00': "Motorola 68000 (M68k)",
    b'\x05\x00': "Motorola 88000 (M88k)",
    b'\x06\x00': "Intel MCU",
    b'\x07\x00': "Intel 80860",
    b'\x08\x00': "MIPS",
    b'\x09\x00': "IBM System/370",
    b'\x0A\x00': "MIPS RS3000 Little-endian",
    b'\x0F\x00': "Hewlett-Packard PA-RISC",
    b'\x13\x00': "Intel 80960",
    b'\x14\x00': "PowerPC",
    b'\x15\x00': "PowerPC (64-bit)",
    b'\x16\x00': "S390, including S390x",
    b'\x17\x00': "IBM SPU/SPC",
    b'\x24\x00': "NEC V800",
    b'\x25\x00': "Fujitsu FR20",
    b'\x26\x00': "TRW RH-32",
    b'\x27\x00': "Motorola RCE",
    ARM_MACHINE : "Arm (up to Armv7/AArch32)",
    b'\x29\x00': "Digital Alpha",
    b'\x2A\x00': "SuperH",
    b'\x2B\x00': "SPARC Version 9",
    b'\x2C\x00': "Siemens TriCore embedded processor",
    b'\x2D\x00': "Argonaut RISC Core",
    b'\x2E\x00': "Hitachi H8/300",
    b'\x2F\x00': "Hitachi H8/300H",
    b'\x30\x00': "Hitachi H8S",
    b'\x31\x00': "Hitachi H8/500",
    b'\x32\x00': "IA-64",
    b'\x33\x00': "Stanford MIPS-X",
    b'\x34\x00': "Motorola ColdFire",
    b'\x35\x00': "Motorola M68HC12",
    b'\x36\x00': "Fujitsu MMA Multimedia Accelerator",
    b'\x37\x00': "Siemens PCP",
    b'\x38\x00': "Sony nCPU embedded RISC processor",
    b'\x39\x00': "Denso NDR1 microprocessor",
    b'\x3A\x00': "Motorola Star*Core processor",
    b'\x3B\x00': "Toyota ME16 processor",
    b'\x3C\x00': "STMicroelectronics ST100 processor",
    b'\x3D\x00': "Advanced Logic Corp. TinyJ embedded processor family",
    b'\x3E\x00': "AMD x86-64",
    b'\x3F\x00': "Sony DSP Processor",
    b'\x40\x00': "Digital Equipment Corp. PDP-10",
    b'\x41\x00': "Digital Equipment Corp. PDP-11",
    b'\x42\x00': "Siemens FX66 microcontroller",
    b'\x43\x00': "STMicroelectronics ST9+ 8/16 bit microcontroller",
    b'\x44\x00': "STMicroelectronics ST7 8-bit microcontroller",
    b'\x45\x00': "Motorola MC68HC16 Microcontroller",
    b'\x46\x00': "Motorola MC68HC11 Microcontroller",
    b'\x47\x00': "Motorola MC68HC08 Microcontroller",
    b'\x48\x00': "Motorola MC68HC05 Microcontroller",
    b'\x49\x00': "Silicon Graphics SVx",
    b'\x4A\x00': "STMicroelectronics ST19 8-bit microcontroller",
    b'\x4B\x00': "Digital VAX",
    b'\x4C\x00': "Axis Communications 32-bit embedded processor",
    b'\x4D\x00': "Infineon Technologies 32-bit embedded processor",
    b'\x4E\x00': "Element 14 64-bit DSP Processor",
    b'\x4F\x00': "LSI Logic 16-bit DSP Processor",
    b'\x8C\x00': "TMS320C6000 Family",
    b'\xAF\x00': "MCST Elbrus e2k",
    b'\xB7\x00': "Arm 64-bits (Armv8/AArch64)",
    b'\xDC\x00': "Zilog Z80",
    b'\xF3\x00': "RISC-V",
    b'\xF7\x00': "Berkeley Packet Filter",
    b'\x01\x01': "WDC 65C816",
    b'\x01\x02': "LoongArch",
}

ARM_EABI_FLAGS = {
    0x00000000: "Unknown",
    0x01000000: "Version 1",
    0x02000000: "Version 2",
    0x03000000: "Version 3",
    0x04000000: "Version 4",
    0x05000000: "Version 5",
}

SEGMENT_TYPES = {
    0x00000000: "PT_NULL",
    0x00000001: "PT_LOAD",
    0x00000002: "PT_DYNAMIC",
    0x00000003: "PT_INTERP",
    0x00000004: "PT_NOTE",
    0x00000005: "PT_SHLIB",
    0x00000006: "PT_PHDR",
    0x00000007: "PT_TLS",
    0x60000000: "PT_LOOS",
    0x6FFFFFFF: "PT_HIOS",
    0x70000000: "PT_LOPROC",
    0x7FFFFFFF: "PT_HIPROC",
}
