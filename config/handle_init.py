import configparser

'''
步骤：
1、写入一个文件路径
2、创建对象
3、读取文件
4、获取你要的数据
5、打印数据查看是否有获取到这个数据

file = 'server.ini'  # 1、写入一个文件路径   请使用相对路径，如果在同一个文件夹直接用.调用(或者输入文件名)
cf = configparser.ConfigParser  # 2、创建对象   调用configparsar.ConfigParser即可
cf.read(file)  # 3、读取文件
cf.get('server', 'host')  # 4、调用.get方法获取你要的数据，传参：ini文件中一级目录名字、要获取值的key
'''


class HandleInit(object):
    def load_file(self, file_path):
        '''
        1、加载文件
        传入文件路径，一定要使用相对路径！！！
        如果在同一个文件夹直接用.调用(或者输入文件名)
        :param file:
        :return:
        '''
        cf = configparser.ConfigParser
        cf.read(file_path)
        return cf

    def get_value(self, file_path, key, node=None):
        '''
        4、获取ini文件的Value
        传参：ini文件中一级目录名字、要获取值的key
        （调用.get方法获取你要的数据）
        :param file_path:
        :param key: 必传。如key不在文件中或未传则返回的数据为空
        :param node: 如果不传，默认就读取server里面的值
        :return:
        '''
        if node == None:
            node = 'server'
        try:
            data = self.load_file(file_path).get(node, key)
        except Exception:
            print('没有传递key的值！')
            data = None
        return data


handle_init = HandleInit()
handle_init.get_value()
