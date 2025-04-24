from nn.model import NeuralNetwork
from nn.layers import Dense, ReLU
from nn.loss import MSELoss

# Create the model
model = NeuralNetwork()
model.add_layer(Dense(input_size=2, output_size=3))
model.add_layer(ReLU())
model.add_layer(Dense(input_size=3, output_size=1))

# Training data
X = [[1, 2], [2, 3], [3, 4]]
y = [[3], [5], [7]]

# Training loop
loss_fn = MSELoss()
learning_rate = 0.01
epochs = 1000

for epoch in range(epochs):
    predictions = model.forward(X)
    loss = loss_fn.forward(predictions, y)
    print(f"Epoch {epoch}, Loss: {loss}")
    loss_grad = loss_fn.backward()
    model.backward(loss_grad, learning_rate)
