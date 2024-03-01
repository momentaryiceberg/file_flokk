import shutil

def move_files():
    target = 'C:\\ostur.txt'
    destination = 'C:\\samloka'
    shutil.move(target, destination)

def find_executable_files():
    """shutil.which() method tells the path to an executable application that would be run if the given cmd was called. This method can be used to find a file on a computer which is present on the PATH."""
    cmd = 'anaconda'
    locate = shutil.which(cmd)
    print(locate)
    # D:\Installation_bulk\Scripts\anaconda.EXE

