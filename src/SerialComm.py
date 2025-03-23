import serial
import threading
from Display import DialogBox
from Data_sharing import comm_port,comm_port_send
from data_json import ConfigJSON
import time


class SerialCommunication:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.running = False
        self.thread = None

    def connect(self):
        
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
            self.running = True
            DialogBox.text_serial("Now Connected!")
            comm_port.put("connected")
            self.threadGet = threading.Thread(target=self.read_serial, daemon=True)
            self.threadGet.start()

            self.threadSend = threading.Thread(target=self.send_message, daemon=True)
            self.threadSend.start()
            
        except serial.SerialException as e:
            error = f"Error: Unable to open serial port {self.port} - {e}"
            DialogBox.text_serial(error)
            print(error)

    def read_serial(self):
        while self.running:
            if self.ser and self.ser.in_waiting:
                try:
                    data = self.ser.readline().decode().strip()
                    if data:
                        ###example to get the Temperature from Serial Device
                        print(f"\nData Received: {data}")
                        DialogBox.text_serial(data)
                        if data.startswith("Temperature"):
                            from Buttons import button_widget
                            temp=data.rsplit(' ',1)[-1]
                            button_widget.Temperature(temp)
                            ConfigJSON.update_value("robot.comm.Temperature",temp)

                    print(f"\nData Received: {data}")
                    DialogBox.text_serial(data)
                except Exception as e:
                    print(f"Error while reading serial data: {e}")

    def send_message(self):

        while self.running:            
        
            if self.ser and self.ser.is_open and not comm_port_send.empty():
                
                message=comm_port_send.get()
                self.ser.write(message.encode() + b'\n')
                time.sleep(.8)
                print(f"Message Sent: {message}")

    def disconnect(self):
        self.running = False
        if self.thread:
            self.thread.join()
        if self.ser:
            self.ser.close()
            print("Serial communication successfully closed.")
