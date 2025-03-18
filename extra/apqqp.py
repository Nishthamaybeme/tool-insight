import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
import os
from efficientnet_pytorch import EfficientNet

# Set device to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Data transformations for training
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Pre-trained mean and std
])

# Load the dataset from train_data directory
train_data = datasets.ImageFolder(root='all images dataset', transform=transform)

# DataLoader for training
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)

# Load pre-trained EfficientNet (use efficientnet-b0, you can also try other versions like b1, b2, etc.)
model = EfficientNet.from_pretrained('efficientnet-b0')

# Freeze the weights of pre-trained layers
for param in model.parameters():
    param.requires_grad = False

# Replace the classifier part of EfficientNet to match the number of classes in your dataset
num_classes = len(train_data.classes)  # Automatically gets number of classes from the directory
model._fc = nn.Linear(in_features=model._fc.in_features, out_features=num_classes)

# Move model to device (GPU/CPU)
model = model.to(device)

# Loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model._fc.parameters(), lr=0.001)

# Training the model
num_epochs = 5
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        
        optimizer.zero_grad()
        
        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        
        # Backward pass
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
        
        # Get the predictions
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    
    accuracy = 100 * correct / total
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss/len(train_loader):.4f}, Accuracy: {accuracy:.2f}%")

# Save the trained model
torch.save(model.state_dict(), 'tool_recognition_efficientnet.pth')

# Print final accuracy
print(f"Final Accuracy: {accuracy:.2f}%")
