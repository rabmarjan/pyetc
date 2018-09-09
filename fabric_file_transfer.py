from fabric.api import execute, put
from fabric.network import disconnect_all


if __name__ == "__main__":
    import sys
    # specify hostname to connect to and the remote/local paths
    srcdir, remote_dirname, hostname = sys.argv[1:]
    try:
        s = execute(put, '/home/marjan/Desktop/', '/home/marjan/Pictures/hello', host='192.168.2.80')
        print(repr(s))
    finally:
        disconnect_all()