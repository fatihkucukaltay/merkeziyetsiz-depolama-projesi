# HYDRA: Decentralized & Hybrid Storage Network 🌐

> **Status:** Prototype v0.4 (Active Development)
> **License:** MIT License

## 🚀 Project Overview
HYDRA (Hybrid Yielding Distributed Regenerative Architecture) is a next-generation decentralized storage protocol designed to solve the **Energy Efficiency** and **Scalability** trilemma of traditional data centers.

By leveraging **Edge Computing**, this project utilizes idle resources of Single Board Computers (like Raspberry Pi) and mobile devices to create a self-healing, encrypted, and eco-friendly storage grid.

### 🏆 Key Features
* **♻️ 90% Energy Savings:** Uses low-power ARM devices (Raspberry Pi) instead of energy-hungry servers.
* **🔒 Military-Grade Security:** All data is encrypted with **AES-128-CBC** and sharded before transmission.
* **⚡ Hybrid Architecture:** Separates "Persistence Nodes" (Storage) from "Cache Nodes" (Speed) for optimal performance.
* **❤️ Self-Healing (Heartbeat):** Automatically detects offline nodes and regenerates lost shards (N=3 Replication).



+-----------------+           +------------------+
       |   User (Client) | <-------> |   Cache Nodes    |
       +-----------------+  Fast     | (Mobile Devices) |
               |            Speed    +------------------+
               |                           ^   |
      Encrypted|                           |   | Heartbeat
      Shards   |                           |   | & Sync
               v                           |   v
       +-----------------+           +------------------+
       | Persistence     | --------> |   HYDRA GRID     |
       | Nodes (RasPi)   |  Backup   | (Self-Healing)   |
       +-----------------+           +------------------+

       
---

## 🛠️ Technical Stack
* **Core Logic:** Python 3.9+
* **API Framework:** Flask (RESTful Architecture)
* **Cryptography:** `cryptography` library (Fernet / AES)
* **Hardware Target:** Raspberry Pi 4/5 & Mobile Devices

---

## 📂 Repository Structure
* `ana_sunucu.py`: The core node logic (handles requests, storage, and retrieval).
* `guvenlik.py`: Encryption and decryption modules (AES-128).
* `yonetici.py`: Network orchestration and heartbeat monitoring.
* `uploads/`: Directory where encrypted shards are stored locally.

---

## ⚡ Quick Start (How to Run)

### 1. Clone the Repository

bash
git clone [https://github.com/fatihkucukaltay/merkeziyetsiz-depolama-projesi.git](https://github.com/fatihkucukaltay/merkeziyetsiz-depolama-projesi.git)
cd merkeziyetsiz-depolama-projesi

2. Install Dependencies
pip install flask cryptography requests

3. Run the Node
python ana_sunucu.py

The server will start at http://0.0.0.0:5000
🤝 Contributing
This project is open-source and we welcome contributions!
 * Fork the Project
 * Create your Feature Branch (git checkout -b feature/AmazingFeature)
 * Commit your Changes (git commit -m 'Add some AmazingFeature')
 * Push to the Branch (git push origin feature/AmazingFeature)
 * Open a Pull Request
📬 Contact
Fatih Küçükaltay
fatihkucukaltay@gmail.com
Founder & Lead Developer
