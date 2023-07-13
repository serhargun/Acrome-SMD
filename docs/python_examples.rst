Python Example code
============

AutoTuner 
-----------

In this Python example, the connected motor performs the auto-tune process according to the Ziegler-Nichols method. The calculated values are then stored in the ROM of the Acrome SMD board, and the motor moves to the setpoint value entered by the user

Required equipment:
 - DC motor
 - ACROME SMD

.. code-block:: python

    from smd import actuator
    import time
    import copy

    master = actuator.Master(4096, '/dev/ttyUSB0', baudrate=115200)
    master.AutoScan()

    print(f"Number of Actuator boards connected: {len(master.ActList)}")

    if(len(master.ActList) == 0):
        raise ConnectionError("No Actuator boards detected. Check cable connections!")
    print(f" The connected Actutators' IDs : {master.ActList}")

    # Initial full package read of Actuator parameters
    for act_id in master.ActList:
        master.send(master.Actuators[act_id].Read(full=True))
        time.sleep(0.05)
        master.pass2buffer(master.receive())
        master.findPackage()

    # Using Autotuner for PID gains tuning
    for act_id in master.ActList:
        copyact =  copy.deepcopy(master.Actuators[act_id])
        copyact.Configuration.data.torqueEnable.data = 1
        master.send(master.Actuators[act_id].Write(copyact))

        copyact =  copy.deepcopy(master.Actuators[act_id])
        copyact.Configuration.data.autotunerEnable.data = 1
        master.send(master.Actuators[act_id].Write(copyact))

        copyact =  copy.deepcopy(master.Actuators[act_id])
        copyact.Autotuner.data.method.data = 0x02   # Ziegler Nichols method
        master.send(master.Actuators[act_id].Write(copyact))

    time.sleep(0.3)
    input("Press any key after tuning process is completed. ")

    # Read tuned PID parameters
    for act_id in master.ActList:
        master.send(master.Actuators[act_id].Read(full=True))
        time.sleep(0.05)
        master.pass2buffer(master.receive())
        master.findPackage()

    # Disable Autotuning process
    for act_id in master.ActList:
        copyact =  copy.deepcopy(master.Actuators[act_id])
        copyact.Configuration.data.autotunerEnable.data = 0
        master.send(master.Actuators[act_id].Write(copyact))

    input("Press any key to save the parameters to ROM  ")
    for act_id in master.ActList:
        master.send(master.Actuators[act_id].ROMWrite())

    setpoint = int(input("Enter a setpoint for move Actuators to a position  "))
    for act_id in master.ActList:
        copyact =  copy.deepcopy(master.Actuators[act_id])
        copyact.Configuration.data.operationMode.data = 0   # Position control
        copyact.PositionControl.data.setpoint.data = setpoint
        master.send(master.Actuators[act_id].Write(copyact))
