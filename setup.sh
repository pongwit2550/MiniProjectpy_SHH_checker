#!/usr/bin/env bash

# ตรวจสอบว่ารันด้วยสิทธิ์ root หรือไม่
if [ "$EUID" -ne 0 ]; then
  echo "❌ กรุณารันสคริปต์นี้ด้วยสิทธิ์ root (เช่น: sudo bash setup.sh)"
  exit 1
fi

# ดึง Path ปัจจุบันของโปรเจกต์
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_PATH="$(which python3)"
SERVICE_FILE="/etc/systemd/system/ssh-notify.service"

# หาชื่อ User ที่เรียกใช้ sudo (เพื่อให้สคริปต์รันภายใต้ user นั้น หรือใช้ root)
TARGET_USER="${SUDO_USER:-root}"

echo "=========================================="
echo "🚀 กำลังติดตั้ง SSH Notify Systemd Service"
echo "=========================================="
echo "📂 โฟลเดอร์โปรเจกต์ : $CURRENT_DIR"
echo "🐍 Python Path     : $PYTHON_PATH"
echo "👤 User ที่รัน      : $TARGET_USER"
echo ""

# สร้างไฟล์ Systemd Service แบบ Dynamic
cat << EOF > "$SERVICE_FILE"
[Unit]
Description=SSH Login LINE Notifier
After=network.target

[Service]
Type=simple
User=$TARGET_USER
WorkingDirectory=$CURRENT_DIR
ExecStart=$PYTHON_PATH $CURRENT_DIR/ssh_notify.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

echo "⚙️ กำลังรีโหลด Systemd และเปิดใช้งาน Service..."
systemctl daemon-reload
systemctl enable ssh-notify.service
systemctl restart ssh-notify.service

echo ""
echo "✅ ติดตั้งและเริ่มการทำงานเรียบร้อยแล้วครับ!"
echo "------------------------------------------"
echo "🔍 ตรวจสอบสถานะการทำงานด้วยคำสั่ง:"
echo "   sudo systemctl status ssh-notify.service"
echo "------------------------------------------"