# a rough implementation of DDA algorithm for line drawing 
# the code are in micropython for Raspberry Pi Pico/Pico2

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    xinc = dx / steps
    yinc = dy / steps
    x = x1
    y = y1
    for i in range(steps):
        print("x: ", round(x), " y: ", round(y))
        x += xinc
        y += yinc

