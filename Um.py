import os
import platform

# Check for updates from the Git repository
os.system('git pull')

Approval = platform.architecture()[0]

if Approval == "32bit":
    import usmi32
elif Approval == "64bit":
    import usmi64
