import openpyxl


class CaseData(object):
    """测试数据类"""
    def __init__(self,zip_obj):
        # 遍历打包好的测试数据对象
        for i in zip_obj:
            # 将每一个表格数据的表头作为属性，值作为属性值
            setattr(self,i[0],i[1])


class ReadExcel(object):
    """读取excel文件类"""

    def __init__(self, file_name, sheet_name):
        """
        初始化excel文件对象
        file_name:excel文件名
        sheet_name:excel表单名
        """
        self.file_name = file_name
        self.sheet_name = sheet_name

    def open(self):
        # 打开excel文件，返回一个工作簿对象
        self.wb = openpyxl.load_workbook(self.file_name)
        # 通过工作簿对象，选择表单
        self.sh = self.wb[self.sheet_name]

    def read_excel_obj(self):
        # 调用open()方法，打开excel文件和选择表单
        self.open()
        # 创建一个空列表，用于存放所有测试数据
        cases = []
        # 按行获取所有表格对象，每一行的内容放在一个元组中，以列表形式返回
        rows = list(self.sh.rows)
        # 获取表头
        titles = [t.value for t in rows[0]]
        # 遍历其他行的数据，和表头进行打包
        for row in rows[1:]:
            # 获取每行数据
            data = [i.value for i in row]
            # 和表头打包,生成zip对象
            zip_obj = zip(titles,data)
            # 通过CaseData类创建测试数据对象，将zip_obj作为参数
            case_data = CaseData(zip_obj)
            cases.append(case_data)
        # 将包含所有测试数据的列表cases返回
        return cases

    def write(self,row,column,value):
        """
        row:写入的行
        column:写放的列
        value:写入的内容
        """
        # 打开文件
        self.open()
        # 按照传入的行、列、内容进行写入
        self.sh.cell(row=row,column=column,value=value)
        # 保存生效
        self.wb.save(self.file_name)

