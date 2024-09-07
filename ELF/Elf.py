from ELF.ElfHeader import ElfHeader

class Elf:
    def __init__(self, input_path: str, verbose: bool) -> None:
        self.elf_header = ElfHeader(input_path)
        self.VERBOSE = verbose

    def parse(self) -> bool:
        if not self.elf_header.parse():
            return False

        if self.VERBOSE:
            self.elf_header.dump_values()

        return True
