'''
    爬取虎牙直播王者荣耀直播区的主播名字和观看人数的数据，并进行排序处理
'''

'''
    导入必要的包
'''
# 导入正则表达式的包
import re 

# 绕过ssl校验
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 导入获取html的包
from urllib import request

class Spider():
    '''
        This is a class
    '''

    '''定义必要的类变量'''
    url = 'https://www.huya.com/g/wzry' # 爬取的地址，存储在url变量中
    list_pattern = '<li class="game-live-item" gid="[\d]*" data-lp="[\d]*"([\s\S]*?)</li>' # 最大范围的正则表达式
    name_pattern = '<i class="nick" title="[\s\S]*?"([\s\S]*?)</i>' # 主播名字的正则表达式
    number_pattern = '<i class="js-num"([\s\S]*?)</i>' # 观看人数的正则表达式
    # 对比原示例代码，在前一个标签中去除了'>'，因为网页可能要给名字和人数添加样式，此时正则表达式会不对应

    '''
        这是一个获取页面数据，并转换为字符串的函数。
    '''
    def __fetch_content(self):
        r = request.urlopen(Spider.url) # 请求访问url地址
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    '''
        这是一个通过正则表达式获取目标字符串的函数。
    '''
    def __analysis(self, htmls):
        list_html = re.findall(Spider.list_pattern, htmls) # 获取最大匹配范围字符串的结果
        anchors = []
        for html in list_html:
            unfinal_name = re.findall(Spider.name_pattern, html) # 获取名字(不是纯名字字符串)
            name = re.findall('>([\s\S]*)', unfinal_name[0]) # 提纯名字字符串
            unfinal_number = re.findall(Spider.number_pattern, html) # 获取观看人数
            number = re.findall('>([\s\S]*)', unfinal_number[0]) # 提纯人数字符串
            anchor = {'name' : name[0], 'number' : number[0]} # 组成一个字典的形式,注意name和number的类型
            anchors.append(anchor) # 将字典添加到列表中
        return anchors
    
    '''
        这是一个处理字典格式的函数。
        通过修改前面的代码，可以省略这部分函数。
    '''
    # def __refine(self, anchors):
    #     l = lambda anchor:{
    #         'name' : anchor['name'][0].strip(),
    #         'number' : anchor['number'][0]
    #     }
    #     return map(l, anchors) # 将列表中的字典进行规整处理

    '''
        这是一个排序的主函数。
    '''
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    '''
        这是一个排序的辅助函数。
    '''
    def __sort_seed(self, anchor):
        s_number_pattern = '[1-9]\d*\.?\d*' # 匹配人数，包括特殊格式的人数如：1.8万人（存在以万为单位的人数）
        r = re.findall(s_number_pattern, anchor['number']) 
        number = float(r[0]) # 人数以万为单位时可能存在小数点
        if '万' in anchor['number']:
            number *= 10000
        return number

    '''
        这是一个打印结果的函数。
    '''
    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            # print(f"rank{(rank + 1)}: {anchors[rank]['name']} {anchors[rank]['number']}")
            print('rank' + str(rank+1) + ": " + anchors[rank]['name'] + ' ' + anchors[rank]['number'])

    '''
        这是一个流程控制函数。
    '''
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        # anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)
    
'''
    实例化对象，执行流程控制函数。
'''
spider = Spider()
spider.go()

"""
    代码的不足：
    1、无法实现刷新抓取数据。
    2、只能抓取一个页面的数据，不能换页抓取。
    3、正则表达式在网页后台代码改变时很可能不能有效适配，抗变化能力弱。
"""
'''
    代码与示例代码的不同（改进）：
    1、正则表达式的优化：
        由于注意到网页可能在标签中加其他的样式代码，此时原来的正则表达式就会失效，
        所以修改了正则表达式，通过二次提取来获得姓名和人数数据。
    2、删除了非必要的__refine函数。
'''