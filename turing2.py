def findJudge(N, trust):
    result = None
    for trust_item in trust:
        for item in trust_item:
            if N in item:
                result = N
            else:
                result = -1
    return result

print(findJudge(2, trust=[[1,2]]))