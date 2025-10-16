#!/bin/bash
# Test script to verify monitoring tools are installed and working

echo "=== System Monitoring Tools Test ==="
echo ""

# Test basic monitoring tools
echo "Testing htop..."
if command -v htop &> /dev/null; then
    echo "✓ htop is installed"
    htop --version
else
    echo "✗ htop is NOT installed"
fi
echo ""

echo "Testing btop..."
if command -v btop &> /dev/null; then
    echo "✓ btop is installed"
    btop --version
else
    echo "✗ btop is NOT installed"
fi
echo ""

echo "Testing glances..."
if command -v glances &> /dev/null; then
    echo "✓ glances is installed"
    glances --version
else
    echo "✗ glances is NOT installed"
fi
echo ""

echo "Testing sysstat (sar)..."
if command -v sar &> /dev/null; then
    echo "✓ sysstat is installed"
    sar -V
else
    echo "✗ sysstat is NOT installed"
fi
echo ""

echo "Testing iotop..."
if command -v iotop &> /dev/null; then
    echo "✓ iotop is installed"
    iotop --version
else
    echo "✗ iotop is NOT installed"
fi
echo ""

echo "Testing Python psutil..."
python3 -c "import psutil; print('✓ psutil is installed'); print('CPU count:', psutil.cpu_count())" 2>/dev/null || echo "✗ psutil is NOT installed"
echo ""

echo "Testing network tools..."
if command -v iftop &> /dev/null; then
    echo "✓ iftop is installed"
else
    echo "✗ iftop is NOT installed"
fi

if command -v nethogs &> /dev/null; then
    echo "✓ nethogs is installed"
else
    echo "✗ nethogs is NOT installed"
fi
echo ""

echo "=== Quick System Stats ==="
echo "CPU cores: $(nproc)"
echo "Memory: $(free -h | grep Mem | awk '{print $2}')"
echo "Disk usage: $(df -h / | tail -1 | awk '{print $5}')"
echo ""

echo "=== Test Complete ==="
