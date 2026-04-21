import os
import time
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.text import Text
from rich.align import Align
from rich.live import Live

console = Console()

# --- UTILS / FUNGSI DASAR ---

def clear():
    os.system('clear')

def press_enter_to_continue():
    print("\n")
    with Live(Text(" ➜  Tekan Enter untuk kembali...", style="bold cyan"), refresh_per_second=4) as live:
        console.input("") 

def get_device_status():
    try:
        result = subprocess.check_output(["fastboot", "devices"], stderr=subprocess.STDOUT, timeout=1).decode("utf-8").strip()
        if result:
            return "[bold blue]ONLINE[/bold blue]", result.split()[0]
        return "[bold red]OFFLINE[/bold red]", "None"
    except:
        return "[bold red]OFFLINE[/bold red]", "None"

def draw_header():
    status, serial = get_device_status()
    ascii_lines = [
        "╦═╗╔═╗╔═╗╔═╗╦  ╦╔═╗╦═╗╦ ╦",
        "╠╦╝║╣ ║  ║ ║╚╗╔╝║╣ ╠╦╝╚╦╝",
        "╩╚═╚═╝╚═╝╚═╝ ╚╝ ╚═╝╩╚═ ╩ "
    ]
    subtitle = "Advanced Termux Fastboot Toolkit"
    header_text = Text()
    for line in ascii_lines:
        header_text.append(line + "\n", style="bold cyan")
    header_text.append(subtitle, style="italic white")
    
    console.print(Panel(Align.center(header_text), border_style="blue", padding=(1, 0)))
    status_line = Text.from_markup(f"ID: [bold white]{serial}[/bold white]  |  STATUS: {status}")
    console.print(Align.center(status_line))

def run_progress(task_name):
    with Progress(
        SpinnerColumn(spinner_name="dots12"),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(bar_width=None, pulse_style="bold cyan"),
        TextColumn("[bold white]{task.percentage:>3.0f}%"),
        transient=True
    ) as progress:
        task = progress.add_task(f"{task_name}...", total=100)
        while not progress.finished:
            progress.update(task, advance=5)
            time.sleep(0.03)

def run_safe_command(command, task_name):
    command = command.strip()
    if not command: return

    status, _ = get_device_status()
    if "ONLINE" in status:
        run_progress(task_name)
        console.print(Panel(f"[bold yellow]Executing:[/bold yellow] [white]{command}[/white]", border_style="blue", expand=False))
        try:
            process = subprocess.run(command, shell=True, capture_output=True, text=True)
            output = process.stdout + process.stderr
            if output.strip():
                console.print(Panel(Text(output.strip(), style="green"), title="[bold green]Output Log[/bold green]", border_style="green", expand=False))
            console.print(f"\n[bold green]✔[/bold green] [bold white]{task_name} Selesai![/bold white]")
        except Exception as e:
            console.print(Panel(Text(str(e), style="red"), title="[bold red]Error[/bold red]", border_style="red", expand=False))
        
        # Cleanup temp file jika ada proses flashing
        home = os.path.expanduser("~")
        temp = os.path.join(home, "temp_flash.img")
        if os.path.exists(temp) and "temp_flash.img" in command:
            os.remove(temp)
            
        press_enter_to_continue()
    else:
        clear(); draw_header()
        console.print(Panel("[bold red]✘ GAGAL: PERANGKAT TIDAK TERDETEKSI![/bold red]", title="Error", border_style="red", padding=(0,2)))
        press_enter_to_continue()

# --- MENUS ---

def flash_menu():
    while True:
        clear(); draw_header()
        table = Table(show_header=False, box=None, padding=(0, 1))
        table.add_column("Key", style="bold blue")
        table.add_column("Value", style="white")
        options = [("1", "Flash Recovery"), ("2", "Flash Vendor Boot"), 
                   ("3", "Flash Boot Image"), ("4", "Flash Init Boot"), ("0", "Kembali")]
        for k, v in options: table.add_row(f"[{k}]", v)
        console.print(Panel(Align.left(table, pad=True), title="[bold white]Flashing Menu[/bold white]", border_style="blue", padding=(0, 2)))
        
        c = Prompt.ask("\n[bold white]Pilih nomor[/bold white]", choices=[x[0] for x in options])
        if c == "0": break
        
        target_map = {"1": "recovery", "2": "vendor_boot", "3": "boot", "4": "init_boot"}
        part = target_map[c]
        
        home = os.path.expanduser("~")
        temp_file = os.path.join(home, "temp_flash.img")
        
        clear(); draw_header()
        console.print(Panel(Align.center(f"Pilih file image untuk partisi: [bold cyan]{part}[/bold cyan]"), border_style="blue"))
        if Confirm.ask("[bold white]Buka File Manager?[/bold white]"):
            subprocess.run(['termux-storage-get', temp_file])
            if os.path.exists(temp_file) and os.path.getsize(temp_file) > 0:
                run_safe_command(f"fastboot flash {part} {temp_file}", f"Flashing {part}")
            else:
                console.print("[bold red]✘ File tidak dipilih atau kosong.[/bold red]")
                time.sleep(1.5)

def wipe_menu():
    while True:
        clear(); draw_header()
        table = Table(show_header=False, box=None, padding=(0, 1))
        table.add_column("Key", style="bold blue")
        table.add_column("Value", style="white")
        options = [("1", "Wipe Metadata"), ("2", "Wipe Userdata"), ("3", "Wipe Cache"), ("0", "Kembali")]
        for k, v in options: table.add_row(f"[{k}]", v)
        console.print(Panel(Align.left(table, pad=True), title="[bold white]Wipe Menu[/bold white]", border_style="blue", padding=(0, 2)))
        
        c = Prompt.ask("\n[bold white]Pilih nomor[/bold white]", choices=["1", "2", "3", "0"])
        if c == "1": run_safe_command("fastboot erase metadata", "Wiping Metadata")
        elif c == "2": run_safe_command("fastboot erase userdata", "Wiping Userdata")
        elif c == "3": run_safe_command("fastboot erase cache", "Wiping Cache")
        else: break

def reboot_menu():
    while True:
        clear(); draw_header()
        table = Table(show_header=False, box=None, padding=(0, 1))
        table.add_column("Key", style="bold blue")
        table.add_column("Value", style="white")
        options = [("1", "Reboot System"), ("2", "Reboot Recovery"), ("3", "Reboot Bootloader"), ("0", "Kembali")]
        for k, v in options: table.add_row(f"[{k}]", v)
        console.print(Panel(Align.left(table, pad=True), title="[bold white]Reboot Options[/bold white]", border_style="blue", padding=(0, 2)))
        
        c = Prompt.ask("\n[bold white]Pilih nomor[/bold white]", choices=["1", "2", "3", "0"])
        cmd_map = {"1": "reboot", "2": "reboot recovery", "3": "reboot-bootloader"}
        if c != "0": 
            run_safe_command(f"fastboot {cmd_map[c]}", f"Rebooting {cmd_map[c]}")
            break
        else: break

def custom_command_mode():
    while True:
        clear(); draw_header()
        console.print(Panel("[bold white]CUSTOM FASTBOOT COMMAND MODE[/bold white]\n"
                            "[bold yellow]Ketik perintah lengkap (contoh: fastboot devices)[/bold yellow]\n"
                            "[bold red]Ketik 'exit' untuk kembali[/bold red]", border_style="blue", padding=(0, 2)))
        cmd = Prompt.ask("\n[bold cyan]Terminal[/bold cyan] $")
        if cmd.lower() == 'exit': break
        if cmd: run_safe_command(cmd, f"Custom CMD")

# --- MAIN LOOP ---

if __name__ == "__main__":
    while True:
        clear()
        draw_header()
        
        main_table = Table(show_header=False, box=None, padding=(0, 1))
        main_table.add_column("Key", style="bold blue")
        main_table.add_column("Value", style="white")

        menu_items = [
            ("1", "Flash Menu"), ("2", "Wipe Menu"),
            ("3", "Reboot Menu"), ("4", "Check Devices"),
            ("5", "Custom Command"), ("0", "Exit")
        ]
        for k, v in menu_items: main_table.add_row(f"[{k}]", v)

        console.print(Panel(Align.left(main_table, pad=True), title="[bold white]Main Menu[/bold white]", border_style="blue", padding=(0, 2)))
        
        choice = Prompt.ask("\n[bold white]Pilih nomor[/bold white]", choices=[str(i) for i in range(6)])

        if choice == "1": flash_menu()
        elif choice == "2": wipe_menu()
        elif choice == "3": reboot_menu()
        elif choice == "4":
            clear(); draw_header()
            res = subprocess.getoutput("fastboot devices")
            content = f"[bold green]{res}[/bold green]" if res else "[bold red]No Device Detected[/bold red]"
            console.print(Panel(Align.left(content, pad=True), title="Connected Devices", border_style="blue", padding=(0, 2)))
            press_enter_to_continue()
        elif choice == "5": custom_command_mode()
        elif choice == "0":
            console.print("\n[bold cyan]Exiting... Stay safe rooting![/bold cyan]")
            break
