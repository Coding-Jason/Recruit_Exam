#!/bin/bash
# 自动运行 helloRM.py 脚本

echo "====== $(date '+%Y-%m-%d %H:%M:%S') ======"
python3 "$(dirname "$0")/helloRM.py"