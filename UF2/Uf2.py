from Constants.Constants import *
from UF2.Constants.Uf2Constants import *
from UF2.Uf2Block import Uf2Block

class Uf2:
    def __init__(self, output_path: str, flags: int, target_addr: int, payload_size: int, family_id: int = None) -> None:
        self.OUTPUT_PATH = output_path
        self.FLAGS = flags
        self.TARGET_ADDR = target_addr
        self.PAYLOAD_SIZE = payload_size
        self.FAMILY_ID = family_id

        self.blocks = []

    def populate_blocks(self, data: bytes) -> bool:
        # TODO: chunk data into self.PAYLOAD_SIZE bytes for each block

        data_size = len(data)
        if data_size > BLOCK_DATA_SIZE:
            print(f"Error: data size of {data_size} bytes exceeds maximum of {BLOCK_DATA_SIZE} bytes")
            return False

        self.blocks += [Uf2Block(self.FLAGS, self.TARGET_ADDR, len(self.blocks), self.FAMILY_ID, data)]

    def write_blocks(self) -> bool:
        total_num_blocks = len(self.blocks)

        with open(self.OUTPUT_PATH, 'wb') as uf2_file:
            for i in range(0, total_num_blocks):
                self.blocks[i].set_num_blocks(total_num_blocks)
                self.blocks[i].write(uf2_file)
