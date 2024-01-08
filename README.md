# Direct-Link-Player-Extension

**Overview:**
Direct-Link-Player-Extension is a browser extension that enhances your media player experience by providing a right-click menu option to open video links directly in your media player. Please exercise caution and ensure the safety of the links you open, as this functionality can pose security risks.

**Compatibility:**
- This extension is set up for Chrome and Edge browsers. While it has not been tested on Mozilla, it may work with appropriate adjustments.

**Requirements:**
- Your media player must support opening online streaming from direct download links and do so from the command line.
- We recommend using [MPV Player](https://mpv.io/installation/), a reliable and compatible media player.

## Extension Setup:

**1. Clone the Project:**
   - Open a terminal and run the following command:
     ```bash
     git clone https://github.com/mett-E/Direct-Link-Player-Extension
     ```
   - Alternatively, download the files to a folder.

**2. Load Extension:**
   - Open your browser and go to:
     - `chrome://extensions` for Chrome.
     - `edge://extensions` for Edge.
   - Turn on "Developer mode" and click "Load unpacked," then select the directory containing extension files.
   - A new extension will appear in your browser.

**3. Add Native Manifest:**
   - Open a command prompt (cmd) and add the native manifest JSON file:
     - For Chrome:
       ```bash
       REG ADD HKCU\Software\Google\Chrome\NativeMessagingHosts\com.metti.pythonnativehost /ve /t REG_SZ /d "path/to/native/native manifest.json" /f
       ```
     - For Edge:
       ```bash
       REG ADD "HKCU\Software\Microsoft\Edge\NativeMessagingHosts\com.metti.pythonnativehost" /ve /t REG_SZ /d "path/to/native/native manifest.json" /f
       ```
     - Replace "path/to/native/native manifest.json" with the actual path.

**4. Update Native Manifest:**
   - Add the extension's ID to "allowed_origins" in the native manifest JSON file. Find the ID in the extensions menu of your browser.

**5. Modify Native.py:**
   - Make the necessary changes to `native.py`, especially the `videoplayer_executable_path`.

**6. Compile with PyInstaller:**
   - Open a terminal and run the following command to compile `native.py` with PyInstaller:
     ```python
     pyinstaller --onefile --noconsole native.py
     ```
   - Add the path of the executable to your "native manifest.json" file.
