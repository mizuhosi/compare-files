import os

def compare_files(folder1, folder2):
    # フォルダ内のファイルリストを取得（サブフォルダを含む）
    files1 = set()
    for root, _, files in os.walk(folder1):
        for file in files:
            files1.add(os.path.relpath(os.path.join(root, file), folder1))

    files2 = set()
    for root, _, files in os.walk(folder2):
        for file in files:
            files2.add(os.path.relpath(os.path.join(root, file), folder2))

    # 共通のファイルを見つける
    common_files = files1.intersection(files2)

    # 各フォルダにのみ存在するファイルを見つける
    unique_files1 = files1 - files2
    unique_files2 = files2 - files1

    # 共通のファイルを比較
    for file in common_files:
        try:
            with open(os.path.join(folder1, file), 'r', encoding='utf-8') as f1, open(os.path.join(folder2, file), 'r', encoding='utf-8') as f2:
                content1 = f1.read()
                content2 = f2.read()
                if content1 != content2:
                    print(os.path.join(folder1, file))
                    print(os.path.join(folder2, file))
        except UnicodeDecodeError:
            try:
                with open(os.path.join(folder1, file), 'r', encoding='latin-1') as f1, open(os.path.join(folder2, file), 'r', encoding='latin-1') as f2:
                    content1 = f1.read()
                    content2 = f2.read()
                    if content1 != content2:
                        print(os.path.join(folder1, file))
                        print(os.path.join(folder2, file))
            except PermissionError as e:
                print(f"PermissionError: {e}")
            except UnicodeDecodeError as e:
                print(f"UnicodeDecodeError: {e}")
        except PermissionError as e:
            print(f"PermissionError: {e}")

    # 各フォルダにのみ存在するファイルのパスを出力
    for file in unique_files1:
        print(os.path.join(folder1, file))
    for file in unique_files2:
        print(os.path.join(folder2, file))


# 使用例
folder1 = './CodeChecker_Diff/base/'
folder2 = './CodeChecker_Diff/recent/'
compare_files(folder1, folder2)
