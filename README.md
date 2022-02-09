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
