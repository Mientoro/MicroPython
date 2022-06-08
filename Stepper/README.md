This library is for 4 wire bipolar stepper motors, like common Nema 3D printer motors.

The library has multiple functions to customize the control of a stepper motor.

The constructor requires at least 4 parameters for the Pin objects for the microcontroller, with 2 more parameters with changeable default values:
  pin_1, pin_2, pin_3, pin_4, steps_per_rotation = 200, rpm = 50
  
The pin parameters must be Pin objects created from the machine library built into MicroPython, while the steps per rotation should be changed for your specific motor. Typical rpm values range from 50-70 rpm.

The position value of a Stepper object keeps track of the step position of the motor from the starting point.

The following functions are included in the library:

    step(steps): Turns the motor the entered amount of steps. Can be a positive or negative integer value.
    reset(): Resets the current position of the motor and its status - also turns off the motors holding power.
    setPosition(steps): Turns the motor to a specific step amount relative to the starting position 0.
    rotate(rotations): Turns the motor a specific number of rotations. Can be a positive or negative integer value.
    setRPM(rpm): Changes the speed of the motor in rotations per minute.
    release(): Turns off the motors holding power.
    hold(): Turns on the motors holding power.
