from ELF.Constants.ElfConstants import *
from ELF.ElfHeader import ElfHeader
from ELF.ProgramHeader import ElfProgramHeader
from ELF.SectionHeader import ElfSectionHeader
from Parser.TextFormatters import *

class Elf:
    def __init__(self, input_path: str, verbose: bool) -> None:
        self.INPUT_PATH = input_path
        self.VERBOSE = verbose

        self.arch = Architecture.UNKNOWN
        self.endianess = Endianess.UNKNOWN
        self.elf_header = ElfHeader(input_path)
        self.program_headers = []
        self.section_headers = []

    def __parse_elf_header(self) -> bool:
        if not self.elf_header.parse():
            print("Error: failed to parse ELF header")
            return False

        self.arch = self.elf_header.architecture()
        self.endianess = self.elf_header.endianess()

        if not self.VERBOSE:
            return True

        self.elf_header.dump_values()
        return True

    def __parse_program_header_table(self) -> bool:
        ph_entry_size = self.elf_header.ph_entry_size()
        ph_table_offset = self.elf_header.ph_table_offset()

        for i in range(self.elf_header.ph_table_entry_count()):
            self.program_headers += [ElfProgramHeader(self.INPUT_PATH, ph_entry_size, ph_table_offset, self.arch, self.endianess)]
            ph_table_offset += ph_entry_size

            if not self.program_headers[i].parse():
                print(f"Error: failed to parse ELF program header entry {i + 1}")
                return False

        if not self.VERBOSE:
            return True

        print(f"{TEXT_BOLD}{TEXT_UNDERLINE}Program header table:{TEXT_END}\n")
        for i in range(self.elf_header.ph_table_entry_count()):
            self.program_headers[i].dump_values(i + 1)

        return True

    def __parse_section_header_table(self) -> bool:
        sh_entry_size = self.elf_header.sh_entry_size()
        sh_table_offset = self.elf_header.sh_table_offset()

        for i in range(self.elf_header.sh_table_entry_count()):
            self.section_headers += [ElfSectionHeader(self.INPUT_PATH, sh_entry_size, sh_table_offset, self.arch, self.endianess)]
            sh_table_offset += sh_entry_size

            if not self.section_headers[i].parse():
                print(f"Error: failed to parse ELF program header entry {i + 1}")
                return False

        if not self.VERBOSE:
            return True

        section_name_index = self.elf_header.section_name_index()
        if section_name_index >= len(self.section_headers):
            print(f"Warning: invalid section name header index, {section_name_index}; couldn't dump section header table")
            return True

        string_table_offset = self.section_headers[section_name_index].offset()

        print(f"{TEXT_BOLD}{TEXT_UNDERLINE}Section header table:{TEXT_END}\n")
        for i in range(self.elf_header.sh_table_entry_count()):
            self.section_headers[i].dump_values(i + 1, string_table_offset)

        return True

    def parse(self) -> bool:
        if not self.__parse_elf_header():
            return False

        if not self.__parse_program_header_table():
            return False

        if not self.__parse_section_header_table():
            return False

        return True
