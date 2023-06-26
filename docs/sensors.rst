Sensors Overview
=====
Acrome Smart Motor Drivers offer an advanced solution for motor control, incorporating a range of attachable sensor modules. These sensors greatly enhance user interaction and control capacity, providing feedback, and automation capabilities. By integrating sensors, Acrome Smart Motor Drivers deliver intelligent and adaptable systems that optimize performance, safety, and efficiency, making them an ideal choice for various applications requiring precise motor control and seamless integration with the environment.


How To Use?
------------
When using sensors with Acrome Smart Motor Driver boards, certain steps should be followed. Firstly, the compatible sensors and their specific functionalities for the desired application should be identified. Next, the sensors should be connected to the RJ11 socket provided on the board using the I2C communication protocol. It is important to ensure that the sensors are securely plugged in to establish a reliable connection. Once the sensors are connected, communication should be established with them through the I2C line to collect real-time data. The sensor data should be read using the appropriate code or programming interface. (Refer to the BRUSHED DC MOTOR BOARD API section)  Based on the acquired sensor data, the desired control logic or action should be implemented on the motor driver board. The modular design of Acrome Smart Motor Driver boards allows sensors to be attached and detached at runtime, providing flexibility and adaptability for projects.

.. _HC-SR04:
HC-SR04 Ultrasonic Distance Sensor Module
------------

 (Device ID: 0x06)

 Range min-max

 Distance(cm) : 2-400

The HC-SR04 is an affordable sensor used for measuring distances. It emits sound waves and calculates the distance by measuring the time it takes for the waves to bounce back. It has a range of 2 cm to 400 cm and is commonly used for obstacle avoidance and distance measurement in various projects.


.. _QTR-3A:
QTR-3A Reflectance Sensor Module
------------

 (Device ID: 0x0A)

The QTR sensor detects the reflectance of a surface using infrared light. It consists of three phototransistors that measure the amount of reflected light. It is commonly used in robotics and automation to detect objects or track positions on a line.


.. _LightSensor:
Ambient Light Sensor Module(IN-S32GTLS)
------------

 (Device ID:0x05)

 Range min-max

 Wavelength  : 300-700 nm 

 Flux per unit area 	: 0-2600 lux

The Ambient Light Sensor (IN-S32GTLS) measures the light level in its surroundings. It is often found in electronic devices like smartphones and laptops to automatically adjust screen brightness. The sensor provides data on the intensity of ambient light and is useful for creating light level related control flows and systems.


.. _Joystick:
Joystick Module
------------

 (Device ID: 0x09)

The Joystick module enables users to control compatible devices by providing input through joystick movements. It typically has two potentiometers for the X and Y axes and a push button. The module provides position and button status data, enabling users to interact with the system through joystick movements. 


.. _Button:
Button Module
------------

 (Device ID:0x08 )

The button module is a simple input device that detects when a button is pressed. It is commonly used for user input and interaction with the system. 


.. _IMU:
Inertial Measurement Unit (IMU) Module(MPU9250)
------------

The MPU9250 IMU is a sensor that combines an accelerometer, gyroscope, and magnetometer in a single package. It provides accurate measurements of linear acceleration, angular rate, and magnetic field. The sensor is used to determine orientation, position, and velocity in various applications.


