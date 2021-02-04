def climbing(scores, chacha):
    unique_scores = list(reversed(sorted(set(scores))))

    i = len(chacha)-1
    j = 0
    ans = []

    while i >= 0:
        if j >= len(unique_scores) or unique_scores[j] <= chacha[i]:
            ans.append(j+1)
            i -= 1
        else:
            j += 1

    return reversed(ans)
scores_count = int(input())
scores = list(map(int, input().rstrip().split()))
chacha_count = int(input())
chacha = list(map(int, input().rstrip().split()))
result = climbing(scores, chacha)
print(list(result))
