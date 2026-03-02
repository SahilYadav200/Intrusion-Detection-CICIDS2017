# IDS-INT: Intrusion Detection System Using Transformer-Based Transfer

## Paper Overview
<!-- Summary of the paper's goals and contributions -->
- Paper Title: IDS-INT: Intrusion Detection System Using Transformer-Based Transfer
- TODO: Add authors, publication venue, and year from the PDF

## Problem Statement
<!-- What problem does the paper address? -->
- Network intrusion detection using the CIC-IDS2017 dataset
- TODO: Add specific problem statement details from the PDF

## Dataset
- **Name:** CIC-IDS2017 (Canadian Institute for Cybersecurity)
- **Files:** 8 CSV files covering Monday–Friday network traffic
- **Attack Types:** BENIGN, DDoS, DoS (Hulk, GoldenEye, Slowloris, Slowhttptest), PortScan, Brute Force (FTP-Patator, SSH-Patator), Bot, Web Attack (Brute Force, XSS, SQL Injection), Infiltration, Heartbleed
- TODO: Add any additional dataset details from the PDF

## Preprocessing Pipeline
- Strip whitespace from column names
- Remove duplicate rows
- Replace infinite values with NaN, fill NaN with column median
- Map original labels to grouped attack categories
- Memory optimization via numeric downcasting
- Drop zero-variance columns
- StandardScaler for feature scaling
- Incremental PCA for dimensionality reduction (retain ~50% of components)
- TODO: Add any additional preprocessing steps described in the PDF

## Model Architecture
### Transformer Encoder (from the repository implementation)
- **Type:** Tabular Transformer Encoder
- **Feature Embedding:** Each scalar feature projected to `d_model` dimensions via Linear(1, d_model)
- **CLS Token:** Learnable [CLS] token prepended to feature sequence
- **Positional Encoding:** Learnable positional embeddings
- **Encoder Layers:** Standard TransformerEncoderLayer with multi-head self-attention
- **Classification Head:** Linear → ReLU → Dropout → Linear
- **Hyperparameters:**
  - d_model: 64
  - nhead: 4
  - num_layers: 2 (binary) / 3 (multi-class)
  - dim_feedforward: 128
  - dropout: 0.1

- TODO: Add the specific transformer architecture and transfer learning details from the PDF

## Training Configuration
- **Optimizer:** Adam (lr=1e-3)
- **Scheduler:** StepLR (step_size=7, gamma=0.5)
- **Loss:** CrossEntropyLoss
- **Epochs:** 20 (binary) / 25 (multi-class)
- **Batch Size:** 256
- **Class Balancing:** SMOTE for multi-class; undersampling of benign class + 15,000 samples for binary

- TODO: Add any additional training details from the PDF

## Evaluation Metrics
- Accuracy
- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)
- ROC Curve and AUC (binary classification)
- Precision-Recall Curve (binary classification)

- TODO: Add specific results/scores from the PDF

## Key Findings & Conclusions
- Transformer Encoder can effectively classify network traffic from CIC-IDS2017
- Self-attention captures complex feature interactions advantageous over traditional ML
- Both binary (Benign vs Attack) and multi-class (attack type) classification supported

- TODO: Add specific findings, comparison results, and conclusions from the PDF

## References
- TODO: Add key references cited in the PDF
