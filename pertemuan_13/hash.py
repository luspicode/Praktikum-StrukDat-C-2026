class HashTable:
    def __init__(self, ukuran=10):
        self.ukuran = ukuran
        self.table = [[] for _ in range(ukuran)]

    def hash_function(self, kode):
        total = 0

        for char in kode:
            total += ord(char)

        return total % self.ukuran

    def insert(self, kode, judul):
        index = self.hash_function(kode)

        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == kode:
                bucket[i] = (kode, judul)
                print(f"{kode} -> {judul}")
                return

        bucket.append((kode, judul))
        print(f"{kode} -> {judul}")

    def search(self, kode):
        index = self.hash_function(kode)

        bucket = self.table[index]

        for data in bucket:
            if data[0] == kode:
                print(f"{kode} : {data[1]}")
                return

        print(f"Buku ({kode}) tidak ditemukan")

    def delete(self, kode):
        index = self.hash_function(kode)

        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == kode:
                del bucket[i]
                print(f"Buku {kode} berhasil dihapus")
                return

        print("Buku tidak ditemukan")

    def display(self):
        print("\n===== ISI HASH TABLE =====")

        for i in range(self.ukuran):
            print(f"Bucket {i} :", end=" ")

            if len(self.table[i]) == 0:
                print("Kosong")
            else:
                for kode, judul in self.table[i]:
                    print(f"[{kode} : {judul}]", end=" ")

                print()


ht = HashTable()

ht.insert("BK111", "Mahir C++ Dalam Satu Jam")
ht.insert("BK222", "Python Dasar")
ht.insert("BK333", "Matematika Diskrit")
ht.insert("BK444", "Atomic Habits")

ht.display()

print("\n=== INSERT DATA BARU ===")

ht.insert("BK045", "Mein Kampf")
ht.insert("BK111", "Bumi Manusia")

ht.display()

print("\n=== SEARCH ===")

ht.search("BK222")
ht.search("BK999")

print("\n=== DELETE ===")

ht.delete("BK333")

ht.display()