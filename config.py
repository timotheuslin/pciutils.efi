# Configuration file for PUG.
#
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, line-too-long
#
# (c) 2019 Timothy Lin <timothy.gh.lin@gmail.com>, BSD 3-Clause License.
#

"""
TODO:
1. automate the LibraryClasses content of the existing INF using info from:
     1.1 their static_library_files.lst, and
     1.2 their $(BASE_NAME).map - 'Linker script and memory map'
2. automate the global/local (fixed) PCD settings from the -y/-Y build log.
"""

__all__ = ['WORKSPACE', 'CODETREE', 'PLATFORM', 'TARGET_TXT', 'COMPONENTS']

import os
import sys


DEFAULT_WORKSPACE_DIR = os.getcwd()
DEFAULT_UDK_DIR = os.path.join(os.path.expanduser('~'), '.cache', 'pug', 'edk2')
DEFAULT_MSVC_TAG = 'VS2012x86'

# Basic global settings for all the workspace.
# Any relative-path is relative to the current-working-dir.
WORKSPACE = {
    'path'              : os.environ.get('WORKSPACE', DEFAULT_WORKSPACE_DIR),
    'output_directory'  : os.path.join('Build', 'Pug'),
    'platform_name'     : 'Pug',
    'target_arch'       : 'X64',            # 'IA32', 'X64', 'IA32 X64'
    'tool_chain_tag'    : DEFAULT_MSVC_TAG if (os.name == 'nt') else 'XCODE5' if (sys.platform == 'darwin') else 'GCC5',
    'target'            : 'RELEASE',        # 'DEBUG', 'NOOPT', 'RELEASE', 'RELEASE DEBUG'
    'log_type'          : 'PCD',            # 'PCD', 'LIBRARY', 'FLASH', 'DEPEX', 'HASH', 'BUILD_FLAGS', 'FIXED_ADDRESS'
}
WORKSPACE.update({
    'conf_path'         : os.environ.get('CONF_PATH', os.path.join(WORKSPACE['output_directory'], 'Conf')),
    # [TODO] disable logging due to the failure of report-log under Windows.
    #'report_log'        : '' if os.name == 'nt' else WORKSPACE['output_directory'] + '/build_report.log'
})


# Code tree layout for those remote repositories.
# The relative-paths are relative to the current-working-dir.
CODETREE = {
    'edk2'              : {
        'path'          : DEFAULT_UDK_DIR,
        'source'        : {
            'url'       : 'https://github.com/tianocore/edk2.git',
            'signature' : 'edk2-stable201903',
        },
        'multiworkspace': True
    }
}
CODETREE['edk2']['path'] = os.path.join(CODETREE['edk2']['path'], CODETREE['edk2']['source']['signature'])

CODETREE.update({
    'openssl'           : {
        'path'          : os.path.join(CODETREE['edk2']['path'], 'CryptoPkg', 'Library', 'OpensslLib', 'openssl'),
        'source'        : {
            'url'       : 'https://github.com/openssl/openssl.git',
            'signature' : 'OpenSSL_1_1_0j',
        },
    },
})
CODETREE.update({
    'PciUtils'    : {
        'path'          : os.path.join(os.getcwd(), 'PciUtilsPkg', 'pciutils'),
        'source'        : {
            'url'       : 'https://github.com/pciutils/pciutils.git',
            'signature' : 'v3.6.2',
        },
        #'multiworkspace': True
    }
})

#
# PLATFORM DSC's content.
# The relative-paths are relative to entries in {$(WORKSPACE), $(PACKAGES_PATH)}
PLATFORM = {}


# Conf/target.txt
# Ref. BaseTools/Conf/target.template
# The relative-paths are relative to entries in {$(WORKSPACE), $(PACKAGES_PATH)}
TARGET_TXT = {
    'path'              : os.path.join(WORKSPACE['conf_path'], 'target.txt'),
    'update'            : True,
    'TOOL_CHAIN_CONF'   : 'tools_def.txt',
    'BUILD_RULE_CONF'   : 'build_rule.txt',
    #'ACTIVE_PLATFORM'   : PLATFORM['path'],
    'TARGET'            : WORKSPACE['target'],
    'TARGET_ARCH'       : WORKSPACE['target_arch'],
    'TOOL_CHAIN_TAG'    : WORKSPACE['tool_chain_tag']
}


COMPONENTS = []
