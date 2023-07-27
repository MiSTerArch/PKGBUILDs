CROSS_COMPILE ?= /usr/local/x-tools7h/arm-unknown-linux-gnueabihf/bin/
PKGDEST ?= $(realpath .)/../binaries/repo/

.PHONY: %.pkg
%.pkg: %/PKGBUILD
	cd $*; CROSS_COMPILE=${CROSS_COMPILE} PKGDEST=${PKGDEST} ARCH='arm' CARCH="armv7h" makepkg -s
# BUG: linux-mister package fails with this invocation

.PRECIOUS: %/aur
%/aur:
	git clone ssh://aur@aur.archlinux.org/$*.git $*/aur

.PHONY: %.update_aur
%.update_aur: %/PKGBUILD %/aur
	# delete everything that was there before
	-cd $*/aur; git rm -rf .; rm -Rf *

	# add all new files
	cp $(shell git ls-files $*) $*/aur

	# SRCINFO is needed for the AUR
	cd $*/aur; makepkg --printsrcinfo > .SRCINFO

	# Include global gitignore
	cat .gitignore > $*/aur/.gitignore

	# generate original.commit file
	echo >$*/aur/original.commit "This is an automatically generated copy of the package, originally from https://github.com/MiSTerArch/PKGBUILDs:"
	git log -n1 $* >> $*/aur/original.commit

	# add and commit
	cd $*/aur; git add .
	cd $*/aur; git commit -m "make $*.update_aur"

.PHONY: clean
clean:
	-rm -Rf */{pkg,src}
	-rm -Rf */*pkg.tar*
