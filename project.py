#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, line-too-long
#
# (c) 2019-2020 Timothy Lin <timothy.gh.lin@gmail.com>, BSD 3-Clause License.
#

"""
This is the project configuration file as well the starter script for iPug.
"""

import os


# These UDK tag source trees have been build-tested:
DEFAULT_EDK2_TAG = 'edk2-stable202008'
#DEFAULT_EDK2_TAG = 'edk2-stable201911'


CODETREE = {
    # edk2-libc is a new edk2 repo since edk2-stable201905. StdLib resides in this repo.
    'edk2-libc'    : {
        #'path'          : os.path.join(os.path.expanduser('~'), '.cache', 'pug', 'edk2-libc'),
        'path'          : os.path.join(os.getcwd(), 'edk2-libc'),
        'source'        : {
            'url'       : 'https://github.com/tianocore/edk2-libc.git',
            #'signature' : '6168716',   # 61687168fe02ac4d933a36c9145fdd242ac424d1 @ Apr/25/2019
        },
        'multiworkspace': True,
        'patch'         : 'git apply --directory=edk2-libc edk2-libc.patch',
    },
    'PciUtils'      : {
        'path'          : os.path.join(os.getcwd(), 'PciUtilsPkg', 'pciutils'),
        'source'        : {
            'url'       : 'https://github.com/pciutils/pciutils.git',
            'signature' : 'v3.7.0',
        },
    }
}

DEFAULT_ACTIVE_PLATFORM = 'PciUtilsPkg/PciUtilsPkg.dsc'

###################################################################################################


if __name__ == '__main__':
    import sys
    sys.dont_write_bytecode = True      # To inhibit the creation of .pyc file

    import runpy
    runpy.run_module('ipug')

