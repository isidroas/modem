import serial
from modem import YMODEM

if __name__=='__main__':
    ser= serial.Serial('COM20', baudrate=19600, timeout=20)

    def getc(size, timeout=0):
        read= ser.read(size)
        print('[main.getc] read=0x'+ read.hex().upper())


    def putc(data, timeout=0):
        ser.write(data)
        ser.flushOutput()
        print('[main.putc] write=0x'+ data.hex().upper())
        return len(data)
    

    ymodem = YMODEM(getc, putc)
    ymodem.send('*.img')
