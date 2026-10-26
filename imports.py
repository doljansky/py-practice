from lib.stat_file import stat_file
from lib.dump import dump

dump('./moby_01_out.txt', **stat_file('./moby_01.txt'))
