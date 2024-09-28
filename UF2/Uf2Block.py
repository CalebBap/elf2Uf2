from UF2.Constants.Uf2Constants import *
from Utilities.Utilities import *
from typing import BinaryIO

class Uf2Block:
    def __init__(self, flags: int, target_addr: int, block_no: int, family_id: int, data: bytes) -> None:
        self.MAGIC_START_0 = 0x0A324655
        self.MAGIC_START_1 = 0x9E5D5157
        self.FLAGS = flags
        self.TARGET_ADDR = target_addr
        self.PAYLOAD_SIZE = len(data)
        self.BLOCK_NO = block_no
        self.NUM_BLOCKS = None
        self.FILE_SIZE = family_id if family_id is not None else 0
        self.DATA = zero_pad_data(data, BLOCK_DATA_SIZE)
        self.MAGIC_END = 0x0AB16F30

    def set_num_blocks(self, num_blocks: int) -> None:
        self.NUM_BLOCKS = num_blocks

    def write(self, file: BinaryIO) -> bool:
        if (self.NUM_BLOCKS == None):
            print("Error: total number of blocks is not set")
            return False

        fields = [
            self.MAGIC_START_0,
            self.MAGIC_START_1,
            self.FLAGS,
            self.TARGET_ADDR,
            self.PAYLOAD_SIZE,
            self.BLOCK_NO,
            self.NUM_BLOCKS,
            self.FILE_SIZE,
            self.DATA,
            self.MAGIC_END
        ]

        data = b''
        for field in fields:
            if isinstance(field, bytes):
                data += field
            elif isinstance(field, int):
                data += field.to_bytes(BLOCK_FIELD_SIZE, 'little')
            else:
                print(f"Unhandled field type - {type(field)}")

        if len(data) != BLOCK_SIZE:
            print(f"Error: invalid block size - {len(data)} bytes")
            return False

        if file.write(data) != BLOCK_SIZE:
            print(f"Error: failed to write UF2 block data")
            return False

        return True
