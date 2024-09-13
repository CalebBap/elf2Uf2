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
    0x01: "32-bit",
    0x02: "64-bit"
}

DATA_VALUES = {
    0x01: "little",
    0x02: "big"
}

ABI_VALUES = {
    0x00: "System V",
    0x01: "HP-UX",
    0x02: "NetBSD",
    0x03: "Linux",
    0x04: "GNU Hurd",
    0x06: "Solaris",
    0x07: "AIX (Monterey)",
    0x08: "IRIX",
    0x09: "FreeBSD",
    0x0A: "Tru64",
    0x0B: "Novell Modesto",
    0x0C: "OpenBSD",
    0x0D: "OpenVMS",
    0x0E: "NonStop Kernel",
    0x0F: "AROS",
    0x10: "FenixOS",
    0x11: "Nuxi CloudABI",
    0x12: "Stratus Technologies OpenVOS",
}

OBJECT_FILE_TYPES = {
    0x0000: "ET_NONE (Unknown)",
    0x0001: "ET_REL (Relocatable file)",
    0x0002: "ET_EXEC (Executable file)",
    0x0003: "ET_DYN (Shared object)",
    0x0004: "ET_CORE (Core file)",
    0xFE00: "ET_LOOS",
    0xFEFF: "ET_HIOS",
    0xFF00: "ET_LOPROC",
    0xFFFF: "ET_HIPROC",
}

MACHINE_TYPES = {
    0x0000: "Unspecified",
    0x0001: "AT&T WE 32100",
    0x0002: "SPARC",
    0x0003: "x86",
    0x0004: "Motorola 68000 (M68k)",
    0x0005: "Motorola 88000 (M88k)",
    0x0006: "Intel MCU",
    0x0007: "Intel 80860",
    0x0008: "MIPS",
    0x0009: "IBM System/370",
    0x000A: "MIPS RS3000 Little-endian",
    0x000F: "Hewlett-Packard PA-RISC",
    0x0013: "Intel 80960",
    0x0014: "PowerPC",
    0x0015: "PowerPC (64-bit)",
    0x0016: "S390, including S390x",
    0x0017: "IBM SPU/SPC",
    0x0024: "NEC V800",
    0x0025: "Fujitsu FR20",
    0x0026: "TRW RH-32",
    0x0027: "Motorola RCE",
    0x0028 : "Arm (up to Armv7/AArch32)",
    0x0029: "Digital Alpha",
    0x002A: "SuperH",
    0x002B: "SPARC Version 9",
    0x002C: "Siemens TriCore embedded processor",
    0x002D: "Argonaut RISC Core",
    0x002E: "Hitachi H8/300",
    0x002F: "Hitachi H8/300H",
    0x0030: "Hitachi H8S",
    0x0031: "Hitachi H8/500",
    0x0032: "IA-64",
    0x0033: "Stanford MIPS-X",
    0x0034: "Motorola ColdFire",
    0x0035: "Motorola M68HC12",
    0x0036: "Fujitsu MMA Multimedia Accelerator",
    0x0037: "Siemens PCP",
    0x0038: "Sony nCPU embedded RISC processor",
    0x0039: "Denso NDR1 microprocessor",
    0x003A: "Motorola Star*Core processor",
    0x003B: "Toyota ME16 processor",
    0x003C: "STMicroelectronics ST100 processor",
    0x003D: "Advanced Logic Corp. TinyJ embedded processor family",
    0x003E: "AMD x86-64",
    0x003F: "Sony DSP Processor",
    0x0040: "Digital Equipment Corp. PDP-10",
    0x0041: "Digital Equipment Corp. PDP-11",
    0x0042: "Siemens FX66 microcontroller",
    0x0043: "STMicroelectronics ST9+ 8/16 bit microcontroller",
    0x0044: "STMicroelectronics ST7 8-bit microcontroller",
    0x0045: "Motorola MC68HC16 Microcontroller",
    0x0046: "Motorola MC68HC11 Microcontroller",
    0x0047: "Motorola MC68HC08 Microcontroller",
    0x0048: "Motorola MC68HC05 Microcontroller",
    0x0049: "Silicon Graphics SVx",
    0x004A: "STMicroelectronics ST19 8-bit microcontroller",
    0x004B: "Digital VAX",
    0x004C: "Axis Communications 32-bit embedded processor",
    0x004D: "Infineon Technologies 32-bit embedded processor",
    0x004E: "Element 14 64-bit DSP Processor",
    0x004F: "LSI Logic 16-bit DSP Processor",
    0x008C: "TMS320C6000 Family",
    0x00AF: "MCST Elbrus e2k",
    0x00B7: "Arm 64-bits (Armv8/AArch64)",
    0x00DC: "Zilog Z80",
    0x00F3: "RISC-V",
    0x00F7: "Berkeley Packet Filter",
    0x0101: "WDC 65C816",
    0x0102: "LoongArch",
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
