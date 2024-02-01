

# def climbingLeaderboard(ranked, player):
#     # Write your code here
#     rank = sorted(list(set(ranked)))
#     rank.reverse()
#     result = []
#     for person in player:
#         rank_no = 1
#         for place in rank:
#             if person == place or  person > place:
#                 result.append(rank_no)
#                 break
#             elif person > place and place == rank[0]:
#                 result.append(1)
#                 break
#             elif person < place and place == rank[len(rank)-1]:
#                 result.append(rank_no+1)
#                 break
#             rank_no += 1

#     return result

def climbingLeaderboard(ranked, player):
    unique_ranked = list(reversed(sorted(set(ranked))))
    result = []
    
    rank_no = len(unique_ranked) + 1
    i = len(unique_ranked) - 1
    
    for person in player:
        while i >= 0 and person >= unique_ranked[i]:
            rank_no -= 1
            i -= 1
        result.append(rank_no)
    
    return result



ranked = [100,100,50,40,40,20,10]
player = [5,25,50,120]

print(climbingLeaderboard(ranked, player))