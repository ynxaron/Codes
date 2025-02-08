def trapping_rain_water(inp: list[int]) -> int:
    stack = []
    water = 0
    i = 0
    while i < len(inp) - 1:
        if i == 0:
            stack.append(inp[i])
        elif (i > 0) and (stack[-1] > inp[i]):
            stack.append(inp[i])
        else:
            l = len(stack) - 1
            while (l > 0) and stack[l] < inp[i]:
                l -= 1
            height = min(stack[l], inp[i])

            h = len(stack) - 1
            while (h > l):
                water += (height - stack[h])
                stack[h] = height
                h -= 1

            if stack[l] < height:
                stack = [inp[i]]
            else:
                stack.append(inp[i])

        i += 1
    return water

print(trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
