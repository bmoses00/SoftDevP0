#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/SoftDevP0/")
sys.path.insert(0,"/var/www/SoftDevP0/SoftDevP0/")

import logging
logging.basicConfig(stream=sys.stderr)

from SoftDevP0 import app as application
