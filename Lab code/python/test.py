import serial

def setup_serial():
    serial_name = 'COM5'
    ser = serial.Serial(serial_name, 9600)  # open serial port
    print(ser.name)         # check which port was really used
    return ser

def send_serial(ser):
    S_List = ['start',' data']


    for S in S_List:
        ser.write(S.encode('utf-8'))         # write a string

def main():
    ser = setup_serial()
    send_serial(ser)
    ser.close()

if __name__== "__main__":
    main()
