import os

import comet_ml
import torch
import torchvision
from pl_bolts.datamodules import CIFAR10DataModule
from pl_bolts.transforms.dataset_normalizations import cifar10_normalization
from pytorch_lightning import LightningModule, Trainer, seed_everything
from pytorch_lightning.callbacks import LearningRateMonitor
from pytorch_lightning.callbacks.progress import TQDMProgressBar
from pytorch_lightning.loggers import CometLogger

from model import LitResnet

seed_everything(7)

if __name__ == '__main__':
    # prepare dataloader
    train_transforms = torchvision.transforms.Compose(
        [
            torchvision.transforms.RandomCrop(32, padding=4),
            torchvision.transforms.RandomHorizontalFlip(),
            torchvision.transforms.ToTensor(),
            cifar10_normalization(),
        ]
    )

    test_transforms = torchvision.transforms.Compose(
        [
            torchvision.transforms.ToTensor(),
            cifar10_normalization(),
        ]
    )

    cifar10_dm = CIFAR10DataModule(
        data_dir=os.environ.get("PATH_DATASETS", "."),
        batch_size=256,
        train_transforms=train_transforms,
        test_transforms=test_transforms,
        val_transforms=test_transforms,
    )

    # prepare model
    model = LitResnet(lr=0.05)

    # logger
    comet_logger = CometLogger()

    trainer = Trainer(
        max_epochs=30,
        accelerator='gpu',
        logger=comet_logger,
        callbacks=[LearningRateMonitor(logging_interval="step"), TQDMProgressBar(refresh_rate=10)],
    )

    trainer.fit(model, cifar10_dm)
    trainer.test(model, datamodule=cifar10_dm)

    print("DONE")

