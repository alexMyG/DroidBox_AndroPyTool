#!/bin/sh

emulator -avd $1 -system images/system.img -ramdisk images/ramdisk.img -wipe-data -prop dalvik.vm.execution-mode=int:portable -no-audio -no-window -memory 2000 &
