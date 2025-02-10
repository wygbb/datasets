import os
import json
import argparse


def merge_json_files(directory):
    merged_data = []

    # 确保目录存在
    if not os.path.isdir(directory):
        print(f"目录 {directory} 不存在")
        return

    # 遍历目录中的所有 JSON 文件
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        merged_data.extend(data)
                    else:
                        merged_data.append(data)
            except Exception as e:
                print(f"文件 {filename} 读取失败: {e}")

    # 生成合并后的 JSON 文件
    output_file = "merged.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=4)

    print(f"合并完成，生成文件: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="合并目录中的多个 JSON 文件为一个 JSON 文件")
    parser.add_argument("directory", type=str, help="包含 JSON 文件的目录")
    args = parser.parse_args()

    merge_json_files(args.directory)
