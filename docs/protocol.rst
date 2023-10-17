SMD Communication Protocol
================================

Acrome Smart Motor Drivers communication protocol employs UART protocol with a multidrop RS-485 configuration at the hardware level. A detailed introduction to the software layer of the protocol is explained below. 

1. Protocol Overview
---------------------------

The SMD communicaton protocol is working on a UART interface at up to 12.5M baud. Each package transmitted from the host device needs to be followed by a delay of minimum 1-byte-long of the selected baud rate at the time. However, a 2-byte-long delay is recommended to tolerate any possible timing issues since UART is an asynchronous communication interface.
	
Each package must have a preliminary information part before data bytes and an MPEG2 CRC32 value at the end of the package. These values are disclosed in Table 1. The whole communication protocol is based on little-endian architecture.


**Note:** If the user wants to broadcast a command to all the slave devices in the communication line, Device ID field should set to 0xFF. When a broadcast massage is transmitted, no reply will be received from any of the SMDs on the bus.

1.1. Command Types
~~~~~~~~~~~~~~~~~~


1.1.1. Ping Command
********************************
When the SMD receives a package with a ping command, it will reply to the user with a ping package. The only difference between two packages is the status register read from the SMD.

1.1.2. Write Command
********************************
When the user wants to change the registers of the SMD, the user should send a package that contains information about the required register pointers and register values with this command. The user should place pointer values and register data in the data field of the package template according to the given example below.


1.1.3. Read Command
********************************
When the user wants to read the registers of the SMD, the user should send a package that contains information about the required register pointers with this command. The user should place pointer values in the data field of the package template according to the given example below.


1.1.4. EEPROM Write Command
********************************
When the user wants to save already-written data to the non-volatile memory of the SMD, should send a package with this command. SMDs do not respond this command. Execution of this command takes about 300ms since writing to flash memory is a relatively slow operation. Keeping torque output disabled is recommended but not mandatory while sending this command.

1.1.5. Reboot Command
********************************
When the user wants to reboot the device, should send a package with this command. The device will be rebooted immediately and all parameters on the RAM will be replaced with the values that stored on the EEPROM.

1.1.6. Hard Reset Command
********************************
When the user wants to replace all parameters with the default ones, should send a package with this command. When this command is sent, SMD is going to reset all parameters to their out-of-factory values, including ones that are saved to the EEPROM.


2. Registers
------------

2.0. Header
~~~~~~~~~~~~~~
All data packages transferred between an SMD and a host (a device with UART capabilities) carries a header value in the first byte of the package which indicates the start of a package. The header value for SMD is chosen to be **0x55**.


2.1. Device ID
~~~~~~~~~~~~~~

Device ID register defines how to address a specific SMD connected to the serial bus. The device ID of an SMD can be changed by writing to this register. The SMD boards will not check the bus for duplicate ID addresses. It is user's responsibility to ensure there are no duplicate IDs if a collision is not desired. This register can have values between 0 to 254. **0xFF** is reserved for broadcast commands.

User should perform an EEPROM Write to save the registered device ID. Otherwise the value will return to default on the next reset. 


2.2. Device Family
~~~~~~~~~~~~~~~~~~

This register indicates which device family the SMD driver belongs to (Red, Blue, Green). This register is used to address differences in different device families. The value is **0xBA** for SMD Red, **0xBB** for SMD Blue and **0xBC** for SMD Green.

2.3. Package Size
~~~~~~~~~~~~~~~~~~
This register holds the size of the package which is transmitted on the serial bus.

2.4. Command
~~~~~~~~~~~~~~~~~~
This register holds the command of the package which is transmitted on the serial bus. SMD will behave according to the command.

2.5. Hardware Version
~~~~~~~~~~~~~~~~~~~~~~~
This register is read only and holds the hardware version of the device. 

2.6. Software Version
~~~~~~~~~~~~~~~~~~~~~~~
This register is read only and holds the software version of the device. 

2.7. Baud Rate
~~~~~~~~~~~~~~~~~~

This register defines the speed which UART peripheral clocks out and samples in serial data. The baud rate can be selected between 3.057 KBits to 12.5MBits to communicate with the SMD drivers on the bus. Each SMD should be configured to use the selected baud rate before-hand. The default baud rate is 115200.

**Users should prioritize selecting well known baud rates when configuring this register. If an arbitrary baud rate is to be used, users must ensure that their device can provide necessary baud rates. Even then, the arbitrary selections may exceed the acceptable discrepancy percentage the UART peripheral can handle.**

2.8. Status
~~~~~~~~~~~~~~~~~~

This register holds the error flags of the SMD driver.
    
* **Position Error:** This error bit will be set when the motor moves past the position limits of the SMD.

* **Torque Error:** This error bit will be set when the current the motor draws exceed the torque limit of the SMD. If this flag is set SMD will disable its torque output.

* **Memory Error:** This error bit will be set if an error occurs during saving to or reading configuration from the EEPROM IC on the driver.

* **Communication Error:** This error bit will be set if protocol initialization is faulty or unexpected events occurs related to peripheral. Faulty packages do not trigger this flag.

* **Hardware Version Error:** This error bit will be set if the reading of the hardware version from the EEPROM IC on the driver.

* **Tuning (NOT AN ERROR):** This is not an error bit. This bit is set when a PID tuning process starts and is cleared after the process ends.

2.9. Operation Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register is can be used to select the preferred operation mode of the SMD between the modes listed below.

 * PWM Control Mode (Default)
 * Position Control Mode 
 * Velocity Control Mode
 * Torque Control Mode


#. **PWM Control Mode:** When this operation mode is selected, the SMD will perform its movement according to the duty cycle parameter. To configure this operation mode, the user should set the Operation Mode register to **0x00**.
 
#. **Position Control Mode:** When this operation mode is selected, the SMD will perform its movement according to position control mode parameters. Users can configure the SMD to move to a specific position with this configuration. To configure this operation mode, the user should set the Operation Mode register to **0x01**.

#. **Velocity Control Mode:** When this operation mode is selected, the SMD will perform its movement according to velocity control mode parameters. Users can configure the SMD to move continuously at desired velocity with this configuration. To configure this operation mode, the user should set the Operation Mode register to **0x02**.

#. **Torque Control Mode:** When this operation mode is selected, the SMD will perform its movement according to torque control mode parameters. Users can configure the SMD to move with constant torque. To configure this operation mode, the user should set the Operation Mode register to **0x03**.

2.10. Torque Enable
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register controls the motor driver output. User should write 1 to enable motor driver output and 0 to disable.

2.11. Motor Output Shaft CPR
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the CPR (counts per revolution) value of the connected motor's output shaft. This register has an effect only when the motor has an encoder. If this register is configured with false value, the tuning algorithm and PID algorithm may produce unpredictable results.

2.12. Motor Output Shaft RPM
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the maximum RPM (revolutions per minute) value of the connected motor's output shaft. This register has an effect only when the motor has an encoder. If this register is configured with false value, the tuning algorithm and PID algorithm may produce unpredictable results.

2.13. User Indicator
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register flashes the RGB LED for 5 seconds on the SMD when set to 1. This register is cleared automatically.  

2.14. Minimum Position Limit
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the minimum position limit a motor can move. If the read position is lower than this register's value motor driver output of the SMD will be disabled. This value can be configured according to user's needs. This register can have values between -2,147,483,648 - 2,147,483,647 and represents position limit in encoder ticks.

2.15. Maximum Position Limit
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the maximum position limit a motor can move. If the read position is higher than this register's value motor driver output of the SMD will be disabled. This value can be configured according to user's needs. This register can have values between -2,147,483,648 - 2,147,483,647 and represents position limit in encoder ticks.

2.16. Torque Limit
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the maximum allowable current flow to the motor. When the absolute current flowing through the motor is higher than this value, motor driver output will be disabled. The user can configure this value according to its own needs. This register can have values between 0-65535 and represent current flowing through the motor in milliamps. This register takes in effect after a non-configurable time delay. This register is independent from the operation mode and always will be checked in any operation mode.

2.17. RESERVED 
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register is depreciated.

2.18. Position Control Feed Forward
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the feed forward parameter of the PID algorithm that is used for position control.

2.19. Velocity Control Feed Forward
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the feed forward parameter of the PID algorithm that is used for velocity control.

2.20. Torque Control Feed Forward
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the feed forward parameter of the PID algorithm that is used for torque control.

2.21. Position Control Deadband
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the deadband parameter of the PID algorithm that is used for position control.

2.22. Velocity Control Deadband
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the deadband parameter of the PID algorithm that is used for velocity control.

2.23. Torque Control Deadband
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the deadband parameter of the PID algorithm that is used for torque control.

2.24. Position Control Output Limit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the maximum PWM output of the PID algorithm that is used for position control. This register can be configured between 0 - 1000.

2.25. Velocity Control Output Limit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the maximum PWM output of the PID algorithm that is used for velocity control. This register can be configured between 0 - 1000.

2.26. Torque Control Output Limit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the maximum PWM output of the PID algorithm that is used for torque control. This register can be configured between 0 - 1000.

2.27. Position Control Scaler Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the scaler gain parameter of the PID algorithm that is used for position control. It is recommended to keep this value at 1.0 and configure kp, ki and kd instead.

2.28. Position Control P Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the kp parameter of the PID algorithm that is used for position control.

2.29. Position Control I Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the ki parameter of the PID algorithm that is used for position control.

2.30. Position Control D Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the kd parameter of the PID algorithm that is used for position control.

2.31. Velocity Control Scaler Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the scaler gain parameter of the PID algorithm that is used for velocity control. It is recommended to keep this value at 1.0 and configure kp, ki and kd instead.

2.32. Velocity Control P Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the kp parameter of the PID algorithm that is used for velocity control.

2.33. Velocity Control I Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the ki parameter of the PID algorithm that is used for velocity control.

2.34. Velocity Control D Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the kd parameter of the PID algorithm that is used for velocity control.

2.35. Torque Control Scaler Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the scaler gain parameter of the PID algorithm that is used for torque control. It is recommended to keep this value at 1.0 and configure kp, ki and kd instead.

2.36. Torque Control P Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the kp parameter of the PID algorithm that is used for torque control.

2.37. Torque Control I Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the ki parameter of the PID algorithm that is used for torque control.

2.38. Torque Control D Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the kd parameter of the PID algorithm that is used for torque control.

2.39. Position Control Setpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register is the setpoint of the position control algorithm. The register value corresponds to encoder ticks. 

2.40. Velocity Control Setpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register is the setpoint of the velocity control algorithm. The register value corresponds to RPM.

2.41. Torque Control Setpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register is the setpoint of the torque control algorithm. The register value corresponds to mA.

2.42. PWM Control Setpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register is the setpoint of the torque control algorithm. The register value corresponds to duty cycle permillage .

2.43. Buzzer 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register generates sound on 1th buzzer add-on when set. 

2.44. Buzzer 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register generates sound on 2th buzzer add-on when set.

2.45. Buzzer 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register generates sound on 3th buzzer add-on when set.

2.45. Buzzer 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register generates sound on 4th buzzer add-on when set.

2.46. Buzzer 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register generates sound on 5th buzzer add-on when set.

2.47 Servo 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register moves 1th servo add-on to a desired angle. 

2.48 Servo 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register moves 2th servo add-on to a desired angle. 

2.49 Servo 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register moves 3th servo add-on to a desired angle. 

2.50 Servo 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register moves 4th servo add-on to a desired angle. 

2.51 Servo 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register moves 5th servo add-on to a desired angle. 

2.52 RGB 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register flashes the 1th RGB add-on with desired color.

2.53 RGB 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register flashes the 2th RGB add-on with desired color.

2.54 RGB 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register flashes the 3th RGB add-on with desired color.

2.55 RGB 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register flashes the 4th RGB add-on with desired color.

2.56 RGB 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register flashes the 5th RGB add-on with desired color.

2.57. Present Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the position of the motor in encoder ticks on requested time.

2.58. Present Velocity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the velocity of the motor in RPM on requested time.

2.59. Present Motor Current
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register represents the torque of the motor in milliamps on requested time.

2.60. Analog Port
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the ADC conversion on user analog port on requested time in range 0 - 4095.

2.61 Button 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the button state of the 1th button add-on. 1 for pressed 0 when not.

2.62 Button 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the button state of the 2th button add-on. 1 for pressed 0 when not.

2.63 Button 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the button state of the 3th button add-on. 1 for pressed 0 when not.

2.64 Button 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the button state of the 4th button add-on. 1 for pressed 0 when not.

2.65 Button 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the button state of the 5th button add-on. 1 for pressed 0 when not.

2.66 Light 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the luminance value conversion from 1th ambient light add-on. 

2.67 Light 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the luminance value conversion from 2th ambient light add-on.

2.68 Light 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the luminance value conversion from 3th ambient light add-on.

2.69 Light 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the luminance value conversion from 4th ambient light add-on.

2.70 Light 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the luminance value conversion from 5th ambient light add-on.

2.71 Joystick 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the ADC conversion of X, Y axes and joystick button state of the 1th joystick add-on. A read request on this register returns two float and one unsigned int values respective to X, Y and button state. 

2.72 Joystick 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the ADC conversion of X, Y axes and joystick button state of the 2th joystick add-on. A read request on this register returns two float and one unsigned int values respective to X, Y and button state.

2.73 Joystick 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the ADC conversion of X, Y axes and joystick button state of the 3th joystick add-on. A read request on this register returns two float and one unsigned int values respective to X, Y and button state.

2.74 Joystick 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the ADC conversion of X, Y axes and joystick button state of the 4th joystick add-on. A read request on this register returns two float and one unsigned int values respective to X, Y and button state.

2.75 Joystick 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the ADC conversion of X, Y axes and joystick button state of the 5th joystick add-on. A read request on this register returns two float and one unsigned int values respective to X, Y and button state.

2.76 Distance 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the distance (in cm) read from 1th ultrasonic distance add-on .

2.77 Distance 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the distance (in cm) read from 2th ultrasonic distance add-on .

2.78 Distance 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the distance (in cm) read from 3th ultrasonic distance add-on .

2.79 Distance 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the distance (in cm) read from 4th ultrasonic distance add-on .

2.80 Distance 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the distance (in cm) read from 5th ultrasonic distance add-on .

2.81 QTR 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the 1th QTR 3A reflectance add-on data in its least significant 3 bits where every bit indicates one IR LED/phototransistor pairs. 

2.82 QTR 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the 2th QTR 3A reflectance add-on data in its least significant 3 bits where every bit indicates one IR LED/phototransistor pairs. 

2.83 QTR 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the 3th QTR 3A reflectance add-on data in its least significant 3 bits where every bit indicates one IR LED/phototransistor pairs. 

2.83 QTR 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the 4th QTR 3A reflectance add-on data in its least significant 3 bits where every bit indicates one IR LED/phototransistor pairs. 

2.85 QTR 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the 5th QTR 3A reflectance add-on data in its least significant 3 bits where every bit indicates one IR LED/phototransistor pairs. 

2.86 Pot 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the ADC conversion from the 1th potantiometer add-on.

2.87 Pot 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the ADC conversion from the 2th potantiometer add-on.

2.88 Pot 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the ADC conversion from the 3th potantiometer add-on.

2.89 Pot 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the ADC conversion from the 4th potantiometer add-on.

2.90 Pot 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the ADC conversion from the 5th potantiometer add-on.

2.91 IMU 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the pitch and roll angles of the 1th MPU6050 IMU add-on. A read request on this register returns two float values respective to pitch and roll angles.

2.92 IMU 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the pitch and roll angles of the 2th MPU6050 IMU add-on. A read request on this register returns two float values respective to pitch and roll angles.

2.93 IMU 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the pitch and roll angles of the 3th MPU6050 IMU add-on. A read request on this register returns two float values respective to pitch and roll angles.

2.94 IMU 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the pitch and roll angles of the 4th MPU6050 IMU add-on. A read request on this register returns two float values respective to pitch and roll angles.

2.95 IMU 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This register holds the pitch and roll angles of the 5th MPU6050 IMU add-on. A read request on this register returns two float values respective to pitch and roll angles.

