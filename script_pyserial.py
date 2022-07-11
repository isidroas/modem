import serial
from modem import YMODEM

if __name__=='__main__':
    ser= serial.Serial('/dev/pts/8')

    def getc(size, timeout=0):
        ser.read(size)


    def putc(data, timeout=0):
        ser.write(data)
        ser.flushOutput()
    

    ymodem = YMODEM(getc, putc)
    ymodem.send('/etc/issue')
