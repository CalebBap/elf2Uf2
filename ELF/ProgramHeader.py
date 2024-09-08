from Parser.Parser import *

class ElfProgramHeader:
    def __init__(self, input_path: str, size: int, offset: int):
        self.INPUT_PATH = input_path
        self.SIZE = size
        self.OFFSET = offset
        self.p_type = None
        self.p_flags = None
        self.p_offset = None
        self.p_vaddr = None
        self.p_paddr = None
        self.p_filesz = None
        self.p_memsz = None
        self.p_flags = None
        self.p_align = None

    def dump_values(self) -> str:
        dump_values("Program Header values", [])

    def parse(self) -> bool:
        with open(self.INPUT_PATH, 'rb') as elf_file:
            elf_file.seek(self.OFFSET)

            return True
