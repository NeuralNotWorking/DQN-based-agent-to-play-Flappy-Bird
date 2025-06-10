class RLConfig:
    
    # Environment settings
    ENV_CONFIG = {
        'state_type': 'vector',  # 'vector' or 'image'
        'render_mode': 'rgb_array',
        'max_episode_steps': 10000,
    }
    
    # DQN Configuration Template
    DQN_CONFIG = {
        # TODO: Set hyperparameters for DQN
        'learning_rate': 0.001, #learning rate, of course
        'gamma': 0.9,  # discount factor
    }
    
    
