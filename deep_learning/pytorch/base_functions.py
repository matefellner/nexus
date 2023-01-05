import torch
import numpy as np

# 2. Creating tensor from nested list of ndarray

example_list = [1,2,3]
x = torch.tensor(example_list)
print(x)
# Output tensor([1, 2, 3])


# 3. Cloning a tensor

y = x.clone()
print(y)
# Output tensor([1, 2, 3])


# 4. Getting Size and Shapes

x = torch.randn((10,10))
print(x.size())
# or
print(x.shape)
# Output torch.Size([10, 10])


# 5. Concatenating tensors along dimensions

tensor_seq = [torch.randn(1,2),torch.randn(1,2)]
x = torch.cat(tensor_seq, dim=0)
print(x)


#  6. Reshaping tensor to dimension: (1, any)

x = torch.randn(10,2)
y = x.view(1,-1)
print(y.shape)
# Output torch.Size([1, 20])


# 7. Swapping specific dimensions of a tensor

x = torch.randn(1,2)
print(x)
y = x.transpose(0,1)
print(y)


# 8. Adding an axis to tensor

x = torch.randn(2,2)
print(x.shape)
y = x.unsqueeze(dim=0)                      
print(y.shape)


# 9. Removing all dimensions of size 1

x = torch.randn(10,10,1)
print(x.shape)
y = x.squeeze()
print(y.shape)


# 10. Matrix multiplication

A = torch.ones(2,2)
B = torch.randn(2,2)
print(A)
print(B)
print(A.mm(B))


# 11. Matrix-vector multiplication

A = torch.tensor([[1,2],[3,4]])
x = torch.tensor([1,2])
print(A.mv(x))


# 12. Matrix transpose

x = torch.randn(1,2)
print(x)
x = x.t()
print(x)


# 13. Checking for cuda availability

print(torch.cuda.is_available())


# 14. Moving tensor data from CPU to GPU and return new object

x = torch.randn(2,2)
print(x)
x = x.cuda()
print(x)


# 16. Device agnostic code and modularity

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)# Outputdevice(type='cuda', index=0)


# 17. Copy tensors to a device (gpu, cpu)

x = x.to(device)
print(x)


# 18. Check if it is a Pytorch tensor

print(torch.is_tensor(x))


# 19. Check if it is a Pytorch storage object

print(torch.is_storage(x))


# 20. Getting the total number of elements in the input tensor

x = torch.randn(2,2) # 4 elements
torch.numel(x)


# 21. Getting the identity matrix for a given size

size = 5
print(torch.eye(size))


# 22. Converting from numpy array to torch tensor

x = np.random.rand(2,2)
print(torch.from_numpy(x))


# 23. Basic linear spacing (like in numpy’s np.linspace)

print(np.linspace(1,5,10))
print(torch.linspace(1, 5, steps=10))


# 24. Logarithmic Spacing

torch.logspace(start=-10, end=10, steps=15)


# 25. Splitting a Pytorch tensor into small chunks

x = torch.linspace(1,10,10)
print(torch.chunk(x,chunks=5))


# 26. Basic neural network

import torch.nn as nn

class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(1,1)
        self.relu = nn.ReLU()
        
    
    def forward(self,x):
        x = self.fc1(x)
        x = self.relu(x)
        
        return x
net = NeuralNet()
net


# 27. Creating tensors to hold inputs and outputs for training a neural network

x = torch.linspace(-10, 10, 2000).view(-1,1)
y = torch.square(x)


# 28. Loading the neural network and setting up a loss function and optimizer

model = NeuralNet()
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-6)


# 29. Training loop, printing the output every 10 epochs

epochs = 50
for t in range(epochs):
    # Forward pass: computing prediction
    y_pred = model(x)

    # Compute the loss and printing ever 10 iterations
    loss = criterion(y_pred, y)
    if t % 10 == 9:
        print(t, loss.item())

    # Zero gradients, perform a backward pass, and update the weights.
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()