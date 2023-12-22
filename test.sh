#!/bin/bash

METHODS=("pivot_median")
VALUES=($((10 ** 2)) $((10 ** 3)) $((10 ** 4)) $((10 ** 5)))
SHUFFLE=(5 25 45)

for j in ${METHODS[@]}; do
    for k in ${VALUES[@]}; do
        for l in ${SHUFFLE[@]}; do
            for i in {1..10}; do
                python3 ./main.py --elements $k --shuffle $l --pivot $j
            done
        done
    done
done