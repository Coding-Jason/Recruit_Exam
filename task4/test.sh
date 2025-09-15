#!/bin/bash
# 使用: bash test.sh <start_x> <start_y> <goal_x> <goal_y>

if [ $# -ne 4 ]; then
    echo "Usage: bash test.sh <start_x> <start_y> <goal_x> <goal_y>"
    exit 1
fi

START_X=$1
START_Y=$2
GOAL_X=$3
GOAL_Y=$4

chmod +x pathfinder.py
./pathfinder.py map.txt $START_X $START_Y $GOAL_X $GOAL_Y
