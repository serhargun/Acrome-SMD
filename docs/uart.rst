Arduino Library
================

How to set up? Step by step
---------------------------

* İnstall this code https://github.com/Acrome-Robin/SmartActuator_Ardunio_Library 
* Unzip this file 
* Move this file to the Arduino library . (Default library location C:\Users\Documents\Arduino\libraries)
* If you will install first library, you can create folder called "libraries"

How can I include the Actuator library in my Arduino code?
-----------------------------------------------------------
.. figure:: figures/includeactuatorlibrary.png
   :alt: IncludeActuatorLibrary

Example code
================

tAutotuneMethod
----------------

This type definition is used for autotune methods of Actuator. The definition is an enum with 2 different possible values.

Possible values are:

- ZieglerNichols: The Ziegler-Nichols tuning method is a process for determining the optimal parameters for a PID (Proportional-Integral-Derivative) control system to achieve stable and accurate control of a dynamic process.

- Cohen Coon: The Cohen-Coon method is a process for determining the optimal parameters for a PID (Proportional-Integral-Derivative) control system by using frequency response data to model the process and provide improved robustness compared to the Ziegler-Nichols method.

Void Actuator::setAutotuneEnable()
----------------------------------

This method sends a write package and does not return any value. When this command is applied, the Actuator board enables autotune.

Example Usage
-------------
    myActuator.setAutotuneEnable(1);  //Enable Auto tuner
    
    myActuator.setAutotuneEnable(0);  //Disable Auto tuner
    
    
    
    
    
    
