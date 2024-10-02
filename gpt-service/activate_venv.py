import os
import subprocess
import sys

venv_path = os.path.join('.venv', 'Scripts', 'activate')

if os.name == 'nt':
    activate_command = f'{venv_path}.bat'

subprocess.call(activate_command, shell=True)
