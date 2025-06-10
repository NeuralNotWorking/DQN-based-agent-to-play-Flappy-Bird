# DQN-based-agent-to-play-Flappy-Bird
A DQN agent trained (without explicit target network) which can play a custom pygame - implementation of the classic Flappy Bird game. No GPU needed. 

For those who don't know - DQN stands for Double Q Network, in which we just add a neural network to the standard learning loop of an RL agent. The neural network approximation the Q value for all the actions at a particular state (Q stands for Quality), instead of maintaining a Q table for all states. 

We have chosen the state dimension to be 3, which includes (normalized) bird velocity and the relative positions of the bird wrt the next gap (rel y and rel x for two states).

The action has dimension 2, which stands for - no action and flap(). flap() is the usual flap if the game is running, else it starts the game. 
Apart from input (state) and output (action) layers, we have 3 hidden layers in the neural network, with 128,64 and 32 neurons respectively. 

For the reward, we are awarding the bird 0.1 points for surviving every step, 10 points for passing a pipe and 0.1*(1-|y1-y2|/game_height) for being close to the gap (y1,y2 represent bird's and gap's y coordinates).

We also have a scaling_parameter, which speeds up the game so that the training is done quickly. Don't worry, the model hence the agent is independent of the scaling_parameter, which means that we can train the model at 5x speed (300 fps) and then it will run in 1x speed (60 fps by default) just fine. This is because the state variables are all independent of the scaling_factor. 

We trained the model for ~18000 games in 5x speed (2-2.5 hrs), then in normal speed, in which he easily reached a high score of 60+ within 100 games. 
The trained model is saved as .pth file after 50 games. The same goes for scores, etc. in form of a .json file. 

Any other things? Go through the code and find out! All the best!

![WhatsApp Image 2025-06-10 at 17 12 39_16d1a465](https://github.com/user-attachments/assets/845ac001-3a19-4c27-ba8e-8f245b380c49)


