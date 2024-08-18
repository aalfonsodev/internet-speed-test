import speedtest
import psutil
import subprocess
import platform

def get_connected_network_info():
    if platform.system() == "Windows":
        try:
            # Get the SSID and signal strength
            result = subprocess.check_output("netsh wlan show interfaces", shell=True, text=True)
            ssid = None
            signal = None
            for line in result.split('\n'):
                if "SSID" in line:
                    ssid = line.split(":")[1].strip()
                if "Signal" in line:
                    signal = line.split(":")[1].strip()
            return ssid, signal
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving network information: {e}")
            return None, None
    else:
        print("This script is designed to run on Windows.")
        return None, None

def test_speed():
    st = speedtest.Speedtest()
    
    print("\n==============================")
    print("       Internet Speed Test     ")
    print("==============================\n")
    
    ssid, signal = get_connected_network_info()
    if ssid and signal:
        print(f"Connected to: {ssid}")
        print(f"Signal Strength: {signal}\n")
    else:
        print("Could not retrieve connected network information.\n")
    
    print("Wait a moment... Speed test is running...\n")
    
    print("1- Finding the best server...")
    best_server = st.get_best_server()
    print(f"   Found: {best_server['host']} located in {best_server['name']}, {best_server['country']}\n")
    
    print("2- Performing download test...")
    download_speed = st.download()
    download_speed_mbps = download_speed / 1_000_000  # Convert to Mbps
    print(f"   Download Speed: {download_speed_mbps:.2f} Mbps\n")
    
    print("3- Performing upload test...")
    upload_speed = st.upload()
    upload_speed_mbps = upload_speed / 1_000_000      # Convert to Mbps
    print(f"   Upload Speed: {upload_speed_mbps:.2f} Mbps\n")
    
    print("==============================\n")
    print("      Test Completed!         \n")
    print("==============================\n")

if __name__ == "__main__":
    test_speed()
    input("Press Enter to exit...")  # Keep the cmd open until Enter is pressed




