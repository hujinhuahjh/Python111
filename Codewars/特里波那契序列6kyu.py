def tribonacci(signature, n):
    x = 0
    for x in range(n):
        # signature.append(signature[-1] + signature[-2] + signature[-3])
        signature.append(sum(signature[-3:]))
    return signature[:n]

print(tribonacci([1, 0, 0], 10))