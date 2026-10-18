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
1.
```Bash
git clone [https://github.com/pongwit2550/MiniProjectpy_SSH_checker.git](https://github.com/pongwit2550/MiniProjectpy_SSH_checker.git)
cd MiniProjectpy_SSH_checker
```
