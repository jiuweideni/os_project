#函数可见性漏洞
import re
def check_function_visibility_advanced(file_path):
    visibility_keywords = ["public", "external", "internal", "private"]
    found = False

    with open(file_path, "r", encoding='utf-8') as file:  # 添加编码参数
        lines = file.readlines()

    for line_number, line in enumerate(lines, start=1):
        if line.strip().startswith(("//", "*")):
            continue

        if re.match(r"^\s*function\s+\w+\s*\(", line):
            if not any(keyword in line for keyword in visibility_keywords):
                print(f"检测到未指定可见性的函数")
                print(f"  位置: 第 {line_number} 行")
                print(f"  内容: {line.strip()}")
                found = True

    if not found:
        print("所有函数均已指定可见性")


input_file = "sol.txt"
check_function_visibility_advanced(input_file)