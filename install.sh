#!/data/data/com.termux/files/usr/bin/bash

# ==========================================
# COLOR SCHEME
# ==========================================
R='\e[1;31m'
G='\e[1;32m'
B='\e[1;34m'
C='\e[1;36m'
Y='\e[1;33m'
M='\e[1;35m'
W='\e[1;37m'
D='\e[2m'
BG_M='\e[45;1;37m' # Background Magenta, Teks Putih Bold
BG_B='\e[44;1;37m' # Background Biru, Teks Putih Bold
NC='\e[0m'

# ==========================================
# UI COMPONENTS
# ==========================================
banner() {
    clear
    echo -e "${C}┌──────────────────────────────────────────┐${NC}"
    echo -e "${C}│${NC}${BOLD}${W}        FASTBOOT TOOLKIT DEPLOYMENT       ${NC}${C}│${NC}"
    echo -e "${C}└──────────────────────────────────────────┘${NC}"
    echo -e " ${D}System Time: $(date +'%H:%M:%S') | Ver: 2.0.4${NC}\n"
}

divider() {
    echo -e "${D}--------------------------------------------${NC}"
}

# ==========================================
# MAIN EXECUTION
# ==========================================
banner

# STEP 1: REPOSITORY
echo -e "${B}[ 01 ]${NC} ${W}CORE REPOSITORY${NC}"
echo -ne "${D}       Status: ${NC}${Y}Updating...${NC}\r"
pkg update && pkg upgrade -y > /dev/null 2>&1
echo -e "${D}       Status: ${NC}${G}Repositories Synced!${NC}     "
divider

# STEP 2: DEPENDENCIES
echo -e "${B}[ 02 ]${NC} ${W}SYSTEM BINARIES${NC}"
echo -e "${D}       Installing: python, android-tools${NC}"
pkg install python android-tools -y > /dev/null 2>&1
echo -e "${D}       Progress: ${NC}${G}[####################] 100%${NC}"
divider

# STEP 3: LIBRARIES
echo -e "${B}[ 03 ]${NC} ${W}PYTHON ENVIRONMENT${NC}"
echo -e "${D}       pip install rich --quiet${NC}"
pip install rich --quiet > /dev/null 2>&1
echo -e "${D}       Status: ${NC}${G}Rich Library Injected${NC}"
divider

# STEP 4: SHORTCUT
echo -e "${B}[ 04 ]${NC} ${W}SYSTEM SYMLINK${NC}"
if [ -f "fastboot.py" ]; then
    chmod +x fastboot.py
    ln -sf $(pwd)/fastboot.py $PREFIX/bin/fastboot-tk
    LINK_STATUS="${G}ACTIVE${NC}"
else
    LINK_STATUS="${R}MISSING${NC}"
fi
echo -e "${D}       Symlink Status: [ ${LINK_STATUS} ]${NC}"
divider

# ==========================================
# NEW STATUS CARDS (GANTI KOTAK UNGU)
# ==========================================
echo -e "\n${BG_M}  SYSTEM SUMMARY  ${NC}"
echo -e "  ${M}•${NC} Os Type   : ${W}Android / Termux${NC}"
echo -e "  ${M}•${NC} Service   : ${W}Fastboot-Toolkit${NC}"
echo -e "  ${M}•${NC} Link      : ${LINK_STATUS}"

echo -e "\n${BG_B}  LAUNCH COMMAND  ${NC}"
echo -e "  Tulis perintah ini di mana saja:"
echo -e "  ${C}» ${BOLD}fastboot-tk${NC}"

echo -e "\n${D}────────────────────────────────────────────${NC}\n"
