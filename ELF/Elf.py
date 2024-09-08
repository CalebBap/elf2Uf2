from ELF.ElfHeader import ElfHeader
from ELF.ProgramHeader import ElfProgramHeader
from Parser.TextFormatters import *

class Elf:
    def __init__(self, input_path: str, verbose: bool) -> None:
        self.INPUT_PATH = input_path
        self.VERBOSE = verbose

        self.elf_header = ElfHeader(input_path)
        self.program_headers = []

    def parse(self) -> bool:
        if not self.elf_header.parse():
            print("Error: failed to parse ELF header")
            return False

        if self.VERBOSE:
            self.elf_header.dump_values()

        ph_entry_size = self.elf_header.ph_entry_size()
        ph_table_offset = self.elf_header.ph_table_offset()

        for i in range(self.elf_header.ph_table_entry_count()):
            self.program_headers += [ElfProgramHeader(self.INPUT_PATH, ph_entry_size, ph_table_offset)]
            ph_table_offset += ph_entry_size

            if not self.program_headers[i].parse():
                print(f"Error: failed to parse ELF program header entry {i}")
                return False

            if self.VERBOSE:
                print(f"{TEXT_BOLD}{TEXT_UNDERLINE}Program header entry #{i + 1}:{TEXT_END}\n")
                self.program_headers[i].dump_values()


        return True
