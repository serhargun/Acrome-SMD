Example code - 
============

Sweep Motor
-----------
Required equipment:
 - DC motor
 - ACROME SDK -Red


.. code-block:: cpp

   #include <acromesmd.h>
   AcromeSMD myActuator(0,Serial);
   float position;

   void setup() {
       myActuator.begin(115200);
       myActuator.setOperationMode(PositionControl);    
   }

   void loop() { 
       myActuator.torqueEnable(1);
       position = myActuator.getPosition();
       myActuator.setpoint(PositionControl,position+500.0);
       delay(1500);
       position =(position>25000)?0:position;
   }

