#!/data/data/com.termux/files/usr/bin/bash

# ==========================================
# DEFINISI WARNA & FUNGSI
# ==========================================
GREEN='\e[1;32m'
CYAN='\e[1;36m'
BOLD='\e[1m'
NC='\e[0m' # No Color (Reset)

# Fungsi untuk membuat kotak pesan otomatis
print_box() {
    local pesan="$1"
    local lebar=${#pesan}
    local garis=""
    for ((i=0; i<lebar+4; i++)); do garis+="─"; done
    
    echo -e "${GREEN}┌${garis}┐"
    echo -e "│  ${BOLD}${pesan}${NC}${GREEN}  │"
    echo -e "└${garis}┘${NC}"
}

# ==========================================
# PROSES EKSEKUSI
# ==========================================

# Bersihkan layar saat script mulai
clear

echo -e "${CYAN}Starting Installation System...${NC}\n"

# Step 1: Update & Install Apps
print_box "Menginstal dependencies (Python & ADB Tools)..."
pkg update && pkg upgrade -y
pkg install python android-tools -y

echo -e "" # Spasi antar proses

# Step 2: Install Library
print_box "Menginstal library Rich..."
pip install rich

# Step 3: Membuat Shortcut
# Memastikan file bisa dieksekusi dan membuat link ke sistem
if [ -f "fastboot.py" ]; then
    chmod +x fastboot.py
    ln -sf $(pwd)/fastboot.py $PREFIX/bin/fastboot-tk
    SHORTCUT_STATUS="Shortcut 'fastboot-tk' berhasil dibuat!"
else
    SHORTCUT_STATUS="Peringatan: fastboot.py tidak ditemukan di folder ini."
fi

# ==========================================
# SELESAI
# ==========================================
echo -e "\n${GREEN}==========================================${NC}"
echo -e "${GREEN}${BOLD}         SETUP SELESAI DENGAN SUKSES!      ${NC}"
echo -e "${GREEN}==========================================${NC}"
echo -e "${SHORTCUT_STATUS}"
echo -e "Jalankan alat dengan mengetik: ${CYAN}fastboot-tk${NC}\n"
