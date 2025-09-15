#!/usr/bin/env python3
import json
import sys
import os

def main():
    # 检查命令行参数
    if len(sys.argv) != 2:
        print(f"Usage: python3 {os.path.basename(sys.argv[0])} <config.json>")
        sys.exit(1)

    config_path = sys.argv[1]

    # 检查文件是否存在
    if not os.path.isfile(config_path):
        print(f"Error: file '{config_path}' not found")
        sys.exit(1)

    # 读取 JSON 文件
    with open(config_path, "r") as f:
        config = json.load(f)

    # 格式化打印
    print("===== Robot Configuration =====")
    for key, value in config.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
