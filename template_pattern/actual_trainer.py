from template_pattern.trainer import ModelTrainer


class NeuralNetworkTrainer(ModelTrainer):
    def __init__(self):
        self.name = "Neural Network Trainer"

    def pre_process_data(self):
        # Pre-process data specific to neural networks
        print(f"[{self.name}] Neural network data pre-processed.")

    def train_model(self):
        # Train neural network model
        print(f"[{self.name}] Neural network model trained.")

    def evaluate_model(self):
        # Evaluate neural network model
        print(f"[{self.name}] Neural network model evaluated.")



class DecisionTreeTrainer(ModelTrainer):
    def __init__(self):
        self.name = "Decision Tree Trainer"


    def train_model(self):
        # Train decision tree model
        print(f"[{self.name}] Decision tree model trained.")

    def evaluate_model(self):
        # Evaluate decision tree model
        print(f"[{self.name}] Decision tree model evaluated.")

    def save_model(self, path):
        # Save decision tree model
        print(f"[{self.name}] Decision tree model saved to:", path)