import pygame
import serial
import time

# Configure serial to Arduino (Serial1 on Mega = Pins 18/19)
ser = serial.Serial('/dev/serial0', 115200, timeout=1)

# Initialize Pygame for joystick
pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print("Sending controller axis data to Arduino...")

while True:
    pygame.event.pump()

    # Example: Read left stick X/Y left (axes 0 and 1)
    xl_axis = int(100 * joystick.get_axis(0))  # range: -100.0 to 100.0
    yl_axis = int(-100 * joystick.get_axis(1))
    
    # Example: Read left stick X/Y right (axes 3 and 4)
    xr_axis = int(100 * joystick.get_axis(3))  # range: -100.0 to 100.0
    yr_axis = int(-100 * joystick.get_axis(4))

    # Map to 0?180 for servo angles or normalized commands
    xl_mapped = int((xl_axis + 1) * 90)   # -1?0, 1?180
    yl_mapped = int((yl_axis + 1) * 90)
    
    xr_mapped = int((xr_axis + 1) * 90)   # -1?0, 1?180
    yr_mapped = int((yr_axis + 1) * 90)

    # Send as CSV: "x,y\n"
    message = f"{xl_axis},{yl_axis},{xr_axis},{yr_axis}\n"
    message = message.encode('utf-8')
    ser.write(message)
    # print(message)
    time.sleep(0.05)  # 20 Hz update
