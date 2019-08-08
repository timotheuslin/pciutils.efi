# Package's DSC file

# (c) 2019 Timothy Lin <timothy.gh.lin@gmail.com>, BSD 3-Clause License.

[Defines]
  BUILD_TARGETS           = DEBUG|RELEASE|NOOPT
  PLATFORM_NAME           = PciUtilsPkg
  PLATFORM_GUID           = 0257038e-b948-11e9-9059-e34e72aeed44
  PLATFORM_VERSION        = 0.1
  SKUID_IDENTIFIER        = DEFAULT
  OUTPUT_DIRECTORY        = Build/PciUtilsPkg
  DSC_SPECIFICATION       = 0x00010006
  SUPPORTED_ARCHITECTURES = IA32|X64|ARM|AARCH64

[LibraryClasses]
  !include StdLib/StdLib.inc
  PciUtilsLib|PciUtilsPkg/PciUtilsLib.inf
  BaseLib|MdePkg/Library/BaseLib/BaseLib.inf
  UefiLib|MdePkg/Library/UefiLib/UefiLib.inf
  HiiLib|MdeModulePkg/Library/UefiHiiLib/UefiHiiLib.inf
  PrintLib|MdePkg/Library/BasePrintLib/BasePrintLib.inf
  PcdLib|MdePkg/Library/BasePcdLibNull/BasePcdLibNull.inf
  DebugLib|MdePkg/Library/BaseDebugLibNull/BaseDebugLibNull.inf
  IoLib|MdePkg/Library/BaseIoLibIntrinsic/BaseIoLibIntrinsic.inf
  UefiRuntimeLib|MdePkg/Library/UefiRuntimeLib/UefiRuntimeLib.inf
  BaseMemoryLib|MdePkg/Library/BaseMemoryLibRepStr/BaseMemoryLibRepStr.inf
  ShellCEntryLib|ShellPkg/Library/UefiShellCEntryLib/UefiShellCEntryLib.inf
  UefiDriverEntryPoint|MdePkg/Library/UefiDriverEntryPoint/UefiDriverEntryPoint.inf
  UefiHiiServicesLib|MdeModulePkg/Library/UefiHiiServicesLib/UefiHiiServicesLib.inf
  MemoryAllocationLib|MdePkg/Library/UefiMemoryAllocationLib/UefiMemoryAllocationLib.inf
  UefiBootServicesTableLib|MdePkg/Library/UefiBootServicesTableLib/UefiBootServicesTableLib.inf
  UefiApplicationEntryPoint|MdePkg/Library/UefiApplicationEntryPoint/UefiApplicationEntryPoint.inf
  UefiRuntimeServicesTableLib|MdePkg/Library/UefiRuntimeServicesTableLib/UefiRuntimeServicesTableLib.inf
  DevicePathLib|MdePkg/Library/UefiDevicePathLibDevicePathProtocol/UefiDevicePathLibDevicePathProtocol.inf

[Components]
  PciUtilsPkg/lspci.inf
  PciUtilsPkg/setpci.inf
  PciUtilsPkg/example.inf

[BuildOptions]
  MSFT:*_*_*_CC_FLAGS   = /wd4244 /wd4267 /wd4098 /wd4115 /wd4706 /wd4245 /wd4305 /wd4701 /wd4703
  GCC:*_*_*_CC_FLAGS    = -Wall -W -Wno-parentheses -Wno-unused-parameter -Wno-type-limits -Wno-implicit-fallthrough -Wno-sign-compare -Wno-extra
