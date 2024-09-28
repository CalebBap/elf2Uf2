#!/usr/bin/env python3

from Constants.Constants import *
from ELF.Elf import Elf
from UF2.Constants import Uf2Constants
from UF2.Uf2 import Uf2
from argparse import ArgumentParser, Namespace
import errno
import os
import sys

def default_output_path(input_path: str) -> str:
    file_name = os.path.splitext(input_path)[0]
    file_name = os.path.basename(file_name)
    output_path = os.path.join(os.getcwd(), file_name + ".uf2")
    return output_path

def get_input_path(args: Namespace) -> str:
    INPUT_PATH = os.path.abspath(args.input[0])

    if not os.path.isfile(INPUT_PATH):
        print(f"Error: invalid input path {INPUT_PATH}")
        sys.exit(errno.EINVAL)

    return INPUT_PATH

def get_output_path(args: Namespace) -> str:
    if args.output is not None:
        return os.path.abspath(args.output)

    return default_output_path(INPUT_PATH)

def get_family_id(args: Namespace) -> int | None:
    if args.family_id is None:
        return None

    try:
        family_id = int(args.family_id, 16)
    except ValueError:
        print(f"Board family ID {args.family_id} is an invalid hexadecimal string")
        sys.exit(errno.EINVAL)

    if family_id > Uf2Constants.BLOCK_FIELD_MAX_VALUE:
        print(f"Board family ID {args.family_id} is larger than {Uf2Constants.BLOCK_FIELD_SIZE} bytes")
        sys.exit(errno.EINVAL)

    return family_id

def get_flags(family_id: int | None) -> int:
    flags = Uf2Constants.Uf2Flags.NONE.value

    if family_id is not None:
        flags |= Uf2Constants.Uf2Flags.FAMILY_ID_PRESENT

    return flags

def get_data(elf: Elf) -> bytes:
    # TODO: implement
    return b''

if __name__ == "__main__":
    parser = ArgumentParser(prog="elf2Uf2", description="Generate a UF2 image from an ELF file")
    parser.add_argument("input", nargs=1, type=str, help="The ELF file from which to generate the UF2 image")
    parser.add_argument("-o", "--output", nargs='?', type=str, help="The file path to write the generated UF2 image to")
    parser.add_argument("-v", "--verbose", action='store_true', help="Print verbose output")
    parser.add_argument("--family-id", type=str, required=False, help="A board family ID specified as a hexadecimal string")
    parser.add_argument("--payload-size", nargs='?', type=int, default=256, help="Number of data bytes to use per UF2 block")
    args = parser.parse_args()

    VERBOSE = args.verbose
    INPUT_PATH = get_input_path(args)
    OUTPUT_PATH = get_output_path(args)
    FAMILY_ID = get_family_id(args)
    FLAGS = get_flags(FAMILY_ID)
    PAYLOAD_SIZE = args.payload_size

    elf = Elf(INPUT_PATH)
    if VERBOSE:
        elf.dump_values()

    DATA = get_data(elf)
    TARGET_ADDR = elf.entry_point()

    uf2 = Uf2(OUTPUT_PATH, FLAGS, TARGET_ADDR, PAYLOAD_SIZE)
    uf2.populate_blocks(DATA)
    uf2.write_blocks()
