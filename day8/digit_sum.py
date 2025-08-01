 def repeat(a):
        a = str(abs(a))
        c = 0
        for i in range(len(a)):
            c += int(a[i])
        if len(str(c)) != 1:
            return repeat(c)
        return c

    result = repeat(input1)
    if input1 < 0:
        result = -result  # Preserve the negative sign
    return result
