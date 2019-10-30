# def check_matching(data):
#     a = []
#     for i in range(len(data)):
#
#         if i == 0 and data[0] == '(':
#             a.append(data[i])
#         elif i == 0 and data[0] == ')':
#             return false
#
#         elif i < len(data):
#             if data[i] == '(':
#                 a.append(data[i])
#
#             elif data[i] == ')':
#                 if len(a) == 0:
#                     return false
#                 else:
#                     a.pop()
#         elif i == len(data)-1:
#             if len(a) != 0:
#                 return false
#
#         else:
#             return false


def check_matching(data):
    a = []
    for i in range(len(data)):
        if data[i] == '(':
            a.append(data[i])

        elif data[i] == ')':
            if len(a) == 0:
                return False
            pop()
    if len(a) != 0:
        return False
    else:
        return True