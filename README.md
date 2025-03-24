# MarkAI

This project focuses on controlling smart home based iot devices over serial communication along with performing customizable hid commands 

An advanced version of my previous project, Offering a sleek and modern ui using customTkinter with added custom widgets

##### Referenced libraries 

-WhisperAI by OpenAi for speech to text model

-torch in order to run Whisper on cuda for significantly faster transcriptions

-pyserial to Communicate devices over Serial Ports

### Configuration files

**configuration.json** : An easily readable and modifiable file to predefine the hid and robot functions and necessary starting configurations of the  python file

**themes/** : Folder containing  various configurations of different themes defined for customtkinter (Credit: CTkThemesPack)
## Class Description:

###### Data_sharing: 
**whisper_data** (maxsize=1)

**comm_port_send**  *to send commands over serial port*

**comm_port** 


###### WhisperAI: 
Captures real time audio for 3 seconds from the system mic and converts it to text. The model used here is *medium* , which requires atleast 6gb vram to run efficiently.

*The converted text is stored in the queue **whisper_data***

*runs as a separate thread  **t1** in order to only consume memory when required* 

###### SerialComm:
SerialCommunication

*Runs as a different Thread **t3***

- connect : To try to connect to the selected port -- *updates comm_port value to "Connected" if the connection is established else throws an error*
- read_Serial : Reads the data of the Serial Device at a specific baud rate
- send_message : Takes the data as parameter and sends it to the serial device
- disconnect : disconnects the library resource 

###### Icon:
HomuChan_icon : Responsible for the app tile icon and the default image upon opening (Windows Specific)

###### Buttons:
ButtonFrame

- clickable_buttons : Contains 5 clickable buttons which can be used for any defined purpose
- slider : Contains a slider which can be used for any Display or Set value

###### Display:
DialogBox:

- output_box : Creates a widget TextBox to diplay whatever WhisperAI  is transcribing
- text_whisper : Continuously updates the output_box based on the text recieved from whisper_data (*Runs as a different Thread **t2***)
- Serial_Box : Creates a widget TextBox to display the output over Serial Communication 
- text_serial : Continuosly updates the Serial_Box based on the text recieved by serial port
- Serial_enter : Creates a separate widget TextBox to get the user input to send it to device
- clear_text : To clear all the texts of the output_box
- clear_text_1 : To clear all the texts of the Serial_Box
- get_text : Maybe used to fetch texts of output_box
-robot_display : To display the commands  

###### TrySelf:

***The main class to call different files and their classes and pass their respective frames on where to place them***

Contains different frames to place different widgets

This project is made keeping in mind to be completely customizable by the end user by some minor tweaks

### Basic Info:

***This project uses Whisper AI model ("small") which on real time StT model consumes Memory of around***

***Default Baud Rate for communication is 115200 which can be changed under function 'port_select' in the class DropDownMenu***

### Currently Working On:

* To be able to communicate to devices over WiFi communications
* To perform Robot functions on computer
* To also use LLM TtT models to understand basic speech and perform respective operations
* To add more custom themes

Looking forward for positive reviews for my work

*you can reach out to me at anshuldevacc@gmail.com*


