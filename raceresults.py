

def race(my_time, opp1_time, opp2_time, opp3_time):
    if my_time < opp1_time and my_time < opp2_time and my_time < opp3_time:
        return "Gold"

    elif my_time > opp1_time and my_time < opp2_time and my_time < opp3_time:
        return "Silver"

    elif my_time > opp1_time and my_time > opp2_time and my_time < opp3_time:
        return "Bronze"

    else:
        return "no medal"


print (race(12,13,14,15))


