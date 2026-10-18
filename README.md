# 🛡️ SSH Login Notifier

> สคริปต์ภาษา Python น้ำหนักเบา สำหรับตรวจจับการเข้าสู่ระบบผ่าน SSH แบบ Real-time บนระบบ Linux และส่งแจ้งเตือนเข้าแอปพลิเคชัน LINE ทันที

---

## ✨ คุณสมบัติเด่น (Features)

* **⚡ Real-time Monitoring:** ดึงข้อมูล Log จากระบบ systemd (`journalctl`) ทันทีที่มีการ SSH สำเร็จ (รองรับทั้ง Password และ Public Key)
* **🧩 Zero Dependencies:** ใช้ Python Standard Library ล้วน ๆ ไม่ต้องติดตั้งไลบรารีภายนอกเพิ่มเติม
* **🔒 Secure Config:** โหลดข้อมูลลับและ Token ต่างๆ ผ่านไฟล์ `.env` อย่างปลอดภัย
* **⚙️ Systemd Ready:** รองรับการทำ Background Service เพื่อรันอัตโนมัติทุกครั้งที่เปิดเครื่อง

---

## 📁 โครงสร้างโปรเจกต์ (Project Structure)

```text
MiniProjectpy_SSH_checker/
├── .env              # ไฟล์เก็บค่า Config และ LINE Token (ต้องสร้างเพิ่ม)
├── ssh_notify.py     # สคริปต์หลักสำหรับดึง Log และส่ง LINE
├── setup.sh          # สคริปต์ติดตั้ง Systemd Service อัตโนมัติ
└── README.md         # เอกสารอธิบายโปรเจกต์
```

---
1. clone
```Bash
git clone [https://github.com/pongwit2550/MiniProjectpy_SSH_checker.git](https://github.com/pongwit2550/MiniProjectpy_SSH_checker.git)
cd MiniProjectpy_SSH_checker
```
2. .env setup (Line Token)
สร้างไฟล์ .env ขึ้นมาในโฟลเดอร์หลักของโปรเจกต์:

```Bash
nano .env
```
จากนั้นใส่ค่า Token และ User ID ของคุณ:

```ข้อมูลโค้ด
LINE_CHANNEL_TOKEN=your_line_channel_access_token_here
LINE_USER_ID=your_line_user_id_or_group_id_here
```
3. ติดตั้งและเปิดใช้งาน Systemd Service (แนะนำ)
เพื่อให้สคริปต์รันเบื้องหลังและทำงานอัตโนมัติทุกครั้งที่เปิดเครื่อง ให้ใช้สคริปต์ setup.sh ที่เตรียมไว้:

```Bash
chmod +x setup.sh
sudo bash setup.sh
```
