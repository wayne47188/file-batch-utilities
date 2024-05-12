import shutil

# 定義要複製的檔案路徑
source_file = r"C:\Users\ox060\Downloads\國小簡報範本.pptx"

# 定義目標檔案夾列表
target_folders = [
    "1-1 情境動畫：如何服務長者？",
    "2-1 系統拆解",
    "2-2 QR Code 是什麼？",
    "2-3 使用 「QR Code」擴充功能",
    "2-4 掃瞄 QR Code",
    "3-1 系統拆解",
    "3-2 認識 Teachable Machine",
    "3-3 開啟建立模型介面",
    "3-4 輸入範例─網路攝影機",
    "3-5 輸入範例─影像檔案",
    "3-6 進行訓練",
    "3-7 檢視與輸出模型",
    "4-1 系統拆解",
    "4-2 使用「TM2Scratch」擴充功能",
    "4-3 連接分類模型網址",
    "4-4 建立Google試算表",
    "4-5 使用「讀寫Google試算表」擴充功能",
    "4-5 記錄兌換資訊",
    "5-1 系統拆解",
    "5-2 使用「讀寫 Google 試算表」擴充功能",
    "5-3 連結雲端資料庫",
    "5-4 查詢點數",
    "5-5 查詢兌換次數"
]

# 將檔案複製到每個目標檔案夾中
for folder in target_folders:
    target_folder = rf"C:\Users\ox060\Downloads\【國小資訊教育】搭起青銀共好\【國小資訊教育】搭起青銀共好\{folder}\\"
    shutil.copy(source_file, target_folder)
