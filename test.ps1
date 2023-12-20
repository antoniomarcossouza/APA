$METHODS = @("pivot_median")
$VALUES = @(100, 1000, 10000, 100000)
$SHUFFLE = @(5, 25, 45)

foreach ($j in $METHODS) {
    foreach ($k in $VALUES) {
        foreach ($l in $SHUFFLE) {
            for ($i = 1; $i -le 10; $i++) {
                python ./main.py --elements $k --shuffle $l --pivot $j
            }
        }
    }
}