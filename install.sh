#!/data/data/com.termux/files/usr/bin/bash

# Definisi Warna
HIJAU='\e[1;32m'
NORMAL='\e[0m'

echo -e "${HIJAU}Mengecek dan Mengupdate Repository...${NORMAL}"
pkg update && pkg upgrade -y

echo -e "${HIJAU}Menginstal dependencies (Python & ADB Tools)...${NORMAL}"
pkg install python android-tools -y

echo -e "${HIJAU}Menginstal library Rich...${NORMAL}"
pip install rich

# Membuat shortcut otomatis
chmod +x fastboot.py
ln -sf $(pwd)/fastboot.py $PREFIX/bin/fastboot-tk

echo -e "\n${HIJAU}=========================================="
echo -e "      SETUP SELESAI DENGAN SUKSES!        "
echo -e "==========================================${NORMAL}"
echo -e "Jalankan alat dengan mengetik: ${HIJAU}fastboot-tk${NORMAL} atau ${HIJAU}python fastboot.py${NORMAL}"
