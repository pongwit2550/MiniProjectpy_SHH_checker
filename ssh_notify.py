#!/usr/bin/env python3
"""ssh_notify - Monitor SSH logins and send LINE notifications. Stdlib only."""
import os
import re
import subprocess
import sys
import json
import urllib.request
from pathlib import Path

# รูปแบบ Log ของ SSH ที่บอกว่าล็อกอินสำเร็จ
# ตัวอย่าง: Accepted publickey for root from 192.168.1.50 port 54321 ssh2
LOGIN_REGEX = re.compile(
    r"Accepted\s+(?:publickey|password)\s+for\s+(\S+)\s+from\s+(\S+)\s+port\s+\d+"
)


def load_env():
    """โหลดค่าจากไฟล์ .env เข้า os.environ"""
    env_path = Path.cwd() / ".env"
    if not env_path.is_file():
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[7:]
        key, _, val = line.partition("=")
        os.environ.setdefault(key.strip(), val.strip().strip("'\""))


def send_line(text):
    """ส่งข้อความแจ้งเตือนผ่าน LINE Messaging API"""
    try:
        token = os.environ["LINE_CHANNEL_TOKEN"]
        to = os.environ["LINE_USER_ID"]
    except KeyError as e:
        print(f"Error: ขาดตัวแปร {e.args[0]} ในไฟล์ .env", file=sys.stderr)
        return

    req = urllib.request.Request(
        "https://api.line.me/v2/bot/message/push",
        data=json.dumps(
            {"to": to, "messages": [{"type": "text", "text": text[:5000]}]}
        ).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
    )
    try:
        urllib.request.urlopen(req, timeout=10).close()
    except Exception as e:
        print(f"Error: ส่งข้อความ LINE ไม่สำเร็จ: {e}", file=sys.stderr)


def main():
    load_env()
    print("🚀 เริ่มต้นระบบตรวจจับ SSH Login (กด Ctrl+C เพื่อหยุด)...")

    # ใช้ journalctl เพื่อติดตาม log ของ ssh แบบ real-time
    cmd = ["journalctl", "-u", "sshd", "-f", "--no-tail"]
    
    try:
        process = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True
        )
        
        for line in process.stdout:
            match = LOGIN_REGEX.search(line)
            if match:
                user, ip = match.groups()
                msg = f"🔔 แจ้งเตือนการ SSH เข้าสู่ระบบ\n👤 User: {user}\n💻 IP: {ip}"
                print(msg)
                send_line(msg)
                
    except KeyboardInterrupt:
        print("\n🛑 หยุดการทำงาน")
        sys.exit(0)
    except FileNotFoundError:
        print("Error: ไม่พบคำสั่ง journalctl (สคริปต์นี้เหมาะสำหรับ Linux ที่ใช้ Systemd)", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()