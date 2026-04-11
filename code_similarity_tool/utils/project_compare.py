from .file_reader import read_code_from_folder
from .string_compare import calculate_string_similarity
from .tfidf_compare import calculate_tfidf_similarity

def compare_projects(folder1, folder2):
    code1, names1 = read_code_from_folder(folder1)
    code2, names2 = read_code_from_folder(folder2)

    if not code1 or not code2:
        print("Một trong hai thư mục không có code .py để so sánh!")
        return

    print("\n===== 1. TRÙNG LẶP CODE (STRING) =====")
    for i, t1 in enumerate(code1):
        for j, t2 in enumerate(code2):
            sim = calculate_string_similarity(t1, t2)
            print(f"{names1[i]} vs {names2[j]}: {sim:.2f}%")

    print("\n===== 2. TRÙNG LẶP LOGIC (TF-IDF) =====")
    combined = code1 + code2
    sim_matrix = calculate_tfidf_similarity(combined)

    n1 = len(code1)
    for i in range(n1):
        for j in range(n1, len(combined)):
            print(f"{names1[i]} vs {names2[j-n1]}: {sim_matrix[i][j]*100:.2f}%")