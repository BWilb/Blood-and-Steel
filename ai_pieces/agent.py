import torch
import random
import numpy as np
from collections import deque

MAX_MEMORY = 200_000
BATCH_SIZE = 2000
LR = 0.001

class Agent:
    def __init__(self):
        self.attempts = 0
        # agent will be based off of economic, social, and (soon to be) political attempts
        self.epsilon = 0  # control randomness
        self.gamma = 0.9  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)  # automatically remove from left side if run out of room
        """self.model = Linear_QNet(11, 256, 3)
        # 11 states and 3 outputs
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)"""
        # self.model
        # self.trainer
