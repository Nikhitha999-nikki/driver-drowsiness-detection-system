# Driver Drowsiness De## Key Features
- Real-time monitoring of driver's eyes using a camera
- Fatigue and drowsiness detection algorithm
- Timely alerts to prevent the driver from falling asleep
- Non-intrusive and easy to set up
- **📱 Progressive Web App (PWA) support - Install like a native app!**
- **🔄 Offline functionality with caching**
- **🚀 Fast loading with optimized performance**on System

<p align="center">
  <img src="https://img.shields.io/github/stars/Gagandeep-2003/Driver-Drowsiness-Detection-System?style=social" alt="GitHub stars" />
  <img src="https://img.shields.io/github/forks/Gagandeep-2003/Driver-Drowsiness-Detection-System?style=social" alt="GitHub forks" />
  <img src="https://img.shields.io/github/issues/Gagandeep-2003/Driver-Drowsiness-Detection-System" alt="GitHub issues" />
</p>


## Project Overview
The Driver Drowsiness Detection System is a non-intrusive solution designed to monitor and detect signs of fatigue in drivers. By analyzing eye states through a camera feed, the system can identify early symptoms of drowsiness and issue timely warnings, helping to prevent accidents caused by driver fatigue. This project aims to enhance road safety, especially for those driving long distances who may not recognize their own drowsiness in time.

## ⭐ Support the Project

If you find this project helpful, please consider giving it a **star** ⭐ on GitHub!  
It helps others discover the project and motivates us to keep improving it.

👉 Click the ⭐ button at the top-right of this page!

[![GitHub stars](https://img.shields.io/github/stars/Gagandeep-2003/Driver-Drowsiness-Detection-System.svg?style=social)](https://github.com/Gagandeep-2003/Driver-Drowsiness-Detection-System/stargazers)


## Key Features
- Real-time monitoring of driver’s eyes using a camera
- Fatigue and drowsiness detection algorithm
- Timely alerts to prevent the driver from falling asleep
- Non-intrusive and easy to set up

## Technologies Used
- Python
- OpenCV
- Dlib or Mediapipe (for facial landmark detection)
- NumPy, Pandas

  
 ## Optional: create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Gagandeep-2003/Driver-Drowsiness-Detection-System.git
   cd Driver-Drowsiness-Detection-System
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python main.py
   ```
   (Replace `main.py` with the actual entry point if different.)

## Usage
- Ensure your webcam is connected.
- Run the application as shown above.
- The system will start monitoring your eyes and alert you if signs of drowsiness are detected.

## Folder Structure
```
Driver-Drowsiness-Detection-System/
├── drowsiness_detector/
│   ├── detector.py
│   └── utils.py
├── models/
│   └── shape_predictor_68_face_landmarks.dat
├── assets/
│   └── demo.gif
├── main.py
├── requirements.txt
├── README.md

```

## Contribution Guidelines
We welcome contributions to improve this project! To get started:
1. **Star** ⭐ this repository to show your support.
2. **Fork** 🍴 the repository to your own GitHub account.
3. Create a new branch for your feature or bugfix.
4. Make your changes and commit them with clear messages.
5. Push your branch to your forked repo.
6. Open a Pull Request describing your changes.

---

## 📋 Project Board & Roadmap

We are actively tracking progress and assigning tasks for **GSSoC'25** in our GitHub Project Board.  
You can see which issues are **To Do**, **In Progress**, or **Completed**, and pick one to start contributing.

🚀 **[View the GSSoC 2025 Roadmap Project →](https://github.com/users/Gagandeep-2003/projects/1)**

> ℹ️ To work on an issue:
> 1. Comment on the issue stating your interest.
> 2. We’ll assign it to you under the appropriate GSSoC’25 level.
> 3. Track your progress via the Project Board.

## 🌐 Streamlit Web App (New Feature!)

This app version uses Streamlit + Mediapipe to detect drowsiness via webcam directly in the browser.

### Usage:
```bash
# Standard web app
streamlit run streamlit_app/streamlit_app.py

# Or run the enhanced PWA version
streamlit run streamlit_app/streamlit_app_pwa.py
```

## 📱 Progressive Web App (PWA) Support

**NEW!** This project now supports Progressive Web App functionality! Install it like a native app on your device.

### PWA Features:
- 📱 **Installable**: Add to home screen on mobile/desktop
- 🚀 **Fast Loading**: Cached resources for better performance  
- 🔄 **Offline Support**: Basic functionality without internet
- 📲 **App-like Experience**: Full-screen, native app behavior

### Quick PWA Installation:
1. **Mobile**: Open in browser → Menu → "Add to Home Screen"
2. **Desktop**: Look for install icon in address bar → Click "Install"

📖 **[Complete PWA Guide](PWA_README.md)** - Detailed installation and usage instructions

Dependencies:
Install using:
```bash
pip install -r requirements.txt
```

Features:
- Real-time Eye Aspect Ratio (EAR) monitoring
- Drowsiness warning overlay
- Web-based UI with live video
- **PWA installable web app**
- **Offline caching support**

**Note:** Please do not add a license section. A contributor will be adding license information soon.

If you have any questions or need guidance, feel free to open an issue or ask in the discussions!

---

Thank you for your interest in improving the Driver Drowsiness Detection System! Your contributions are greatly appreciated.

<p align="center">
  <a href="#top" style="font-size: 18px; padding: 8px 16px; display: inline-block; border: 1px solid #ccc; border-radius: 6px; text-decoration: none;">
    ⬆️ Back to Top
  </a>
</p>
