#!/bin/bash
# OmegaLinux NEXT Fixup script that runs before finishing calamares installation, hopefully i can do better after release.
# 15 February 2026

# Fix xscreensaver lock bug where the user cant unlock, with an authentication fail error.
rm -rf /etc/pam.d/xscreensaver
cp -rf /usr/fancy-stuff/xsc/xscreensaver /etc/pam.d/

# Populate arch keyrings, without this the average user wouldnt be able to even use OLN at all.
pacman-key --init
pacman-key --populate archlinux
pacman -Sy

# We do the new fancy ahh sounding omegalinux sound, and since we cant change sound scheme on LXDE we js gonna do this shit.
# And honestly i wanted to 
rm -rf /usr/share/sounds/freedesktop/stereo/dialog-warning.oga
cp -rf /usr/fancy-stuff/dialog-warning.ogg /usr/share/sounds/freedesktop/stereo/

# Now we do this shit: we change the logout banner on the installed environment but that means the ugly ass-looking lxde banner on the live env is still there, fck
# rm -rf /usr/share/lxde/images/logout-banner.png
# cp -rf /usr/fancy-stuff/logout-banner.png /usr/share/lxde/images/