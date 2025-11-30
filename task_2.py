
import psutil # pyright: ignore[reportMissingModuleSource]
import time
import sys

def monitor_cpu(threshold=80):
    """
    Monitors CPU usage and alerts if it exceeds the threshold.
    Runs indefinitely until interrupted.
    """
    print("Monitoring CPU usage... (Press Ctrl+C to stop)")
    try:
        while True:
            # Get CPU usage percentage (over 1 second interval)
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            time.sleep(1)  # Optional: Adjust polling interval as needed
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Error during monitoring: {e}")
        sys.exit(1)

if __name__ == "__main__":
    monitor_cpu()  # Default threshold is 80%