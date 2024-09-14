pciutils.efi
===
**pciutils.efi/PciUtilsPkg** is an EDKII/UEFI porting of the [GNU's pciutils](https://github.com/pciutils/pciutils) for its handy PCI tools: `lspci` and `setpci`<br>

As a full EDKII package, **PciUtilsPkg** can be built with the guides in/from: 
1. [EDK II Build Specification](https://edk2-docs.gitbooks.io/edk-ii-build-specification/) or
2. [Getting Started with EDK II](https://tianocore-docs.github.io/edk2-BuildSpecification/release-1.28/) or
3. [iPug](https://github.com/timotheuslin/ipug)


## Prerequisites:
1. Python 3.10+
2. git 2.44+
3. The EDKII/TianoCore code tree in following tags: edk2-stable{202405, 202408}
4. git-cloned [GNU's pciutils](https://github.com/pciutils/pciutils) to the directory `PciUtilsPkg/pciutils` (if not using iPug)


## Generic prerequisites for the the EDKII/UEFI porting:
1. nasm (2.15.05+)
    - (Windows) add the nasm's folder to the environment variable "PATH" list setting
2. iASL (version 2020xxxx or later, maybe optional)
3. MSVC(Windows) or Xcode(Mac) or GCC(Open-source Posix)
4. build-essential uuid-dev (Posix)
5. ~~motc (Xcode)~~
0. Reference:
    - [Getting Started with EDK II](https://github.com/tianocore/tianocore.github.io/wiki/Getting%20Started%20with%20EDK%20II) 
    - [Xcode](https://github.com/tianocore/tianocore.github.io/wiki/Xcode)


## Tools installation for any Debian-Based Linux:
- `sudo apt update && sudo apt install nasm iasl build-essential uuid-dev`
- When using the latest iPug:
    - `pip install ipug --user --upgrade`


## Known issues:
1. Only Linux/GCC (Debian/Ubuntu/MintLinux & ArchLinux/Manjaro) and Windows/MSVC build are tested. No plan to cover OSX/Xcode.
2. The double/triple/quadruple command with {'x', 'm', 'v' ...} may not work correctly.
3. ~~"pci.ids" database is not working yet.~~ (Many thanks to http://www.lab-z.com/disfopen/)


## Build using iPug (Optional) :
1. `git clone https://github.com/timotheuslin/pciutils.efi.git`
2. Change-directory to folder **pciutils.efi** .
3. (Optional) Edit `CODETREE` in `project.py` to specify where to place the downloaded source files of the EDKII/TianoCore git repo or any other additional respos.
4. To build the code, run `python project.py setup` then `python project.py`. (iPug will then handle all the rest of the tedious works with the EDKII/TianoCore code tree setup and the build process.)
5. Browse to folder **Build/PciUtilsPkg** for the build results.
6. Browse to folder **Build/Conf** for CONF_PATH setting files.
7. Run `python project.py {clean, cleanall}` to clean (all) the intermediate files.
8. The PCI list data base file, `pci.ids` must be copied alone with `lspci.efi`.


## Tech notes with iPug (Optional) :
1. The full [EDKII code tree](https://github.com/tianocore/edk2) is git-cloned-checked-out to:
    - Windows: %USERPROFILE%/.cache/pug/edk2
    - Linux:  $HOME/.cache/pug/edk2
2. On Windows, VS2022 is tested as the default compiler. The following command should be run first in the windows command console:
    - `%comspec% /k "C:\Program Files\Microsoft Visual Studio\2022\Professional\Common7\Tools\VsDevCmd.bat"`
3. **pciutils.efi**, as the current working directory, is assigned as the "WORKSPACE" directory. **[PACKAGES_PATH a.k.a. MULTIPLE-WORKSPACE](https://github.com/tianocore/tianocore.github.io/wiki/Multiple_Workspace)** is used here to implicitly reference other standard packages outside the current working directory tree.
4. For the 1st-time one-shot setup, following code trees are automatically git-cloned:
    - [the EDKII/TianoCore code tree](https://github.com/tianocore/edk2)
        - submodules such as the openssl repo and some other CryptoPkg's submodules, maybe.
    - [the edk2-libc code tree](https://github.com/tianocore/edk2-libc) - The StdLib package.
    - [the GNU pciutils source](https://github.com/pciutils/pciutils)
