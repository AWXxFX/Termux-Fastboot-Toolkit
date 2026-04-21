# 🛠️ Advanced Termux Fastboot Toolkit

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Termux](https://img.shields.io/badge/Platform-Termux-orange.svg)](https://termux.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Toolkit berbasis Python yang dirancang khusus untuk pengguna **Termux** guna mempermudah proses flashing, wiping, dan manajemen perangkat Android dalam mode **Fastboot**. Dilengkapi dengan UI modern menggunakan library `rich`.

---

## ✨ Fitur Utama

* **⚡ Smart Flashing:** Flash Partisi Recovery, Boot, Vendor, dan Init Boot dengan mudah.
* **🧹 Wipe Tool:** Hapus Userdata, Metadata, dan Cache secara instan.
* **🔄 Reboot Options:** Navigasi cepat ke System, Recovery, atau Bootloader.
* **💻 Custom Command:** Masukkan perintah fastboot manual tanpa keluar dari toolkit.
* **🎨 Rich UI:** Tampilan tabel, progress bar, dan status perangkat yang interaktif.
* **📂 File Manager Integration:** Terintegrasi dengan storage Android untuk memilih file `.img`.

---

## 🚀 Prasyarat

Sebelum menginstall, pastikan kamu sudah menjalankan perintah berikut di Termux untuk memberikan akses penyimpanan:

```bash
termux-setup-storage

```
## 📥 Instalasi & Penggunaan
Cukup salin dan tempel baris perintah berikut di terminal Termux kamu:
1. Clone repository ini
```bash
git clone https://github.com/AWxXFX/Termux-Fastboot-Toolkit.git
```
2. Masuk ke direktori
```bash
cd Termux-Fastboot-Toolkit
```
3. Jalankan installer otomatis
```bash
bash install.sh
```
4. Jalankan toolkit
```bash
python fastboot.py
```
## 🛠️ Struktur Menu
 1. **Flash Menu:** Pilih partisi target, lalu pilih file .img dari internal storage kamu.
 2. **Wipe Menu:** Membersihkan partisi standar untuk reset perangkat.
 3. **Reboot Menu:** Kontrol navigasi booting perangkat yang terhubung.
 4. **Check Devices:** Verifikasi apakah perangkat sudah terdeteksi di mode fastboot.
 5. **Custom Command:** Terminal khusus untuk perintah fastboot bebas.
## ⚠️ Peringatan (Disclaimer)
**Gunakan dengan risiko sendiri!** Tool ini melakukan modifikasi pada sistem tingkat rendah. Pastikan Anda memahami apa yang Anda flash. Penulis tidak bertanggung jawab atas kerusakan perangkat (hardbrick), kehilangan data, atau perang nuklir yang disebabkan oleh penggunaan toolkit ini.
## 🤝 Kontribusi
Punya ide untuk fitur baru atau menemukan bug? Silakan buka **Issue** atau kirim **Pull Request**. Kontribusi dalam bentuk apa pun sangat dihargai!
**Dibuat dengan ❤️ untuk komunitas oprek Android Indonesia.**
