import os

# 定義目標檔案夾列表及新檔案名稱
target_folders = [
    ("1-1 AI 姿勢辨識與生活上的應用", "1-1 AI 姿勢辨識與生活上的應用.pptx"),
("2-1 什麼是PoseNet", "2-1 什麼是PoseNet.pptx"),
("2-2 使用「PoseNet2Scratch」擴充功能", "2-2 使用「PoseNet2Scratch」擴充功能.pptx"),
("2-3 繪製人體骨架", "2-3 繪製人體骨架.pptx"),
("3-1 系統拆解", "3-1 系統拆解.pptx"),
("3-2 使用「PoseNet2Scratch」擴充功能", "3-2 使用「PoseNet2Scratch」擴充功能.pptx"),
("3-3 設定初始值", "3-3 設定初始值.pptx"),
("3-4 遊戲說明", "3-4 遊戲說明.pptx"),
("3-5 開始計時", "3-5 開始計時.pptx"),
("3-6 公佈分數", "3-6 公佈分數.pptx"),
("4-1 認識 Teachable Machine", "4-1 認識 Teachable Machine.pptx"),
("4-2 開啟建立模型介面", "4-2 開啟建立模型介面.pptx"),
("4-3 輸入範例 - 網路攝影機", "4-3 輸入範例 - 網路攝影機.pptx"),
("4-4 輸入範例 - 影像檔案", "4-4 輸入範例 - 影像檔案.pptx"),
("4-5 進行訓練", "4-5 進行訓練.pptx"),
("4-6 檢視與輸出模型", "4-6 檢視與輸出模型.pptx"),
("5-1 系統拆解", "5-1 系統拆解.pptx"),
("5-2 連接姿勢分類模型", "5-2 連接姿勢分類模型.pptx"),
("5-3 連接Google試算表", "5-3 連接Google試算表.pptx"),
("5-4 製作出題按鈕廣播", "5-4 製作出題按鈕廣播.pptx"),
("5-5 製作答題按鈕廣播", "5-5 製作答題按鈕廣播.pptx")
]

# 修改檔名
for folder, new_filename in target_folders:
    target_folder = rf"C:\Users\ox060\Downloads\【國中資訊科技】姿勢辨識\【國中資訊科技】姿勢辨識\{folder}\\"
    old_filename = r"國中簡報範本.pptx"
    old_file_path = os.path.join(target_folder, old_filename)
    new_file_path = os.path.join(target_folder, new_filename)
    os.rename(old_file_path, new_file_path)
