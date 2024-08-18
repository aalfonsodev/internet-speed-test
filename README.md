# Internet Speed Test Script

This script is designed to perform an internet speed test and provide information about the currently connected Wi-Fi network on Windows. It utilizes the `speedtest` library to measure download and upload speeds, and `subprocess` to retrieve network information.

## Features

- **Wi-Fi Network Information:** The script retrieves the SSID (network name) and signal strength of the connected Wi-Fi network (Windows only).
- **Internet Speed Test:** It measures the download and upload speeds using the `speedtest` library and provides detailed output.

## Prerequisites

Before running the script, ensure that you have the following installed:

- Python 3.x
- `speedtest-cli` library

You can install the `speedtest-cli` library using pip:

```bash
pip install speedtest-cli

