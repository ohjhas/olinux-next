# OmegaLinux NEXT - An attempt of rebasing OmegaLinux from lubuntu to Arch Linux.

# Why?
Canonical is doing some ugly ahh looking stuff to Ubuntu that makes customizing their isos more complicated, and also ugly stuff to ubuntu in general.

# And why arch?
First i actually thought of rebasing it in vanilla Debian, but i came to the conclusion that it would be a 1:1 copy of other distros like Loc-OS, and i didnt want that, so i choose arch, not only because of that, but because it is rolling release meaning that users would always get the latest features of the Linux kernel and apps and other stuff in general. Another reason of why i choosed Arch, is because of archiso, which this may be controversial, but its actually easier to cook an ISO than ubuntu, since on ubuntu i had to do everything manually and that took some days or even weeks.

# Any release date?
Hmm, not at all, if this project succeeds we may see one, because there is some stuff (mostly the installer) that i still have to set up and also some bugs.

# Note for MBR Users
If you want to try this on real hardware and you have MBR, don't. For now MBR is not supported due to calamares misconfigurations, i will try to fix it when releasing the iso

# What will happen to lubuntu-based OmegaLinux?
Well, if this project sees light and gets to a stable state, it would mostly replace regular OmegaLinux which is based on ubuntu, meaning that 2.x and 3.x would be the last ubuntu based omegalinux versions with support, that will end along of EOL dates of ubuntu 22.04 and 24.04, and there would be no OmegaLinux based on 26.04.

# How to build?
If you really wanna test this, first of all you need an Arch Linux environment (kinda obvious since this is built with archiso)

You do this in simple 3 steps

1: Install the archiso package
```
sudo pacman -S archiso
```

2: git clone this repository
```
git clone https://github.com/omega-linux/olinux-next.git
```

3: go to the recently cloned repo directory and run:
```
sudo ./Build.sh
```

Wait until the system builds and the output iso file should be at the "ISOs" directory.
