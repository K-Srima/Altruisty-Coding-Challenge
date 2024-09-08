def reduce_ticket_price(tickets, k):
    stack = []
    for digit in tickets:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k > 0:
        stack.pop()
        k -= 1
    result = ''.join(stack).lstrip('0')
    return result if result else '0'
tickets = "203"
k = 2
print(reduce_ticket_price(tickets, k))
