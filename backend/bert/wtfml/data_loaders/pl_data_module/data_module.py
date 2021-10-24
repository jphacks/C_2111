import pytorch_lightning as pl
from torch.utils.data import DataLoader


class plDataModule(pl.LightningDataModule):
    def __init__(
        self,
        train_dataset,
        val_dataset,
        test_dataset=None,
        num_workers=2,
        train_sampler=None,
        train_shuffle=True,
        train_batch_size=64,
        train_drop_last=False,
        val_batch_size=16,
        val_shuffle=False,
        val_sampler=None,
        train_dataloader=None,
        val_dataloader=None,
        test_dataloader=None,
    ):
        super().__init__()
        self.train_dataset = train_dataset
        self.val_dataset = val_dataset
        self.test_dataset = test_dataset

        self.num_workers = num_workers
        self.train_sampler = train_sampler
        self.train_shuffle = train_shuffle
        self.train_batch_size = train_batch_size
        self.train_drop_last = train_drop_last

        self.val_batch_size = val_batch_size
        self.val_shuffle = val_shuffle
        self.val_sampler = val_sampler

        self.created_train_dataloader = train_dataloader
        self.created_val_dataloader = val_dataloader
        self.created_test_dataloader = test_dataloader

    def train_dataloader(self):
        if self.created_train_dataloader:
            return self.created_train_dataloader
        return DataLoader(
            self.train_dataset,
            batch_size=self.train_batch_size,
            sampler=self.train_sampler,
            drop_last=self.train_drop_last,
            num_workers=self.num_workers,
            shuffle=self.train_shuffle if not self.train_sampler else False,
        )

    def val_dataloader(self):
        if self.created_val_dataloader:
            return self.created_val_dataloader
        return DataLoader(
            self.val_dataset,
            batch_size=self.val_batch_size,
            sampler=self.val_sampler,
            drop_last=False,
            num_workers=self.num_workers,
            shuffle=self.val_shuffle if not self.val_sampler else False,
        )

    def test_dataloader(self):
        if self.created_test_dataloader:
            return self.created_test_dataloader
        if self.test_dataset:
            return DataLoader(
                self.test_dataset,
                batch_size=self.val_batch_size,
                sampler=self.val_sampler,
                drop_last=False,
                num_workers=self.num_workers,
                shuffle=self.val_shuffle if not self.val_sampler else False,
            )
