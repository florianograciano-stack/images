#!/usr/bin/env python3
"""
Example system monitoring script using psutil.
This demonstrates the monitoring capabilities available in the container.
"""

import psutil
import time
import sys


def print_separator(char="=", length=60):
    """Print a separator line."""
    print(char * length)


def monitor_cpu():
    """Monitor CPU usage."""
    print("\n🖥️  CPU Information")
    print_separator("-")
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores: {psutil.cpu_count(logical=True)}")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    
    # Per-core usage
    per_cpu = psutil.cpu_percent(interval=1, percpu=True)
    for i, cpu in enumerate(per_cpu):
        print(f"Core {i}: {cpu}%")


def monitor_memory():
    """Monitor memory usage."""
    print("\n💾 Memory Information")
    print_separator("-")
    mem = psutil.virtual_memory()
    print(f"Total: {mem.total / (1024**3):.2f} GB")
    print(f"Available: {mem.available / (1024**3):.2f} GB")
    print(f"Used: {mem.used / (1024**3):.2f} GB ({mem.percent}%)")
    print(f"Free: {mem.free / (1024**3):.2f} GB")
    
    # Swap memory
    swap = psutil.swap_memory()
    print(f"\nSwap Total: {swap.total / (1024**3):.2f} GB")
    print(f"Swap Used: {swap.used / (1024**3):.2f} GB ({swap.percent}%)")


def monitor_disk():
    """Monitor disk usage."""
    print("\n💿 Disk Information")
    print_separator("-")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"\nDevice: {partition.device}")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system: {partition.fstype}")
            print(f"  Total: {usage.total / (1024**3):.2f} GB")
            print(f"  Used: {usage.used / (1024**3):.2f} GB ({usage.percent}%)")
            print(f"  Free: {usage.free / (1024**3):.2f} GB")
        except PermissionError:
            continue


def monitor_network():
    """Monitor network statistics."""
    print("\n🌐 Network Information")
    print_separator("-")
    net_io = psutil.net_io_counters()
    print(f"Bytes sent: {net_io.bytes_sent / (1024**2):.2f} MB")
    print(f"Bytes received: {net_io.bytes_recv / (1024**2):.2f} MB")
    print(f"Packets sent: {net_io.packets_sent}")
    print(f"Packets received: {net_io.packets_recv}")
    
    # Per-interface stats
    net_if = psutil.net_io_counters(pernic=True)
    print("\nPer-interface statistics:")
    for interface, stats in net_if.items():
        print(f"  {interface}:")
        print(f"    Sent: {stats.bytes_sent / (1024**2):.2f} MB")
        print(f"    Received: {stats.bytes_recv / (1024**2):.2f} MB")


def monitor_processes(top_n=5):
    """Monitor top processes by CPU and memory usage."""
    print(f"\n⚙️  Top {top_n} Processes by CPU")
    print_separator("-")
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    # Sort by CPU usage
    cpu_sorted = sorted(processes, key=lambda x: x['cpu_percent'] or 0, reverse=True)
    for i, proc in enumerate(cpu_sorted[:top_n], 1):
        print(f"{i}. {proc['name']} (PID: {proc['pid']})")
        print(f"   CPU: {proc['cpu_percent'] or 0}%, Memory: {proc['memory_percent'] or 0:.2f}%")
    
    print(f"\n📊 Top {top_n} Processes by Memory")
    print_separator("-")
    mem_sorted = sorted(processes, key=lambda x: x['memory_percent'] or 0, reverse=True)
    for i, proc in enumerate(mem_sorted[:top_n], 1):
        print(f"{i}. {proc['name']} (PID: {proc['pid']})")
        print(f"   CPU: {proc['cpu_percent'] or 0}%, Memory: {proc['memory_percent'] or 0:.2f}%")


def continuous_monitor(interval=2, duration=10):
    """Continuously monitor system for specified duration."""
    print(f"\n🔄 Continuous Monitoring (every {interval}s for {duration}s)")
    print_separator("=")
    
    iterations = duration // interval
    for i in range(iterations):
        cpu = psutil.cpu_percent(interval=0.5)
        mem = psutil.virtual_memory()
        net = psutil.net_io_counters()
        
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] CPU: {cpu:5.1f}% | "
              f"Memory: {mem.percent:5.1f}% | "
              f"Disk: {psutil.disk_usage('/').percent:5.1f}% | "
              f"Net: ↓{net.bytes_recv/(1024**2):7.1f}MB ↑{net.bytes_sent/(1024**2):7.1f}MB")
        
        if i < iterations - 1:
            time.sleep(interval)


def main():
    """Main function to run all monitoring tasks."""
    print_separator("=")
    print("🔍 System Monitoring Demo")
    print("Using psutil in the System Monitor Dev Container")
    print_separator("=")
    
    try:
        monitor_cpu()
        monitor_memory()
        monitor_disk()
        monitor_network()
        monitor_processes()
        continuous_monitor()
        
        print("\n" + "="*60)
        print("✅ Monitoring complete!")
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Monitoring interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
