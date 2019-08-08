//
// A hardcoded config file for the UDK porting.
//
// Timothy Lin 2019, BSD 3-Clause License.
//

#pragma once

#include <X64/machine/int_fmtio.h>
#pragma GCC diagnostic ignored "-Wparentheses"

#define PCI_IDS "pci.ids"
#define PCI_OS_GNU
#define PCILIB_VERSION "3.6.2"
#define PCI_PATH_IDS_DIR "."
#define PCI_HAVE_STDINT_H
#define PCI_HAVE_PM_INTEL_CONF

//BUGBUG: A crude ugly smelly patch.
#undef stderr
#define stderr stdout

