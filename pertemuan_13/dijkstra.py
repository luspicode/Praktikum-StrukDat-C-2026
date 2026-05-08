class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_kota(self, nama):
        if nama not in self.graph:
            self.graph[nama] = []

    def tambah_jalan(self, u, v, jarak):
        self.tambah_kota(u)
        self.tambah_kota(v)

        self.graph[u].append((v, jarak))
        self.graph[v].append((u, jarak))

        print(f'Menambahkan jalan: {u} - {v} ({jarak} km)')

    def tampilkan_graph(self):
        print("\nStruktur Jaringan Distribusi:")

        for kota in self.graph:
            tetangga = []

            for tujuan, jarak in self.graph[kota]:
                tetangga.append(f"{tujuan} ({jarak})")

            print(f"- {kota} terhubung ke: {', '.join(tetangga)}")

    def dijkstra(self, kota_asal):
        jarak = {}

        for kota in self.graph:
            jarak[kota] = float('inf')

        jarak[kota_asal] = 0

        sudah_dikunjungi = []

        while len(sudah_dikunjungi) < len(self.graph):

            kota_terdekat = None
            jarak_terkecil = float('inf')

            for kota in self.graph:
                if kota not in sudah_dikunjungi and jarak[kota] < jarak_terkecil:
                    jarak_terkecil = jarak[kota]
                    kota_terdekat = kota

            if kota_terdekat is None:
                break

            sudah_dikunjungi.append(kota_terdekat)

            for tetangga, bobot in self.graph[kota_terdekat]:

                jarak_baru = jarak[kota_terdekat] + bobot

                if jarak_baru < jarak[tetangga]:
                    jarak[tetangga] = jarak_baru

        return jarak


print("SISTEM NAVIGASI LOGISTIK 'KILAT MAJU'")
print("=" * 45)

g = Graph()

g.tambah_jalan("Jakarta", "Bandung", 150)
g.tambah_jalan("Jakarta", "Cirebon", 200)
g.tambah_jalan("Bandung", "Tasikmalaya", 100)
g.tambah_jalan("Bandung", "Cirebon", 130)
g.tambah_jalan("Cirebon", "Semarang", 250)
g.tambah_jalan("Tasikmalaya", "Semarang", 200)

g.tampilkan_graph()

print("\nMenghitung rute terpendek dari: Jakarta...")

hasil = g.dijkstra("Jakarta")

print("\nJarak Terpendek dari Jakarta:")

nomor = 1

for kota, jarak in hasil.items():
    if kota != "Jakarta":
        print(f"{nomor}. Ke {kota}: {jarak} km")
        nomor += 1

print("=" * 45)
print("Simulasi Navigasi Selesai!")