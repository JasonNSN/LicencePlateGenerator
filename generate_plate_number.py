import numpy as np

"""随机生成规避规范的车牌号"""

# 省份
provinces = {
    "京": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z'],
    "津": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z'],
    "冀": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'R', 'T'],
    "晋": ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'J', 'K', 'L', 'M'],
    "蒙": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M'],
    "辽": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P'],
    "吉": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'],
    "黑": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R'],
    "沪": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z'],
    "苏": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N'],
    "浙": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L'],
    "皖": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S'],
    "闽": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'],
    "赣": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M'],
    "鲁": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'U', 'V', 'Y'],
    "豫": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'U'],
    "鄂": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S'],
    "湘": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'S', 'U'],
    "粤": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y'],
    "桂": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R'],
    "琼": ['A', 'B', 'C', 'D', 'E', 'F'],
    "渝": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z'],
    "川": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z'],
    "贵": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J'],
    "云": ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S'],
    "藏": ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    "陕": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'V'],
    "甘": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P'],
    "青": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    "宁": ['A', 'B', 'C', 'D', 'E'],
    "新": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R']
}
provinces_idx = ["京", "津", "冀", "晋", "蒙", "辽", "吉", "黑", "沪",
                 "苏", "浙", "皖", "闽", "赣", "鲁", "豫", "鄂", "湘",
                 "粤", "桂", "琼", "渝", "川", "贵", "云", "藏", "陕",
                 "甘", "青", "宁", "新"]
# 阿拉伯数字
nums = ['{}'.format(x) for x in range(10)]

# 英文字母（除I和O外）
# chr用于将数字转为对应的ASCII码，ord反之
letters = [chr(x + ord('A')) for x in range(26) if not chr(x + ord('A')) in ['I', 'O']]


def random_select_one(lst):
    """从给定的列表中随机选择一个元素"""
    return np.random.choice(lst, 1, replace=False)[0]


def generate_plate_num(plate_type=0, province='甘'):
    """
    随机生成车牌号
    plate_type：车牌号类型，0为绿牌，1为蓝牌
    province：省份
    """
    if plate_type == 0:
        # 绿牌：第一位序号使用L及以后的英文字母（除O外），其余5位使用数字
        res = province + random_select_one(provinces.get(province))
        letters_for_green = letters[letters.index('L'):]  # L及以后的英文字母（除O外）
        res += random_select_one(letters_for_green)
        for _ in range(5):
            # 生成数字
            res += random_select_one(nums)
    else:
        # 蓝牌：5位车牌号中使用3位英文字母（除I和O）或使用不存在的发牌机关代号，两种方式随机选择
        sel_num = np.random.randint(0, 2)
        if province in ['京', '津', '沪', '渝'] or sel_num == 0:
            # 5位车牌号中使用3位英文字母（除I和O）
            res = province + random_select_one(provinces.get(province))
            letter_idx = list(np.random.choice(5, 3, replace=False))  # 使用英文字母的位置
            for idx in range(5):
                if idx in letter_idx:
                    # 生成字母
                    res += random_select_one(letters)
                else:
                    # 生成数字
                    res += random_select_one(nums)
        else:
            # 使用不存在的发牌机关代号，setdiff1d用于求差集（前有后没有的元素）
            res = province + random_select_one(np.setdiff1d(letters, provinces.get(province)))
            letter_num = np.random.randint(0, 3)  # 英文字母的个数
            letter_idx = []
            if letter_num > 0:
                letter_idx = list(np.random.choice(5, letter_num, replace=False))  # 使用英文字母的位置
            for i in range(5):
                if i in letter_idx:
                    # 生成字母
                    res += random_select_one(letters)
                else:
                    # 生成数字
                    res += random_select_one(nums)
    return res


if __name__ == '__main__':
    for i in range(10):
        print(generate_plate_num(0, '甘'))
