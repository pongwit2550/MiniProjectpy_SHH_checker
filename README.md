# MiniProjectpy_SHH_checker

# 🔔 SSH Login Notifier (Python)

A lightweight, zero-dependency Python script designed for Linux environments (such as Fedora/RHEL and Ubuntu/Debian) to monitor SSH login events in real-time using `journalctl` and send instant alerts to your LINE chat via the LINE Messaging API.

---

## ✨ Features
* **Real-time Monitoring:** Listens to systemd journals for successful SSH logins (both password and public key).
* **Zero Dependencies:** Uses Python's standard library only (no external packages like `requests` needed).
* **Environment Configuration:** Securely loads your LINE credentials from a `.env` file.
* **Systemd Integration:** Can be configured to run automatically as a background service at system startup.

---

## ⚙️ Prerequisites & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/pongwit2550/MiniProjectpy_SSH_checker.git](https://github.com/pongwit2550/MiniProjectpy_SSH_checker.git)
   cd MiniProjectpy_SSH_checker
