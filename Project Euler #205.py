from decimal import Decimal as D

def count_die_rolls(num_dice, num_sides=6):
    # Initialize DP array for a single die
    dp = [0] * (num_dice * num_sides + 1)
    
    # There is 1 way to roll each value of a single die
    for i in range(1, num_sides + 1):
        dp[i] = 1

    # Update the DP array for each additional die
    for dice in range(2, num_dice + 1):
        new_dp = [0] * (num_dice * num_sides + 1)
        for value in range(dice, dice * num_sides + 1):
            for face in range(1, num_sides + 1):
                if value - face >= dice - 1:
                    new_dp[value] += dp[value - face]
        dp = new_dp

    return dp

Colin_sides = 6
Colin_Die = 6
Peter_sides = 4
Peter_Die = 9

Colin = [0]*(Colin_sides * Colin_Die)
Colin_total = Colin_sides ** Colin_Die
Colin = count_die_rolls(Colin_Die, Colin_sides)


Peter = [0]*(Peter_sides*Peter_Die)
Peter_total = Peter_sides ** Peter_Die
Peter = count_die_rolls(Peter_Die, Peter_sides)

Colin = [D(i) / D(Colin_total) for i in Colin]
Peter = [D(i) / D(Peter_total) for i in Peter]

counter = 0

for i in range(0, len(Colin)):
	counter += Peter[i] * sum(Colin[i:])#At first, I accidentally calculated probability Colin won or drawed, oops

print(round(1 - counter, 7))#To ammend my mistake, I subtracted my result from one