from abc import ABC, abstractmethod


class ModelTrainer(ABC):
    name = "Model Trainer"

    def load_data(self, path):
        print(f"[{self.name}] Loading data from:", path)

    def pre_process_data(self):
        print(f"[{self.name}] Pre-processing data...")

    @abstractmethod
    def train_model(self):
        print(f"[{self.name}] Training model...")

    @abstractmethod
    def evaluate_model(self):
        print(f"[{self.name}] Evaluating model...")

    def save_model(self, path):
        print(f"[{self.name}] Saving model to:", path)

    def train(self, path: str = "model_path"):
        print(f"[{self.name}] Starting training process...")
        self.load_data(path)
        self.pre_process_data()
        self.train_model()
        self.evaluate_model()
        self.save_model("model_path")
        print(f"[{self.name}] Training process completed.")