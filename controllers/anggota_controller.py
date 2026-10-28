# Ibnaty Naeela_F5212510008
import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()
        self.id_anggota_terpilih = None

        # Menghubungkan tombol dengan fungsi
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )
        self.view.btn_hapus.configure(
            command=self.hapus_data
        )
        self.view.btn_update.configure(
            command=self.perbarui_data
        )

        # Menghubungkan tabel dengan fungsi pilih data
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_data
        )

        # Menampilkan data anggota
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Menghapus isi tabel sebelum memuat ulang
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_anggota = self.model.get_all_anggota()

        # Memasukkan data anggota ke tabel
        for anggota in data_anggota:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    anggota["id_anggota"],
                    anggota["nama"],
                    anggota["alamat"]
                )
            )

    def pilih_data(self, event=None):
        # Mengambil baris yang dipilih
        pilihan = self.view.tabel.selection()

        if not pilihan:
            return

        data = self.view.tabel.item(
            pilihan[0], "values"
        )

        # Menyimpan ID anggota yang dipilih
        self.id_anggota_terpilih = data[0]

        # Menampilkan data ke form
        self.view.entry_nama.delete(0, "end")
        self.view.entry_nama.insert(0, data[1])

        self.view.entry_alamat.delete(0, "end")
        self.view.entry_alamat.insert(0, data[2])

    def simpan_data(self):
        # Mengambil data dari form
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        # Memeriksa apakah kolom sudah diisi
        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat harus diisi!"
            )
            return

        # Menyimpan data anggota
        berhasil = self.model.create_anggota(
            nama, alamat
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil disimpan!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal disimpan!"
            )

    def perbarui_data(self):
        # Memeriksa apakah anggota sudah dipilih
        if self.id_anggota_terpilih is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih anggota terlebih dahulu!"
            )
            return

        # Mengambil data terbaru dari form
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat harus diisi!"
            )
            return

        # Memperbarui data anggota berdasarkan ID
        berhasil = self.model.update_anggota(
            self.id_anggota_terpilih,
            nama,
            alamat
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil diperbarui!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal diperbarui!"
            )

    def hapus_data(self):
        # Memeriksa apakah anggota sudah dipilih
        if self.id_anggota_terpilih is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih anggota terlebih dahulu!"
            )
            return

        # Meminta konfirmasi sebelum menghapus
        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Hapus data anggota yang dipilih?"
        )

        if not konfirmasi:
            return

        # Menghapus data berdasarkan ID
        berhasil = self.model.delete_anggota(
            self.id_anggota_terpilih
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil dihapus!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal dihapus!"
            )

    def bersihkan_form(self):
        # Mengosongkan form
        self.view.entry_nama.delete(0, "end")
        self.view.entry_alamat.delete(0, "end")

        self.id_anggota_terpilih = None

        # Menghilangkan pilihan pada tabel
        pilihan = self.view.tabel.selection()
        if pilihan:
            self.view.tabel.selection_remove(*pilihan)

    def run(self):
        self.view.mainloop()

if __name__ == "__main__":
    app = AnggotaController()
    app.run()