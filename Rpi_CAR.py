import RPi.GPIO as io
import time
import config as con

class Car:
    
    io.setmode(io.BOARD)	
    left_wheel =(35,38)
    right_wheel =(37,36)
        
        
    #MOVE
    def left(self):
	try:
	    io.cleanup()
	
	finally:
	    io.setup(35,io.OUT)
	io.output(35,True)

    def right(self):
        try:
            io.cleanup()

        finally:
            io.setup(38,io.OUT)
        io.output(38,True)

    def forward(self):
        try:
            io.cleanup()

        finally:
            io.setup(35,io.OUT)
            io.setup(38,io.OUT)
	io.output(35,True)
	io.output(38,True)

    def backward(self):
        try:
            io.cleanup()

        finally:
            io.setup(36,io.OUT)
            io.setup(37,io.OUT)
	io.output(36,True)
	io.output(37,True)
    def stop(self):
        try:
            io.cleanup()

        finally:
            print 'Stop'



		
