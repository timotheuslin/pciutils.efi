@echo off
del /f /s /q Build\PciUtilsPkg\
del /f /s /q Build\PciUtilsPkg\DEBUG_VS2019\X64\PciUtilsPkg
call edksetup.bat
@REM call build -p PciUtilsPkg\PciUtilsPkg.dsc -t VS2019 -a X64 -m PciUtilsPkg\lspci.inf -s -n 72 -D HAVE_GETOPT
call build -p PciUtilsPkg\PciUtilsPkg.dsc -t VS2019 -a X64 -m PciUtilsPkg\lspci.inf -s -n 72
