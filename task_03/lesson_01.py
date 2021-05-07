def div():
    try:
        arg1 = int(input("Input dividend "))
        arg2 = int(input("Input divider "))
        res = arg1 // arg2

        if arg2 != 0:
            return arg1 / arg2
        else:
            print("Wrong number! Divider can't be null")

    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong divider! You can't use zero as a divider"

    return res


print(f'result  {div()}')
