euro = [1,2,5,10,20,50,100,200,300,500]

def how_to_pay(amount,currency):
    currency.sort(reverse = True)
    answer ={}
    for a in currency:
        answer[a] = 0
        while amount - a >= 0:
            answer[a] += 1
            amount -= a
        if answer[a] == 0:
            answer.pop(a)
    return answer

print(how_to_pay(533,euro))
