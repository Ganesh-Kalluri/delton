#!/usr/bin/env bash

sudo mount -o remount,rw /

sudo service led-status stop
sudo service leewise stop

cd /home/pi/leewise
localbranch=$(git symbolic-ref -q --short HEAD)
localremote=$(git config branch.$localbranch.remote)

echo "addons/point_of_sale/tools/posbox/overwrite_after_init/home/pi/leewise" >> .git/info/sparse-checkout

git fetch "${localremote}" "${localbranch}" --depth=1
git reset "${localremote}"/"${localbranch}" --hard

git clean -dfx
cp -a /home/pi/leewise/addons/point_of_sale/tools/posbox/overwrite_after_init/home/pi/leewise/* /home/pi/leewise/
rm -r /home/pi/leewise/addons/point_of_sale/tools/posbox/overwrite_after_init

sudo find / -type f -name "*.iotpatch" 2> /dev/null | while read iotpatch; do
    DIR=$(dirname "${iotpatch}")
    BASE=$(basename "${iotpatch%.iotpatch}")
    sudo find "${DIR}" -type f -name "${BASE}" ! -name "*.iotpatch" | while read file; do
        sudo patch -f "${file}" < "${iotpatch}"
    done
done

sudo mount -o remount,ro /
sudo mount -o remount,rw /root_bypass_ramdisks/etc/cups

sudo service led-status start

(sleep 5 && sudo service leewise restart) &
