#!/data/data/com.termux/files/usr/bin/bash

echo "Installing dependencies..."
pkg update && pkg upgrade -y
pkg install python android-tools -y

# Alih-alih 'pip install rich', gunakan ini:
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    pip install rich
fi

echo -e "\nSetup Selesai! Jalankan dengan: python fastboot.py"
