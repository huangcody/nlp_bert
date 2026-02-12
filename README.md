# 中文句子情緒分類

使用 BERT 預訓練模型進行微調 (Fine-tune)，將中文句子分類為 8 種情緒類別。

## 訓練資料來源
- [Datasets:Johnson8187/Chinese_Multi-Emotion_Dialogue_Dataset](https://huggingface.co/datasets/Johnson8187/Chinese_Multi-Emotion_Dialogue_Dataset)

## 基礎模型
- [google-bert/bert-base-chinese](https://huggingface.co/google-bert/bert-base-chinese)

## 安裝套件

### 主要套件
```bash
pip install --extra-index-url https://download.pytorch.org/whl/cu125 \
    torch==2.4.1 \
    torchvision==0.19.1 \
    torchaudio==2.4.1 \
    accelerate==1.8.1 \
    transformers \
    datasets \
    evaluate \
    scikit-learn \
    pandas
```

### 套件版本（實際使用）
- **torch**: 2.4.1 (CUDA 12.5)
- **torchvision**: 0.19.1
- **torchaudio**: 2.4.1
- **transformers**: 5.0.0
- **datasets**: 4.0.0
- **evaluate**: 0.4.6
- **accelerate**: 1.8.1
- **scikit-learn**: 1.6.1
- **pandas**: 2.2.2

### 執行環境
- **Python**: 3.12.12
- **CUDA**: 12.8
- **GPU**: Tesla T4 (Google Colab)
- **OS**: Ubuntu 22.04.5 LTS

## 說明

本專案使用 `google-bert/bert-base-chinese` 預訓練模型，針對中文情緒對話資料集進行微調，實現多元情緒分類任務。

### 情緒類別 (共 8 類)
| ID | 情緒類別 | 資料筆數 |
|----|----------|----------|
| 0  | 厭惡語調 | 404      |
| 1  | 平淡語氣 | 705      |
| 2  | 悲傷語調 | 486      |
| 3  | 憤怒語調 | 527      |
| 4  | 疑問語調 | 386      |
| 5  | 開心語調 | 592      |
| 6  | 關切語調 | 560      |
| 7  | 驚奇語調 | 499      |

**總計**: 4,159 筆資料 (訓練集: 3,327 筆 / 驗證集: 832 筆)

### 訓練參數
- **訓練回合數 (Epochs)**: 4
- **批次大小 (Batch Size)**: 16 (per device)
- **梯度累積步數 (Gradient Accumulation Steps)**: 2 (有效 batch size = 32)
- **學習率 (Learning Rate)**: 5e-5
- **預熱步數 (Warmup Steps)**: 31
- **權重衰減 (Weight Decay)**: 0.01
- **最大序列長度 (Max Sequence Length)**: 512
- **學習率調度器 (LR Scheduler)**: linear
- **評估指標 (Metric)**: Weighted F1 Score
- **隨機種子 (Random Seed)**: 42

### 預測結果
```
我每天都能跟她一起上學，我好開心！ => 開心語調 (1.0)
最好的朋友要離開臺灣了，以後可能不容易再見面... => 悲傷語調 (1.0)
我覺得我快不行了... => 悲傷語調 (0.99)
剛剛收到研究所錄取的通知書！ => 開心語調 (0.99)
今年的冬天好像比較晚來。 => 平淡語氣 (0.99)
```

**模型準確度**: 所有測試句子的預測信心度皆達 0.99 以上，顯示模型訓練效果良好。

## 檔案結構
```
├── output/                    # 微調後的模型檔案
│   ├── model.safetensors     # 模型權重 (391MB, Git LFS)
│   ├── config.json           # 模型配置
│   ├── label_mapping.json    # 情緒標籤對應表
│   ├── tokenizer.json        # 分詞器 (Git LFS)
│   ├── tokenizer_config.json # 分詞器配置
│   └── training_args.bin     # 訓練參數 (Git LFS)
├── finetune.ipynb            # 模型微調 Notebook
├── predict.ipynb             # 模型預測 Notebook
├── .gitattributes            # Git LFS 設定
└── README.md                 # 專案說明文件
```

> **注意**: 大型模型檔案（*.safetensors, *.bin, tokenizer.json）使用 Git LFS 儲存。

## 使用方式
1. 在 Google Colab 中開啟 `finetune.ipynb`，執行所有 cell 進行模型微調
2. 微調完成後，開啟 `predict.ipynb`，執行所有 cell 進行預測

## 成果
<!-- 請在此處放上執行過程的擷圖或說明圖片 -->
<!-- ![](執行過程的擷圖) -->

<!-- 請在此處放上影片連結 -->
<!-- [影片名稱](你的影片連結) -->
