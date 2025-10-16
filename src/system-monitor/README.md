# System Monitor Development Container

This development container includes a comprehensive set of system monitoring tools for analyzing PC/system performance, processes, network activity, and resource usage.

## Tools Included

### Process and CPU Monitoring
- **htop** - Interactive process viewer
- **btop** - Modern resource monitor with a clean interface
- **atop** - Advanced system and process monitor
- **glances** - Cross-platform monitoring tool with web UI
- **nmon** - Performance monitoring tool

### System Statistics
- **sysstat** - Collection of performance monitoring tools (sar, iostat, mpstat, pidstat)
- **dstat** - Versatile resource statistics tool

### I/O and Disk Monitoring
- **iotop** - I/O monitoring per process
- **ncdu** - Disk usage analyzer with ncurses interface
- **smartmontools** - Disk health monitoring

### Network Monitoring
- **iftop** - Network bandwidth monitoring
- **nethogs** - Network traffic per process
- **nmap** - Network discovery and security auditing
- **tcpdump** - Packet analyzer

### System Information
- **lshw** - Hardware information
- **lsof** - List open files
- **strace** - System call tracer
- **perf** - Performance analysis tools
- **psutil** (Python) - System and process monitoring library (installed via apt)

## Usage

### Quick Start

1. Open this folder in VS Code with the Dev Containers extension installed
2. When prompted, click "Reopen in Container"
3. Start monitoring with your preferred tool:

```bash
# Interactive process monitoring
htop

# Modern resource monitor
btop

# Comprehensive system monitoring with web interface
glances

# Network bandwidth monitoring
sudo iftop

# I/O monitoring
sudo iotop

# System statistics
sar -u 2 10  # CPU usage every 2 seconds, 10 times
```

### Common Monitoring Commands

#### CPU Monitoring
```bash
# Real-time CPU usage
mpstat 1

# Per-process CPU usage
pidstat 1

# CPU information
lscpu
python3 -c "import cpuinfo; print(cpuinfo.get_cpu_info())"
```

#### Memory Monitoring
```bash
# Memory usage
free -h

# Per-process memory
ps aux --sort=-%mem | head

# Detailed memory statistics
vmstat 1
```

#### Disk Monitoring
```bash
# Disk usage
df -h

# Disk I/O statistics
iostat -x 2

# Directory size
ncdu /

# SMART disk health
sudo smartctl -a /dev/sda
```

#### Network Monitoring
```bash
# Network interface statistics
ip -s link

# Network connections
ss -tunapl

# Real-time bandwidth per interface
iftop -i eth0

# Bandwidth per process
sudo nethogs
```

#### Process Monitoring
```bash
# Interactive process viewer
htop

# Find process by name
pgrep -l firefox

# Process details
ps -fp <PID>

# Open files by process
lsof -p <PID>
```

### Python Monitoring Scripts

```python
import psutil

# CPU usage
print(f"CPU Usage: {psutil.cpu_percent()}%")

# Memory usage
mem = psutil.virtual_memory()
print(f"Memory Usage: {mem.percent}%")

# Disk usage
disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}%")

# Network I/O
net = psutil.net_io_counters()
print(f"Bytes Sent: {net.bytes_sent}, Bytes Received: {net.bytes_recv}")
```

## Container Features

This container includes special capabilities for system monitoring:
- `SYS_PTRACE` - For process tracing with tools like strace
- `NET_ADMIN` - For network monitoring tools
- `SYS_ADMIN` - For advanced system monitoring

Host `/proc` and `/sys` are mounted as read-only for system information access.

## Use Cases

- Performance analysis and optimization
- System resource monitoring
- Network traffic analysis
- Process debugging and profiling
- Capacity planning
- Identifying bottlenecks
- Security monitoring and auditing

## Notes

- Some monitoring tools require elevated privileges (sudo)
- Network monitoring tools work best when run with appropriate permissions
- For production monitoring, consider using dedicated monitoring solutions like Prometheus, Grafana, or Datadog

## Contributing

See the [main repository](https://github.com/devcontainers/images) for contribution guidelines.

## License

Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License. See [LICENSE](https://github.com/devcontainers/images/blob/main/LICENSE).
