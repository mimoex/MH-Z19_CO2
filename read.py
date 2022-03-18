import datetime
import serial

if __name__ == '__main__':
	serial_dev='/dev/serial0'

	ser=serial.Serial(serial_dev,baudrate=9600)
	result=ser.write(b"\xff\x01\x86\x00\x00\x00\x00\x00\x79")
	s=ser.read(9)

	if len(s) >=4 and s[0] ==0xff and s[1] == 0x86:
		nowtime=datetime.datetime.now()
		now="{0:%Y-%m-%d %H:%M:%S}".format(nowtime)
		co2=s[2]*256+s[3]
		output=now + ',' + str(co2)
		print(output)
