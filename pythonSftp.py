import pysftp as sftp


def sftp_example():
    try:
        srv = sftp.Connection(host="192.168.2.80", username="marjan", password="ma")
        remote_path = "/home/marjan/Pictures"
        local_path = "/home/marjan/Pictures/oracle.jpg"
        srv.put(local_path, remote_path)
        srv.close()
    except Exception:
        print("Connection not establish")


if __name__ == "__main__":
    sftp_example()
