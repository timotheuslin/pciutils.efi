// alloca() is said to be more agile than malloc() for smaller data block allocation.
// But the supported platforms are rare.

// (c) 2019 Timothy Lin <timothy.gh.lin@gmail.com>, BSD 3-Clause License.

#pragma once

#define alloca(x) malloc(x)

//BUGBUG: A crude ugly smelly patch.
#undef stderr
#define stderr stdout