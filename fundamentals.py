from datetime import datetime, timedelta


class Member:
    def __init__(self, id_member, nama_member):
        self.id_member = id_member
        self.nama_member = nama_member
class Ruangan:
    def __init__(self, id_ruangan, nama_ruangan, capacity):
        self.id_ruangan = id_ruangan
        self.nama_ruangan = nama_ruangan
        self.capacity = capacity

    def validateBooking(self, participants = 1):
        if participants > self.capacity:
            raise ValueError("Jumlah peserta melebihi kapasitas ruangan")

class GedungF(Ruangan):
    def __init__(self, id_ruangan, nama_ruangan, capacity):
        super().__init__(id_ruangan, nama_ruangan, capacity)
    
    def validateBooking(self, participants = 1):
        super().validateBooking(participants)

class GedungG(Ruangan):
    def __init__(self, id_ruangan, nama_ruangan, capacity, jumlah_gpu):
        self.jumlah_gpu = jumlah_gpu
        super().__init__(id_ruangan, nama_ruangan, capacity)

    def validateBooking(self, participants = 1):
        super().validateBooking(participants)

class Reservasi:
    def __init__(self, id_reservasi, id_member, id_ruangan, jam_mulai, durasi, jumlah_orang):
        if durasi <= 0:
            raise ValueError("Durasi harus lebih besar dari 0")
        self.id_reservasi = id_reservasi
        self.id_member = id_member
        self.id_ruangan = id_ruangan
        self.jam_mulai = jam_mulai
        self.durasi = durasi
        self.jumlah_orang = jumlah_orang
        self.status = "ACTIVE"

    @property
    def get_jamslesai(self):
        return self.jam_mulai + timedelta(hours=self.durasi)
    
    def is_terjadwal(self, jam_mulai, jam_slesai):
        if self.status != "ACTIVE":
            return False
        jam_slesai_lainnya = jam_mulai + timedelta(hours=jam_slesai)

        return max(self.jam_mulai, jam_mulai) < min(self.jam_slesai, jam_slesai_lainnya)

    def batalkan_reservasi(self):
        if self.status == "CANCELLED":
            raise ValueError("Udah di cancel")
        self.status = "CANCELLED"

class BookingRuangan:
    def __init__(self):
        self.member = {}
        self.ruangan = {}
        self.reservasi = {}
    
    def tambah_member(self, member: Member):
        if member.id_member in self.member:
            raise ValueError("Member sudah ada")
        self.member[member.id_member] = member

    def tambah_ruangan(self, ruangan: Ruangan):
        if ruangan.id_ruangan in self.ruangan:
            raise ValueError("Ruangan sudah ada")
        self.ruangan[ruangan.id_ruangan] = ruangan

    def buat_reservasi(self, id_ruangan, id_reservasi, id_member, jam_mulai, durasi, participants = 1):
        member = self.member[id_member]
        ruangan = self.ruangan[id_ruangan]

        ruangan.validateBooking(participants)

        for res in self.reservasi.values:
            if res.ruangan.id_ruangan == id_reservasi and res.is_terjadwal(jam_mulai, durasi):
                raise ValueError("Ruangan sudah ada yang reservasi di jam tersebut")
        
        res = Reservasi(id_reservasi, id_member, id_ruangan, jam_mulai, participants)
        self.reservasi[id_reservasi] = res
        return res
    
    def cancel_reservasi(self, id_reservasi):
        if id_reservasi not in self.reservasi:
            raise ValueError("Reservasi tidak ditemukan")
        self.reservasi[id_reservasi].batalkan_reservasi()
    

booking = BookingRuangan()

booking.tambah_ruangan(GedungF("F01", "Ruang Kelas F2", 100))
booking.tambah_ruangan(GedungF("F02", "Ruang Kelas F2", 100))
booking.tambah_ruangan(GedungG("G01", "Ruang AI F2", 100, 2))
booking.tambah_ruangan(GedungG("G02", "Ruang AI F2", 100, 2))


