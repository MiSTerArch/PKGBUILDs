# Installation Instructions

## Using the prebuilt image

From time to time I automatically build a complete SD card
image, that image can be easily updated to latest once it's booted.

You can download it from https://github.com/MiSTerArch/binaries/releases/latest.
After unpacking you can just dd it to an sd card, or perhaps use your favorite
[etcher](https://www.balena.io/etcher/) like tool if you're afraid of
erasing your hard drive.

```bash
wget https://github.com/MiSTerArch/binaries/releases/latest/download/MiSTerArch.img.tar.gz
tar xf MiSTerArch.img.tar.gz
dd if=MiSTerArch.img of=/dev/mmcblk0 bs=1M status=progress
sync
```

Plug the SD card in the DE10 board and after a couple of minutes mister-bin
should be showing on the HDMI.

You can complete the setup (including expanding to fill the whole SD
card) by running `finish_misterarch_install.sh` either via SSH or via
the Scripts/ menu in the GUI (press ESC). At the end it will provide a
suggestion on how to fill your [/media/fat](https://github.com/MiSTerArch/PKGBUILDs/blob/main/README.md#mediafat)
directory.

After running `finish_misterarch_install.sh` you should reboot as there's
probably updates you want to reload.
You should do this **nicely** from the console using `sudo reboot`,
either via SSH or from the menu by pressing F6, not just by power cycling.

SSH is enabled by default. Login with username: `alarm`, password: `alarm`.
Root is accessible with sudo.

### "Preferences" the prebuilt image comes with

Besides the MiSTer stuff, here are some differences from vanilla Arch Linux ARM:

* python
* base-devel
* networkmanager, use `nmtui` to configure it
* btrfs, `root/` as a subvolume allows easy snapshotting in the future
* pikaur [AUR](https://wiki.archlinux.org/title/Arch_User_Repository) helper

## From Scratch

If you want to get a more custom experience, you can start from scratch:

### Building

All of these PKGBUILDs can be built using x86 arch:

```
linux-mister$ CROSS_COMPILE='/usr/local/x-tools7h/arm-unknown-linux-gnueabihf/bin/' ARCH='arm' CARCH="armv7h" makepkg -s
```

The kernels and other heavy compiling ones require a cross compiler. I recommend
x-tools7h from the [Arch Linux ARM Cross-Compiling instructions](https://archlinuxarm.org/wiki/Distcc_Cross-Compiling).

Some (uboot) might need a specialized cross-compiler, but the PKGBUILD
should grab it automatically into the local `src/` folder.

### Installing

You need an SD card, create a empty msdos table, then partition it:

* `/boot`, fat32 (type b), 500ish MB
* u-boot-with-spl, [partition type](https://unix.stackexchange.com/questions/508890/how-to-change-partition-type-id-without-formatting) `a2`, 3MB
* rootfs and any other partitions you want. These can all be `ext4` or
  even `btrfs`.

You need to grab a generic
[ArchLinuxARM-armv7-latest.tar.gz](http://fl.us.mirror.archlinuxarm.org/os/ArchLinuxARM-armv7-latest.tar.gz)
and unpack it into the rootfs.

You need to manually grab the contents of the `uboot-mister` (all files) and `linux-mister` (only what is in /boot)
[packages](https://github.com/MiSTerArch/binaries/tree/binaries/repo) and put them
properly in the `/boot` partition.

`dd if=/boot/uboot.img` into the 3MB partition. This is what the de10 board looks
for in order to start the bootloader.

Edit `/boot/linux/u-boot.txt` to change the kernel cmdline if your root
partition is not `/dev/mmcblk0p3`. You probably want to do this if you want
your rootfs to be on a USB HD, or even NFS.

At this point you can boot. You must check the USB console if you're not sure
of what it's doing.

Login with username: `alarm`, password: `alarm`. You can change this password,
or create another user if you want. The openssh server starts at first boot as
well, it will also generate its own server keys, to maintain privacy. `su -`
will give you root access after entering the password `root`. Installing
[sudo](https://wiki.archlinux.org/title/Sudo) is recommended to make
this process easier.

Configure your `/etc/fstab` to include the `/boot` partition
([genfstab](https://man.archlinux.org/man/genfstab.8) might help here).
This is **important** even if it looks like your mister works without it,
otherwise any kernel updates will not be applied properly:

```
LABEL=BOOT /boot vfat rw,relatime,fmask=0022,dmask=0022,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro 0 2
```

Before installing any packages you will need to initialize arch's package manager:

```
pacman-key --init && pacman-key --populate archlinuxarm
```

Upstream x86 Arch also has quite a detailed article for [general recommendations after installation](https://wiki.archlinux.org/title/General_recommendations).
Some tips in there might be useful even for a MisterArch setup.

### MisterArch repository setup

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

You want to use the `--overwrite "/boot/*"` argument as well for this first
package install to ignore conflicts with the manually placed files in /boot from
the earlier steps.

In the future all it would take is an invocation of `pacman -Syu` to get both
arch linux and mister updates (for the stuff this project has packaged).

Make sure you follow the `systemctl enable MiSTer` tip printed during the
mister-bin installation and then ponder on how to fill your [/media/fat](https://github.com/MiSTerArch/PKGBUILDs/blob/main/README.md#mediafat)
directory.
