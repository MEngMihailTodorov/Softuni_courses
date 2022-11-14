def negative_vs_positive(numb):

    def negative_sum(num):
        neg_sum = 0
        for el in num:
            if el < 0:
                neg_sum += el
            else:
                pass
        return neg_sum

    def positive_sum(n):
        pos_sum = 0
        for el in n:
            if el > 0:
                pos_sum += el
            else:
                pass
        return pos_sum

    print(negative_sum(numb))
    print(positive_sum(numb))

    if abs(positive_sum(numb)) > abs(negative_sum(numb)):
        return "The positives are stronger than the negatives"
    return "The negatives are stronger than the positives"


numbers = list(map(int, input().split()))
print(negative_vs_positive(numbers))