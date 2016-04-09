# -*- coding: utf-8 -*-
""" Convert to Chinese numerals """


# Define exceptions
class NotIntegerError(Exception):
    pass


def to_chinese(number):
    """ convert integer to Chinese numeral """

    chinese_numeral_dict = {
        '0': '零',
        '1': '一',
        '2': '二',
        '3': '三',
        '4': '四',
        '5': '五',
        '6': '六',
        '7': '七',
        '8': '八',
        '9': '九'
    }
    chinese_unit_map = [('', '十', '百', '千'),
                        ('万', '十万', '百万', '千万'),
                        ('亿', '十亿', '百亿', '千亿'),
                        ('兆', '十兆', '百兆', '千兆'),
                        ('吉', '十吉', '百吉', '千吉')]
    chinese_unit_sep = ['万', '亿', '兆', '吉']

    reversed_n_string = reversed(str(number))

    result_lst = []
    unit = 0

    for integer in reversed_n_string:
        if integer is not '0':
            result_lst.append(chinese_unit_map[unit // 4][unit % 4])
            result_lst.append(chinese_numeral_dict[integer])
            unit += 1
        else:
            if result_lst and result_lst[-1] != '零':
                result_lst.append('零')
            unit += 1

    result_lst.reverse()

    # clean convert result, make it more natural
    if result_lst[-1] is '零':
        result_lst.pop()

    result_lst = list(''.join(result_lst))

    for unit_sep in chinese_unit_sep:
        flag = result_lst.count(unit_sep)
        while flag > 1:
            result_lst.pop(result_lst.index(unit_sep))
            flag -= 1

    '''
    length = len(str(number))
    if 4 < length <= 8:
        flag = result_lst.count('万')
        while flag > 1:
            result_lst.pop(result_lst.index('万'))
            flag -= 1
    elif 8 < length <= 12:
        flag = result_lst.count('亿')
        while flag > 1:
            result_lst.pop(result_lst.index('亿'))
            flag -= 1
    elif 12 < length <= 16:
        flag = result_lst.count('兆')
        while flag > 1:
            result_lst.pop(result_lst.index('兆'))
            flag -= 1
    elif 16 < length <= 20:
        flag = result_lst.count('吉')
        while flag > 1:
            result_lst.pop(result_lst.index('吉'))
            flag -= 1
    '''

    return ''.join(result_lst)


if __name__ == '__main__':
    foo = ''
    for i in range(1, 100001):
        foo += to_chinese(i) + '\n'
    print(foo)
#        print('对不起,第{0}遍'.format(to_chinese(i)))
