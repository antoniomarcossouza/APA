@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

SET METHODS=pivot_first pivot_middle pivot_mean pivot_random
SET VALUES=10000 100000 1000000 10000000 100000000
SET SHUFFLE=5 25 45

FOR %%j IN (%METHODS%) DO (
    FOR %%k IN (%VALUES%) DO (
        FOR %%l IN (%SHUFFLE%) DO (
            FOR /L %%i IN (1,1,10) DO (
                python ./main.py --elements %%k --shuffle %%l --pivot %%j
            )
        )
    )
)

ENDLOCAL
