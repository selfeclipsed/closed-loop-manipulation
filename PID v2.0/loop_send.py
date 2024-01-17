import subprocess
import time

# 路径点
path = [[650, 550], [550, 550], [550, 450], [550, 350], [650, 350], [650, 250], [550, 150], [550, 150], [450, 150], [350, 150], [350, 250], [350, 350], [350, 450], [250, 450], [150, 450], [150, 350], [150, 250], [150, 150], [150, 50]]

current_run = 1

def run_another_script1():
    try:
        # 在这里替换成你想要运行的脚本的路径
        script_path = 'C:/python programs/closed-loop direction.py'
        
        # 使用subprocess运行脚本
        subprocess.run(['python', script_path])
    except Exception as e:
        print(f"Error running script: {e}")

def run_another_script2():
    try:
        # 在这里替换成你想要运行的脚本的路径
        script_path = 'C:/python programs/closed-loop control.py'
        
        # 使用subprocess运行脚本
        subprocess.run(['python', script_path ,str(current_run)])
    except Exception as e:
        print(f"Error running script: {e}")

# 循环运行的次数，可以根据需要更改
num_runs = 1000

# 循环
for i in range(num_runs):
    
    flag1=False
    flag2=False

    print(f"Running script iteration {i + 1}")
    
    # 调用运行另一个脚本的函数
    run_another_script1()
    
    # 检测状态
    f=open('C:/python programs/test.txt','r')
    if(f.read()=='0') :
        flag1=True
    f.close()
    
    # 等待一段时间，可以根据需要更改
    time.sleep(0.5)  # 等待0.5秒钟
    
    # 调用运行另一个脚本的函数
    run_another_script2()
    
    # 检测状态
    f=open('C:/python programs/test.txt','r')
    if(f.read()=='0') :
        flag2=True
    f.close()
    
    # 等待一段时间，可以根据需要更改
    time.sleep(0.5)  # 等待0.5秒钟

    # 判断是否需要进入下一个点
    if(flag1==True and flag2==True):
        current_run += 1