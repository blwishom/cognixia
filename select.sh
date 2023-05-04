# COLORS="red blue green orange"
# select color in $COLORS; do
#     echo "You have chosen the color $color!"
#     break
# done


# COLORS=("red" "blue" "green" "orange")
# select color in ${COLORS[@]}; do
#     echo "You have chosen the color $color!"
#     break
# done


NUMBERS=(20 30 40 50 60)
select number in ${NUMBERS[@]}; do
    echo "You have chosen the number $number!"
    break
done
