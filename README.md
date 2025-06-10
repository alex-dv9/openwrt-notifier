# openwrt-notifier

simple script that send message to your telegram account when someone:
  1. start or exit ssh session
  2. establish ssh connection using some publickey
  3. successfully login to web interface (luci)

## why there are two different scripts that, basically, do same thing?

the first one I wrote was the .py version, but I realized that it would be problematic to install python on my router... so I rewrote the script in bash... ash... whatever.
