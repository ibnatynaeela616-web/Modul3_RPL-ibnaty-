# Ibnaty Naeela_f5212510008
from unittest.mock import MagicMock, patch
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

@patch("models.buku_model.Database")
def test_get_all_buku(mock_database):
    # Membuat data buku contoh
    data_buku = [
        {
            "id_buku": 1,
            "judul": "Janji",
            "penulis": "Tere Liye",
            "tahun_terbit": 2021
        },
        {
            "id_buku": 2,
            "judul": "Bumi",
            "penulis": "Tere Liye",
            "tahun_terbit": 2014
        }
    ]

    # Membuat koneksi dan cursor tiruan
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_database.return_value.get_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    # Mengatur hasil query tiruan
    mock_cursor.fetchall.return_value = data_buku

    # Menginisialisasi Model
    model = BukuModel()

    # Menjalankan fungsi get_all_buku()
    hasil = model.get_all_buku()

    # Memeriksa hasil data
    assert hasil == data_buku
    assert len(hasil) == 2

    # Memastikan query dijalankan
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM buku"
    )

    # Memastikan cursor ditutup
    mock_cursor.close.assert_called_once()
