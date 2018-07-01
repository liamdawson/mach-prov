#!/bin/bash

TEST_FILE='pool/main/f/firefox/firefox_60.0.2+build1-0ubuntu0.18.04.1_amd64.deb'
MIRRORS=(http://ftp.iinet.net.au/pub/ubuntu/ http://mirror.netspace.net.au/pub/ubuntu/ http://mirror.as24220.net/pub/ubuntu/ http://ubuntu.mirror.solnode.io/ubuntu/ http://mirror.overthewire.com.au/ubuntu/ http://mirror.tcc.wa.edu.au/ubuntu/ http://mirror.internode.on.net/pub/ubuntu/ubuntu/ http://mirror.as24220.net/pub/ubuntu-archive/ http://ubuntu.mirror.serversaustralia.com.au/ubuntu/ http://ubuntu.melbourneitmirror.net/archive/ http://mirror.aarnet.edu.au/pub/ubuntu/archive/ http://mirror.waia.asn.au/ubuntu/ http://mirror.intergrid.com.au/ubuntu/ http://ubuntu.mirror.digitalpacific.com.au/archive/ http://archive.ubuntu.com/ubuntu/)

echo "Mirror, Download time"
for MIRROR in "${MIRRORS[@]}"; do
  echo -e "${MIRROR}, "
  curl -sSL "${MIRROR}${TEST_FILE}" -o /dev/null -w "%{time_total}\n"
done
