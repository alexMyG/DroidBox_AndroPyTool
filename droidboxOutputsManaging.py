import sys
from argparse import RawTextHelpFormatter

import argparse
from os import listdir
import re
import better_exceptions
import os
import shutil
import ntpath
import time
from os.path import join as join_dir

OUTPUT_FOLDER_OLD_FILES = "straceTXT/"


def main():
    parser = argparse.ArgumentParser(
        description="Strace parser",
        formatter_class=RawTextHelpFormatter)

    parser.add_argument('-s', '--source', help='Source directory for droidbox output files', required=True)
    parser.add_argument('-o', '--output', help='Output directory for droidbox analysis files in JSON', required=True)
    parser.add_argument('-str', '--outputStrace', help='Output directory for strace output files converted', required=True)
    parser.add_argument('-other', '--otherFiles', help='Output directory for other files', required=True)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()

    parse_droidbox_outputs(source_folder=args.source,
                           output_droidbox=args.output,
                           output_strace=args.outputStrace,
                           output_other=args.otherFiles)


def parse_droidbox_outputs(source_folder, output_droidbox, output_strace, output_other):
    source_folder = source_folder + "/"

    list_files = []
    for path, subdirs, files in os.walk(source_folder):
        for name in files:
            list_files.append(os.path.join(path, name))


    list_droidbox_files = [f for f in list_files if f.startswith("analysis")]
    list_strace_files = [f for f in list_files if f.startswith("strace")]
    list_logcat_files = [f for f in list_files if f.startswith("logcat")]

    if not os.path.exists(output_droidbox):
        os.makedirs(output_droidbox)

    if not os.path.exists(output_strace):
        os.makedirs(output_strace)

    if not os.path.exists(output_other):
        os.makedirs(output_other)

    # STRACE
    for file in list_strace_files:
        output_file = ntpath.basename(file).replace(".txt", ".csv")
        with open(file, "rb") as f:
            lines = f.readlines()

        with open(join_dir(output_strace, output_file), 'wb') as fp:

            for line in lines:

                line = re.sub(" +", " ", line)
                line = line.split(" ", 2)

                content = {"process_number": line[0], "system_call": line[2]}
                # TIMESTAMP is the key and it includes the process number and the system call

                fp.write(line[1] + "," + line[0] + "," + line[2])

        shutil.move(file, join_dir(output_other, file))

    # Droidbox
    for file in list_droidbox_files:
        output_file = ntpath.basename(file)
        shutil.move(file, join_dir(output_droidbox, output_file))

    # Logcat
    for file in list_logcat_files:
        output_file = ntpath.basename(file)
        shutil.move(file, join_dir(output_other, output_file))


if __name__ == '__main__':
    main()
