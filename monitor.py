import psutil
import time
import datetime

from tkinter import Tk, Label, messagebox, Button
import threading

freetime = [[12*60, 13*60+40], [22*60+20, 22*60+40]]

# Configuration
TARGET_APPS = {
    "原神.exe": 10,  
    "chrome.exe": 10,   
    'msedge.exe': 10,
    'wechat.exe': 10,
    'qq.exe': 10,
    'team.exe': 10,
    'Discord.exe': 10,
    'Blender.exe': 10,
    'Unity.exe': 10,
    # Add your target apps here
}

# Record app usage time and reminder windows
app_usage_time = {}
app_reminder_windows = {}
app_name=[]
def get_app_processes():
    """Get all running processes of a specified app"""
    target_processes = []
    for proc in psutil.process_iter(['name']):
        if not(proc.info['name'] in app_name):
            target_processes.append(proc)
            print(proc)
    return target_processes

def show_reminder(app_name, remaining_time):
    """显示提醒窗口"""
    if app_name in app_reminder_windows:
        app_reminder_windows[app_name].destroy()
    root = Tk()
    root.withdraw()  # 隐藏主窗口
    label = Label(root, text=f"{app_name}将在{remaining_time}分钟后关闭。")
    label.pack()
    button = Button(root, text="我知道了", command=lambda: root.destroy())
    button.pack()
    app_reminder_windows[app_name] = root
    root.after(remaining_time*60000, lambda: root.destroy())  # 设置窗口在剩余时间后自动关闭
    root.mainloop()  # Keep the window open until it's closed

def kill_process(proc, app_name):
    """Kill a process"""
    try:
        
        proc.terminate()
    except Exception as e:
        print(f"Failed to kill process {app_name}: {e}")

def print_monitored_processes():
    while True:
        monitored_processes = [proc['app_name'] for proc in app_usage_time.values() if 'app_name' in proc]
        #print(f"Monitored processes: {', '.join(monitored_processes)}")
        time.sleep(20)

threading.Thread(target=print_monitored_processes).start()

def monitor_apps():
    """Monitor multiple apps' usage time and show reminders"""
    while True:
        current_time = time.time()
        with open("running_processes.txt", "a") as f:
            
            if True :
                for app_name, max_time in TARGET_APPS.items():
                    for proc in get_app_processes(app_name):
                        if proc.pid not in app_usage_time:
                            
                            app_usage_time[proc.pid] = {'app_name': app_name, 'start_time': current_time}
                            f.write(f"Running processes at {current_time}\n")
                            f.write(f"  - {app_name} (PID: {proc.pid})\n")
                        elif (current_time - app_usage_time[proc.pid]['start_time']) / 60 > (max_time - 1):
                            # Show reminder if usage time is about to reach limit
                            show_reminder(app_name, 1)
                            # Add logic to kill process if needed
                            if (current_time - app_usage_time[proc.pid]['start_time']) / 60 > max_time:
                                for i in proc:
                                    #kill all progress named app_name
                                    [proc['app_name'] for proc in app_usage_time.values() if 'app_name' in proc]
                                    kill_process(proc, app_name)
                                f.write(f"kill process{app_name} at {current_time}\n")
                                app_usage_time.pop(proc.pid, None)
            

if __name__ == "__main__":
    monitor_apps()