from plot import plot
import numpy as np


class Robot:
    def __init__(self, pos):
        self.pos = pos    # robot initialized position

    def move(self):
        self.pos += 1

    def pole_detected(self, poles):
        if self.pos + 1 in poles:
            return True
        else:
            return False


def bayes(PBA, PA, PB):
    # This function compute the Bayes rule and returns the posterior probability
    """your code here"""
    '''****************'''
    # estimate to be one line of code here
    '''****************'''
    return PAB



def shift_priors_with_uncertainty(P_loc_i):
    # Shift all probabilities to the right by one unit with the probability of 90%
    # Shift all probabilities to the right by two units with the probability of 10%
    """your code here"""
    '''****************'''
    # around 4-6 lines of code here
    '''****************'''


def update_loc_posteri():
    # Perform Bayes Rule on each location.
    """your code here"""
    '''****************'''
    # around 5 lines of code here
    '''****************'''


distance = 40

robot = Robot(pos=2)  # change the initialized location to 5, and see the difference with loc=2
poles = [5, 9, 13]

# Initalize variables (generally you do not need to do this in python,
# but I did this so you can see if the variable is a vector or a scalar.)
# Initalize bayes probabilities. Create as many probabilities or beliefs as
# the same number of discrete locations the robot can occupy.
P_loc_i_prior = np.zeros(distance)  # P(Li) - Prior belief of being in location i.
P_loc_i_posteri = np.zeros(distance)  # posterior belief of being in location i, updated by performing Bayes Rule.
P_D = 0.   # P(D) -- Probability of Detecting a Pole.
P_not_D = 0.   # P(!D) -- Probability of Not Detecting Pole.
P_D_given_loc_i = np.zeros(distance)  # P(D|Li) - Probability of detecting a pole, given at location i.
P_not_D_given_loc_i = np.zeros(distance)  # P(!D|Li) - Probability of not detecting a pole, given at location i.


# Set the prior assuming the robot has equal probability to be at each location.
"""your code here"""
'''****************'''
# one line of code here
'''****************'''

# Set probabilities of detecting a pole or not.
"""your code here"""
'''****************'''
# Two lines of code here
'''****************'''

# Sensor model (Observation model):
# Set the probabilities for a pole being detected or not detected for each location i.
# Assuming the sensor can 100% accurately detect the pole only at one-unit before the pole
"""your code here"""
'''****************'''
# around 6 lines of code here
'''****************'''


# Setup done, run first calculation of robots location.
update_loc_posteri()
plot(distance, poles, P_loc_i_posteri, robot, block=True)

# Begin Moving
for j in range(13):
    robot.move()
    # Shift the priors to follow the robot moving.
    shift_priors_with_uncertainty(P_loc_i_posteri)
    # Set prior using the previous posterior, so we can start the iteration over again.
    P_loc_i_prior = P_loc_i_posteri
    # Perform Bayes Rule using new measurement about whether the robot sensor detected a pole.
    update_loc_posteri()
    plot(distance, poles, P_loc_i_posteri, robot, block=True)

plot(distance, poles, P_loc_i_posteri, robot, block=True, pause_time=1)
