import os

def rename_fif_to_png(directory):
    """
    將指定目錄中所有.fif檔案重命名為.png檔案
    
    參數:
    directory (str): 包含要重命名檔案的目錄路徑
    """
    # 檢查目錄是否存在
    if not os.path.exists(directory):
        print(f"錯誤: 目錄 '{directory}' 不存在")
        return
    
    # 計數器
    count = 0
    
    # 遍歷目錄中的所有檔案
    for filename in os.listdir(directory):
        # 檢查檔案是否以.fif結尾
        if filename.endswith('.jfif'):
            # 構建新檔案名稱
            new_filename = filename[:-4] + '.png'
            # 構建完整的檔案路徑
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            
            try:
                # 重命名檔案
                os.rename(old_file, new_file)
                print(f"已重命名: {filename} -> {new_filename}")
                count += 1
            except Exception as e:
                print(f"重命名 {filename} 時出錯: {str(e)}")
    
    print(f"完成! 共重命名了 {count} 個檔案。")

# 使用範例
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
        rename_fif_to_png(directory_path)
    else:
        print("請提供一個目錄路徑作為參數")
