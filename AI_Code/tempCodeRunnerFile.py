import os
from google import genai

SUPPORTED_LANGUAGES = [
    "Python", "JavaScript", "HTML", "CSS", "Java",
    "C++", "C#", "PHP", "Go", "Rust", "SQL"
]


def build_prompt(user_request: str, language: str, style: str) -> str:
    return f"""
Bạn là một AI chuyên sinh code chất lượng cao.

Yêu cầu người dùng:
{user_request}

Ngôn ngữ cần sinh:
{language}

Phong cách mong muốn:
{style}

Hãy trả lời theo đúng định dạng sau:

1. Mô tả ngắn giải pháp
2. Code hoàn chỉnh, chạy được
3. Nếu cần, thêm hướng dẫn chạy ngắn gọn

Yêu cầu rất quan trọng:
- Code phải sạch, dễ đọc
- Hạn chế lỗi cú pháp
- Không giải thích lan man
- Ưu tiên code hoàn chỉnh
""".strip()


def generate_code(user_request, language, style):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("❌ Chưa set GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    prompt = build_prompt(user_request, language, style)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text


def main():
    print("===== AI CODE GENERATOR (CLI) =====")

    while True:
        print("\nNhập yêu cầu (hoặc 'exit' để thoát):")
        user_request = input(">>> ")

        if user_request.lower() == "exit":
            break

        print("\nChọn ngôn ngữ:")
        for i, lang in enumerate(SUPPORTED_LANGUAGES, 1):
            print(f"{i}. {lang}")

        try:
            choice = int(input("Chọn số: "))
            language = SUPPORTED_LANGUAGES[choice - 1]
        except:
            language = "Python"

        style = input("Phong cách (Enter = mặc định): ").strip()
        if not style:
            style = "Clean, production-ready"

        print("\n⏳ Đang sinh code...\n")

        try:
            result = generate_code(user_request, language, style)
            print("===== KẾT QUẢ =====\n")
            print(result)
        except Exception as e:
            print(f"❌ Lỗi: {e}")


if __name__ == "__main__":
    main()