import socket
import sys
from datetime import datetime

class BaseScanner:
    """Class abstrak sebagai blueprint scanner jaringan."""

    def __init__(self, host, start_port, end_port):
        self._host = host
        self._start_port = start_port
        self._end_port = end_port
        self._open_ports = []

    def scan(self):
        """Method yang wajib diimplementasi oleh child class."""
        raise NotImplementedError("Method scan() harus diimplementasi.")

    def get_open_ports(self):
        return self._open_ports

    def get_host(self):
        return self._host


class TCPPortScanner(BaseScanner):
    """Child class yang mengimplementasi scanning port TCP."""

    def __init__(self, host, start_port, end_port, timeout=0.5):
        super().__init__(host, start_port, end_port)
        self._timeout = timeout
        self._target_ip = self._resolve_host()

    def _resolve_host(self):
        """Mengubah hostname menjadi IP address."""
        try:
            return socket.gethostbyname(self._host)
        except socket.gaierror:
            print("\n[!] Host tidak dapat diselesaikan.")
            sys.exit(1)

    def get_target_ip(self):
        return self._target_ip

    def scan(self):
        """Implementasi scanning port TCP."""
        print("-" * 50)
        print(f" Memindai Target IP : {self._target_ip}")
        print(f" Rentang Port       : {self._start_port} - {self._end_port}")
        print(f" Waktu Mulai        : {str(datetime.now())}")
        print("-" * 50)

        try:
            for port in range(self._start_port, self._end_port + 1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(self._timeout)
                result = s.connect_ex((self._target_ip, port))
                s.close()

                if result == 0:
                    print(f"[+] Port {port} : TERBUKA")
                    self._open_ports.append(port)

        except KeyboardInterrupt:
            print("\n[!] Pemindaian dibatalkan.")

        print("-" * 50)
        print(f" Selesai. Total port terbuka: {len(self._open_ports)}")
        print("-" * 50)