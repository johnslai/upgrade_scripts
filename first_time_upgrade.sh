#!/bin/sh
#url=http://192.168.1.68:8000/images/console-image-beaglebone.tar.gz
#url=http://98.207.234.138:8001/images/console-image-beaglebone.tar.gz
url=http://192.168.1.68:8000/images/console-image-beaglebone.tar.gz

#bud=work
#port=2222

bud=192.168.1.92
port=22

#cd ${ANGSTROM_PATH}/build/tmp-angstrom_v2013_12-eglibc/work/armv7ahf-vfp-neon-angstrom-linux-gnueabi/
scp -P ${port} ./python-argparse_1.2.1-r4.0_armv7ahf-vfp-neon.ipk root@${bud}:
scp -P ${port} ./vt-upgrade_0.1-git4+7bc2990037-r1.1_armv7ahf-vfp-neon.ipk root@${bud}:
ssh -p ${port} root@${bud} opkg install python-argparse_1.2.1-r4.0_armv7ahf-vfp-neon.ipk
ssh -p ${port} root@${bud} opkg install vt-upgrade_0.1-git4+7bc2990037-r1.1_armv7ahf-vfp-neon.ipk
ssh -p ${port} root@${bud} "/usr/bin/python /usr/bin/upgrade.py ${url}"

