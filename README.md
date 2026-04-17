# 📡 Network Utilization Monitor using POX (SDN)

## 📌 Overview

This project implements a **Network Utilization Monitor** using the **POX SDN Controller** and **Mininet**.
It measures bandwidth usage across network links by collecting **OpenFlow port statistics** from switches and computing real-time utilization.

---

## 🎯 Objectives

* Collect network statistics from OpenFlow switches
* Calculate bandwidth usage (Rx/Tx rates)
* Compute link utilization percentage
* Display real-time monitoring output

---

## 🧠 How It Works

1. POX controller sends **Port Statistics Request** to switches
2. Switch replies with **rx_bytes and tx_bytes**
3. Controller calculates:

   * Data rate = (bytes difference / time interval) × 8
   * Convert to Mbps
4. Utilization is computed as:

   * Utilization (%) = (Current Rate / Link Capacity) × 100
5. Results are printed every second

---

## 🏗️ Architecture

Mininet (Hosts + Switch)
↓
OpenFlow Switch (OVS)
↓
POX Controller (monitor.py)
↓
Statistics Collection → Utilization Calculation → Output

---

## ⚙️ Requirements

* Ubuntu / WSL
* Python 3
* Mininet
* POX Controller

---

## 🔧 Installation

### 1. Install Mininet

```bash
sudo apt update
sudo apt install mininet
```

### 2. Clone POX

```bash
git clone https://github.com/noxrepo/pox.git
cd pox
```

---

## ▶️ Running the Project

### Step 1: Start POX Controller

```bash
cd ~/pox
./pox.py misc.monitor
```

### Step 2: Start Mininet (new terminal)

```bash
sudo mn --topo single,3 --controller=remote
```

### Step 3: Generate Traffic

Inside Mininet:

```bash
pingall
```

OR

```bash
iperf
```

---

## 📊 Sample Output

```
Switch 1 Port 1 | RX: 2.34 Mbps TX: 0.50 Mbps Util: 28.40%
Switch 1 Port 2 | RX: 1.10 Mbps TX: 0.30 Mbps Util: 14.00%
```

---

## 📁 Project Structure

```
network-utilization-pox/
│
├── monitor.py
├── README.md
└── screenshots/
```

---

## 🚀 Features

* Real-time bandwidth monitoring
* SDN-based approach
* Uses OpenFlow protocol
* Lightweight and efficient

---

## ⚠️ Common Issues

* No output → Ensure Mininet is connected to controller
* Wrong controller IP → Use `--controller=remote,ip=127.0.0.1`
* No traffic → Use `pingall` or `iperf`

---

## 🔮 Future Enhancements

* Graph visualization (Matplotlib)
* GUI dashboard
* Threshold-based alerts
* Multi-switch monitoring

---

## 📚 Concepts Used

* Software Defined Networking (SDN)
* OpenFlow Protocol
* Network Monitoring
* Bandwidth Utilization

---

## 👤 Author

* Your Name

---

## 📜 License

This project is for educational purposes.
