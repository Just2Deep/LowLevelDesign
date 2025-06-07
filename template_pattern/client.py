from template_pattern.actual_trainer import DecisionTreeTrainer, NeuralNetworkTrainer
from template_pattern.trainer import ModelTrainer


class Client:
    def __init__(self, template: ModelTrainer):
        self.template = template

    def run(self, path: str):
        print("Client is running with the following template:")
        self.template.train(path)

if __name__ == "__main__":
    neural_network_trainer = NeuralNetworkTrainer()
    client = Client(neural_network_trainer)
    client.run("neural_network_data.csv")

    decision_tree_trainer = DecisionTreeTrainer()
    client = Client(decision_tree_trainer)
    client.run("decision_tree_data.csv")