# MiSTer + Arch Linux ARM

I found out about [MiSTerFPGA](https://github.com/MiSTer-devel/Main_MiSTer/wiki)
via [LGR's MiSTer Multisystem video](https://www.youtube.com/watch?v=qx45r-BRHxY),
since then I've been enjoying it very much.

One thing I've had difficulties with was the OS. Despite it being designed
to be an appliance, it seems very brittle to store an OS's worth of data
(and precious saved games / hard drive images) on a FAT 32 SD card.
Also, any modifications you make to the OS might be lost come update time.

I want to be able to run Arch on my MiSTer! If you want to do the same
this project is for you.

## Packages

This repository contains the arch packages required to run the MiSTer hardware.
Including MiSTer's official uboot, kernel, binaries and support files
(ex: .rbf files for cores). Ideally all updates will now be done through
pacman, and there should be no need to run MiSTer's update scripts.

## Building

All of these PKGBUILDs can be built using x86 arch:

```
linux-mister$ CROSS_COMPILE='/usr/local/x-tools7h/arm-unknown-linux-gnueabihf/bin/' ARCH='arm' CARCH="armv7h" makepkg -s
```

The kernels and other heavy compiling ones require a cross compiler. I recommend
x-tools7h from the [Arch Linux ARM Cross-Compiling instructions](https://archlinuxarm.org/wiki/Distcc_Cross-Compiling).

Some (uboot) might need a specialized cross-compiler, but the PKGBUILD
should grab it automatically into the local `src/` folder.

## Installing

You need an SD card, format it msdos, then partition it:

* `/boot`, fat32, 500ish MB
* u-boot-with-spl, [partition type](https://unix.stackexchange.com/questions/508890/how-to-change-partition-type-id-without-formatting) `a2`, 3MB
* rootfs and any other partitions you want. These can all be `ext4` or
  even `btrfs`.

You need to grab a generic
[ArchLinuxARM-armv7-latest.tar.gz](http://fl.us.mirror.archlinuxarm.org/os/ArchLinuxARM-armv7-latest.tar.gz)
and unpack it into the rootfs.

You need to manually grab the contents of the `uboot-mister` and `linux-mister`
packages and put them properly in the `/boot` partition.

`dd if=/boot/uboot.img` into the 3MB partition. This is what the de10 board looks
for in order to start the bootloader.

Edit `/boot/linux/u-boot.txt` to change the kernel cmdline if your root
partition is not `/dev/mmcblk0p3`. You probably want to do this if you want
your rootfs to be on a USB HD, or even NFS.

Configure your `/etc/fstab` to include the `/boot` partition
([genfstab](https://man.archlinux.org/man/genfstab.8) might help here):

```
LABEL=BOOT /boot vfat rw,relatime,fmask=0022,dmask=0022,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro 0 2
```

Boot and install the .pkg files properly with `pacman -U`, you might need
`--overwrite "*"` for the files you manually added earlier

TODO: All of these install steps might come soon to an
[ansible script](https://github.com/amstan/alarm-ansible) near you.


## What now?

Now that the MiSTer runs Arch, what more could it do?

* sshfs mounting of remote filesystem, even with
  [systemd automounting](https://wiki.archlinux.org/title/SSHFS#Automounting)
* [btrfs](https://wiki.archlinux.org/title/Btrfs) and
  [btrbk remote snapshot](https://github.com/digint/btrbk) possiblities
* [USB/IP](https://wiki.archlinux.org/title/USB/IP) in case you don't have a
  carrier board yet and forgot to buy an usb otg cable, just ssh in and
  forward your usb device from another computer. This happened to me.
* Repurpose the hardware for other FPGA shenanigans, maybe you want to develop
  your own FPGA stuff but still want to run arch on the resulting system,
  [zangman style](https://github.com/zangman/de10-nano/wiki).
    * Maybe you want to write linux drivers for
    [LiteX IP](https://github.com/enjoy-digital/litex) blocks.
