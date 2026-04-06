# 🖱️ Virtual Mouse

Welcome to the **Virtual Mouse**! This tool lets you control your computer's mouse using **hand gestures**  captured via your **webcam**. 🎥

![Virtual Mouse](https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/VirtualMouseDemo.gif)

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

## 💻 How It Works

1. 🎥 **Capture video** from the webcam in real time.
2. ✋ **Detect hand landmarks** using **MediaPipe**.
3. 🖱️ **Index finger tip** controls the cursor position on the screen.

### ✋ Gesture Based Mouse Actions

| Gesture 👋              | Fingers State 🖐️                   | Distance Condition 📏  | 
| ----------------------- | ----------------------------------- | ---------------------- |
| **Left Click**          | Index ✅, Middle ✅, Pinky ❌          | Index ↔️ Middle < 25px |
| **Right Click**         | Index ✅, Middle ✅, Pinky ✅          | Index ↔️ Middle < 25px |
| **Scroll Down**         | Index ✅, Middle ✅, Pinky ❌, Thumb ✅ | Index ↔️ Middle < 25px |
| **Scroll Up**           | Index ✅, Middle ✅, Pinky ✅, Thumb ✅ | Index ↔️ Middle < 25px |
| **Double Click**        | Index ✅, Middle ❌, Pinky ❌, Thumb ✅ | _Not Required_ |

* ✅ = **Finger Up**
* ❌ = **Finger Down**
* ↔️ = **Distance between fingertips**

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/KrishBharadwaj5678/VirtualMouse.git
   ```

2. **Navigate into the project directory**

   ```bash
   cd VirtualMouse
   ```

3. **Install the required dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the application**

   ```bash
   python app.py
   ```
---

## Contributing 🤝

Want to contribute? Here's how:

1. 🍴 Fork the repository.
2. 🌿 Create a new branch (`git checkout -b feature-name`).
3. ✍️ Make your changes and commit them (`git commit -am 'Add feature-name'`).
4. 🚀 Push to your branch (`git push origin feature-name`).
5. 🔄 Submit a pull request to merge into the main branch.

