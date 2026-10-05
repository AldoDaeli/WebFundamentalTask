import sys
sys.path.append('.')

from oop.scanner import TCPPortScanner
from oop.report import PDFReportExporter, JSONReportExporter

def main():
    print("=== APLIKASI PORT SCANNER & EXPORTER (OOP) ===")
    target = input("Masukkan IP atau Domain target (contoh: 127.0.0.1): ").strip()

    try:
        start = int(input("Masukkan port awal (contoh: 1): "))
        end = int(input("Masukkan port akhir (contoh: 1024): "))
    except ValueError:
        print("[!] Masukkan angka port yang valid.")
        sys.exit(1)

    # 1. Scan port menggunakan OOP
    scanner = TCPPortScanner(target, start, end, timeout=0.4)
    scanner.scan()

    # 2. Ambil hasil scan
    open_ports = scanner.get_open_ports()
    target_ip = scanner.get_target_ip()

    # 3. Export hasil ke PDF dan JSON
    pdf_exporter = PDFReportExporter(target, target_ip, start, end, open_ports)
    pdf_exporter.export()

    json_exporter = JSONReportExporter(target, target_ip, start, end, open_ports)
    json_exporter.export()

if __name__ == "__main__":
    main()