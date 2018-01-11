def wash(level):
    # --- 洗衣过程 ---
    if level == 'low':
        print('加水20L')
        print('搅拌30分钟')
    elif level == 'high':
        print('加水50L')
        print('搅拌60分钟')

def dry(times):
    # --- 甩干过程 ---
    print('放水且甩干')
    for i in range(times):
        print('加水30L')
        print('搅拌5分钟')
        print('甩干')

'''
aadf
fsdasda
'''
# ** key
def wash_dry(obj, level='low', times=1):
    '''
    欢迎使用
    obj:投入衣物
    level:设定水位
    times:甩干次数
    '''
    print('=== 开始洗衣 ===')
    wash(level)
    dry(times)
    print('%s 洗干净了'%obj)
    
if __name__ == '__main__':
    wash_dry('衣服')
    wash_dry('毛毯', 'high', 3)
    wash_dry('被套', times=2)
