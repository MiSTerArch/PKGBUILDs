# Installation Instructions

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
[packages](https://github.com/MiSTerArch/binaries/tree/binaries/repo) and put them
properly in the `/boot` partition.

`dd if=/boot/uboot.img` into the 3MB partition. This is what the de10 board looks
for in order to start the bootloader.

Edit `/boot/linux/u-boot.txt` to change the kernel cmdline if your root
partition is not `/dev/mmcblk0p3`. You probably want to do this if you want
your rootfs to be on a USB HD, or even NFS.

At this point you can boot. You can check the USB console if you're not sure
of what it's doing.

Login with username: `alarm`, password: `alarm`. You can change this password,
or create another user if you want. The openssh server starts at first boot as
well, it will also generate its own server keys, to maintain privacy.

Configure your `/etc/fstab` to include the `/boot` partition
([genfstab](https://man.archlinux.org/man/genfstab.8) might help here).
This is **important** even if it looks like your mister works without it,
otherwise any kernel updates will not be applied properly:

```
LABEL=BOOT /boot vfat rw,relatime,fmask=0022,dmask=0022,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro 0 2
```

## Repository setup

Add another paragraph to `/etc/pacman.conf`:

```
[misterarch]
SigLevel = Optional TrustedOnly
Server = http://misterarch.hypertriangle.com/repo
```

At this point you can install the mister packages provided by this project:

```
pacman -Syu uboot-mister linux-mister mister-bin mister-menu
```

You want to use the `--overwrite "/boot/*"` argument as well for the first
pacman invocation to not conflict with the manually placed files in /boot from
the earlier steps.

In the future all it would take is an invocation of `pacman -Syu` to get both
arch linux and mister updates (for the stuff this project has packaged).
