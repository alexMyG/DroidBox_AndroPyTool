import sys, signal
import subprocess
import time
import os
from os.path import isfile, join, isdir
from os import listdir
#from termcolor import colored
from scripts import droidbox
import argparse
from argparse import RawTextHelpFormatter

# current_directory = os.path.dirname(os.path.realpath(__file__))

# os.chdir(current_directory)


deviceId = "droidbox-emulator"

strace_analysis = True



can_break = False


def sigint_handler(signal, frame):
    global can_break
    can_break = True
    print 'Interrupted'
    subprocess.Popen(["./killAllEmulators.sh"])
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)


def main():
    parser = argparse.ArgumentParser(
        description="Welcome to AndroPyTool\n\n" +
                    '[!] You must provide the source directory where apks are contained. ',
        formatter_class=RawTextHelpFormatter)

    parser.add_argument('-s', '--source', help='Source directory for APKs', required=True)

    parser.add_argument('-d', '--duration', help='DroidBox analysis duration', required=True)

    parser.add_argument('-o', '--output', help='Output directory for results', required=True)

    parser.add_argument('-g', '--gui', help='GUI Mode: True or False', required=True)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    analyze_with_droidbox(args.source, args.duration, args.output, args.gui)


def analyze_with_droidbox(apks_folders, duration, output_directory, gui):
    current_directory = os.path.dirname(os.path.realpath(__file__))

    os.chdir(current_directory)

    print "Killing current active emulators..."
    subprocess.Popen(["./killAllEmulators.sh"])

    # output_directory = "logs_outputs_" + filter(None, apks_folders.split("/"))[-1] + "/"

    apks_folders += "/"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    list_folders = [f for f in listdir(apks_folders) if isdir(join(apks_folders, f))]

    print "NUM APKS FOUND: " + str(len(list_folders))

    # apk_list = [f for f in listdir(apks_folders) if isfile(join(apks_folders, f)) and f.endswith(".apk")]

    apk_list = []
    for path, subdirs, files in os.walk(apks_folders):
        for name in files:
            if name.endswith(".apk"):
                apk_list.append(os.path.join(path, name))

    count = 0
    for apk_name in apk_list:
        count += 1
        completed_percentage = "{0:.2f}".format((float(count) / float(len(apk_list)))*100.0)
        print "\n##########################"
        print str(completed_percentage) + "% NEW APK: " + apk_name
        print "##########################"

        apk_id = apk_name.split("/")[-1]

        log_file_name = "logcat_" + apk_id.replace(".apk", ".txt")
        json_file_name = "analysis_" + apk_id.replace(".apk", ".json")

        if isfile(join(output_directory, log_file_name)) or isfile(join(output_directory, json_file_name)):
            print "EXISTS: " + output_directory + log_file_name
            print "!! APK already analysed: " + apk_name
            continue

        file_output_log = open(output_directory + log_file_name, "w")
        file_output_json = open(output_directory + json_file_name, "w")

        print "\nStarting emulator "
        p = None
        if not gui:
            #print colored('STARTING ' + ' EMULATOR IN NON GUI MODE...', 'green')
            print 'STARTING ' + ' EMULATOR IN NON GUI MODE...'

            subprocess.Popen(["./startemuNoGUI.sh", deviceId])

            print "ADB DEVICE RUNNING "

        else:
            # print colored('STARTING ' + ' EMULATOR IN GUI MODE...', 'green')
            print 'STARTING ' + ' EMULATOR IN GUI MODE...'
            subprocess.Popen(["./startemu.sh", deviceId])

        print "subprocess called"

        p = subprocess.Popen(["adb", "shell", "getprop", "sys.boot_completed"], stdout=subprocess.PIPE)
        output = p.stdout.read()

        print "Waiting until boot is completed"

        while(1):
            if output.startswith("1"):
                break
            else:
                print "Boot not completed"
                time.sleep(1)
            p = subprocess.Popen(["adb", "shell", "getprop", "sys.boot_completed"], stdout=subprocess.PIPE)
            output = p.stdout.read()

        print "Boot completed !"

        print "Calling droidbox..."
        output_log, output_json = droidbox.execute_droidbox(["", apk_name, duration], logs_directory=output_directory)

        file_output_log.write(output_log)
        file_output_log.close()

        file_output_json.write(output_json)
        file_output_json.close()

        subprocess.Popen(["adb", "-s", "emulator-5554", "emu", "kill"])

        print "-----------------"
        print "-----------------"
        print "-----------------"
        print "-----------------\n\n"


if __name__ == '__main__':
    main()
