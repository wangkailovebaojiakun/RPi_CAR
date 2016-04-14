import RPi.GPIO as io
import time
io.setmode(io.BOARD)

class Wheel(object):
    def __init__(self,in_pin1,in_pin2):
        self.pin1 = in_pin1
	self.pin2 = in_pin2
	# setup I/O OUT
	io.setup(in_pin1,io.OUT)
	io.setup(in_pin2,io.OUT)
    # MOVE
    def forward(self):
	io.output(self.pin1,True)
	io.output(self.pin2,False)
    def backward(self):
	io.output(self.pin1,False)
	io.output(self.pin2,True)
    def stop(self):
	io.output(self.pin1,False)
	io.output(self.pin2,False)

class Car(object):
    def __int__(self):
	
	self.left_wheel = Wheel(37,36)
	self.right_wheel = Wheel(35,38)
    #MOVE
    def forward(self):
	self.left_wheel.forward()
	self.right_wheel.forward()
    def backward(self):
	self.left_wheel.backward()
	self.right_wheel.backward()
    def left(self):
	self.left_wheel.forward()
	self.right_wheel.stop()
    def left_point(self):
	self.left_wheel.forward()
	self.right_wheel.backward()
    def right(self):
	self.right_wheel.forward()
	self.left_wheel.stop()
    def right_point(self):
	self.right_wheel.forward()
	self.left_wheel.backward()
    def stop(self):
	self.left_wheel.stop()
	self.right_wheel.stop()
    def shutdown(self):
	self.stop()
	io.cleanup()

