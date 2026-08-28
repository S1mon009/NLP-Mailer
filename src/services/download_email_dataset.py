from datasets import load_dataset

from src.config.config import DATASET_LOCAL_PATH, DATASET_NAME


def main():
    dataset = load_dataset(DATASET_NAME, split='train')
    DATASET_LOCAL_PATH.mkdir(parents=True, exist_ok=True)
    dataset.save_to_disk(str(DATASET_LOCAL_PATH))
    print(f"Saved {len(dataset)} rows to {DATASET_LOCAL_PATH}")


if __name__ == '__main__':
    main()
