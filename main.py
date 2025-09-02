ir = 0

def on_ir_callbackuserv2(message):
    global ir
    ir = message
    if message == BitIR.IR_KeyValue(BitIR.enIRButton.UP):
        ir = 1
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.DOWN):
        ir = 2
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.LEFT):
        ir = 3
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.RIGHT):
        ir = 4
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.SPIN_LEFT):
        ir = 5
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.SPIN_RIGHT):
        ir = 6
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.BEEP):
        ir = 7
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.POWER):
        ir = 8
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.ADD):
        ir = 9
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.ZERO):
        ir = 10
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.MINUS):
        ir = 11
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.ONE):
        ir = 12
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.TWO):
        ir = 13
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.THREE):
        ir = 14
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.FOUR):
        ir = 15
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.FIVE):
        ir = 16
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.SIX):
        ir = 17
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.SEVEN):
        ir = 18
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.EIGHT):
        ir = 19
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.NINE):
        ir = 20
    elif message == BitIR.IR_KeyValue(BitIR.enIRButton.LIGHT):
        ir = 21
BitIR.IR_callbackUserV2(on_ir_callbackuserv2)

def on_forever():
    global ir
    if ir == 2:
        ir = 0
        mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RUN, 100)
        basic.pause(300)
        mbit_Robot.car_ctrl(mbit_Robot.CarState.CAR_STOP)
    elif ir == 2:
        ir = 0
        mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_BACK, 100)
        basic.pause(300)
        mbit_Robot.car_ctrl(mbit_Robot.CarState.CAR_STOP)
    elif ir == 3:
        ir = 0
        mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_LEFT, 100)
        basic.pause(300)
        mbit_Robot.car_ctrl(mbit_Robot.CarState.CAR_STOP)
    elif ir == 4:
        ir = 0
        mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RIGHT, 100)
        basic.pause(300)
        mbit_Robot.car_ctrl(mbit_Robot.CarState.CAR_STOP)
    elif ir == 5:
        ir = 0
        mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_SPINLEFT, 100)
        basic.pause(300)
        mbit_Robot.car_ctrl(mbit_Robot.CarState.CAR_STOP)
    elif ir == 6:
        ir = 0
        mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_SPINRIGHT, 100)
        basic.pause(300)
        mbit_Robot.car_ctrl(mbit_Robot.CarState.CAR_STOP)
    elif ir == 7:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
    elif ir == 8:
        mbit_Robot.RGB_Car_Big2(mbit_Robot.enColor.OFF)
    elif ir == 9:
        mbit_Robot.RGB_Car_Big2(mbit_Robot.enColor.RED)
    elif ir == 10:
        mbit_Robot.RGB_Car_Big2(mbit_Robot.enColor.GREEN)
    elif ir == 11:
        mbit_Robot.RGB_Car_Big2(mbit_Robot.enColor.BLUE)
    elif ir == 12:
        basic.show_number(1)
    elif ir == 13:
        basic.show_number(2)
    elif ir == 14:
        basic.show_number(3)
    elif ir == 15:
        basic.show_number(4)
    elif ir == 16:
        basic.show_number(5)
    elif ir == 17:
        basic.show_number(6)
    elif ir == 18:
        basic.show_number(7)
    elif ir == 19:
        basic.show_number(8)
    elif ir == 20:
        basic.show_number(9)
    elif ir == 21:
        mbit_Robot.RGB_Car_Big2(mbit_Robot.enColor.WHITE)
basic.forever(on_forever)
