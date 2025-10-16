# System Monitor Test Project

This test project verifies that all monitoring tools are properly installed and working.

## Running Tests

```bash
# Make the test script executable
chmod +x monitor_test.sh

# Run the test
./monitor_test.sh
```

## Example Python Monitoring Script

Create a file `monitor.py`:

```python
#!/usr/bin/env python3
import psutil
import time

def monitor_system(duration=10, interval=1):
    """Monitor system resources for a specified duration."""
    print("=== System Monitoring ===")
    print(f"Monitoring for {duration} seconds...\n")
    
    for i in range(duration):
        # CPU
        cpu_percent = psutil.cpu_percent(interval=0.1)
        
        # Memory
        mem = psutil.virtual_memory()
        
        # Disk
        disk = psutil.disk_usage('/')
        
        # Network
        net = psutil.net_io_counters()
        
        print(f"[{i+1}] CPU: {cpu_percent}% | "
              f"Memory: {mem.percent}% | "
              f"Disk: {disk.percent}% | "
              f"Net: ↓{net.bytes_recv/1024/1024:.1f}MB ↑{net.bytes_sent/1024/1024:.1f}MB")
        
        time.sleep(interval)
    
    print("\nMonitoring complete!")

if __name__ == "__main__":
    monitor_system()
```

Then run it:
```bash
python3 monitor.py
```
