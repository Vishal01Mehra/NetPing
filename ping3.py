import tkinter as tk
from tkinter import ttk
import subprocess
import platform
import threading

class ConnectionIndicator:
    def __init__(self, root, name, ip, row, interval=1000):
        self.ip = ip 
        self.name = name 
        self.interval = interval 
        self.label = ttk.Label(root, text=f"{self.name}")
        self.label.grid(row=row, column=0, padx=6, pady=6)
        self.indicator = tk.Canvas(root, width=20, height=20)
        self.indicator.grid(row=row, column=1, padx=5, pady=5)
        self.circle = self.indicator.create_oval(5, 5, 20, 20, fill='red')
        self.indicator.grid(row=row, column=1, padx=5, pady=5)
        self.running = True
        self.update_status()

    def update_status(self):
        if not self.running:
            return
        threading.Thread(target=self.check_and_update).start()
        root.after(self.interval, self.update_status)

    def check_and_update(self):
        is_connected = self.check_connection(self.ip)
        color = 'green' if is_connected else 'red'
        self.indicator.itemconfig(self.circle, fill=color)

    @staticmethod
    def check_connection(ip):
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', '-W', '1', ip] if platform.system().lower() != 'windows' else ['ping', param, '1', '-w', '1000', ip]
        try:
            output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return output.returncode == 0
        except Exception as e:
            print(f"Exception occurred while pinging {ip}: {e}")
            return False

    def stop(self):
        self.running = False

def main():
    global root
    root = tk.Tk()
    root.title("Ping")
    
    devices = {
        'Winch': '192.168.1.202',
        'Camera': '192.168.1.200',
        'Drone': '192.168.1.201',
        'Radio (AIR)': '192.168.1.18'
    }
    
    indicators = []
    for i, (name, ip) in enumerate(devices.items()):
        indicator = ConnectionIndicator(root, name, ip, i, interval=500)
        indicators.append(indicator)
    
    def on_closing():
        for indicator in indicators:
            indicator.stop()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
