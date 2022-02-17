import abc
from datetime import datetime

class WriteFile:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return

    def __init__(self, filename):
        self.filename = filename

    def write_line(self, text):
        fh = open(self.filename, 'a')
        fh.write(text + '\n')
        fh.close()

class DelimFile(WriteFile):
    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim

    def write(self, this_list):
        line = self.delim.join(this_list)
        self.write_line(line)

class LogFile(WriteFile):
    def write(self, this_line):
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M')
        self.write_line('{0}     {1}'.format(date_str, this_line))

log = LogFile('log.txt')
c = DelimFile('text.csv', ',')
log.write('this is a log message')
log.write('this is another log message')

c.write(['a','b','c','d','e'])
c.write(['1','2','3','4','5'])
