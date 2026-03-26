"""
Chapter 12: Applications and Ethics
Grad-CAM for CNN interpretability
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms, models
import numpy as np


class GradCAM:
    """Grad-CAM implementation for CNN interpretability."""
    def __init__(self, model, target_layer):
        self.model = model
        self.target_layer = target_layer
        self.gradients = None
        self.activations = None
        self._register_hooks()

    def _register_hooks(self):
        def forward_hook(module, input, output):
            self.activations = output.detach()

        def backward_hook(module, grad_input, grad_output):
            self.gradients = grad_output[0].detach()

        self.target_layer.register_forward_hook(forward_hook)
        self.target_layer.register_full_backward_hook(backward_hook)

    def __call__(self, x, class_idx=None):
        self.model.eval()
        output = self.model(x)
        if class_idx is None:
            class_idx = output.argmax(dim=1)

        self.model.zero_grad()
        one_hot = torch.zeros_like(output)
        one_hot[0, class_idx] = 1
        output.backward(gradient=one_hot)

        # Global average pooling of gradients
        weights = self.gradients.mean(dim=[2, 3], keepdim=True)  # (B,C,1,1)
        cam = (weights * self.activations).sum(dim=1, keepdim=True)
        cam = F.relu(cam)
        cam = F.interpolate(cam, size=x.shape[2:], mode='bilinear',
                           align_corners=False)
        # Normalize
        cam = cam - cam.min()
        cam = cam / (cam.max() + 1e-8)
        return cam.squeeze().numpy()


if __name__ == '__main__':
    # Simple CNN for demonstration
    class SimpleCNN(nn.Module):
        def __init__(self):
            super().__init__()
            self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
            self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
            self.pool = nn.MaxPool2d(2)
            self.fc = nn.Linear(32 * 7 * 7, 10)

        def forward(self, x):
            x = F.relu(self.conv1(x))
            x = self.pool(x)
            x = F.relu(self.conv2(x))
            x = self.pool(x)
            return self.fc(x.view(x.size(0), -1))

    model = SimpleCNN()
    # Load a test image
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    test_data = datasets.MNIST('./data', train=False, download=True,
                               transform=transform)
    img, label = test_data[0]
    img = img.unsqueeze(0)

    # Apply Grad-CAM
    grad_cam = GradCAM(model, model.conv2)
    cam = grad_cam(img)

    print(f"Image label: {label}")
    print(f"Predicted: {model(img).argmax().item()}")
    print(f"CAM shape: {cam.shape}")
    print(f"CAM range: [{cam.min():.3f}, {cam.max():.3f}]")
