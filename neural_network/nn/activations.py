class ReLU:
    def forward(self, x):
        self.input = x
        return [[max(0, val) for val in row] for row in x]

    def backward(self, grad_output):
        return [[grad_output[i][j] if self.input[i][j] > 0 else 0 for j in range(len(row))] for i, row in enumerate(self.input)]

class Sigmoid:
    def forward(self, x):
        from math import exp
        self.output = [[1 / (1 + exp(-val)) for val in row] for row in x]
        return self.output

    def backward(self, grad_output):
        return [[grad_output[i][j] * self.output[i][j] * (1 - self.output[i][j]) for j in range(len(row))] for i, row in enumerate(self.output)]
