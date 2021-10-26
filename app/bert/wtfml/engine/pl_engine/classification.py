"""
__author__: Abhishek Thakur
"""

from typing import Optional

import pytorch_lightning as pl
import torch
import torch.nn as nn
import torch.optim as optim
import torchmetrics
from tqdm import tqdm


class ClassificationEngine(pl.LightningModule):
    def __init__(
        self,
        model,
        loss_fn=nn.CrossEntropyLoss(),
        train_acc=torchmetrics.Accuracy(),
        valid_acc=torchmetrics.Accuracy(),
        lr: float = 0.001,
    ):
        super(ClassificationEngine, self).__init__()
        self.model = model
        self.scaler = None
        self.loss_function = loss_fn
        self.train_acc = train_acc
        self.valid_acc = valid_acc
        self.lr = lr

    def forward(self, x):
        x = self.model(x)
        return x

    def training_step(self, batch, batch_idx):
        # REQUIRED
        image, target = batch
        # target = main_target + sub_target * self.sub_adjustment
        pred_batch_train = self.forward(image)
        train_loss = self.loss_function(pred_batch_train, target)
        self.train_acc(pred_batch_train, target)
        self.log(
            "train_acc",
            self.train_acc,
            on_step=True,
            on_epoch=False,
            logger=True,
            prog_bar=True,
        )

        self.log(
            "train_loss",
            train_loss,
            prog_bar=True,
            on_epoch=True,
            on_step=True,
            logger=True,
        )
        return {"loss": train_loss}

    def validation_step(self, batch, batch_idx):
        # OPTIONAL
        image, target = batch
        # target = main_target + sub_target * self.sub_adjustment
        out = self.forward(image)
        self.valid_acc(out, target)
        loss = self.loss_function(out, target)
        loss = loss
        self.log(
            "valid_F_score",
            self.valid_acc,
            prog_bar=True,
            logger=True,
            on_epoch=True,
            on_step=False,
        )
        self.log(
            "valid_loss",
            loss,
            prog_bar=True,
            logger=True,
            on_epoch=True,
            on_step=False,
        )
        return {
            "val_loss": loss,
            # "acc": acc,
        }

    def configure_optimizers(self):
        # REQUIRED
        opt = optim.Adam(self.model.parameters(), lr=self.lr)
        sch = optim.lr_scheduler.ExponentialLR(opt, gamma=0.96)
        return [opt], [sch]
