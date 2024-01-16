import subprocess
import time

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
        subprocess.run(['python', script_path])
    except Exception as e:
        print(f"Error running script: {e}")

# 循环运行的次数，可以根据需要更改
num_runs = 1000

# 循环
for i in range(num_runs):
    print(f"Running script iteration {i + 1}")
    
    # 调用运行另一个脚本的函数
    run_another_script1()
    
    # 等待一段时间，可以根据需要更改
    time.sleep(5)  # 等待5秒钟
    
    # 调用运行另一个脚本的函数
    run_another_script2()
    
    # 等待一段时间，可以根据需要更改
    time.sleep(5)  # 等待5秒钟