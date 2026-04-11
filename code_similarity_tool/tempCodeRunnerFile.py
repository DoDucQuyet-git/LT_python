# ==============================
# TOOL KIỂM TRA TRÙNG LẶP CODE
# ==============================

import os
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ======================================
# PHẦN 1: ĐỌC CODE TỪ THƯ MỤC
# ======================================
def read_code_from_folder(folder_path):
    code_texts = []
    file_names = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    code_texts.append(f.read())
                    file_names.append(file)

    return code_texts, file_names

# ======================================
# PHẦN 2: SO SÁNH TRÙNG LẶP TEXT (% GIỐNG)
# ======================================
def string_similarity(text1, text2):
    return difflib.SequenceMatcher(None, text1, text2).ratio() * 100

# ======================================
# PHẦN 3: SO SÁNH LOGIC (TF-IDF)
# ======================================
def tfidf_similarity(texts):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    return cosine_similarity(tfidf_matrix)

# ======================================
# PHẦN 4: SO SÁNH 2 PROJECT
# ======================================
def compare_projects(folder1, folder2):
    code1, names1 = read_code_from_folder(folder1)
    code2, names2 = read_code_from_folder(folder2)

    print("\n===== 1. TRÙNG LẶP CODE (STRING) =====")
    for i, t1 in enumerate(code1):
        for j, t2 in enumerate(code2):
            sim = string_similarity(t1, t2)
            print(f"{names1[i]} vs {names2[j]}: {sim:.2f}%")

    print("\n===== 2. TRÙNG LẶP LOGIC (TF-IDF) =====")
    combined = code1 + code2
    sim_matrix = tfidf_similarity(combined)

    n1 = len(code1)
    for i in range(n1):
        for j in range(n1, len(combined)):
            print(f"{names1[i]} vs {names2[j-n1]}: {sim_matrix[i][j]*100:.2f}%")

# ======================================
# PHẦN 5: SO SÁNH BÀI TIỂU LUẬN / REPORT
# ======================================
def compare_documents(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1:
        text1 = f1.read()
    with open(file2, 'r', encoding='utf-8') as f2:
        text2 = f2.read()

    string_sim = string_similarity(text1, text2)
    tfidf_sim = tfidf_similarity([text1, text2])[0][1] * 100

    print("\n===== 3. SO SÁNH BÁO CÁO =====")
    print(f"Giống text: {string_sim:.2f}%")
    print(f"Giống ý nghĩa: {tfidf_sim:.2f}%")

# ======================================
# PHẦN 6: MENU CHẠY CHƯƠNG TRÌNH
# ======================================
def main():
    print("\n====== TOOL CHECK ĐẠO CODE ======")
    print("1. So sánh 2 project code")
    print("2. So sánh 2 file báo cáo")

    choice = input("Chọn chức năng (1/2): ")

    if choice == '1':
        folder1 = input("Nhập đường dẫn project 1: ")
        folder2 = input("Nhập đường dẫn project 2: ")
        compare_projects(folder1, folder2)

    elif choice == '2':
        file1 = input("Nhập file báo cáo 1: ")
        file2 = input("Nhập file báo cáo 2: ")
        compare_documents(file1, file2)

    else:
        print("Lựa chọn không hợp lệ")

# ======================================
# RUN
# ======================================
if __name__ == "__main__":
    main()
