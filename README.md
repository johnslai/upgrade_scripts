upgrade scripts
===============
Scripts for deploying bud firmware upgrades

First Time Upgrade
------------------
It assumes that the bud was loaded with old firmware without upgrading capabilities, but the emmc has already been partitioned into 4 blocks.

###To use
* script name: *first_time_upgrade.sh*.
* Modify the first 3 lines of the scripts:
    * url: url where firmware and the md5 file are hosted.
    * bud: ip address or fqdn of the bud
    * port: ssh port to communicate with bud
* I use it by cloning this repo to the server which can access the buds(tunnel.building.ai)

Convert gdaq configuration
--------------------------
New GDAQ uses configuration format and parameters different from that of old GDAQ.
conf_to_json.py convert the old configuration(*gdaq.conf*) automatically to the new one(*gdaq.json*).

###To use
* script name: conf_to_json.py
* copy */etc/conf.d/gdaq.conf* from the bud
```sh
cd conf_to_json
python conf_to_json.py gdaq.conf
```
The converted configuration *gdaq.json* will be generated.
