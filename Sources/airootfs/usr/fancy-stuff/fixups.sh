#!/bin/bash
# OmegaLinux NEXT Fixup script that runs before finishing calamares installation, hopefully i can do better after release.
# 15 February 2026

# Populate arch keyrings, without this the average user wouldnt be able to even use OLN at all.
pacman-key --init
pacman-key --populate archlinux
pacman -Sy

# We do the new fancy ahh sounding omegalinux sound, and since we cant change sound scheme on LXDE we js gonna do this shit.
# And honestly i wanted to 
rm -rf /usr/share/sounds/freedesktop/stereo/dialog-warning.oga
cp -rf /usr/fancy-stuff/dialog-warning.ogg /usr/share/sounds/freedesktop/stereo/