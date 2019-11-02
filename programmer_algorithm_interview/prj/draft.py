class User():
    def __init__(self):
        print('User 初始化成功---')

    def __del__(self):
        print('User 对象被回收---')


# 创建一个user对象
u = User()

# 删除该User对象
del u

print('del u -------------')