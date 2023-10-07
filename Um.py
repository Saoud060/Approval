import subprocess
import platform

# Replace 'um.so_url' with the raw URL to the 'um.so' file on GitHub.
um_so_url = "https://github.com/Saoud060/Approval/raw/main/um.so"

# Determine the architecture of your Android device.
architecture = platform.architecture()[0]

if "64" in architecture:
    # 64-bit architecture
    arch_dir = "x86_64"  # Update this according to the architecture of your um.so file
else:
    # 32-bit architecture
    arch_dir = "x86"  # Update this according to the architecture of your um.so file

# Download the shared object file.
subprocess.run(["curl", "-o", "um.so", um_so_url])

# Run the shared object file based on the architecture.
try:
    subprocess.run([f"./{arch_dir}/um.so"])
except Exception as e:
    print(f"Error: {e}")
