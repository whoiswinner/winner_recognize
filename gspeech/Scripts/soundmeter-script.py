#!C:\Users\tpgns\PycharmProjects\gspeech\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'soundmeter==0.1.5','console_scripts','soundmeter'
__requires__ = 'soundmeter==0.1.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('soundmeter==0.1.5', 'console_scripts', 'soundmeter')()
    )
