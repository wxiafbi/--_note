import requests
from PIL import Image
from io import BytesIO

# 设置登录信息
login_url = 'http://124.115.190.134:8501/View/login.htm'
username = 'your_username'
password = 'your_password'

# 创建会话
session = requests.Session()

# 获取验证码
captcha_url = 'https://example.com/captcha'
captcha_response = session.get(captcha_url)
captcha_image = Image.open(BytesIO(captcha_response.content))
captcha_image.show()

# 输入验证码
captcha_code = input('请输入验证码: ')

# 设置登录数据
login_data = {
    'username': username,
    'password': password,
    'captcha': captcha_code
}

# 发送登录请求
response = session.post(login_url, data=login_data)

# 检查登录状态
if response.url == login_url:
    print('登录失败')
else:
    print('登录成功')
