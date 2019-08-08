pciutils.efi
===
pciutils.efi is a UDK/EDK2 porting of the GNU's [pciutils](https://github.com/pciutils/pciutils) for the handy PCI tools: `lspci` and `setpci` using [PUG](https://github.com/timotheuslin/PugPkg).

## Prerequisites:
1. Python 2.7.10+ or Python 3.7.0+
2. git 2.17.0+

## Generic prerequisites for the UDK porting:
0. Reference:
    - [Getting Started with EDK II](https://github.com/tianocore/tianocore.github.io/wiki/Getting%20Started%20with%20EDK%20II) 
    - [Xcode](https://github.com/tianocore/tianocore.github.io/wiki/Xcode)
1. nasm (2.0 or above)
2. iasl (version 2018xxxx or later)
3. MSVC(Windows) or Xcode(Mac) or GCC(Open-source Posix)
4. build-essential uuid-dev (Posix)
5. pip2 install future (Python 2.7.x)
6. motc (Xcode)

## Tool installation for any Debian-Based Linux:
 `$ sudo apt update ; sudo apt install nasm iasl build-essential uuid-dev`

## Usage: 
0. Change-directory to folder **pciutils.efi** .
1. (Optional) Edit `config.py` for the settings accordingly in: WORKSPACE, TARGET_TXT.
2. (Optional) Edit `CODETREE` in `config.py` to specify where to place the downloaded source files of the UDK git repo or any other additional respos.
4. To build the code, run `make` (Linux) or `nmake` (Windows) or `python pug.py -p PciUtilsPkg/PciUtilsPkg.dsc` <br>
    For the 1st time setup, `pug.py` would automatically try to git-clone:
    - the [UDK code tree](https://github.com/tianocore/edk2)
    - the openssl repo
    - the [pciutils source](https://github.com/pciutils/pciutils)
5. Browse to folder **Build/PciUtilsPkg** for the build results.
6. Browse to folder **Build/Pug/Conf** for CONF_PATH setting files.
7. Run `{make, nmake, "python pug.py -p PciUtilsPkg/PciUtilsPkg.dsc"} {clean, cleanall}` to clean (all) the intermediate files.

## Known issues:
1. Only Linux (Debian & Arch) and Windows build are tested. Xcode is not covered yet.
2. "pci.ids" database is not working yet.
3. The double/triple/quadruple command with {'x', 'm', 'v' ...} may not work correctly.
4. UDK with Python3 has build-dependency issue which causes slow re-building. Python2 is still recommended before its enf-of-life.

## Tech notes:
1. The full [UDK code tree](https://github.com/tianocore/edk2) is git-cloned-checked-out to:
    - Windows: %USERPROFILE%/.cache/pug/edk2
    - Linux:  $HOME/.cache/pug/edk2
2. On Windows, the default MSVC tool chain tag is vs2012x86. The following command should be run first in the command console:
    - "C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x86
3. **pciutils.efi**, as the current working directory, is assigned as the "WORKSPACE" directory. **PACKAGES_PATH a.k.a. MULTIPLE-WORKSPACE** is used here to implicitly reference other standard packages outside the current working directory tree.


## Have Fun!
