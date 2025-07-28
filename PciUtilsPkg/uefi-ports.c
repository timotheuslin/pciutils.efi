


#include <PiDxe.h>
#include <Protocol/PciIo.h>
#include <Library/DebugLib.h>
#include <Library/BaseMemoryLib.h>
#include <Library/UefiBootServicesTableLib.h>
#include <Library/MemoryAllocationLib.h>
#include <Library/BaseLib.h>
#include <Library/UefiLib.h>
#include <Library/PrintLib.h>
#include "internal.h"
#include <string.h>


static void
conf12_init(struct pci_access *a)
{
}

static void
conf12_cleanup(struct pci_access *a)
{
}

/*
 *	Configuration type 1
 */

static int
conf12_detect(struct pci_access *a)
{

  return 1;
}

static int
conf12_read(struct pci_dev *d, int pos, byte *buf, int len)
{
  int res = 1;
  EFI_STATUS                         Status;
  EFI_PCI_IO_PROTOCOL                *PciIo;

  PciIo = (EFI_PCI_IO_PROTOCOL*)d->backend_data;
  Status = PciIo->Pci.Read (
                      PciIo,
                      EfiPciIoWidthUint8,
                      pos,
                      len,
                      buf
                      );
  if (EFI_ERROR (Status)) {
    d->access->error("PciIo Read Error %r", Status);
    res = 0;
  }
  return res;
}

static int
conf12_write(struct pci_dev *d, int pos, byte *buf, int len)
{
  int res = 1;
  EFI_STATUS                         Status;
  EFI_PCI_IO_PROTOCOL                *PciIo;

  PciIo = (EFI_PCI_IO_PROTOCOL*)d->backend_data;
  Status = PciIo->Pci.Read (
                      PciIo,
                      EfiPciIoWidthUint8,
                      pos,
                      len,
                      buf
                      );
  if (EFI_ERROR (Status)) {
    d->access->error("PciIo Write Error %r", Status);
    res = 0;
  }
  return res;
}

/*
 *	use UEFI PciIo protocol to access PCI configuration space. maybe bridge io protocol also works
 */

void
pci_uefi_scan(struct pci_access *a)
{
  struct pci_dev *d;
  EFI_STATUS                         Status;
  UINTN                              Index;
  UINTN                              HandleCount;
  EFI_HANDLE                         *HandleBuffer;
  EFI_PCI_IO_PROTOCOL                *PciIo;
  UINTN                              Segment;
  UINTN                              Bus;
  UINTN                              Device;
  UINTN                              Function;

  HandleCount     = 0;
  HandleBuffer    = NULL;

  Status = gBS->LocateHandleBuffer (
                  ByProtocol,
                  &gEfiPciIoProtocolGuid,
                  NULL,
                  &HandleCount,
                  &HandleBuffer
                  );
  a->debug("..PciIo HandleCount %d\n", HandleCount);
  //
  // Traverse all PCI I/O Protocol instances, and record the protocol
  // instances, together with their segment numbers and bus ranges.
  //
  for (Index = 0; Index < HandleCount; Index++) {
    Status = gBS->HandleProtocol (
                    HandleBuffer[Index],
                    &gEfiPciIoProtocolGuid,
                    (VOID **)&PciIo
                    );
    if (EFI_ERROR (Status)) {
      continue;
    }

    PciIo->GetLocation (PciIo, &Segment, &Bus, &Device, &Function);
    a->debug(".Scan Pci %x|%x|%x|%x\n", Segment, Bus, Device, Function);

    d = pci_alloc_dev(a);
    d->domain = Segment;
    d->bus = Bus;
    d->dev = Device;
    d->func = Function;
    d->known_fields = PCI_FILL_IDENT;
    d->backend_data = (VOID*)PciIo;
    conf12_read (d, PCI_VENDOR_ID, (UINT8*)&d->vendor_id, 2);
    conf12_read (d, PCI_DEVICE_ID, (UINT8*)&d->device_id, 2);
    conf12_read (d, PCI_HEADER_TYPE, (UINT8*)&d->hdrtype, 1);
    d->hdrtype &= 0x7F;
	  pci_link_dev(a, d);
  }

  if (HandleBuffer != NULL)
    FreePool (HandleBuffer);

}
/*
  fake methods for testing
*/
struct pci_methods pm_intel_conf1 = {
  .name = "intel-conf1",
  .help = "Raw I/O port access using UEFI PciIo protocol interface",
  .detect = conf12_detect,
  .init = conf12_init,
  .cleanup = conf12_cleanup,
  .scan = pci_uefi_scan,
  .fill_info = pci_generic_fill_info,
  .read = conf12_read,
  .write = conf12_write,
};

struct pci_methods pm_intel_conf2 = {
  .name = "intel-conf2",
  .help = "Raw I/O port access using UEFI PciIo protocol interface",
  .detect = conf12_detect,
  .init = conf12_init,
  .cleanup = conf12_cleanup,
  .scan = pci_uefi_scan,
  .fill_info = pci_generic_fill_info,
  .read = conf12_read,
  .write = conf12_write,
};
