import random


def random_mobile():
    """随机生成手机号替换动态参数"""
    # db = ReadSQL()
    # while True:
    mobile = '13'
    for i in range(9):
        num = random.randint(0, 9)
        mobile += str(num)
        # 数据库中查找该手机号是否存在
        # sql = "select * from member where MobilePhone='{}';".format(phone)
        # if not db.find_one(sql):
    return mobile


class RandomName():
    def GBK2312(self):
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
        val = f'{head:x}{body:x}'
        st = bytes.fromhex(val).decode('gb2312')
        return st

    def first_name(self):  # 随机取姓氏字典
        first_name_list = [
            '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
            '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
            '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
            '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
            '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
            '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
            '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
        n = random.randint(0, len(first_name_list) - 1)
        f_name = first_name_list[n]
        return f_name

    def second_name(self):
        # 随机取数组中字符，取到空字符则没有second_name
        second_name_list = [self.GBK2312(), '']
        n = random.randint(0, 1)
        s_name = second_name_list[n]
        return s_name

    def last_name(self):
        return self.GBK2312()

    def create_name(self):
        n = random.randint(1, 2)
        name = ''
        for i in range(n):
            s = self.GBK2312()
            name = name + s
        return self.first_name() + name


randomname = RandomName()

