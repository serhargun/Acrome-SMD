1. Registers
---------

1.1. Device ID
~~~~~~~~~

The user can change the ID of an Actuator by writing to this register. The Actuator boards will not check the bus for duplicate ID addresses so the user should be careful about duplicate IDs on the bus. This register can have values between 0 to 254. 0xFF is reserved for broadcast commands.

Users must reset the Torque Enable register to change device ID. If the Actuator receives a command to change this value while the Torque Enable register is set, the command will be discarded, and no changes will be made. 

1.2. Baud Rate
~~~~~~~~~

The user can select a baud rate between 1527 to 6250000 to communicate with the Actuator boards on the bus. Each actuator should be configured to use the selected baud rate before-hand. The default baud rate is 115200.

**Users must reset the Torque Enable register to change baud rate. If the Actuator receives a command to change this value while the Torque Enable register is set, the command will be discarded, and no changes will be made.** 
**Users should prioritize selecting **well known baud rates** when configuring this register. If an **arbitrary baud rate** is to be used, users must ensure that their device can provide necessary baud rates. Even then, the arbitrary selections may exceed the acceptable discrepancy percentage the UART peripheral can handle.**

1.3. Status
~~~~~~~~~

This register holds the error flags of the Actuator and should be used for clearing any errors. (See: Error clear command)
    
* Input Voltage Error: This error bit will be set when the input voltage of the Actuator is higher than maximum input voltage or lower than minimum input voltage registers. These registers are configurable by the user. While this flag is set, the Actuator will keep its torque output disabled.

* Overheat Error: This error bit will be set when the temperature of the Actuator board is higher than the temperature limit register. This register is configurable by the user. While this flag is set, the Actuator will keep its torque output disabled.

* Overload Error: This error bit will be set when the flowing current on the motor driver is higher than the torque limit register. This register is configurable by the user. While this flag is set, the Actuator will keep its torque output disabled.

* Encoder Error: This error bit will be set when the Actuator fails to gather any encoder information for a period of time while applying power to the motor. While this flag is set, the Actuator will keep its torque output disabled.

* Communication Error: This error bit will be set when the Actuator receives a faulty package. This flag does not affect any operations of the Actuator and was added for informative purposes only.

* Flash Error: This error bit will be set when the Actuator fails to read from or write to EEPROM. When this flag is set, the user should check parameters for any misconfiguration first. If the Actuator fails to read from EEPROM, it will start with factory default parameters.

Please refer to the table below for read/write operations on this register.


