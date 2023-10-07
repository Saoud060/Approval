import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
Approval=platform.architecture()[0]
if Approval=="32bit":__import__("usmi32")
elif Approval=="64bit":__import__("usmi64")
