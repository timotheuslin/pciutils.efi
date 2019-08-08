# Makefile for The PCI Utilities for the UDK/EDK2 porting.

# (c) 2019 Timothy Lin <timothy.gh.lin@gmail.com>, BSD 3-Clause License.

PYTHON_COMMAND  =   python

all: python_v
	$(PYTHON_COMMAND) pug.py -p PciUtilsPkg/PciUtilsPkg.dsc

clean: python_v
	$(PYTHON_COMMAND) pug.py -p PciUtilsPkg/PciUtilsPkg.dsc clean

cleanall: python_v
	$(PYTHON_COMMAND) pug.py -p PciUtilsPkg/PciUtilsPkg.dsc cleanall

python_v:
	$(PYTHON_COMMAND) --version
