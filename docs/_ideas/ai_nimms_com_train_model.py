# ai_nimms_com_train_model.py
# Purpose: Train AI model using TriadicFrameworks repo content
# GPU: RTX 3050 | CUDA: 12.4 | PyTorch: cu124

import os
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset, Dataset

# 🔍 Validate GPU availability
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 📁 Load markdown scrolls from repo
def load_scrolls(folder_path):
    scrolls = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                scrolls.append({"text": f.read(), "label": 0})  # Default label for now
    return Dataset.from_list(scrolls)

# 🧠 Load dataset
repo_path = "../docs/TFT_3Pack_v1.3"
dataset = load_scrolls(repo_path)

# 🧬 Tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

# 🧪 Tokenize
def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True)

dataset = dataset.map(tokenize, batched=True)

# 🛠️ Training config
training_args = TrainingArguments(
    output_dir="./model_output",
    evaluation_strategy="epoch",
    per_device_train_batch_size=4,
    num_train_epochs=3,
    logging_dir="./logs",
    logging_steps=10,
)

# 🚀 Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

# 🧠 Train
trainer.train()
