"""
Download and store the training dataset locally.

This module provides an entry point for downloading the configured
training dataset from Hugging Face Datasets and saving it to the
local filesystem.

The dataset name and destination path are configured through
:mod:`src.config.config` using ``DATASET_NAME`` and
``DATASET_LOCAL_PATH``.
"""
from datasets import load_dataset
from src.config.config import DATASET_LOCAL_PATH, DATASET_NAME


def main() -> None:
    """Download and save the training dataset locally.

    Loads the training split of the configured dataset from Hugging Face
    Datasets, creates the local destination directory if it does not exist,
    and saves the dataset to disk.

    Returns:
        None.
    """
    dataset = load_dataset(DATASET_NAME, split='train')
    DATASET_LOCAL_PATH.mkdir(parents=True, exist_ok=True)
    dataset.save_to_disk(str(DATASET_LOCAL_PATH))
    print(f"Saved {len(dataset)} rows to {DATASET_LOCAL_PATH}")


if __name__ == '__main__':
    main()
