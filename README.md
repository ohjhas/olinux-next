# OmegaLinux NEXT - rebasing OmegaLinux from lubuntu to Arch Linux.
These are the sources to build a working OmegaLinux NEXT image

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
