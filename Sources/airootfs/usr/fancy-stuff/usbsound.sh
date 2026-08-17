#!/bin/bash

CONNECT_SOUND="/usr/share/sounds/freedesktop/stereo/device-added.ogg"
DISCONNECT_SOUND="/usr/share/sounds/freedesktop/stereo/device-removed.ogg"

play_sound() {
    play "$1"
}

action=""
devtype=""

udevadm monitor --udev --subsystem-match=usb --property | while read -r line; do
    if [ -z "$line" ]; then
        if [ "$devtype" = "usb_device" ]; then
            if [ "$action" = "add" ]; then
                play_sound "$CONNECT_SOUND"
            elif [ "$action" = "remove" ]; then
                play_sound "$DISCONNECT_SOUND"
            fi
        fi
        action=""
        devtype=""
        continue
    fi

    case "$line" in
        ACTION=*) action="${line#ACTION=}" ;;
        DEVTYPE=*) devtype="${line#DEVTYPE=}" ;;
    esac
done
