// A hard-coded config file for the UDK porting.

// (c) 2019 Timothy Lin <timothy.gh.lin@gmail.com>, BSD 3-Clause License.

#pragma once

#include <X64/machine/int_fmtio.h>

#define PCI_IDS "pci.ids"
#define PCI_OS_GNU
#define PCILIB_VERSION "3.13.0"
#define PCI_PATH_IDS_DIR "."
#define PCI_HAVE_STDINT_H
#define PCI_HAVE_PM_INTEL_CONF
#define PCI_HAVE_64BIT_ADDRESS

//BUGBUG: A crude ugly smelly patch.
#undef stderr
#define stderr stdout

