import subprocess
import os
import sys

result = subprocess.check_output( ["python", "dev\main.py", "data"] ).decode("UTF-8").strip()
if result == '1274383':
  print('OK')
else:
  print('NG')
