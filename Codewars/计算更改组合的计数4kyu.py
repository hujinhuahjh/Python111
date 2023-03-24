# from itertools import combinations_with_replacement
# def count_change(money, coins):
#     i,m,s = 0,0,0
#     r = list()
#     min1 = min(coins)
#     if min1 >= money:
#         return 1
#     while s < money:
#         s += min1
#         if s <= money:
#             i += 1
#     for n in range(i + 1):
#         r += list(combinations_with_replacement(coins, n))
#     for l in range(len(r)):
#         if sum(r[l]) == money:
#             m += 1
#     return m

def count_change(money, coins):
    dp = [1] + [0] * money
    for coin in coins:
        for x in range(coin, money + 1):
            dp[x] += dp[x-coin]
        print(dp)
    print(dp)
    return dp[money]

print(count_change(4, [1,2]))