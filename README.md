# OmegaLinux NEXT - An attempt of rebasing OmegaLinux from lubuntu to Arch Linux.

# Why?
Canonical is doing some ugly ahh looking stuff to Ubuntu that makes customizing their isos more complicated, and also ugly stuff to ubuntu in general.

# And why arch?
First i actually thought of rebasing it in vanilla Debian, but i came to the conclusion that it would be a 1:1 copy of other distros like Loc-OS, and i didnt want that, so i choose arch, not only because of that, but because it is rolling release meaning that users would always get the latest features of the Linux kernel and apps and other stuff in general. Another reason of why i choosed Arch, is because of archiso, which this may be controversial, but its actually easier to cook an ISO than ubuntu, since on ubuntu i had to do everything manually and that took some days or even weeks.

# Any release date?
Now. Download prebuilt iso at https://github.com/omega-linux/page/releases/tag/deepbluesea1

# What will happen to lubuntu-based OmegaLinux?
Well, if this goes actually well, it would mostly replace regular OmegaLinux which is based on ubuntu, meaning that 2.x and 3.x would be the last ubuntu based omegalinux versions with support, that will end along of EOL dates of ubuntu 22.04 and 24.04, and there would be no OmegaLinux based on 26.04.

# How to build?
If you want to make your own build, first of all you need an Arch Linux environment (kinda obvious since this is built with archiso)

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
