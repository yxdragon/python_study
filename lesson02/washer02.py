print('请选择水位：high/low')
level = input()
# --- 洗衣过程 ---
if level == 'low':
    print('加水20L')
    print('搅拌30分钟')
elif level == 'high':
    print('加水50L')
    print('搅拌60分钟')
# --- 甩干过程 ---
print('放水且甩干')
print('加水30L')
print('搅拌5分钟')
print('甩干')
