import os

def read_file_content(path):
    """Đọc nội dung một file văn bản."""
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read().strip()
    except Exception as e:
        print(f"Lỗi không thể đọc file {path}: {e}")
        return ""

def read_code_from_folder(folder_path):
    """Đọc tất cả file .py trong thư mục."""
    code_texts = []
    file_names = []
    
    if not os.path.exists(folder_path):
        print(f"Đường dẫn không tồn tại: {folder_path}")
        return code_texts, file_names

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                content = read_file_content(path)
                if content:
                    code_texts.append(content)
                    file_names.append(file)
    return code_texts, file_names