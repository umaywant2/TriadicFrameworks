# ai_nimms_com_train_model.py
# Purpose: Train AI model using TriadicFrameworks/_ideas scrolls
# GPU: RTX 3050 | CUDA: 12.4 | PyTorch: cu124

import os
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset

# 🔍 Check GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 🏷️ Assign labels based on filename or embedded glyphs
def label_scrolls(filename, content):
    # Example logic — customize as needed
    if "validator" in filename.lower():
        return 1  # Label for validator logic
    elif "glyph" in content.lower():
        return 2  # Label for symbolic/glyph-based scrolls
    elif "ritual" in content.lower():
        return 3  # Label for ritual scrolls
    else:
        return 0  # Default label

# 📁 Load scrolls from _ideas folder
def load_scrolls(folder_path):
    scrolls = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            full_path = os.path.join(folder_path, filename)
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
                label = label_scrolls(filename, content)
                scrolls.append({"text": content, "label": label})
    return Dataset.from_list(scrolls)

repo_path = "../docs/_ideas"
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
