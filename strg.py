import msvcrt

hi = 0
while True:
    hi += 1
    print(hi)
    if msvcrt.kbhit() and ord(msvcrt.getch()) == 27:
        aborted = True
        break