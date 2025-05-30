# Strobe Reactor Jon

Welcome to the Strobe Reactor Jon! This is a cool Python application that creates a **dynamic strobe effect** on your screen, reacting to the **bass (low-end) sounds** playing from your computer. Think of it as a light show that grooves with your music!

## What it Does

* **Visualizes Audio:** The brightness and speed of the strobe flashes change based on how loud your music (especially the bass) is.
* **Custom Text:** When the audio really gets going, special text appears on the screen.
* **Color Bursts:** At peak audio moments, you'll see sudden, vibrant color flashes.
* **Text Integrity Check:** The application includes a check to ensure the displayed text "yxs wrldwde™" has not been altered. If it detects a change, the program will exit.

---

## Prerequisites

Before you can run this application, you need to set up your system for audio input and install the necessary Python libraries.

### 1. Python Environment

* **Python 3.x:** Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/downloads/).
* **Required Python Libraries:**
    * `pygame`
    * `sounddevice`
    * `numpy`
    * `scipy`
    * `hashlib` (usually comes with Python)

### 2. Virtual Audio Cable (Essential for Desktop Audio Input)

To enable the script to listen to your desktop audio (e.g., music from Spotify, YouTube, games), you need a virtual audio cable. This acts like an invisible wire that sends your computer's sound into the program.

* **VB-Audio Virtual Cable:** This is a popular and reliable free option.
    * **Download:** Visit the official VB-Audio website: [https://vb-audio.com/Cable/index.htm](https://vb-audio.com/Cable/index.htm)
    * **Installation:** Download the correct version for your operating system (Windows/macOS) and follow their provided installation instructions. This usually involves unzipping the downloaded file and running the setup executable as an administrator. A system restart might be required.

## Installation & Setup Guide

Follow these steps to get the Strobe Reactor running on your machine:

### Step 1: Get the Project Files

First, you need to get all the code files onto your computer.

1.  **Clone the Repository:** If you're familiar with Git, you can clone this repository:
    ```bash
    git clone [https://github.com/YourUsername/StrobeReactorJon.git](https://github.com/YourUsername/StrobeReactorJon.git)
    cd StrobeReactorJon
    ```
    *(Remember to replace `YourUsername` with your actual GitHub username and `StrobeReactorJon` with your repository name.)*

2.  **Or, Download the ZIP (Easier for Beginners):**
    * On the GitHub page, look for a green button that says **"< > Code"**. Click it.
    * In the small window that pops up, click **"Download ZIP"**.
    * Once the file downloads, find it in your "Downloads" folder. Right-click it and choose **"Extract All..."** (on Windows) or simply double-click it (on macOS) to open the folder.
    * Move this extracted folder (e.g., `StrobeReactorJon-main`) to a place you'll remember easily, like your Desktop or Documents folder. You can rename it to `StrobeReactorJon` if you like.

### Step 2: Install Python Dependencies

With your Python environment set up, install the required libraries using `pip`:

1.  **Open Command Prompt/Terminal:**
    * **Windows:** Search for "cmd" in the Start menu and open "Command Prompt."
    * **macOS:** Search for "Terminal" and open it.
2.  **Navigate to Your Project Folder:** In the Command Prompt/Terminal, type `cd` (which means "change directory") followed by the path to your `StrobeReactorJon` folder.
    * **Example (if on Desktop):** `cd C:\Users\YourName\Desktop\StrobeReactorJon` (Windows) or `cd ~/Desktop/StrobeReactorJon` (macOS).
    * Press Enter.
3.  **Install Libraries:** Once you're in the correct folder, type this command and press Enter:
    ```bash
    pip install -r requirements.txt
    ```
    This command tells Python to install all the necessary libraries listed in the `requirements.txt` file.

### Step 3: Configure Your System Audio

This is the most crucial part for ensuring the script reacts to your desktop audio.

1.  **Set "CABLE Input" as Default Playback Device:**
    * **Windows:**
        * **Right-click** on the speaker icon in the bottom-right corner of your screen (in the system tray).
        * Click **"Sound settings"** (or "Sounds").
        * In the window that opens, go to the **"Playback"** tab.
        * Locate the device named **"CABLE Input (VB-Audio Virtual Cable)"** or similar.
        * **Right-click** on it and select **"Set as Default Device."**
        * **What this does:** Now, all the sound from your computer (music, videos, games) will go into this virtual cable.
        * **Important:** You might not hear your computer's sound through your actual speakers anymore, because it's being "piped" into the virtual cable. Don't worry, we'll fix this in the next optional step if you want to hear it!
    * **macOS:**
        * Go to `System Settings` > `Sound`.
        * In the **"Output"** tab, select **"VB-Cable"** as your output device.

2.  **(Optional, but Recommended): Hear Your Audio While the Program Runs (Using VoiceMeeter)**
    If you set "CABLE Input" as your default playback device, you won't hear your desktop audio through your actual speakers directly. **VoiceMeeter** can help you listen to it while the strobe reactor is listening to it too.

    * **Download VoiceMeeter:** Go to [https://vb-audio.com/Voicemeeter/index.htm](https://vb-audio.com/Voicemeeter/index.htm) and download "VoiceMeeter Standard" (or "Banana" for more features if you're curious).
    * **Install VoiceMeeter:** Follow their installation guide.
    * **Basic VoiceMeeter Setup:**
        * Open VoiceMeeter.
        * In one of the "Virtual Input" sections (e.g., "VoiceMeeter Input"), ensure it's receiving audio from your system's default playback, which is now "CABLE Input."
        * In the "Hardware Out" section (labeled "A1," "A2," etc.), click it and select your actual physical speaker or headphone device (e.g., "Speakers (Realtek Audio)").
        * Make sure the "A1" (or corresponding) button is lit up under that "Virtual Input" to send the audio from the virtual cable back out to your speakers.
    * **Disabling Extra Devices (If You See Too Many):** If you find VoiceMeeter or other audio drivers create a lot of extra "Playback" or "Recording" devices you don't use, you can hide them. In Windows, go to `Sound settings` -> `Playback` or `Recording` tabs, right-click on an unwanted device, and choose "Disable." For macOS, you can manage aggregate devices if they were created, or simply select the desired input/output.

### Step 4: Configure the Script's Audio Input Device

Your Python script needs to know which audio input device to listen to. This will be the "CABLE Output" (the output of the virtual cable, which acts as an input to your script).

1.  **Identify the "CABLE Output" Device Index:**
    * In the same Command Prompt/Terminal you used in Step 2, type these two lines one after the other and press Enter after each:
        ```bash
        python -c "import sounddevice as sd; print(sd.query_devices())"
        ```
    * This will print a long list of all audio devices on your computer.
    * Look through the list carefully for a device named **"CABLE Output (VB-Audio Virtual Cable)"** or something similar.
    * Next to its name, you'll see a number. This is its **index**. For example, if it says `> 3 CABLE Output (VB-Audio Virtual Cable)`, then `3` is the index. **Write down this number!**

2.  **Edit the Code File (`strobe_reactor_jon.py`):**
    * Go back to your `StrobeReactorJon` folder and open the `strobe_reactor_jon.py` file using a simple text editor like Notepad (Windows), TextEdit (macOS - make sure it's in plain text mode), or a code editor like VS Code (recommended!).
    * Scroll to the very bottom of the file. You'll see a section that starts with `try:`.
    * Find the line that looks like this:
        ```python
        with sd.InputStream(callback=audio_callback, samplerate=sample_rate, blocksize=block_size, channels=1, device=None):
        ```
    * You need to change `device=None` to `device=YOUR_INDEX_NUMBER`.
    * **Example:** If the index you found was `3`, change it to:
        ```python
        with sd.InputStream(callback=audio_callback, samplerate=sample_rate, blocksize=block_size, channels=1, device=3):
        ```
    * **Save the `strobe_reactor_jon.py` file.**

### Step 5: Run the Strobe Reactor!

Almost there! Now you can start the program.

1.  **Ensure Audio is Flowing:** Make sure you've set "CABLE Input" as your computer's default playback device (Step 3.3) and that your music or audio is actually playing. If you're using VoiceMeeter to monitor, make sure VoiceMeeter is running too.
2.  **Run the Script:** In your Command Prompt/Terminal (make sure you're still in the `StrobeReactorJon` folder from Step 2.2), type:
    ```bash
    python strobe_reactor_jon.py
    ```
    And press Enter.

A new window should pop up, and as your audio plays, it will start to strobe!

---

## Code Details for Developers

For those interested in the code, here are some specifics:

* **Audio Processing:** The script uses `scipy.signal` for a Butterworth low-pass filter to isolate bass frequencies from the audio input. `numpy` is used for numerical operations on audio data.
* **Visuals:** `pygame` handles the graphical display, drawing the background colors and text.
* **Audio Input:** `sounddevice` manages the real-time audio input stream.
* **Text Integrity Check:**
    The `strobe_reactor_jon.py` file contains the following lines at the top to secure the `ACTUAL_DISPLAY_TEXT`:

    ```python
    # The actual text that will be displayed.
    ACTUAL_DISPLAY_TEXT = "yxs wrldwde™"

    # A SHA256 hash of the original "yxs wrldwde™" text.
    # This hash is used to verify that the ACTUAL_DISPLAY_TEXT has not been altered.
    # This value should NOT be changed unless you intend to change the secured text.
    SECURE_TEXT_HASH = "279a0937a44f8000438a956100570b55b62b1448b15d263901b526978119c43b"

    def verify_text_integrity():
        """
        Verifies the integrity of the display text.
        Calculates the SHA256 hash of ACTUAL_DISPLAY_TEXT and compares it
        to the predefined SECURE_TEXT_HASH. If they do not match,
        the program prints an error and exits.
        """
        current_text_bytes = ACTUAL_DISPLAY_TEXT.encode('utf-8')
        current_hash = hashlib.sha256(current_text_bytes).hexdigest()

        if current_hash != SECURE_TEXT_HASH:
            print("--------------------------------------------------")
            print("!!! INTEGRITY CHECK FAILED: Display text has been altered. !!!")
            print("!!! The program will now exit to maintain integrity. !!!")
            print("--------------------------------------------------")
            pygame.quit()
            exit()
    ```
    This `verify_text_integrity()` function is called at the beginning of the `strobe_loop()` to ensure the `ACTUAL_DISPLAY_TEXT` matches its original hash. If the text is modified, the program will terminate.

---

## Troubleshooting

* **"Integrity Check Failed" Error:**
    This means the text `"yxs wrldwde™"` in the `ACTUAL_DISPLAY_TEXT` variable within `strobe_reactor_jon.py` has been altered. To fix this, ensure the `ACTUAL_DISPLAY_TEXT` variable is **exactly** `"yxs wrldwde™"` (no extra spaces, no missing characters). If you're absolutely sure it's correct and still getting the error, you can generate the correct hash for your specific file's encoding by running this in your terminal (from the project folder):
    ```bash
    python -c "import hashlib; print(hashlib.sha256('yxs wrldwde™'.encode('utf-8')).hexdigest())"
    ```
    Then, copy the output and replace the `SECURE_TEXT_HASH` value in your `strobe_reactor_jon.py` file with the newly generated hash.
* For other issues, please refer to the troubleshooting steps in Step 6 of the "Installation & Setup Guide" above.

---

Enjoy the light show!
