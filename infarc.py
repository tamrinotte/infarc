#!/usr/bin/python3

from argparse import ArgumentParser
from os import makedirs, path
from shutil import copytree, make_archive, ignore_patterns, rmtree, unpack_archive
from pathlib import Path
from logging import basicConfig, DEBUG, debug, disable, CRITICAL

# Doing the basic configuration for the debugging feature
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Disabling the debugging feature. Comment out the line to enable debugging.
disable(CRITICAL)

# FUNCTIONS
def compress(source_path, destionation_path, compression_type, skip_hidden_files):
    """A function that compresses files"""
    
    # Check if source path is not exists
    if not path.exists(source_path):

        print('Source path does not exist.')

        return

    # Check if compress type if "zip and destination path is not exists or check if compression type is tar and destination path is not exists
    if (compression_type == "zip" and not path.exists(f'{destionation_path}.zip')) or (compression_type == "tar" and not path.exists(f'{destionation_path}.tar')):

        if skip_hidden_files:

            tDP = str(Path(f'{destionation_path}_tmp'))

            copytree(source_path, tDP, ignore=ignore_patterns('.*'))

            make_archive(destionation_path, compression_type, tDP)

            rmtree(tDP)

        else:

            make_archive(destionation_path, compression_type, source_path)
        
        print(f'Compressed folder is available in {destionation_path}.{compression_type}')

    else:

        print('Destination path already exists.')


def extract(source_path, destionation_path):
    """A function that extracts files from compressed folders"""

    if not path.exists(source_path):

        print('Source path does not exist.')

        return

    if not path.exists(destionation_path):

        makedirs(destionation_path)

        unpack_archive(source_path, destionation_path)

        print(f'Extracted files are available in {destionation_path}')

    else:

        print('Destination path already exists.')


def main():
    """The function which runs the entire program"""

    # Create an argument parser
    parser = ArgumentParser(description="A command line tool to compress and/or extract files or folders.")

    # Add arguments
    parser.add_argument("-c", "--compress", action="store_true", help="Compress")

    parser.add_argument("-e", "--extract", action="store_true", help="Extract from a compressed folder")

    parser.add_argument("-t", "--tar", action="store_true", help="Set the compression type to tar")

    parser.add_argument("-z", "--zip", action="store_true", help="Set the compression type to zip")

    parser.add_argument("-s", "--skip-hidden", action="store_true", help="Ignore hidden files and folders")

    parser.add_argument("source_path", help="Source directory path")

    parser.add_argument("destination_path", help="Destination directory path")

    # Parse arguments
    args = parser.parse_args()

    # Check if user is trying to use the compress feature
    if args.compress:

        compression_type = 'tar' if args.tar else 'zip'

        compress(args.source_path, args.destination_path, compression_type, args.skip_hidden)

    # Check if user is trying to use the extract feature
    elif args.extract:

        extract(args.source_path, args.destination_path)

    # Check if user is using neither compress nor extract feature of this application
    else:

        print("Invalid usage. Use -h or --help to get more information.")

# Evaluate if the source is being run on its own or being imported somewhere else. With this conditional in place, your code can not be imported somewhere else.
if __name__ == '__main__':
    main()
