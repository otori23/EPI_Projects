import random
        
def bruteForce(S):
    pMax = float('-inf')
    for p_i in S:
        for p_j in S[1:]:
            if (p_j - p_i) > pMax:
                pMax = p_j - p_i
    return pMax

def divideAndConquer(S):
    result = 0.0
    if len(S) <= 1:
        result = 0.0
    elif len(S) == 2:
        result = S[1] - S[0]
    else:
        p1 = divideAndConquer(S[:len(S)/2])
        p2 = divideAndConquer(S[(len(S)/2 + 1):])
        p3 = max(S[(len(S)/2 + 1):]) - min(S[:len(S)/2])
        result = max(p1, p2, p3);
    return result
    
def linearTimeAlg(S):
    minPrice = float('inf')           
    maxProfit = float('-inf')
    for p in S:
        if p < minPrice:
            minPrice = p
            
        tempMax = p - minPrice
        
        if tempMax > maxProfit:
            maxProfit = tempMax
    return maxProfit
                 
             
if __name__ == '__main__':
    random.seed(0)
    numDays = 10
    S = []
    for i in range(numDays):
        S.append(100 * random.random())
        
    print S
    print bruteForce(S)
    print divideAndConquer(S)
    print linearTimeAlg(S)                    