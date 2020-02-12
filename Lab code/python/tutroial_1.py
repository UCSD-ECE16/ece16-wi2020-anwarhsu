import serial
import numpy as np

string_buffer = []
data_array = np.array([])

def setup_serial():
    serial_name = 'COM5'
    ser = serial.Serial(serial_name, 9600)  # open serial port
    print(ser.name)         # check which port was really used
    return ser

def send_serial(ser):

    S_List = ['Hello',' World','!','\n']


    for S in S_List:
        ser.write(S.encode('utf-8'))
        

def read_serial1(ser):
    s = ser.read(30).decode('utf-8')     # read 30 bytes and decode it
    print(s)

def readSerial2(ser):
    n=0
    while (n<30):
        s = ser.read(1).decode('utf-8')     # read 1 byte and decode it
        print(s)
        n=n+1
        
def readSerial3(ser):
    n=0
    full_string = []
    while (n<30):
        s = ser.read(1).decode('utf-8')     # read 1 byte and decode it
        full_string.append(s)
        n=n+1
    print(full_string)

def readSerial4(ser):
    
    while True:
        try:
            s = ser.read(1)         # read 1 byte and decode to utf-8
            print(s)
        except(KeyboardInterrupt):
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break

def receive_data(ser):
    # Send start data
    while True:
        try:
            receive_sample(ser)
        except(KeyboardInterrupt):
            # Send stop data 
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break
    # Send stop data 

def receive_sample(ser):
    global string_buffer
    global data_array

    s = ser.read(1).decode('utf-8')# read a byte from serial (remember to decode)
    if( s == '\n'):
        data_string = ''.join(string_buffer) #JOIN buffer 
        print(data_string)
        temp_data_array = np.fromstring(data_string, dtype = int, sep = ',')#string to np array
        if(data_array.size == 0): 
            data_array = temp_data_array
        else:
            data_array = np.vstack((data_array,temp_data_array))#vstack temp_data_array to end of data_array
        string_buffer = [] # reset string_buffer to []
    else:
        string_buffer.append(s) # append the new char to string_buffer



def main():
    ser = setup_serial()
    data_array = receive_data(ser)
    print(data_array)
    ser.close()

if __name__== "__main__":
    main()




