//
// UDK's IO functions.
//
// Timothy Lin 2019, BSD 3-Clause License.
//

#pragma once

#include <Library/IoLib.h>

#define inb(x) IoRead8(x)
#define inw(x) IoRead16(x)
#define inl(x) IoRead32(x)

#define outb(x,y) IoWrite8(y, x)
#define outw(x,y) IoWrite16(y, x)
#define outl(x,y) IoWrite32(y, x)

static inline int ioperm(int x, int y, int z) {return 0;}

//BUGBUG: A crude ugly smelly patch.
#undef stderr
#define stderr stdout
