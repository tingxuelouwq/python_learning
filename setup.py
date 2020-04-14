from distutils.core import setup

setup(
    name='demo',    # 对外我们模块的名字
    version='1.0',  # 版本号
    description='这是第一个对外发布的模块',  #描述
    author='kevin', # 作者
    author_email='kevin@163.com',
    py_modules=['pkg.module_A','pkg.module_A2','pkg.aa.module_AA'] # 要发布的模块
)
