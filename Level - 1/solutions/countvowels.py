i = input().split()

vowel_count = [0] * len(i)

for idx, h in enumerate(i):
    for g in h:
        if g in "aeiouAEIOU":
            vowel_count[idx] += 1

print(*vowel_count)
