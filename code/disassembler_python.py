'''
Name    : Nithik Nishanth Sudhakar
Date    : 09 March 2025
Routine : disassembler_python.py
Desc    : Sample of python byte code disassembler function
*********
Changelog
*********

20250309    -   Initial Draft


'''


import dis

def printing(n):
    if n == 0:
        print("input param is 0")
    else:
        print("We got a numerical input parameter")

dis.dis(printing)