from .file_reader import read_file_content
from .string_compare import calculate_string_similarity
from .tfidf_compare import calculate_tfidf_similarity

def compare_documents(file1, file2):
    text1 = read_file_content(file1)
    text2 = read_file_content(file2)

    if not text1 or not text2:
        print("Lỗi: Một trong hai file báo cáo bị rỗng hoặc không tìm thấy!")
        return

    string_sim = calculate_string_similarity(text1, text2)
    # TF-IDF cần một list các văn bản
    sim_matrix = calculate_tfidf_similarity([text1, text2])
    tfidf_sim = sim_matrix[0][1] * 100

    print("\n===== 3. SO SÁNH BÁO CÁO =====")
    print(f"Giống về mặt trình bày (String): {string_sim:.2f}%")
    print(f"Giống về mặt nội dung (TF-IDF): {tfidf_sim:.2f}%")