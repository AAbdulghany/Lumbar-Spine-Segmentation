import torch
import torch.nn as nn

class DiceLoss(nn.Module):
    def __init__(self, smooth=1e-5):
        super(DiceLoss, self).__init__()
        self.smooth = smooth

    def forward(self, outputs, targets):
        outputs = torch.sigmoid(outputs)
        intersection = (outputs * targets).sum(dim=(2, 3, 4))
        dice_coef = (2. * intersection + self.smooth) / (outputs.sum(dim=(2, 3, 4)) + targets.sum(dim=(2, 3, 4)) + self.smooth)
        dice_loss = 1 - dice_coef
        return dice_loss.mean()