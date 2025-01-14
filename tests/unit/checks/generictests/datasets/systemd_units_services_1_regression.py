# yapf: disable
checkname = 'systemd_units'

info = [
    ['[list-unit-files]'],
    ['[all]'],
    ['UNIT', 'LOAD', 'ACTIVE', 'SUB', 'DESCRIPTION'],
    [
        'proc-sys-fs-binfmt_misc.automount', 'loaded', 'active', 'running', 'Arbitrary',
        'Executable', 'File', 'Formats', 'File', 'System', 'Automount', 'Point'
    ],
    [
        'dev-disk-by\\x2did-ata\\x2dAPPLE_SSD_SM0256G_S29CNYDG865465.device', 'loaded', 'active',
        'plugged', 'APPLE_SSD_SM0256G'
    ],
    ['dev-mapper-cryptswap1.device', 'loaded', 'inactive', 'dead', 'dev-mapper-cryptswap1.device'],
    ['cups.path', 'loaded', 'active', 'running', 'CUPS', 'Scheduler'],
    [
        'systemd-ask-password-console.path', 'loaded', 'inactive', 'dead', 'Dispatch', 'Password',
        'Requests', 'to', 'Console', 'Directory', 'Watch'
    ],
    [
        'systemd-ask-password-wall.path', 'loaded', 'active', 'waiting', 'Forward', 'Password',
        'Requests', 'to', 'Wall', 'Directory', 'Watch'
    ],
    ['init.scope', 'loaded', 'active', 'running', 'System', 'and', 'Service', 'Manager'],
    [
        'alsa-restore.service', 'loaded', 'active', 'exited', 'Save/Restore', 'Sound', 'Card',
        'State'
    ],
    ['anacron.service', 'loaded', 'inactive', 'dead', 'Run', 'anacron', 'jobs'],
    ['avahi-daemon.service', 'loaded', 'active', 'running', 'Avahi', 'mDNS/DNS-SD', 'Stack'],
    [
        'binfmt-support.service', 'loaded', 'active', 'exited', 'Enable', 'support', 'for',
        'additional', 'executable', 'binary', 'formats'
    ],
    ['bluetooth.service', 'loaded', 'active', 'running', 'Bluetooth', 'service'],
    ['check-mk-enterprise-1.4.0p34.service', 'loaded', 'active', 'exited', 'LSB:', 'OMD', 'sites'],
    [
        'colord.service', 'loaded', 'active', 'running', 'Manage,', 'Install', 'and', 'Generate',
        'Color', 'Profiles'
    ],
    [
        'cpufrequtils.service', 'loaded', 'active', 'exited', 'LSB:', 'set', 'CPUFreq', 'kernel',
        'parameters'
    ],
    [
        'cron.service', 'loaded', 'active', 'running', 'Regular', 'background', 'program',
        'processing', 'daemon'
    ],
    ['emergency.service', 'loaded', 'inactive', 'dead', 'Emergency', 'Shell'],
    ['festival.service', 'not-found', 'inactive', 'dead', 'festival.service'],
    ['getty@tty1.service', 'loaded', 'active', 'running', 'Getty', 'on', 'tty1'],
    [
        'kmod-static-nodes.service', 'loaded', 'active', 'exited', 'Create', 'list', 'of',
        'required', 'static', 'device', 'nodes', 'for', 'the', 'current', 'kernel'
    ],
    [
        'systemd-cryptsetup@cryptswap1.service', 'loaded', 'failed', 'failed', 'Cryptography',
        'Setup', 'for', 'cryptswap1'
    ],
    ['systemd-udevd.service', 'loaded', 'active', 'running', 'udev', 'Kernel', 'Device', 'Manager'],
    ['systemd-update-done.service', 'not-found', 'inactive', 'dead', 'systemd-update-done.service'],
    [
        'systemd-update-utmp-runlevel.service', 'loaded', 'inactive', 'dead', 'Update', 'UTMP',
        'about', 'System', 'Runlevel', 'Changes'
    ],
    [
        'systemd-update-utmp.service', 'loaded', 'active', 'exited', 'Update', 'UTMP', 'about',
        'System', 'Boot/Shutdown'
    ],
    ['systemd-user-sessions.service', 'loaded', 'active', 'exited', 'Permit', 'User', 'Sessions'],
    [
        'systemd-vconsole-setup.service', 'not-found', 'inactive', 'dead',
        'systemd-vconsole-setup.service'
    ],
    [
        'tacacs_plus.service', 'loaded', 'active', 'running', 'LSB:', 'TACACS+', 'authentication',
        'daemon'
    ],
    ['thermald.service', 'loaded', 'active', 'running', 'Thermal', 'Daemon', 'Service'],
    ['udisks2.service', 'loaded', 'active', 'running', 'Disk', 'Manager'],
    ['ufw.service', 'loaded', 'active', 'exited', 'Uncomplicated', 'firewall'],
    [
        'unattended-upgrades.service', 'loaded', 'active', 'running', 'Unattended', 'Upgrades',
        'Shutdown'
    ],
    ['upower.service', 'loaded', 'active', 'running', 'Daemon', 'for', 'power', 'management'],
    [
        'ureadahead-stop.service', 'loaded', 'inactive', 'dead', 'Stop', 'ureadahead', 'data',
        'collection'
    ],
    [
        'ureadahead.service', 'loaded', 'inactive', 'dead', 'Read', 'required', 'files', 'in',
        'advance'
    ],
    ['user@1000.service', 'loaded', 'active', 'running', 'User', 'Manager', 'for', 'UID', '1000'],
    ['uuidd.service', 'loaded', 'active', 'running', 'Daemon', 'for', 'generating', 'UUIDs'],
    [
        'virtualbox.service', 'loaded', 'active', 'exited', 'LSB:', 'VirtualBox', 'Linux', 'kernel',
        'module'
    ],
    ['whoopsie.service', 'loaded', 'active', 'running', 'crash', 'report', 'submission', 'daemon'],
    ['system-getty.slice', 'loaded', 'active', 'active', 'system-getty.slice'],
    [
        'systemd-initctl.socket', 'loaded', 'active', 'listening', '/dev/initctl', 'Compatibility',
        'Named', 'Pipe'
    ],
    ['systemd-journald.socket', 'loaded', 'active', 'running', 'Journal', 'Socket'],
    [
        'systemd-rfkill.socket', 'loaded', 'active', 'listening', 'Load/Save', 'RF', 'Kill',
        'Switch', 'Status', '/dev/rfkill', 'Watch'
    ],
    ['dev-mapper-cryptswap1.swap', 'loaded', 'inactive', 'dead', '/dev/mapper/cryptswap1'],
    ['swapfile.swap', 'loaded', 'failed', 'failed', '/swapfile'],
    ['all.target', 'not-found', 'inactive', 'dead', 'all.target'],
    ['anacron.timer', 'loaded', 'active', 'waiting', 'Trigger', 'anacron', 'every', 'hour'],
    [
        'apt-daily-upgrade.timer', 'loaded', 'active', 'waiting', 'Daily', 'apt', 'upgrade', 'and',
        'clean', 'activities'
    ],
    ['motd-news.timer', 'loaded', 'active', 'elapsed', 'Message', 'of', 'the', 'Day'],
    [
        'phpsessionclean.timer', 'loaded', 'active', 'waiting', 'Clean', 'PHP', 'session', 'files',
        'every', '30', 'mins'
    ],
    ['snapd.refresh.timer', 'not-found', 'inactive', 'dead', 'snapd.refresh.timer'],
    [
        'snapd.snap-repair.timer', 'loaded', 'inactive', 'dead', 'Timer', 'to', 'automatically',
        'fetch', 'and', 'run', 'repair', 'assertions'
    ],
    [
        'systemd-tmpfiles-clean.timer', 'loaded', 'active', 'waiting', 'Daily', 'Cleanup', 'of',
        'Temporary', 'Directories'
    ],
    [
        'ureadahead-stop.timer', 'loaded', 'active', 'elapsed', 'Stop', 'ureadahead', 'data',
        'collection', '45s', 'after', 'completed', 'startup'
    ],
]

discovery = {'services': [], 'services_summary': [('Summary', {})]}

checks = {
    'services': [
        (
            'virtualbox',
            {
                'states': {
                    'active': 0,
                    'failed': 2,
                    'inactive': 0
                },
                'states_default': 2,
                'else': 2
            },
            [
                (0, "Status: active", []),
                (0, "LSB: VirtualBox Linux kernel module", []),
            ],
        ),
        (
            'jamesthebutler',
            {
                'states': {
                    'active': 0,
                    'failed': 2,
                    'inactive': 0
                },
                'states_default': 2,
                'else': 2
            },
            [
                (2, "Service not found", []),
            ],
        ),
    ],
    'services_summary': [(
        'Summary',
        {
            'states': {
                'active': 0,
                'failed': 2,
                'inactive': 0
            },
            'states_default': 2,
            'else': 2
        },
        [
            (0, '32 services in total', []),
            (2, '1 service failed (systemd-cryptsetup@cryptswap1)', []),
        ],
    ),]
}
