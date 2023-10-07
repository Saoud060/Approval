import os

os.system("xdg-open https://www.youtube.com/@awanoficialchannel")

try:
    import AWN32
except ImportError as e:
    if "dlopen failed" in str(e):
        import um
