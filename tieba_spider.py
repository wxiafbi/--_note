class spider:
    def __init__(self, tieba_name):

        self.url = 'https://tieba.baidu.com/f?kw='+tieba_name+'&ie=utf-8&pn={}'.format()

    def get_url_list(self):

        return [self.url.format(i*50) for i in range(20)]

    def run(self):
        pass
        '''1.获取url'''
        '''2.get请求内容'''
        '''3.保存网页'''



if __name__=='__main__':
    pass