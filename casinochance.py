win_values = input() # 1 2
dice_sides = input() # 1 1 1 2 2 2 

w1, w2 = win_values.split("")


count_w1 = dice_sides.count(w1)
prob_w1 = count_w1/6

count_w2 = dice_sides.count(w2) 
prob_w2 = count_w2/6

print (prob_w1*prob_w2)

