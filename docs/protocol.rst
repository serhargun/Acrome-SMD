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


1.4. Operation Mode
~~~~~~~~~
Users can select the preferred operation mode of the Actuator between the modes listed below.

 * Position Control Mode (Default)
 * Velocity Control Mode
 * Torque Control Mode
 
#. Position Control Mode: When this operation mode is selected, the Actuator will perform its movement according to position control mode parameters. Users can configure the Actuator to move to a specific position with this configuration. To configure this operation mode, the user should set the Operation Mode register to 0x00.

#. Velocity Control Mode: When this operation mode is selected, the Actuator will perform its movement according to velocity control mode parameters. Users can configure the Actuator to move continuously at desired velocity with this configuration. To configure this operation mode, the user should set the Operation Mode register to 0x01.

#. Torque Control Mode: When this operation mode is selected, the Actuator will perform its movement according to torque control mode parameters. Users can configure the Actuator to move with constant torque. To configure this operation mode, the user should set the Operation Mode register to 0x02.

1.5. Temperature Limit
~~~~~~~~~
Users can configure the Actuator board’s upper temperature limit to a certain value. This register represents the temperature value in Celsius degrees and is configurable between 0 to 255.

1.6. Torque Enable
~~~~~~~~~
This register controls the motor driver output. User should write 1 to enable motor driver output and 0 to disable.

1.7. Autotuner Enable
~~~~~~~~~
This register controls the start to autotuner . User should write 1 to enable autotuner  and user can select autotuner methods.

1.8. Minimum Voltage Limit
~~~~~~~~~
When the input voltage of the Actuator is lower than this register’s value, motor driver output of the Actuator will be disabled. The user can configure this value according to its own needs. This register can have values between 0-65535 and represents voltage limit in millivolts.

1.9. Maximum Voltage Limit
~~~~~~~~~
When the input voltage of the Actuator is higher than this register’s value, motor driver output of the Actuator will be disabled. The user can configure this value according to its own needs. This register can have values between 0-65535 and represents voltage limit in millivolts

1.10. Torque Limit Index
~~~~~~~~~
	When the absolute current flowing through the motor is higher than this value, motor driver output will be disabled. The user can configure this value according to its own needs. This register can have values between 0-65535 and represent current flowing through the motor in milliamps. This register is independent from the operation mode and always will be checked in any operation mode.

1.11. Velocity Limit Index
~~~~~~~~~
When the absolute velocity of the motor is higher than this value, motor output will be disabled. The user can configure this value according to its own needs. This register can have values between 0-65535 and represents velocity as encoder ticks per 100ms. This register is independent from the operation mode and always will be checked in any operation mode.

1.12. Autotuner Methods
~~~~~~~~~
Users can select the preferred Autotuner method of the Actuator between the methods  listed below.
* Ziegler Nichols
* Cohen Coon
""! Torque and autotuner must be enabled  before choosing a method.""

**Ziegler Nichols Method**
 When this Autotuner method  is selected, the Actuator will tune control  parameters according to the Ziegler Nichols method. To configure this Autotuner method , the user should set the Autotuner method register to 0x02.

**Cohen Coon**
 When this Autotuner method  is selected, the Actuator will tune control  parameters according to the Cohen Coon  method. To configure this Autotuner method , the user should set the Autotuner method register to 0x03.
 
1.13. Position Control Feed Forward
~~~~~~~~~
This register represents the feed forward parameter of the PID algorithm that is used for position control.

1.14. Velocity Control Feed Forward
~~~~~~~~~
This register represents the feed forward parameter of the PID algorithm that is used for velocity control.

1.15. Torque Control Feed Forward
~~~~~~~~~
This register represents the feed forward parameter of the PID algorithm that is used for torque control.

1.16. Position Control Scaler Gain
~~~~~~~~~
This register represents the scaler gain parameter of the PID algorithm that is used for position control.

1.17. Position Control P Gain
~~~~~~~~~
This register represents the kp parameter of the PID algorithm that is used for position control.

1.18. Position Control I Gain
~~~~~~~~~
This register represents the ki parameter of the PID algorithm that is used for position control.

1.19. Position Control D Gain
~~~~~~~~~
This register represents the kd parameter of the PID algorithm that is used for position control.

1.20. Velocity Control Scaler Gain
~~~~~~~~~
This register represents the scaler gain parameter of the PID algorithm that is used for velocity control.

1.21. Velocity Control P Gain
~~~~~~~~~
This register represents the kp parameter of the PID algorithm that is used for velocity control.

1.22. Velocity Control I Gain
~~~~~~~~~
This register represents the ki parameter of the PID algorithm that is used for velocity control.

1.23. Velocity Control D Gain
~~~~~~~~~
This register represents the kd parameter of the PID algorithm that is used for velocity control.

1.24. Torque Control Scaler Gain
~~~~~~~~~
This register represents the scaler gain parameter of the PID algorithm that is used for torque control.

1.25. Torque Control P Gain
~~~~~~~~~
This register represents the kp parameter of the PID algorithm that is used for torque control.

1.26. Torque Control I Gain
~~~~~~~~~
This register represents the ki parameter of the PID algorithm that is used for torque control.

1.27. Torque Control D Gain
~~~~~~~~~
This register represents the kd parameter of the PID algorithm that is used for torque control.
