Autotuner 
-----------------

PID (proportional-integral-derivative) control is a common control algorithm used in a variety of control systems, including those that regulate temperature, flow, pressure, and other process variables. Autotuning is the process of automatically adjusting the parameters of a PID controller to optimize its performance.

There are several reasons why autotuning PID controllers can be beneficial:

- Improved control performance: Autotuning can help improve the performance of a PID controller by finding the optimal values for the controller's parameters (proportional, integral, and derivative gains). This can result in faster and more accurate control of the process variable.

- Reduced setup time: Autotuning can significantly reduce the time and effort required to set up a PID controller, as it eliminates the need for manual tuning.

- Better response to process changes: Autotuning can help a PID controller adapt to changes in the process being controlled, such as changes in load or operating conditions. This can help maintain stable control of the process and prevent the need for frequent manual adjustments.

Overall, autotuning PID controllers can help improve the performance and efficiency of control systems by optimizing the controller's parameters and adapting to changes in the process being controlled.

Minimum output required for motor motion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is usually a minimum voltage required to supply to an electric motor in order to start it and keep it running. This is because the motor needs a certain amount of current to generate the magnetic field needed to produce torque and rotate the shaft. If the voltage supplied to the motor is too low, the current flowing through the motor will be insufficient to generate the necessary magnetic field, and the motor will not start or will stall if it is already running.
To prevent this situation, the motor must be given a minimum output value.

Ziegler Nichols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Ziegler-Nichols method is a simple and widely used method for autotuning PID controllers. It was developed in the 1940s by John G. Ziegler and Nathaniel B. Nichols, and is based on the idea of using a step response test to determine the optimal values for the controller's proportional, integral, and derivative gains.

The Ziegler-Nichols method involves the following steps:

1. Set the controller's integral and derivative gains to zero and gradually increase the proportional gain until the system becomes unstable and begins oscillating.
2. Measure the period of oscillation (the time it takes for one complete oscillation) and the amplitude of the oscillation (the maximum deviation from the setpoint).
3. Use these measurements to calculate the recommended values for the proportional, integral, and derivative gains using the following formulas:
4. Set the controller's gains to the recommended values.

The Ziegler-Nichols method is simple and easy to use, but it can sometimes result in a controller that is overly aggressive or unstable.

Cohen Coon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cohen-Coon tuning is a method for autotuning PID controllers that was developed by Norm Cohen and Bernard Coon in the 1960s. It is based on the idea of using a step response test to determine the optimal values for the controller's proportional, integral, and derivative gains.

The Cohen-Coon method involves the following steps:

1. In order for the next steps to be correct, first of all, the maximum speed that the motor can reach must be calculated. (Note: It is operated at half power here to avoid damaging the motor and the system.)

2. Dead time (td) calculation

3. Time constant (𝝉) Calculation
 Time constant (𝝉) = Time difference between intersection at the end of dead time, and the PV reaching 63% of its total change.

4. Gp calculation
 Gp = change in PV [in %] / change in CO [in %]

5. Set the controller's gains to the recommended values.

The Cohen-Coon method is similar to the Ziegler-Nichols method, but it is generally considered to be more conservative and less aggressive, resulting in a more stable controller. However, it can still result in a controller that is not optimal for all systems.

