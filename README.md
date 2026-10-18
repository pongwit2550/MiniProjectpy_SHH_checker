# 🔔 SSH Login Notifier

สคริปต์ภาษา Python สำหรับตรวจสอบการเข้าสู่ระบบผ่าน SSH (SSH Login) แบบ Real-time บนระบบ Linux (รองรับ Fedora, RHEL, Ubuntu, Debian) และส่งข้อความแจ้งเตือนเข้า LINE ทันทีผ่าน LINE Messaging API โดยใช้ Standard Library ล้วนๆ ไม่ต้องติดตั้งแพ็กเกจเสริม

---

## ✨ คุณสมบัติเด่น (Features)
* **Real-time Monitoring:** ดึงข้อมูล Log จากระบบ systemd (`journalctl`) ทันทีที่มีการ SSH เข้าสู่ระบบสำเร็จ (รองรับทั้ง Password และ Public Key)
* **Zero Dependencies:** ใช้ Python Standard Library ไม่มีภาระต้องติดตั้งไลบรารีภายนอก (เช่น `requests`) เพิ่มเติม
* **Secure Config:** โหลดค่าคอนฟิกและ Token ต่างๆ จากไฟล์ `.env` อย่างปลอดภัย
* **Systemd Ready:** สามารถตั้งค่าให้รันเป็น Background Service ทำงานอัตโนมัติทุกครั้งที่เปิดเครื่อง

---

## ⚙️ วิธีการติดตั้งและใช้งาน (Installation & Usage)

1. **โคลนโปรเจกต์มายังเครื่องเป้าหมาย:**
   ```bash
   git clone https://github.com/pongwit2550/MiniProjectpy_SSH_checker.git
   cd MiniProjectpy_SSH_checker

2. **Set .env**
   LINE_CHANNEL_TOKEN=ใส่_Channel_Access_Token_ของคุณที่นี่
   LINE_USER_ID=ใส่_User_ID_หรือ_Group_ID_ของคุณที่นี่

3.python3 ssh_notify.py
