# System Monitoring Development Container
# Includes tools for monitoring system resources, processes, and performance

ARG VARIANT=bookworm
FROM debian:${VARIANT}

# Install system monitoring tools
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    # Basic monitoring tools
    htop \
    btop \
    glances \
    sysstat \
    iotop \
    iftop \
    nethogs \
    nmon \
    atop \
    dstat \
    # System information tools
    lshw \
    lsof \
    strace \
    procps \
    psmisc \
    # Network monitoring
    net-tools \
    iproute2 \
    iputils-ping \
    tcpdump \
    nmap \
    # Disk monitoring
    smartmontools \
    iotop \
    ncdu \
    # Performance analysis
    perf-tools-unstable \
    linux-perf \
    sysstat \
    # Additional utilities
    curl \
    wget \
    vim \
    nano \
    git \
    jq \
    python3 \
    python3-pip \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Install Python-based monitoring tools (psutil is already available from system packages)
# Note: Additional Python monitoring packages can be installed with:
# pip3 --disable-pip-version-check --no-cache-dir install --break-system-packages py-cpuinfo gpustat

# Create a non-root user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

USER $USERNAME
