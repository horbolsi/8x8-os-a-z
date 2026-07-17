# 8x8 OS — READ-ONLY ACTIVE SYSTEM AUDIT
Generated: Fri Jul 17 17:15:32 UTC 2026
Signed: FlashTM8 ⚡️🌎🤖 | ©️8x8

## 1. HOST / KERNEL
```
Linux localhost 6.17.0-PRoot-Distro #1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000 aarch64 GNU/Linux
USER=root  HOME=/root  PWD=/root/.hermes
```

## 2. TERMUX (Android native) — runit services
8x8-main-8086
agent-council-pulse
agents-bot
app-bot
bitcoind
capability-broker-v5
chatgpt-ops-bridge
claude-bot
content-factory
continuity-sentinel
control-plane-readonly
crond
cupsd
dashboard-8099
discord-bot
dockerd
electrum
elite-dashboard
flash-360-interface
flash-bounded-code-factory-v1
flash-bounded-policy-guardian-v1
flash-revenue-autopilot-v1
flash-safe-execution-expander-v1
flashtm8-private
ftpd
hermes-gateway
iphone-node
main-py
master-bot
monitor
openclaw
postgres
private-bot
ssh-agent
sshd
studio
telnetd
tor
tx11
tx11-xfce4

## 3. UBUNTU PROOT — listening ports
State Recv-Q Send-Q Local Address:Port Peer Address:PortProcess

## 4. PROCESSES (top by name)
aid_u0_+  4064  0.0  0.0 12367036 2416 ?       S<    2023   0:10 runsv discord-bot
aid_u0_+  4154  3.0  1.7 2336680 203788 ?      S<l   2023  11:07 /usr/local/lib/hermes-agent/venv/bin/python3 /root/.local/bin/hermes gateway run
aid_u0_+  4173  0.0  0.0 12346564 2332 ?       S<    2023   0:10 svlogd -tt /data/data/com.termux/files/usr/var/log/sv/discord-bot
aid_u0_+  5197  0.1  0.0 12408392 3056 ?       S<    2023   0:32 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c bash -lc ' cd /root/claude-bot exec python3 claude_bot_v3.py '
aid_u0_+  5205  0.3  0.1  41172 15936 ?        S<    2023   1:06 python3 claude_bot_v3.py
aid_u0_+  5213  0.0  0.0 12371528 2980 ?       S<    2023   0:01 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c bash -lc ' cd /root/.hermes/orchestration exec python3 MASTER_BOT_CONTROLLER.py '
aid_u0_+  5222  0.0  0.0 108412 10972 ?        S<    2023   0:01 python3 MASTER_BOT_CONTROLLER.py
aid_u0_+  6307  0.0  0.0 104996  5316 ?        S<sl  2023   0:20 /usr/local/lib/hermes-agent/venv/bin/python3 /usr/local/lib/hermes-agent/tools/mcp_stdio_watchdog.py --ppid 4154 --create-time 1680212798.92 -- /usr/bin/node /root/.hermes/mcp/aikido-bearer/dist/index.js
aid_u0_+  6381  0.0  0.0 779632 10280 ?        S<sl  2023   0:03 /usr/bin/node /root/.hermes/mcp/aikido-bearer/dist/index.js
aid_u0_+ 14360  0.0  0.0 12385468 2484 ?       S<    2023   0:02 runsv agents-bot
aid_u0_+ 14364  0.0  0.0 12350652 2368 ?       S<    2023   0:00 runsv iphone-node
aid_u0_+ 14395  0.0  0.0 12350660 2296 ?       S<    2023   0:00 svlogd -tt /data/data/com.termux/files/usr/var/log/sv/agents-bot
aid_u0_+ 16760  1.2  0.0 990740  8244 ?        S<sl  2023   2:13 node /root/.hermes/lsp/bin/pyright-langserver --stdio
aid_u0_+ 17716  1.1  0.0 897848  8652 ?        S<sl  2023   1:53 node /root/.hermes/lsp/bin/pyright-langserver --stdio
aid_u0_+ 18848 21.4  1.5 1749176 181072 pts/0  S<l+  2023  42:00 /usr/local/lib/hermes-agent/venv/bin/python3 /root/.local/bin/hermes chat
aid_u0_+ 18900  0.2  0.0 12403900 2580 ?       S<    2023   0:13 runsv main-py
aid_u0_+ 19069  0.0  0.0 104996  5724 ?        S<sl  2023   0:10 /usr/local/lib/hermes-agent/venv/bin/python3 /usr/local/lib/hermes-agent/tools/mcp_stdio_watchdog.py --ppid 18848 --create-time 1680223125.69 -- /usr/bin/node /root/.hermes/mcp/aikido-bearer/dist/index.js
aid_u0_+ 19086  0.0  0.0 778864 10660 ?        S<sl  2023   0:01 /usr/bin/node /root/.hermes/mcp/aikido-bearer/dist/index.js
aid_u0_+ 20449  0.0  0.0 12403900 2508 ?       S<    2023   0:04 runsv app-bot
aid_u0_+ 21459  1.1  0.0 12346952 2980 ?       S<    2023   0:13 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c /bin/bash -lc '   cd /root/8x8-os || exit 111   exec /usr/bin/python3 main.py '
aid_u0_+ 21469  1.9  0.7 303728 81544 ?        S<l   2023   0:24 /usr/bin/python3 main.py
aid_u0_+ 22128  0.1  0.0  39652 11272 ?        S<    2023   0:01 python3 /root/8x8-os/background_loop.py
aid_u0_+ 22550  0.0  0.0  23244  6580 ?        S<    2023   0:09 python3 private_bot.py
aid_u0_+ 24757  0.0  0.0 12375228 2332 ?       S<    2023   0:00 runsv claude-bot
aid_u0_+ 24758  0.0  0.0 12348604 2336 ?       S<    2023   0:09 runsv private-bot
aid_u0_+ 24765  0.0  0.0 12352700 2384 ?       S<    2023   0:00 runsv master-bot
aid_u0_+ 24776  0.0  0.0 12387524 2404 ?       S<    2023   0:04 svlogd -tt /data/data/com.termux/files/usr/var/log/sv/private-bot
aid_u0_+ 24778  0.0  0.0 12440772 2368 ?       S<    2023   0:00 svlogd -tt /data/data/com.termux/files/usr/var/log/sv/master-bot
aid_u0_+ 24796  0.0  0.0 12377284 2356 ?       S<    2023   0:01 svlogd -tt /data/data/com.termux/files/usr/var/log/sv/claude-bot
aid_u0_+ 24811  0.2  0.0 12394056 3240 ?       S<    2023   1:57 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c bash -lc 'cd /root/8x8-os && exec /usr/bin/python3 /root/8x8-os/api/dashboard_readonly_8099.py'
aid_u0_+ 24815  1.5  0.0 12346760 2872 ?       S<    2023  13:45 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c bash -lc 'export FLASH_REPO=/root/8x8-os FLASH_HERMES=/root/.hermes FLASH_PUBLIC=/root/.hermes/chatgpt_ops_public; exec python3 /root/.hermes/revenue_autopilot_v1/revenue_autopilot_v1.py'
aid_u0_+ 24819  0.2  0.0 12377480 2672 ?       S<    2023   2:30 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c /bin/bash -lc ' cd /root/reborn-r0-workspace/msg118-control-plane exec /usr/bin/python3 -m uvicorn control_plane.readonly_api:app --host 127.0.0.1 --port 9120 >>/tmp/control_plane_readonly.log 2>&1 '
aid_u0_+ 24822  0.0  0.0 12436872 2688 ?       S<    2023   0:01 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c bash -lc 'export FLASH_REPO=/root/8x8-os FLASH_HERMES=/root/.hermes FLASH_PUBLIC=/root/.hermes/chatgpt_ops_public FLASH_360_PORT=8360; exec python3 /root/.hermes/flash_360_interface/flash_360_server.py'
aid_u0_+ 24823  0.0  0.0 12422536 2940 ?       S<    2023   0:02 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c bash -lc 'export FLASH_REPO=/root/8x8-os FLASH_HERMES=/root/.hermes FLASH_PUBLIC=/root/.hermes/chatgpt_ops_public FLASH_CODE_FACTORY_INTERVAL=600; exec python3 /root/.hermes/bounded_code_factory_v1/bounded_code_factory_v1.py'
aid_u0_+ 24830  0.8  0.0 12391816 3052 ?       S<    2023   7:40 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c /bin/bash -lc ' cd /root/reborn-r0-workspace/msg118-control-plane exec /usr/bin/python3 scripts/continuity_sentinel.py >>/tmp/continuity_sentinel.log 2>&1 '
aid_u0_+ 24831  0.0  0.0 12424584 2904 ?       S<    2023   0:12 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c bash -lc 'export FLASH_REPO=/root/8x8-os FLASH_HERMES=/root/.hermes FLASH_PUBLIC=/root/.hermes/chatgpt_ops_public FLASH_SAFE_EXEC_INTERVAL=120; exec python3 /root/.hermes/safe_execution_expander_v1/safe_execution_expander_v1.py'
aid_u0_+ 24861 16.3  0.0 12402056 3160 ?       S<    2023 141:11 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c bash -lc 'cd /root/8x8-os && exec python3 /root/8x8-os/SYSTEM/chatgpt_ops_bridge/chatgpt_ops_bridge.py'
aid_u0_+ 24876 36.8  0.0 12365192 3156 ?       S<    2023 317:40 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c bash -lc 'export FLASH_REPO=/root/8x8-os FLASH_HERMES=/root/.hermes FLASH_PUBLIC=/root/.hermes/chatgpt_ops_public; exec python3 /root/.hermes/capability_broker_v5/capability_broker_v5.py'
aid_u0_+ 24880  1.7  0.0 12389768 3112 ?       S<    2023  14:55 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c /bin/bash -lc '   export FLASHTM8_INTERVAL=60   cd /root/8x8-os   exec /usr/bin/python3     /root/8x8-os/SYSTEM/flashtm8_runtime/flashtm8_private_supervisor.py '
aid_u0_+ 24883  0.0  0.0 12346760 2588 ?       S<    2023   0:08 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c bash -lc 'export FLASH_REPO=/root/8x8-os FLASH_HERMES=/root/.hermes FLASH_PUBLIC=/root/.hermes/chatgpt_ops_public FLASH_BOUNDED_POLICY_INTERVAL=180; exec python3 /root/.hermes/bounded_policy_guardian_v1/bounded_policy_guardian_v1.py'
aid_u0_+ 24970  0.0  0.0  18556  6072 ?        S<    2023   0:02 python3 /root/.hermes/bounded_code_factory_v1/bounded_code_factory_v1.py
aid_u0_+ 24986  0.1  0.1 181604 14964 ?        S<    2023   0:59 /usr/bin/python3 /root/8x8-os/api/dashboard_readonly_8099.py
aid_u0_+ 24992 21.5  0.0  36000 10260 ?        t<    2023 186:10 python3 /root/.hermes/capability_broker_v5/capability_broker_v5.py
aid_u0_+ 25000  0.8  0.0  20400  8280 ?        S<    2023   7:33 python3 /root/.hermes/revenue_autopilot_v1/revenue_autopilot_v1.py
aid_u0_+ 25005  0.6  0.0 170824 10956 ?        S<l   2023   5:23 /usr/bin/python3 -m uvicorn control_plane.readonly_api:app --host 127.0.0.1 --port 9120
aid_u0_+ 25008  0.2  0.1  39740 11548 ?        S<    2023   1:57 python3 claude_bot_v3.py
aid_u0_+ 25014  2.7  1.2 2141244 148500 ?      S<    2023  24:01 /usr/bin/python3 scripts/continuity_sentinel.py
aid_u0_+ 25018  0.0  0.0  19580  4584 ?        S<    2023   0:07 python3 /root/.hermes/bounded_policy_guardian_v1/bounded_policy_guardian_v1.py
aid_u0_+ 25032  0.0  0.0  19580  6016 ?        S<    2023   0:09 python3 /root/.hermes/safe_execution_expander_v1/safe_execution_expander_v1.py
aid_u0_+ 25069  0.0  0.0 105432  8612 ?        S<    2023   0:17 python3 /root/.hermes/flash_360_interface/flash_360_server.py
aid_u0_+ 25074  6.3  0.1  54304 14456 ?        S<    2023  55:07 python3 /root/8x8-os/SYSTEM/chatgpt_ops_bridge/chatgpt_ops_bridge.py
aid_u0_+ 25077  0.0  0.0  33208 10812 ?        S<    2023   0:43 /usr/bin/python3 /root/8x8-os/SYSTEM/flashtm8_runtime/flashtm8_private_supervisor.py
aid_u0_+ 28037  0.0  0.0 12387424 2312 ?       S<    2023   0:00 runsv postgres
aid_u0_+ 28354  0.0  0.0 12377192 2340 ?       S<    2023   0:00 svlogd -tt /sv/postgres
aid_u0_+ 31733 24.3  0.7 22063880 89744 ?      S<sl  2023   0:04 node /root/.hermes/lsp/bin/bash-language-server start
aid_u0_+ 32302 38.6  0.0 12393864 3704 ?       S<    2023   0:01 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c bash -lc ' cd /root/8x8-os/discord TOKEN=$(python3 -c "import json; print(json.load(open(\"config.json\"))[\"DISCORD_BOT_TOKEN\"])") export DISCORD_BOT_TOKEN="$TOKEN" exec python3 discord_bot.py '
aid_u0_+ 32319 42.6  0.4 217152 50516 ?        S<l   2023   0:01 python3 discord_bot.py
aid_u0_+ 32368  117  0.0 12418440 3728 ?       S<    2023   0:00 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c bash -lc ' set -a [ -f /data/data/com.termux/files/usr/var/service/agents-bot/env ] && . /data/data/com.termux/files/usr/var/service/agents-bot/env [ -f /root/8x8-os/bots/.env ] && . /root/8x8-os/bots/.env set +a cd /root/8x8-os/bots exec python3 unified_agents_bot_v6.py '
aid_u0_+ 32369  128  0.0 12400008 3592 ?       S<    2023   0:00 /data/data/com.termux/files/usr/bin/proot --kill-on-exit --link2symlink --sysvipc --kernel-release=\Linux\localhost\6.17.0-PRoot-Distro\#1 SMP PREEMPT_DYNAMIC Fri, 10 Oct 2025 00:00:00 +0000\aarch64\localdomain\-1\ -L --change-id=0:0 --rootfs=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs --cwd=/root --bind=/dev --bind=/proc --bind=/sys --bind=/dev/urandom:/dev/random --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sys_empty:/sys/fs/selinux --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/loadavg:/proc/loadavg --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/stat:/proc/stat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/uptime:/proc/uptime --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/version:/proc/version --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/vmstat:/proc/vmstat --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_entry_cap_last_cap:/proc/sys/kernel/cap_last_cap --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_inotify_max_user_watches:/proc/sys/fs/inotify/max_user_watches --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowuid:/proc/sys/kernel/overflowuid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/sysdata/sysctl_kernel_overflowgid:/proc/sys/kernel/overflowgid --bind=/data/data/com.termux/files/usr/var/lib/proot-distro/containers/ubuntu/rootfs/tmp:/dev/shm --bind=/data/app --bind=/data/dalvik-cache --bind=/data/misc/apexdata/com.android.art/dalvik-cache --bind=/storage/self/primary:/mnt/sdcard --bind=/storage/self/primary:/sdcard --bind=/storage/self/primary:/storage/emulated/0 --bind=/storage/self/primary:/storage/self/primary --bind=/data/data/com.termux/cache --bind=/data/data/com.termux/files/home --bind=/apex --bind=/odm --bind=/product --bind=/system --bind=/system_ext --bind=/vendor --bind=/linkerconfig/ld.config.txt --bind=/linkerconfig/com.android.art/ld.config.txt --bind=/data/data/com.termux/files/usr /bin/bash -c bash -lc 'cd /root/8x8-os/bots && exec /usr/bin/python3 /root/8x8-os/bots/unified_agents_bot_v6.py'
aid_u0_+ 32382  363  0.2  39420 26148 ?        t<    2023   0:00 python3 unified_agents_bot_v6.py

## 5. GITHUB
github.com
  ✓ Logged in to github.com account horbolsi (/root/.config/gh/hosts.yml)
  - Active account: true
  - Git operations protocol: https
  - Token: gho_************************************
  - Token scopes: 'gist', 'read:org', 'repo'
--- repos ---
horbolsi/8x8		public	2026-07-17T16:56:33Z
horbolsi/8x8-os-backup	8x8 OS Full Backup (clean)	private	2026-07-17T16:56:27Z
horbolsi/8x8-memory	Private decision memory, research provenance, evaluations, corrections, and verified reusable knowledge for 8x8 OS.	private	2026-07-16T16:20:47Z
horbolsi/8x8-messages	Private protocol contracts, schemas, fixtures, adapters, and compatibility tests for 8x8 agent messaging.	private	2026-07-14T05:02:35Z
horbolsi/flash-hermes-sync-safe		private	2026-07-04T01:00:46Z
horbolsi/8x8-os-june2026	8x8 OS June 2026 — Full system with Quran v6, 122 agents, trading, content pipeline	private	2026-06-26T12:17:14Z
horbolsi/8x8-os-private	8x8 OS Private - Internal system, agents, trading, all infrastructure	private	2026-06-26T12:16:49Z
horbolsi/8x8-OS-unified	8x8 OS v1.0 — Unified System (Beyond Quantum)	private	2026-06-18T22:53:05Z
horbolsi/8x8-OS-Ecosystem	8x8 OS Ecosystem public hub - v0.0.1	public	2026-06-14T16:02:10Z
horbolsi/8x8-os-hub	8x8 OS Hub - Web3 Operating System	private	2026-06-14T11:20:00Z

## 6. NEON / DB
--- hub server health (port 3000) ---

## 7. DRIVE / rclone / gdrive
/data/data/com.termux/files/usr/bin/rclone
no rclone/gdrive binary

## 8. 8x8 OS PRODUCTION TREE (proot /root/8x8-os)
#!
04_AGENTS
8x8-miniapp
AGENTS
AI_PROJECTS_RESEARCH.json
ANALYSIS_PORTABLEMINDPRO.md
BLUEPRINT_v2.md
BUILD_SEQUENCE.md
BUILD_STATUS.json
BUILD_STATUS.md
CONTENT_MATRIX_v1.md
LIVE_STATUS.md
MASTER_ARCHITECTURE_v4.md
MASTER_PLAN_v3.md
PLAN.md
QUANTUM_WALLET_ARCHITECTURE.md
RESEARCH_REPORT_2026-06-14.md
RESEARCH_REPORT_COMPREHENSIVE_2026-06-14.md
SECURITY_POLICY_PUBLIC_CHANNELS.md
SYSTEM
SYSTEM_MAP.md
SYSTEM_STATE.json
TECHNICAL_REFERENCE_INDEX.md
TEST_REPORT.md
WALLPACK_PACK_v1.md
__pycache__
agent_registry.json
agent_router.py
agents
api
apps
archive
auth.py
background_loop.py
bots
brain
bridge
config
core
dashboard
dashboards
data
debug
discord
discord_bot.py
docs
elite
final_test.sh
freelance
fresh-hub-server
frontend
get_secret.sh
hub-server
hub-server-clean
index.html
iphone_endpoints.py
js
kernel
knowledge_base.db
launch_all.sh
launch_all_fixed.sh
launch_clean.sh
main.py
main.py.bak_singleton_1784305009
main.py.pre-fix-20260712T224307Z
main_launcher.sh
manifests
memory
memory.py
mind_format
miniapp
miniapp_server.py
mobile
msg121_artifacts
nft_catalog.json
one_shot_setup.sh
orchestrator_state.json
osint
package.json
personality
pipeline
pre_commit_test.sh
private_bot
productions
proposals
public-app
quick_test.cjs
references
render.yaml
requirements-deploy.txt
requirements.txt
scripts
security
self_healing
serve_miniapp.py
shared_memory.py
spatial
start_8086.sh
start_8x8.sh
start_all.sh
start_device_capture.sh
start_live_log.sh
start_live_log_bashrc.sh
start_log_services.sh
start_tunnel.sh
start_tunnel.sh.backup-20260616T084639Z
start_tunnel.sh.pre-fix-20260712T224307Z
subagents
tailwind.config.js
test_all.sh
test_os.cjs
tests
tools
trading
uploads
venv
vite.config.js
wallet_config.json
wallet_data
wallet_system.py
--- core ---
8x8_core.py
FINAL_SCORECARD.md
SYSTEM_INVENTORY.md
__init__.py
__pycache__
agent_bot_launcher.sh
agent_bot_v2.py
agent_bot_v2.py.bak_reorgfix2
agent_brain_logger.py
agent_bus.py
agent_learning_engine.py
agent_learning_engine.py.bak_reorgfix
agent_registry.py
agent_registry.py.backup-20260616T085331Z
agent_registry.py.bak_reorgfix
agent_registry.py.before-json-safe-20260616T085657Z
agent_registry.py.pre-json-fix-20260616T085424Z
agent_toolkit.py
ai_proxy.py
backup_system.py
bitget_trading.py
bootstrap_agents.py
bot_intel_ingest.py
bulletbot.py
cleanup_state_db.py
command_router.py
dashboard_api.py
dashboard_router.py
data_collector.log
data_collector.py
fast_search.py
file_scanner.py
full_audit.py
full_sync.py
intelligence_hub.py
intelligence_squeezer.py
letter_intelligence.py
memory_system.py
memory_vault.db
memory_vault.py
--- scripts ---
8086_flap_remediation.sh
8x8_bot_deploy.sh
8x8_bot_fresh_start.sh
8x8_dashboard_gen.py
8x8_safe_dispatcher_v1.py
8x8_safe_dispatcher_v2.py
__pycache__
add_litellm_dummy_route_v1.sh
agent_coordination.py
agent_coordination.py.bak_reorgfix2
agent_voice.py
auto_publisher.py
backup.sh
bot_cron.sh
bot_keeper.sh
bot_launcher.py
bot_quick.sh
bot_restart.sh
bot_start.sh
bot_watchdog.py
bot_watchdog.sh
build_system_index.sh
build_unified_registry.py
build_unified_registry.py.bak_reorgfix
claude_tools_detector.py
configure_redis.sh
content_producer_v2.py
conversation_logger.py
daemon_starter.py
deploy_bots.py
discord_public_exposure_audit.py
disk_cleanup.sh
elevenlabs_tts.py
environment_observer.py
fal_image_gen.py
fix_postgresql.sh
flash_safe_sync_audit_v2.sh
full_bot_restart.sh
generate_litellm_local_config_v1.sh
health_check.sh

## 9. HERMES CONFIG
8x8log
BOT_FLEET_STATUS.md
BROWSER_BYPASS_STRATEGY.md
CHECKPOINT.md
CONSENSUS_BLUEPRINT_v13.md
CONSENSUS_PANEL_v1.md
CREDENTIALS_VAULT.md
DECISIONS.md
DEEP_AUDIT_COMPLETE.md
DEFINITIVE_PLAN_v13.md
DUAL_DEVICE_ARCHITECTURE.md
EMERGENCY_GUIDELINES_v1.md
FLASH_INTELLIGENCE.md
GITHUB_VULN_REPORT.json
GIT_HISTORY_SANITIZATION_PLAN_20260725.md
GIT_HISTORY_SECRET_EXPOSURE_INVENTORY_20260725.md
GOD_MODE_PLAN.md
GOD_MODE_STATUS.md
GROUNDED_BLUEPRINT_v13_FINAL.md
HANDOFF.md
HERMES_BODY.md
HERMES_COMPLETE_UNDERSTANDING.md
HERMES_SELF_UNDERSTANDING.md
HIERARCHICAL_DISPATCH.md
LIFE_BOOK.md
LIVING_BOOK.md
LOCAL_DUPLICATE_CLEANUP_MANIFEST_20260725.md
MASTER_BLUEPRINT_v13.md
MASTER_SYSTEM_BLUEPRINT.md
MASTER_SYSTEM_MAP_v12.md
MASTER_UNIFIED.db
MEMORY.md
MODEL_HANDOFF.md
MODEL_REGISTRY.md
MODEL_ROUTING_MASTER.md
MSG20-MASTER
PERFECT_REBIRTH_PHASE3.md
PERSISTENT_SYSTEM_STATE.json
REBUILD_PLAN_v13.md
SECRET_INVENTORY_ANALYSIS_20260725.md
SECRET_SANITIZATION_PLAN_20260725.md
SECURITY_AUDIT_20260527.md
SECURITY_PROTOCOL.md
SESSION_STATE.md
SHARED_BRAIN.json
SOUL.md
STARTUP.sh
STRATEGIC_PLAN_v1.md
SURVIVAL_PLAN.json
SYSTEM_PARTITION_PLAN.md
SYSTEM_REPORT_20260622.md
SYSTEM_STATUS.json
SYSTEM_UPGRADE_RECONCILE_2026-07-17.md
TEST_RESULTS.json
TOTAL_MEMORY.db
TRADING_ENGINE_DESIGN.md
ULTIMATE_ENHANCEMENT_PLAN.md
ULTIMATE_TEST_RESULTS.json
ULTIMATE_UPGRADE_PLAN.md
USER.md
VPS_GUIDE.md
agent_brain.db
agent_brain_api.py
agent_bridge
agent_content_worker.py
agent_dashboard.html
agent_data
agent_fleet_builder.py
agent_roster.md
agents_bot.log.bak_20260605_184232
app_users.db
archive
archive_old_states
assessments
audio_cache
auth.json
auth.lock
autonomy
backups
bin
bots
bounded_code_factory_v1
bounded_policy_guardian_v1
brain_coordination.db
bridge
build_content_atlas.py
cache
capabilities
capability_broker_v5
channel_directory.json
chatgpt_ops_bridge_runtime
chatgpt_ops_public
checkpoints
config.bak.pre_ultimate_v3
config.yaml
config.yaml.backup-20260616
config.yaml.backup-20260620-055513
config.yaml.backup-pre-proxy
config.yaml.backup_1783475443
config.yaml.bak
config.yaml.bak.20260521_204716
config.yaml.bak.20260522_142519
config.yaml.bak.20260608_164612
config.yaml.bak.20260610
config.yaml.bak.20260612_080339
config.yaml.bak.20260612_084658
config.yaml.bak.20260615_225804
config.yaml.bak.agent_models_1781687039
config.yaml.bak.before_fix_20260612_172700
config.yaml.bak.fallback_dict_1781686613
config.yaml.bak.fallback_order_1781686999
config.yaml.bak.pre-upgrade
config.yaml.bak.pre_7accounts_rebuild
config.yaml.bak.pre_fix
config.yaml.bak.pre_fix_20260611
config.yaml.bak.pre_router_v2
config.yaml.bak.pre_v22
config.yaml.bak.session_restart_20260610_054002
config.yaml.bak.switcher_fix
config.yaml.broken
config.yaml.pre-fix-20260712T224307Z
config_backups
content
content_atlas.db
content_deployer.log
content_empire_v3.py
content_empire_v4.py
content_factory.py
content_factory_state.json
content_factory_v2.py
content_generator.log
content_orchestrator_state.txt
context_length_cache.yaml
continuous_ops
court
credentials_vault.md.gpg
cron
daemon
dashboard
data
decrypt_env.sh
deep_intelligence
discord_expansion_p2_report.json
discord_expansion_report.json
discord_intel.db
discord_telegram_sync_map.json
discord_threads.json
docs
drafts
email_management.md
entertainment_engine.py
entertainment_state.json
facebook
flash_360_interface
flashtm8_private
freelance
gateway
gateway.lock
gateway.log.recovered-20260615
gateway.pid
gateway_healer.py
gateway_monitor.db
gateway_state.json
gateway_state.json.backup.20260614-133821
gateway_voice_mode.json
health_logs
hooks
image_cache
images
income
init_agent_brain.py
integrations
intel
intel_flywheel
intelligence
intelligence_data
interrupt_debug.log
iphone-connect.sh
iphone-node-setup.sh
kanban
kanban.db
kanban.db-shm
kanban.db-wal
kanban.db.dispatch.lock
kanban.db.init.lock
knowledge_distillery
knowledge_graph.db
litellm
litellm_sandbox_v1
logs
lsp
manual_ready
marketing
master_api_registry.json
mcp
memories
memory_backups
memory_graph
memory_graph.db
memory_query.py
memory_vault.db
messages
migration
model_catalog.json
model_catalog.last_refresh
model_ratings.json
model_ratings_final.json
model_usage_tracking.json
models_dev_cache.json
monitor_config_v2.json
msg20-backup
news_aggregator.log
news_intel.db
nodes
notifications
ollama_cloud_models_cache.json
omega
optimal_rotation.json
or_router_v3_state.json
or_router_v5_state.json
orchestration
osint_reports
pairing
pastes
pending
phase-e-backup
plans
plugins
prefill_context.json
prefill_context.json.backup.20260614-132217
prefill_context.json.backup.20260614-132508
prefill_context.md
presence
private_backups
private_reports
private_staging
proactive_log.jsonl
processes.json
profiles
proposals
provider-repair-20260617T075206Z
provider_models_cache.json
provider_resilience
provider_status.json
public_app_bot.log.bak_20260605_184232
publishing_config.json
receipts
recovery-backups
relay
reports
response_cache
response_cache.db
response_cache.json
revenue_autopilot_v1
robustness_report.md
router
safe_execution_expander_v1
sandboxes
scripts
security
security_quarantine
session_history
session_log.jsonl
sessions
sessions.db
skills
smart_model_router_v3.json
smart_router_state.json
smarts
social
soma
staging
state
state-snapshots
state.db
state.db-shm
state.db-wal
studio
task_queue
telegram_intel.db
telegram_user_client
telemetry
territory_map.json
tiktok
trade_journal.db
trades.db
trading
ultimate_router_state.json
vault
venv
venvs
verification_evidence.db
voice_cache
work
working_models.json
x
youtube
--- skills count ---
55

## 10. INTERNAL STORAGE (8x8 OS) top-level
00_CONTROL
00_HERMES_SYNC
00_HERMES_SYNC_BACKUP_20260620_085127
00_HERMES_SYNC_GITHUB_SAFE_EXPORT
01_STUDIO
02_CONTENT
03_TRADING
04_AGENTS
05_SYSTEM
06_MEDIA
07_DOCS
08_ARCHIVE
09_AGENT_LIVE_SYNC
8x8log
AI chats
DASHBOARD.html
EMPIRE
MEDIA
SYSTEM
nodes

## 11. YOUTUBE OAUTH present?
-rw-r--r--+ 1 root root 848 Jul  3 21:56 /root/.hermes/youtube/oauth_token.json

## 12. EMAIL (himalaya)
/root/.local/bin/himalaya
himalaya v1.2.0 +pgp-commands +maildir +wizard +imap +sendmail +smtp
build: linux musl aarch64
git: nix-flake-20260219100512, rev 1b70c4e0eaa72dee48353f0211e6cc0f0776fe98

## 13. FFMPEG / EDGE-TTS / PIL (video pipeline)
/data/data/com.termux/files/usr/bin/ffmpeg
PIL+edge_tts OK
