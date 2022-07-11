import serial
from modem import YMODEM

if __name__=='__main__':
    ser= serial.Serial('COM20', baudrate=19600)

    def getc(size, timeout=0):
        ser.read(size)


    def putc(data, timeout=0):
        ser.write(data)
        ser.flushOutput()
    

    ymodem = YMODEM(getc, putc)
    ymodem.send('*.img')
