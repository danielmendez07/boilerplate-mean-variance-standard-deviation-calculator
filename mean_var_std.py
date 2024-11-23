import numpy as np

import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(input_list).reshape(3, 3)
    
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Mean of each column
            matrix.mean(axis=1).tolist(),  # Mean of each row
            matrix.mean().item()          # Mean of the entire matrix
        ],
        'variance': [
            matrix.var(axis=0).tolist(),  # Variance of each column
            matrix.var(axis=1).tolist(),  # Variance of each row
            matrix.var().item()          # Variance of the entire matrix
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),  # Standard deviation of each column
            matrix.std(axis=1).tolist(),  # Standard deviation of each row
            matrix.std().item()          # Standard deviation of the entire matrix
        ],
        'max': [
            matrix.max(axis=0).tolist(),  # Max of each column
            matrix.max(axis=1).tolist(),  # Max of each row
            matrix.max().item()          # Max of the entire matrix
        ],
        'min': [
            matrix.min(axis=0).tolist(),  # Min of each column
            matrix.min(axis=1).tolist(),  # Min of each row
            matrix.min().item()          # Min of the entire matrix
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),  # Sum of each column
            matrix.sum(axis=1).tolist(),  # Sum of each row
            matrix.sum().item()          # Sum of the entire matrix
        ]
    }
    
    return calculations