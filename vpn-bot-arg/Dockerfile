FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
  apt-get install -y -o APT::Install-Recommends=false -o APT::Install-Suggests=false \
  ca-certificates \
  netcat \
  ipppd \
  wget \
  libgdk-pixbuf2.0-0>=2.22.0 \
  libglib2.0-0>=2.12.0 \
  libgtk2.0-0>=2.24.0 \
  libpango-1.0-0>=1.14.0 \
  libsm6 \
  libx11-6 \
  libxinerama1 \
  && apt-get clean -q && apt-get autoremove --purge \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /root

# Install fortivpn client unofficial .deb
RUN wget 'https://hadler.me/files/forticlient-sslvpn_4.4.2333-1_amd64.deb' -O forticlient-sslvpn_amd64.deb \
    && dpkg -i forticlient-sslvpn_amd64.deb \
    && rm forticlient-sslvpn_amd64.deb \
    && mknod /dev/ppp c 108 0

ENTRYPOINT [ "/opt/forticlient-sslvpn/64bit/forticlientsslvpn_cli" ]

# CMD ["/bin/bash"]

