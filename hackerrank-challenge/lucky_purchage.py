import sys

if __name__ == "__main__":
    laptop_price = ['HackerBook 777444', 'RankBook 3', 'TheBook 777', 'BestBook 47']
    # size = len(laptop_price)
    # n = int(input().strip())
    # for a0 in range(n):
    #     s, n = input().strip().split(' ')
    #     s, n = [str(s), int(n)]
    for ao in laptop_price:
        s, n = ao.split(' ')
        s, n = [str(s), int(n)]
        for n in str(n):
            print(n)
    #     if "4" in str(n) and "7" in str(n):
    #         if "4" and "7" in str(n):
    #             print(s, n)
    # else:
    #     print(-1)
    #
