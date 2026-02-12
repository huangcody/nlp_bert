# 中文句子情緒分類

使用 BERT 預訓練模型進行微調 (Fine-tune)，將中文句子分類為 8 種情緒類別。

## 訓練資料來源
- [Datasets:Johnson8187/Chinese_Multi-Emotion_Dialogue_Dataset](https://huggingface.co/datasets/Johnson8187/Chinese_Multi-Emotion_Dialogue_Dataset)

## 基礎模型
- [google-bert/bert-base-chinese](https://huggingface.co/google-bert/bert-base-chinese)

## 安裝套件
- torch (2.4.1)
- torchvision (0.19.1)
- torchaudio (2.4.1)
- transformers
- datasets
- evaluate
- accelerate (1.8.1)
- scikit-learn
- pandas

(版本號可用 `pip list` 或 `conda list` 來檢視)

## 說明

本專案使用 `google-bert/bert-base-chinese` 預訓練模型，針對中文情緒對話資料集進行微調，實現多元情緒分類任務。

### 情緒類別 (共 8 類)
| ID | 情緒類別 |
|----|----------|
| 0  | 厭惡語調 |
| 1  | 平淡語氣 |
| 2  | 恐懼語調 |
| 3  | 悲傷語調 |
| 4  | 憤怒語調 |
| 5  | 疑問語調 |
| 6  | 開心語調 |
| 7  | 驚奇語調 |

### 訓練參數
- Epochs: 3
- Batch size: 32
- Learning rate: 1e-4 (含 gradient accumulation 補償)
- Warmup steps: 50
- Weight decay: 0.01
- 評估指標: Weighted F1 Score

### 預測範例
```
我每天都能跟她一起上學，我好開心！ => 開心語調 (0.xx)
最好的朋友要離開臺灣了，以後可能不容易再見面... => 悲傷語調 (0.xx)
我覺得我快不行了... => 悲傷語調 (0.xx)
剛剛收到研究所錄取的通知書！ => 開心語調 (0.xx)
今年的冬天好像比較晚來。 => 平淡語氣 (0.xx)
```
(實際分數須以模型微調後的預測結果為準)

## 檔案結構
```
output/          # 微調後的模型 (不包括 checkpoint-* 資料夾)
finetune.ipynb   # 微調用
predict.ipynb    # 預測用
README.md        # 說明文件
```

## 使用方式
1. 在 Google Colab 中開啟 `finetune.ipynb`，執行所有 cell 進行模型微調
2. 微調完成後，開啟 `predict.ipynb`，執行所有 cell 進行預測

## 成果
<!-- 請在此處放上執行過程的擷圖或說明圖片 -->
<!-- ![](執行過程的擷圖) -->

<!-- 請在此處放上影片連結 -->
<!-- [影片名稱](你的影片連結) -->
