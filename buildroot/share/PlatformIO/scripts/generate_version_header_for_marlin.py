#!/usr/bin/python

import subprocess
subprocess.call("./buildroot/bin/generate_version_header_for_marlin Marlin", shell=True)