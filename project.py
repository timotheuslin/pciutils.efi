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
DEFAULT_EDK2_TAG = 'edk2-stable201911'
#DEFAULT_EDK2_TAG = 'edk2-stable201908'
#DEFAULT_EDK2_TAG = 'edk2-stable201905'

# Change any one of them for customization.
#DEFAULT_GCC_TAG = 'GCC5'
#DEFAULT_UDK_DIR = os.environ.get('UDK_DIR', os.path.join(os.path.expanduser('~'), '.cache', 'pug', 'edk2'))
DEFAULT_MSVC_TAG = os.environ.get('MSVC_TAG', 'VS2017')
#DEFAULT_EDK2_REPO = os.environ.get('EDK2_REPO', 'https://github.com/tianocore/edk2.git')
#DEFAULT_XCODE_TAG = 'XCODE5'
#DEFAULT_TARGET_ARCH = os.environ.get('TARGET_ARCH', 'X64')              # 'IA32', 'X64', 'IA32 X64'
#DEFAULT_BUILD_TARGET = os.environ.get('BUILD_TARGET', 'RELEASE')        # 'DEBUG', 'NOOPT', 'RELEASE', 'RELEASE DEBUG'
#DEFAULT_WORKSPACE_DIR = os.environ.get('WORKSPACE', os.getcwd())
#DEFAULT_PATH_APPEND_SIGNATURE = False

CODETREE = {
    # edk2-libc is a new edk2 repo since edk2-stable201905. StdLib resides in this repo.
    'edk2-libc'    : {
        #'path'          : os.path.join(os.path.expanduser('~'), '.cache', 'pug', 'edk2-libc'),
        'path'          : os.path.join(os.getcwd(), 'edk2-libc'),
        'source'        : {
            'url'       : 'https://github.com/tianocore/edk2-libc.git',
            'signature' : '6168716',   # 61687168fe02ac4d933a36c9145fdd242ac424d1 @ Apr/25/2019
        },
        'multiworkspace': True,
        'patch'         : 'git apply --directory=edk2-libc patch.txt',
    },
    'PciUtils'      : {
        'path'          : os.path.join(os.getcwd(), 'PciUtilsPkg', 'pciutils'),
        'source'        : {
            'url'       : 'https://github.com/pciutils/pciutils.git',
            'signature' : 'v3.6.4',
        },
    }
}


###################################################################################################


if __name__ == '__main__':
    import sys
    import runpy

    sys.dont_write_bytecode = True      # To inhibit the creation of .pyc file
    PKG_DSC = 'PciUtilsPkg/PciUtilsPkg.dsc'
    sys.argv += ['-p', PKG_DSC]
    sys.exit(runpy.run_module('ipug'))
