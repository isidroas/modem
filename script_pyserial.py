import serial
from modem import YMODEM

if __name__=='__main__':
    ser= serial.Serial('COM20', baudrate=19600, timeout=20)

    def getc(size, timeout=0):
        read= ser.read(size)
        print('[main.getc] read=0x'+ read.hex().upper(), flush=True)
        print('[main.getc] in_waiting='+ str(ser.in_waiting), flush=True)
        return read


    def putc(data, timeout=0):
        ser.write(data)
        ser.flushOutput()
        print('[main.putc] write=0x'+ data.hex().upper(), flush=True)
        return len(data)
    

    ymodem = YMODEM(getc, putc)
    ymodem.send('*.img')
