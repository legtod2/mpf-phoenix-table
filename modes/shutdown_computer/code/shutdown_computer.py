from mpf.core.mode import Mode
import os
import platform
class shutdown_computer(Mode):
    def mode_init(self):
        self.log.info('shutdown_computer mode_init')
        self.OS_type = platform.system().lower()
    def mode_start(self, **kwargs):
        self.log.info('shutdown_computer mode_start')
        self.add_mode_event_handler('shutdown_host_computer', self.shutdown_host)
    def shutdown_host(self, **kwargs):
        #shutdown the mpf game if it's running
        #shutdown the computer
        if self.OS_type == 'linux':
            shutdown_str = '/usr/sbin/shutdown -h +1 Shutdown in 60 secs'
        elif self.OS_type == 'windows':
            shutdown_str == 'shutdown -s -t 0'
        else:
            self.log.warning(f'Sorry this feature is not available in {self.os_type}')
            return
        os.system(shutdown_str)
    def mode_stop(self, **kwargs):
        self.machine.events.post('shutdown_computer mode_ended')
        self.log.info('shutdown_computer mode_stop')


