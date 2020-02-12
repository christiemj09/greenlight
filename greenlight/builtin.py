"""
Various conditions to wait for.
"""

import os
import subprocess


def pg_isready(host):
    res = subprocess.run(['pg_isready', '-h', host])
    return res.returncode
