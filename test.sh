#!/bin/bash

METHODS=("pivot_first" "pivot_middle" "pivot_mean" "pivot_random")
VALUES=($((10 ** 4)) $((10 ** 6)))

for i in {1..3}; do
    for j in ${METHODS[@]}; do
        for k in ${VALUES[@]}; do
            python3 ./main.py --elements $k --shuffle 5 --pivot $j
        done
    done
done
