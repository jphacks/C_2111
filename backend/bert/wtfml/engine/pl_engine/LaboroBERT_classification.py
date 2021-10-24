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
from transformers import AdamW, get_linear_schedule_with_warmup
from wtfml.engine.nlp.model import LaboroBERTBaseClassifier


class LaboroBERTClassificationPlEngine(pl.LightningModule):
    def __init__(
        self,
        model=LaboroBERTBaseClassifier(num_classes=4),
 
        # loss_fn=nn.BCEWithLogitsLoss(),
        loss_fn = nn.CrossEntropyLoss(),
        train_acc=torchmetrics.Accuracy(),
        valid_acc=torchmetrics.Accuracy(),
        lr: float = 3e-5,
        max_epoch=10,
    ):
        super(LaboroBERTClassificationPlEngine, self).__init__()
        self.model = model
        self.scaler = None
        self.loss_function = loss_fn
        self.train_acc = train_acc
        self.valid_acc = valid_acc
        self.lr = lr
        self.max_epoch = max_epoch

    def forward(self, ids): #, mask):
        x = self.model(ids) #, mask)
        return x

    def training_step(self, batch, batch_idx):
        # REQUIRED
        ids,  target = (
            batch["ids"],
            # batch["mask"],
            # batch["token_type_ids"],
            batch["targets"],
        )
        # target = main_target + sub_target * self.sub_adjustment
        pred_batch_train = self.forward(ids) #, mask)
        train_loss = self.loss_function(pred_batch_train, target)
        pred_batch_train_for_metrics = torch.softmax(pred_batch_train,dim = 1)
        target = target.to(torch.long)
        self.train_acc(pred_batch_train_for_metrics, target)
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
        ids,  target = (
            batch["ids"],
            # batch["mask"],
            # batch["token_type_ids"],
            batch["targets"],
        )
        # target = main_target + sub_target * self.sub_adjustment
        out = self.forward(ids) #, mask)
        # print(out, target)
        loss = self.loss_function(out, target)
        out_for_metrics = torch.softmax(out,dim = 1) 

        target = target.to(torch.long)
        self.valid_acc(out_for_metrics, target)

        self.log(
            "valid_acc",
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

        param_optimizer = list(self.model.named_parameters())
        no_decay = ["bias", "LayerNorm.bias"]
        optimizer_parameters = [
            {
                "params": [
                    p for n, p in param_optimizer if not any(nd in n for nd in no_decay)
                ],
                "weight_decay": 0.001,
            },
            {
                "params": [
                    p for n, p in param_optimizer if any(nd in n for nd in no_decay)
                ],
                "weight_decay": 0.0,
            },
        ]
        opt = AdamW(optimizer_parameters, lr=self.lr)

        # opt = optim.AdamW(self.model.parameters(), lr=self.lr)
        sch = get_linear_schedule_with_warmup(
            opt, num_warmup_steps=3, num_training_steps=self.max_epoch
        )
        return [opt], [sch]
