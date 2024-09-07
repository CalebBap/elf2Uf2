#!/usr/bin/env python3

from ELF.Elf import Elf
import argparse
import errno
import os
import sys

def default_output_path(input_path: str) -> str:
    file_name = os.path.splitext(input_path)[0]
    file_name = os.path.basename(file_name)
    output_path = os.path.join(os.getcwd(), file_name + ".uf2")
    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="elf2Uf2", description="Generate a UF2 image from an ELF file")
    parser.add_argument("input", nargs=1, type=str, help="The ELF file from which to generate the UF2 image")
    parser.add_argument("-o", "--output", nargs='?', type=str, help="The file path to write the generated UF2 image to")
    parser.add_argument("-v", "--verbose", action='store_true', help="Print verbose output")
    args = parser.parse_args()

    INPUT_PATH = os.path.abspath(args.input[0])
    if not os.path.isfile(INPUT_PATH):
        print(f"Error: invalid input path {INPUT_PATH}")
        sys.exit(errno.EINVAL)

    if args.output is not None:
        OUTPUT_PATH = os.path.abspath(args.output)
    else:
        OUTPUT_PATH = default_output_path(INPUT_PATH)

    VERBOSE = args.verbose

    elf = Elf(INPUT_PATH, VERBOSE)
    if not elf.parse():
        print(f"Failed to parse ELF file")
        sys.exit(errno.EINVAL)
