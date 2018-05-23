def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    number1 = 0
    while len(l1) != 0:
        l1_length = len(l1) - 1
        digit1 = l1.pop()
        number1 = number1 + digit1*pow(10,l1_length)
        
    number2 = 0
    while len(l2) != 0:
        l2_length = len(l2) - 1
        digit2 = l2.pop()
        number2 = number2 + digit2*pow(10,l2_length)

    return number1+number2


if __name__ == "__main__":
    l1 = [2,4,3]
    l2 = [5,6,4]
    print (addTwoNumbers(l1, l2))
