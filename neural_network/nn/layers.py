from nn.matrix import matmul, transpose, scalar_add  # Import matrix operations

class Dense:
    def __init__(self, input_size, output_size):
        import random
        # Initialize weights and biases randomly
        self.weights = [[random.uniform(-0.5, 0.5) for _ in range(output_size)] for _ in range(input_size)]
        self.biases = [random.uniform(-0.5, 0.5) for _ in range(output_size)]
        self.input = None

    def forward(self, x):
        """Forward propagation."""
        self.input = x
        # Perform matrix multiplication and add biases
        result = matmul(x, self.weights)
        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j] += self.biases[j]  # Add bias term
        return result

    def backward(self, grad_output, learning_rate):
        """Backward propagation: calculate gradients."""
        # Compute weight gradients
        grad_weights = matmul(transpose(self.input), grad_output)
        # Update weights and biases
        self.weights = scalar_add(self.weights, [[-learning_rate * grad for grad in row] for row in grad_weights])
        for j in range(len(self.biases)):
            self.biases[j] -= learning_rate * sum(grad_output[i][j] for i in range(len(grad_output)))

        # Return gradient to propagate back
        return matmul(grad_output, transpose(self.weights))
