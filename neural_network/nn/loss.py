class MSELoss:
    def forward(self, predictions, targets):
        self.predictions = predictions
        self.targets = targets
        return sum((p - t) ** 2 for p, t in zip(predictions, targets)) / len(targets)

    def backward(self):
        return [[2 * (pred - target) for pred, target in zip(self.predictions, self.targets)]]
