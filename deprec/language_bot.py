from Queue import Queue
import time
from sys import exit
import easing

from ax12 import Ax12
import numpy as np

import thread

servos = Ax12()

class ax12_beta(object):

	def __init__(self, motorList, intialPositions, limitations, motorAngles):
		self.motorList = motorList
		self.intialPositions = intialPositions
		self.motorLimitations = limitations
		self.motorAngles = motorAngles
		self.timeStep = 0.20

		self.moveAllMotors(intialPositions,[300]*3)
		# Ax12.moveSpeedRW(motor_angles, motor_id, 300)

	def moveMotorSpeed(self, motorId, angle, speed):
		index = self.motorList.index(motorId)

		if angle < limitations[index][0]:
			angle = limitations[index][0]
		elif angle > limitations[index][1]:
			angle = limitations[index][1]

		servos.moveSpeed(motorId, angle, speed)
		self.motorAngles[index] = angle
		# return servos.readData(motorId)

	def moveAllMotors(self, targetAngles, speeds):
		for i in range(len(self.motorList)):
			self.moveMotorSpeed(self.motorList[i], targetAngles[i], speeds[i])

	def getAllAngles(self):
		currentAngles = []
		for i in range(len(self.motorList)):
			# vals = servos.readPosition(motorList[i])
			# print vals
			currentAngles.append(servos.readPosition(self.motorList[i]))
		return currentAngles

	def getAllSpeeds(self):
		currentSpeeds = []
		for i in range(len(self.motorList)):
			# print(servos.readSpeed(motorList[i]))
			currentSpeeds.append(servos.readSpeed(self.motorList[i]))
		return currentSpeeds

	def simpleEasing(self, motorId, angle, speed):
		index = self.motorList.index(motorId)
		currentAngle = self.motorAngles[index]

		difference = currentAngle - angle
		direction = np.sign(difference)
		difference = np.abs(difference)

		moveTime = difference / (0.25 * speed + 0.5 * speed)

		print moveTime
		print 0.25 * moveTime

		# self.moveMotorSpeed(motorId, angle, np.int_(0.5 * speed))
		# time.sleep(0.05 * moveTime)
		self.moveMotorSpeed(motorId, angle, np.int_(speed))
		time.sleep(np.int_(0.5 * moveTime))
		self.moveMotorSpeed(motorId, angle, np.int_(0.25 * speed))
		time.sleep(np.int_(0.12 * moveTime))

		return


	def easingMotorAngle(self, motorId, angle):
		index = self.motorList.index(motorId)
		currentAngle = self.motorAngles[index]
		if currentAngle > angle:
			difference = currentAngle - angle
			direction = -1
		else:
			difference = angle - currentAngle
			direction = 1

		size = float(difference) / self.timeStep
		interval = 1.0 / size

		steps = np.arange(0.0, 1 + interval, interval)
		steps = [easing.easeInOutQuart(step) for step in steps]
		steps = np.add(np.array(steps) * difference * direction, currentAngle)

		diff_steps = steps[1:] - steps[:-1]
		speeds = diff_steps / self.timeStep
		speeds = np.append(speeds, speeds[-1])

		speeds = speeds * 0.11 / (6 * 0.29)

		speeds = speeds.astype(int)
		steps = steps.astype(int)
		print steps
		print speeds

		for i in np.arange(steps.size):
			self.moveMotorSpeed(motorId, steps[i], speeds[i])
			time.sleep(0.03)

		return




if __name__ == '__main__':
	limitations = [(0,1000), (225,550), (600,880)]
	motorIds = [2,3,4]
	intialPositions = [200, 225, 880]
	motorAngles = [200, 225, 880]
	ax12Motors = ax12_beta(motorIds, intialPositions, limitations, motorAngles)
	time.sleep(3.0)

	ax12Motors.simpleEasing(3, 550, 200)
	time.sleep(3.0)

	ax12Motors.simpleEasing(3, 225, 200)
	time.sleep(3.0)

	# raw_input('Press enter when you would like to start recording:')
	# states = recording(ax12Motors)

	# print('Finished recording ... \n')
	# sleep(10)
	# print('The past states where:') 
	# print(states)


# def input_thread(list):
#     raw_input()
#     list.append(None)

# def recording(Motors):
#     list = []
#     thread.start_new_thread(input_thread, (list,))

#     record = []
#     while not list:
#     	currentAngles = Motors.getAllAngles()
#     	currentSpeeds = Motors.getAllSpeeds()
#     	print((currentAngles,currentSpeeds))
#     	record.append((currentAngles,currentSpeeds))
#         sleep(0.5)

#     return record
