N = int(input())

score={
    1:"ABCDEFGHJLM",
    2:"ACEFGHILM",
    3:"ACEFGHILM",
    4:"ABCEFGHLM",
    5:"ACEFGHLM",
    6:"ACEFGHLM",
    7:"ACEFGHLM",
    8:"ACEFGHLM",
    9:"ACEFGHLM",
    10:"ABCFGHLM"
}
print(len(score[N]))
for p in score[N]:
    print(p, end=' ')