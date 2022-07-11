import threading
import time
from io import StringIO, BytesIO
import queue
import sys
from modem.protocol.xmodem import XMODEM
from modem.protocol.ymodem import YMODEM

class FakeIO(object):
    def __init__(self):
        self.streams = [queue.Queue(), queue.Queue()]

    def putc(self, data, q=0):
        for char in data:
            self.streams[1-q].put(char)
            print('p%d(0x%x)' % (q, char)),
        return len(data)

    def getc(self, size, q=0):
        data = bytearray()
        while size:
            try:
                char = self.streams[q].get()
                print('r%d(0x%x)' % (q, char)),
                data.append(char)
                size -= 1
            except queue.Empty:
                return None
        return data

class Client(threading.Thread):
    def __init__(self, io, filename):
        threading.Thread.__init__(self)
        self.io     = io
        self.filename=filename
        self.stream = open(filename, 'rb')

    def getc(self, data, timeout=0):
        return self.io.getc(data, 0)

    def putc(self, data, timeout=0):
        return self.io.putc(data, 0)

    def run(self):
        self.xmodem = YMODEM(self.getc, self.putc)
        print('c.send', self.xmodem.send(self.filename))

class Server(threading.Thread):
    def __init__(self, io):
        threading.Thread.__init__(self)
        self.io     = io
        self.stream = BytesIO()

    def getc(self, data, timeout=0):
        return self.io.getc(data, 1)

    def putc(self, data, timeout=0):
        return self.io.putc(data, 1)

    def run(self):
        self.xmodem = YMODEM(self.getc, self.putc)
        print('s.recv', self.xmodem.recv('./ymodem_recv'))
        print('got')
        print(self.stream.getvalue())

if __name__ == '__main__':
    i = FakeIO()
    s = Server(i)
    c = Client(i, sys.argv[1])
    s.start()
    c.start()

