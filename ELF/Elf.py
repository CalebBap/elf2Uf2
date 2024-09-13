from ELF.Constants.ElfConstants import *
from ELF.ElfHeader import ElfHeader
from ELF.ProgramHeader import ElfProgramHeader
from ELF.SectionHeader import ElfSectionHeader
from Parser.TextFormatters import *

class Elf:
    def __init__(self, input_path: str) -> None:
        self.INPUT_PATH = input_path

        self.elf_header = ElfHeader(input_path)
        self.arch = self.elf_header.architecture()
        self.endianess = self.elf_header.endianess()

        self.program_headers = self.__parse_program_header_table()
        self.section_headers = self.__parse_section_header_table()

    def __parse_program_header_table(self) -> bool:
        program_headers = []
        ph_entry_size = self.elf_header.ph_entry_size()
        ph_table_offset = self.elf_header.ph_table_offset()

        for _ in range(self.elf_header.ph_table_entry_count()):
            program_headers += [ElfProgramHeader(self.INPUT_PATH, ph_entry_size, ph_table_offset, self.arch, self.endianess)]
            ph_table_offset += ph_entry_size

        return program_headers

    def __parse_section_header_table(self) -> bool:
        section_headers = []
        sh_entry_size = self.elf_header.sh_entry_size()
        sh_table_offset = self.elf_header.sh_table_offset()

        for _ in range(self.elf_header.sh_table_entry_count()):
            section_headers += [ElfSectionHeader(self.INPUT_PATH, sh_entry_size, sh_table_offset, self.arch, self.endianess)]
            sh_table_offset += sh_entry_size

        return section_headers

    def __dump_program_header_table(self):
        print(f"{TEXT_BOLD}{TEXT_UNDERLINE}Program header table:{TEXT_END}\n")
        for i in range(len(self.program_headers)):
            self.program_headers[i].dump_values(i + 1)

    def __dump_section_header_table(self):
        section_name_index = self.elf_header.section_name_index()
        if section_name_index >= len(self.section_headers):
            print(f"Warning: invalid section name header index, {section_name_index}; couldn't dump section header table")
            return True

        string_table_offset = self.section_headers[section_name_index].offset()

        print(f"{TEXT_BOLD}{TEXT_UNDERLINE}Section header table:{TEXT_END}\n")
        for i in range(len(self.section_headers)):
            self.section_headers[i].dump_values(i + 1, string_table_offset)

    def dump_values(self) -> None:
        self.elf_header.dump_values()
        self.__dump_program_header_table()
        self.__dump_section_header_table()
