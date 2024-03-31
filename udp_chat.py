import subprocess

def run_script(script_name):
    command = ['python', script_name]
    subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)

if __name__ == "__main__":
    run_script('udp_chat_recver.py')
    run_script('udp_chat_sender.py')