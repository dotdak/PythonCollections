def buy_ticket(n, ls, p):
    num_tickets = ls[p]
    subtract = 0
    for i in range(p):
        if i < num_tickets:
            subtract += num_tickets -i
    for i in range(p + 1, n):
        if i < num_tickets - 1:
            subtract += num_tickets -i - 1
    return (num_tickets - 1)*n + p

if __name__ == '__main__':
    print(buy_ticket(3, [1,2,5], 1))
    print(buy_ticket(5, [2,6,3,4,5], 3))
