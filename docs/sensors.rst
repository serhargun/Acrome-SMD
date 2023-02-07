Sensors
=====


.. _HC-SR04:
HC-SR04 
------------

 (Device ID: 0x06)

 Range min-max

 Distance(cm) : 2-400

The HCSR04 is a low-cost ultrasonic distance sensor that can be used to measure the distance of an object from a sensor. It uses sonar to determine the distance to an object by emitting a sound wave at a high frequency, and measuring the time it takes for the sound wave to bounce back.The sensor has four pins: Vcc, Trig, Echo, and GND. The Vcc and GND pins are used to power the sensor, typically with a voltage between 5V and 5.5V. The Trig pin is used to trigger the sensor to send out a sound wave, and the Echo pin is used to receive the sound wave that bounces back from an object.When the Trig pin is set to a high level for at least 10 microseconds, the sensor sends out an 8 cycle sonic burst at a frequency of 40kHz. When the sound wave hits an object, it bounces back and is received by the Echo pin. The time between the Trig signal and the Echo signal is proportional to the distance of the object.The distance can be calculated using the speed of sound and the time it took for the sound wave to return. The distance formula is: distance = (time * speed of sound) / 2.

How to use ? :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data from the sensor is read with Attiny85 and transmitted to the actuator card with the I2C line.The size of the data coming from this sensor with the I2C line is 2 bytes.The sensor module is designed as plug-in.There are 2 RC11 sockets on the module. The sensor data of both sockets can be read. The Actuator.Sensors.distance value in the code is the 2-byte distance data read from the sensor.The distance data read from the sensor was converted into centimeters in Attiny and transferred to the communication line.The sensor is widely used in various applications such as obstacle avoidance, distance measurement, and automation projects. It's easy to use and provides a high precision distance measurement.Please note that the sensor's accuracy can be affected by the object's reflective property, and the ambient temperature. Also, the sensor has a range of 2cm to 400cm, and it's not suitable for measuring short distances or distances less than 2cm.

.. _QTR-3A:
QTR-3A
------------

 (Device ID: 0x0A)

A QTR (Pololu Quad Reflectance Sensor ) is an electronic sensor that is used to detect the reflectance of a surface. It is typically used in robotics and automation applications to detect the presence or absence of an object, or to measure the position of an object.The QTR sensor consists of an array of three phototransistors that are sensitive to infrared light. The sensor is placed in front of a surface, and infrared light is emitted from the sensor towards the surface. Some of the infrared light is reflected back to the sensor, and the amount of light that is reflected back is proportional to the reflectance of the surface.The three phototransistors in the sensor detect the amount of light that is reflected back, and the sensor outputs a signal that is proportional to the reflectance of the surface. The sensor can be used to detect black and white surfaces, or to measure the position of an object on a line.

How to use ? :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Data from the sensor is read with Attiny85 and transmitted to the actuator card with the I2C line.The size of the data coming from this sensor with the I2C line is 1 bytes.The sensor module is designed as plug-in.There are 2 RC11 sockets on the module. The sensor data of both sockets can be read. The Actuator.Sensors.qtrData value in the code is the 1-byte distance data read from the sensor.This 1 byte data include left ,mid and right phototransistors datas.
This byte = Left-Mid-Right-0-0-0-0-0. By bit shifting we can obtain 3 data separately.Actuator.Sensors.qtrData.R is right phototransistor’s data,Actuator.Sensors.qtrData.M is middle phototransistor’s data and Actuator.Sensors.qtrData.L is left phototransistor’s data .

.. _LightSensor:
The Ambient Light Sensor(IN-S32GTLS)
------------

 (Device ID:0x05)

 Range min-max

 Wavelength  : 300-700 nm 

 Flux per unit area 	: 0-2600 lux

The Ambient Light Sensor is a device that measures the amount of light in its surrounding environment. These sensors are commonly used in smartphones, laptops, and other electronic devices to automatically adjust the screen brightness based on the surrounding light level. The output of the sensor is connected to an analog-to-digital converter (ADC) which converts the analog signal into a digital signal that can be read and processed by a microcontroller or computer.

How to use ? :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use the sensor, the data is read with an Attiny85 microcontroller and transmitted to the actuator card using the I2C communication protocol. The size of the data coming from this sensor on the I2C line is 2 bytes. The sensor module is designed as a plug-in and has 2 RC11 sockets on the module, allowing the sensor data of both sockets to be read. The Actuator.Sensors.lightIntensity value in the code represents the 2-byte data read from the sensor, which represents the intensity of the ambient light.

.. _Joystick:
Joystick
------------

 (Device ID: 0x09)

An Arduino joystick module is a device that allows a user to control an Arduino board through the use of a joystick. The module typically includes two potentiometers (one for the x-axis and one for the y-axis) and a push button. These components are connected to an analog input pins of the Acrome Actuator, and the Acrome Actuator software can then read the values of the potentiometers and button to determine the position and status of the joystick. 
 
How to use ? :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To use the sensor, the data is read with an Attiny85 microcontroller and transmitted to the actuator card using the I2C communication protocol. The size of the data coming from this sensor on the I2C line is 5 bytes. The sensor module is designed as a plug-in and has 2 RC11 sockets on the module, allowing the sensor data of both sockets to be read. The Actuator.Sensors.joystickX value in the code represents the 2-byte X-axis position, Actuator.Sensors.joystickY value in the code represents the 2-byte Y-axis position and Actuator.Sensors.joystickButton value in the code represents the 1-byte button situation  read from the sensor.

.. _Button:
Button
------------

 (Device ID:0x08 )

An button module is a device that allows a user to interact with an Acrome Actuator  by pressing a button. A button module typically includes a button that is connected to a digital input pin on the Acrome Actuator. When the button is pressed, it sends a digital signal to the input pin that can be read by the Acrome Actuator  software. 

How to use ? :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To use the button, the data is read with the Attiny85 microcontroller and transmitted to the actuator card using the I2C communication protocol. The size of the data coming from this sensor on the I2C line is 1 byte. The sensor module is designed as a plug-in and has 2 RC11 sockets on the module, allowing the sensor data of both sockets to be read. The Actuator.Sensors.buttonPressed value in the code represents the button status read from the sensor.

.. _IMU:
IMU (MPU9250)
------------

The MPU-9250 is a sensor from Invensense that combines a 3-axis accelerometer, 3-axis gyroscope, and 3-axis magnetometer (compass) into a single package. The sensor provides high accuracy measurement of linear acceleration, angular rate, and magnetic field vector. The sensor communicates with the host device using the I2C interface. The sensor data can be used to calculate orientation, position, and velocity. 

How to use ? :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Data from the sensor is read by the Attiny85 microcontroller. The size of the data coming from the sensor on the I2C line is 6 bytes. The sensor module is designed as a plug-in and has 2 RC11 sockets on the module, allowing the sensor data of both sockets to be read. The Actuator.Sensors.roll value in the code represents the roll angle, measured in degrees. The Actuator.Sensors.pitch value in the code represents the pitch angle, also measured in degrees. The sensor data is transmitted to the actuator card using the I2C communication protocol. It's important to note that the sensor's output may be affected by the ambient temperature and humidity




