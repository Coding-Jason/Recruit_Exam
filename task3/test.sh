#!/bin/bash
# 自动运行 read_config_file.py 并打印时间戳

CONFIG_PATH="$(dirname "$0")/config.json"

# 检查文件是否存在
if [ ! -f "$CONFIG_PATH" ]; then
    echo "Error: file '$CONFIG_PATH' not found"
    exit 1
fi

echo "====== $(date '+%Y-%m-%d %H:%M:%S') ======"
python3 "$(dirname "$0")/read_config_file.py" "$CONFIG_PATH"
