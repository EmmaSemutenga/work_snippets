# import re
# rounds = 1
# score = 0
# opss = ["5","2","C","D","+"]
# opss = ["1"]
opss = ["5", "-2", "4", "C", "D", "9", "+", "+"]
# print(dir(ops))
# ops[:ops.index("C")] = []
# print(ops.index("5"))
# ops.remove(ops[ops.index("C")-1])
# ops[ops.index("+")] = 100
# print(sum(ops[:2]))
# print(ops)
# print(sum(ops))
# "+"" sum of the previous two scores
# "D" 2 * previous score
# "C" remove previuos score
# print(ops[(ops.index("D")-2) : ops.index("D")])
# item = "-2"
# if item.isdigit():
#     ops[ops.index(item)] = int(item)
# print(int(item))

# print(ops)
# my_nums = [2,4,5,8]
# my_nums.append(sum(my_nums[-2:len(my_nums)]))
# print(my_nums)

def calPoints(ops):
    result = None
    new_ops = []
    # loop through until you find the first letter and start
    for item in ops:
        if "-" in item:
            item = item[-1]
            new_ops.append(-(int(item)))
            # print(type(new_ops[-1]))
        elif item.isdigit():#only works for positive numbers
            # convert number strings to actual nums
            new_ops.append(int(item))
        elif item == "C":
            # "C" remove previuos score
            # ops.remove(ops[(ops.index(item)-1):(ops.index(item)+1)])
            new_ops.pop()
        elif item == "D":
            # "D" 2 * previous score
            # ops[ops.index(item)] = (ops[ops.index(item)-1])*2
            new_ops.append(new_ops[-1]*2)
        elif item == "+":
            # "+"" sum of the previous two scores
            # ops[ops.index(item)] = ops[(ops.index(item)-2):ops.index(item)]
            # print(ops[(ops.index(item)-2):ops.index(item)])
            # print(ops)
            new_ops.append(sum(new_ops[-2:len(new_ops)]))

    print(new_ops)
    result = sum(new_ops)
    return result

print(calPoints(opss))