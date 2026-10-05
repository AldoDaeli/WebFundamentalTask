from  abc import ABC, abstractclassmethod

class Notifikasi(ABC):
    def __init__(self, penerima):
        self.penerima = penerima

    @abstractclassmethod 
    def kirim_pesan(self, pesan):
        pass

class NotifikasiTelegram(Notifikasi):
    pass

class NotifikasiWhatsApp(Notifikasi):
    def kirim_pesan(self, pesan):
        print(f"SENT TO: {self.penerima}: '{pesan}'")

wa = NotifikasiWhatsApp("08123456789")
wa.kirim_pesan("Halo, ini uji coba pesan WhatsApp.")

# Test 1 - uncomment untuk uji kontrak
#basis = Notifikasi("test")

# Test 2 - uncomment untuk uji kontrak
tele = NotifikasiTelegram("user_tele")