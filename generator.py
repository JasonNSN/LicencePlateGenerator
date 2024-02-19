import numpy as np
import cv2
from generate_plate_number import provinces_idx
from generate_plate_number import generate_plate_num


def get_char_location(plate_type=0):
    """
    获取各字符在车牌中的坐标
    plate_type：车牌号类型，0为绿牌，1为蓝牌
    """
    length = 8 if plate_type == 0 else 7  # 车牌字符数，7为蓝牌、8为绿牌
    char_location = np.zeros((length, 4), dtype=np.int32)  # [左上x，左上y，右上x，右上y]
    # x轴方向
    space_pro_char1 = 34 if plate_type == 1 else 49  # 发牌机关代号与第一个字符之间的间距
    space_char = 12 if plate_type == 1 else 9  # 各字符之间的间距
    width_char = 45  # 字符宽度（蓝牌所有字符宽度为45，绿牌省份简称字符宽度为45，其余字符宽度均为43，在下方会有更改）
    for i in range(length):
        if i == 0:
            char_location[i, 0] = 15  # 省份简称字符和车牌左端的间距（绿牌为15.5，舍入为15）
        elif i == 2:
            char_location[i, 0] = char_location[i - 1, 2] + space_pro_char1  # 字符左端坐标
        else:
            char_location[i, 0] = char_location[i - 1, 2] + space_char  # 字符左端坐标
        if length == 8 and i > 0:
            width_char = 43  # 绿牌非首字符宽度为43
        char_location[i, 2] = char_location[i, 0] + width_char  # 字符右端坐标
    # y轴方向
    char_location[:, 1] = 25  # 字符顶端坐标（字符顶端与车牌顶端间距 = 25）
    char_location[:, 3] = 115  # 字符底端坐标（字符底端与车牌顶端间距 = 25 + 90）
    return char_location


def generate_plate(plate_num, save_dir):
    """
    生成车牌图片
    plate_num：车牌号
    plate_model_dir：车牌底牌文件夹
    char_model_dir：字符文件夹
    """
    plate_type = 0 if len(plate_num) == 8 else 1  # 车牌号类型，0为绿牌，1为蓝牌
    if plate_type == 0:
        # 绿牌
        char_location = get_char_location(plate_type)  # 字符坐标
        img_plate = cv2.imread('./plate_bgs/green.png')
        for i in range(len(plate_num)):
            # 对单个字符逐个粘贴至车牌底牌
            s = plate_num[i]
            img_char = cv2.imread('./chars/green_' +
                                  ('p' + str(provinces_idx.index(s)) if '\u4e00' <= s <= '\u9fff' else s) + '.jpg')
            location = char_location[i]
            left_top = (location[0] * 2, location[1] * 2)  # 左上角坐标
            right_bottom = (location[2] * 2, location[3] * 2)  # 右下角坐标
            img_plate[left_top[1]: right_bottom[1], left_top[0]: right_bottom[0]] = np.where(
                img_char < 128, 0,
                img_plate[left_top[1]: right_bottom[1], left_top[0]: right_bottom[0]])
        cv2.imencode('.jpg', img_plate)[1].tofile(save_dir + '/' + plate_num + '.jpg')  # 保存文件，避免中文乱码
        # cv2.imshow('', img_plate)
        # cv2.waitKey(0)
    else:
        # 蓝牌
        char_location = get_char_location(plate_type)  # 字符坐标
        img_plate = cv2.imread('./plate_bgs/blue.png')
        for i in range(len(plate_num)):
            # 对单个字符逐个粘贴至车牌底牌
            s = plate_num[i]
            img_char = cv2.imread('./chars/blue_' +
                                  ('p' + str(provinces_idx.index(s)) if '\u4e00' <= s <= '\u9fff' else s) + '.jpg')
            location = char_location[i]
            left_top = (location[0] * 2, location[1] * 2)  # 左上角坐标
            right_bottom = (location[2] * 2, location[3] * 2)  # 右下角坐标
            img_plate[left_top[1]: right_bottom[1], left_top[0]: right_bottom[0]] = np.where(
                img_char < 128, 255,
                img_plate[left_top[1]: right_bottom[1], left_top[0]: right_bottom[0]])
        cv2.imencode('.jpg', img_plate)[1].tofile(save_dir + '/' + plate_num + '.jpg')  # 保存文件，避免中文乱码
        # cv2.imshow('', img_plate)
        # cv2.waitKey(0)
    return img_plate


if __name__ == '__main__':
    for _ in range(10):
        plate_num = generate_plate_num(1, '甘')  # 0绿1蓝
        generate_plate(plate_num, './plates_res')
    # print(get_char_location())
    # generate_plate('京AD12345', './plates_res')
