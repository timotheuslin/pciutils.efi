//
// alloca() is said to be more agile than malloc() for smaller data block allocation.
//
// Timothy Lin 2019, BSD 3-Clause License.
//

#pragma once

#define alloca(x) malloc(x)

//BUGBUG: A crude ugly smelly patch.
#undef stderr
#define stderr stdout