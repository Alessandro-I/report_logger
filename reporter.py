# External libraries
from os import makedirs
from time import strftime
from os.path import exists
from logging import getLogger, Formatter, FileHandler, DEBUG, INFO

if not exists('log'):
    makedirs('log')

INFO = INFO
reporter = getLogger('')

# Handle initialization
__fmt_string = '%(asctime)s.%(msecs)03d -- %(levelname)s -- %(funcName)s in %(module)s: %(message)s'
__date_fmt = '%Y-%m-%d %H:%M:%S'
__formatter = Formatter(__fmt_string, datefmt=__date_fmt)

__handler = FileHandler('log/' + strftime("%Y-%m-%d_") + 'program_report.log')
__handler.setFormatter(__formatter)

# Logger initialization
reporter.setLevel(DEBUG)
reporter.addHandler(__handler)
