# 90-Day Bootcamp - Mobile Server Setup

## Quick Start Guide

This guide will help you run the `anish_90day_bootcamp.html` file on a server accessible from mobile devices.

### Prerequisites
- Python 3.x installed
- Flask library (`pip install flask`)

### Setup Instructions

#### Step 1: Install Flask
```bash
pip install flask
```

#### Step 2: Run the Server
Open PowerShell/Command Prompt in the workspace directory and run:
```bash
python serve.py
```

You should see output like:
```
==================================================
Server is running!
==================================================
Open in browser: http://localhost:5000
Open on mobile: http://192.168.x.x:5000
==================================================
```

#### Step 3: Access on Your Devices

**On Desktop:**
- Open your browser and go to: `http://localhost:5000`

**On Mobile (Phone/Tablet):**
- Make sure your phone is connected to the same WiFi network as your computer
- Note the IP address shown by the server (e.g., `http://192.168.1.100:5000`)
- Open any mobile browser and enter that IP address with port 5000
- Example: `http://192.168.1.100:5000`

### Features

✅ **Mobile Responsive Design**
- Optimized layouts for phones (480px), tablets (768px), and desktops
- Touch-friendly checkboxes and buttons
- Readable fonts on small screens

✅ **Dark Theme**
- Eye-friendly cybersecurity-themed interface
- Green accent colors (#00ff41)

✅ **Progress Tracking**
- Mark lectures as completed
- Real-time progress calculation
- Visual progress bars

✅ **Daily Schedule**
- Built-in timetable
- Time slot management

### Troubleshooting

**Can't access from mobile?**
1. Make sure both devices are on the same WiFi network
2. Check the IP address shown by the server
3. Ensure Windows Firewall allows Python through (may need to allow in firewall settings)
4. Try disabling firewall temporarily to test

**Port 5000 already in use?**
Edit `serve.py` and change `port=5000` to `port=8000` (or any available port)

**Connection refused?**
Make sure the server is still running in the terminal (don't close it)

### Files

- `serve.py` - Flask server application
- `html/90/anish_90day_bootcamp.html` - Main bootcamp page (fully mobile-optimized)

### Data Storage

Your progress (checked lectures) is saved in your browser's local storage. Each device will have its own progress tracking.

---

**Started:** January 3, 2026  
**Target Completion:** April 3, 2026 (90 Days)
