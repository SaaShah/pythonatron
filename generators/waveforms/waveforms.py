'''
Provides single generator that infinitely produces sine, square, ect... waveforms.
Example:
    for x in waveform(frequency, sample_rate, wave_function)
        print(x)
'''
from math import sin, pi

def waveform(freq, sample_rate, function):
    x = 0.0
    while True:
        x += (freq / sample_rate)
        x %= 1
        yield function(x)

def sine(x):
    return sin(x * pi * 2.0)

def square(x):
    return 1.0 if x < .5 else -1.0

def triangle(x):
    if x < .5:
        return x * 4.0 - 1.0
    return 3.0 - x * 4.0

def saw_up(x):
    return 1.0 - x * 2.0

def saw_down(x):
    return x * 2.0 - 1.0

if __name__ == '__main__':
    i = 0
    n = 10 
    wf = waveform(440.0, 44100.0, sine)

    while i < n:
        print(wf.next())
        i += 1

    i = 0
    for x in wf:
        if i > n:
            break 
        i += 1
        print(x)
