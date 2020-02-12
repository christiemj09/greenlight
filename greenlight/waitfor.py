"""
Use an app-specific wait function to poll for a condition.
"""

import importlib
import os
import sys
import time


def console_script():
    script, module_path, wait_function_name, *args = sys.argv
    module = importlib.import_module(module_path)
    wait_function = getattr(module, wait_function_name)
    GREENLIGHT_WAIT_TIME = int(os.environ['GREENLIGHT_WAIT_TIME'])
    GREENLIGHT_MAX_WAITS = int(os.environ['GREENLIGHT_MAX_WAITS'])
    for attempt in range(GREENLIGHT_MAX_WAITS):
        return_code = wait_function(*args)
        if return_code == 0:
            break
        time.sleep(GREENLIGHT_WAIT_TIME)
