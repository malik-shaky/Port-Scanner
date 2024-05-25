# Port-Scanner
This Python script is designed to scan open ports on specified targets and grab banners from those ports. It utilizes *sockets* for network communication and the *termcolor* library for colored terminal output, providing a user-friendly experience.

## Features
- **Port Scanning Prowess:** Initiate scans across a spectrum of ports on one or multiple targets seamlessly.
- **Banner Intelligence:** Gain access to banners from open ports, unraveling essential details about operational services.

## Usage:
1. **Ensure Python is Installed:**
   - Kali Linux comes with Python pre-installed. Verify the installation by opening a terminal and typing:
     ```bash
     python3 --version
     ```

2. **Save the Script:**
   - Clone the repository or download the script.

3. **Run the Script:**
   - Open your terminal.
   - Navigate to the directory where your script is saved using the `cd` command. For example:
     ```bash
     cd path/to/your/script
     ```
   - Run the script by typing:
     ```bash
     python3 port_scanner.py
     ```

4. **Enter the Target Machine/Machines and Ports:**
   - Follow the prompts to input target IP addresses and the desired number of ports to scan.


## Example:
To run the script, follow these steps:
```bash
cd ~/scripts
python3 port_scanner.py
