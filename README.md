# modbus_spec
modbus spec and related slave/master free software

# free master modbus software
Tester.exe
It's a free software which provided by Schneider Electric

qModMaster-Win64-exe-0.5.3-beta.zip
It's a free software which implemented by Qt.
But it's little big than others.

modpoll-3.10.zip
It's a command line toosl which can poll the modbus message from slave.

# free slave modbus software
diagslave-3.4.zip
It's a command line tools to mock as a slave, but seems not powerful than ModRSsim2.

ModRSsim2_V8.21.2.7.exe
You can download from https://sourceforge.net/projects/modrssim2/
It have GUI to configure the register value

# example

Before run the code, please make sure there are two serial port which connected each other.
You can simulator the serial port with Free Virtual Serial Ports in Windows or
You can simulator the serial port with socat 
https://freevirtualserialports.com/
https://stackoverflow.com/questions/52187/virtual-serial-port-for-linux

the example code used two python package: minimalmodbus, pyserial

example/modbus1 direcotry have the simple python code example for communicate with serial
example/modbus2 direcotry have the simple python code example for communicate with serial, the data encode with modbus

# modbus for Omron's E5CN heat contoller
Recently, we are working on the Omron's E5CN heat contoller.
I want to some place for it.
1. it don't have free software to configure and test it
2. we must use CX Thermo to set it, but it need to buy(250 USD~)


