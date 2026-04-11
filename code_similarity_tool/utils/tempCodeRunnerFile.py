from utils.file_reader import read_code_from_folder
from utils.string_compare import string_similarity
from utils.tfidf_compare import tfidf_similarity
print("DEBUG:")
print("Project1 files:", names1)
print("Project2 files:", names2)

print("Project1 content:", code1)
print("Project2 content:", code2)

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

    if len(combined) == 0:
        print("Không có file code để so sánh!")
        return

    sim_matrix = tfidf_similarity(combined)

    n1 = len(code1)
    for i in range(n1):
        for j in range(n1, len(combined)):
            print(f"{names1[i]} vs {names2[j-n1]}: {sim_matrix[i][j]*100:.2f}%")