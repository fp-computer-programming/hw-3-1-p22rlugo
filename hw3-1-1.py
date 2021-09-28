# Ryan Lugo: RJL 9/28/21

# Team weirdos, Team Pogs

weirdos_wins = input("How many wins did the weirdos get?: ")
weirdos_ties = input("how many ties did the weirdos get?: ")

pogs_wins = input("How many wins did the pogs get?: ")
pogs_ties = input("how many ties did the pogs get?: ")

# 3 points for a win, 1 point for a tie
weirdos_wins_points = int(weirdos_wins) * 3
weirdos_total_points = weirdos_wins_points + int(weirdos_ties)

pogs_wins_points = int(pogs_wins) * 3
pogs_total_points = pogs_wins_points + int(pogs_ties)

if weirdos_total_points > pogs_total_points:
    print("Weirdos won against the Pogs!")