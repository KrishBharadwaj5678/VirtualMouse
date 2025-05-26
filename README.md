# 🖱️ Virtual Mouse

Welcome to the **Virtual Mouse** project! This tool lets you control your computer's mouse using **hand gestures**  captured via your **webcam**. 🖐️

---

## 🚀 Features

| Feature 🧩                    | Description 📋                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------------ |
| 🖐️ Hand Gesture Control      | Use your hand to move the mouse pointer in real time.                                 |
| 🖱️ Click Actions             | **Left**, **right**, and **double** click with fingers gestures.                      |
| 🧭 Scroll Up / Down           | Scroll through pages using finger movements.                                         |
| 🎯 Cursor Movement            | Smoothly move the mouse cursor based on hand position.                               |
| 🔄 Real time Tracking         | Fast and responsive tracking using **OpenCV** and **MediaPipe**.                     |
| 🔍 Gesture Recognition        | Detect specific finger configurations for different commands.                        |
| 🧰 Easy Setup & Customization | Simple to install, run, and tweak gesture mappings.                                  |
| 🧑‍💻 Python Powered             | Entirely built using Python and open source libraries.                               |
| 📷 Webcam Integration         | Uses your computer's webcam.                                                          |

---

## 🛠️ Tech Stack

| Technology ⚙️ | Purpose 📋                          |
| ------------- | ----------------------------------- |
| 🐍 Python 3   | Core programming language           |
| 🎥 OpenCV     | Video capture and image processing  |
| ✋ MediaPipe   | Hand tracking and gesture detection |
| 🖱️ PyAutoGUI | Simulate mouse actions              |
| 📦 NumPy      | Efficient numerical operations      |

---

## 📸 How It Works

1. Capture video from webcam
2. Detect hand landmarks using **MediaPipe**
3. Track finger positions to:

   * Move the cursor
   * Perform left and right clicks

## 📦 Installation

```bash
git clone https://github.com/your-username/virtual-mouse.git
cd VirtualMouse
pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
python app.py
```

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.
