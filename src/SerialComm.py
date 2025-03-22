import serial
import threading
from Display import DialogBox
from Data_sharing import comm_port
from data_json import ConfigJSON


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
            self.thread = threading.Thread(target=self.read_serial, daemon=True)
            self.thread.start()
            
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
                        print(f"\nData Received: {data}")
                        DialogBox.text_serial(data)
                        if data.startswith("Temperature"): ConfigJSON.update_value("robot.comm.Temperature",data.rsplit(' ',1)[-1])

                except Exception as e:
                    print(f"Error while reading serial data: {e}")

    def send_message(self, message):
        if self.ser and self.ser.is_open:
            self.ser.write(message.encode() + b'\n')
            print(f"Message Sent: {message}")

    def disconnect(self):
        self.running = False
        if self.thread:
            self.thread.join()
        if self.ser:
            self.ser.close()
            print("Serial communication successfully closed.")
