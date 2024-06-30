import torch
import torch.nn as nn

class DiceLoss(nn.Module):
    def __init__(self, smooth=1.0):
        super(DiceLoss, self).__init__()
        self.smooth = smooth

    def forward(self, outputs, targets):
        outputs = torch.sigmoid(outputs)  # Apply sigmoid to get probabilities in range [0, 1]
        outputs = outputs.contiguous().view(-1)  # Flatten the tensor
        targets = targets.contiguous().view(-1)  # Flatten the tensor
        
        intersection = (outputs * targets).sum()  # Compute intersection
        dice = (2. * intersection + self.smooth) / (outputs.sum() + targets.sum() + self.smooth)  # Compute Dice coefficient
        return 1 - dice  # Return Dice loss
