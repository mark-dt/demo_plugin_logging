from ruxit.api.base_plugin import BasePlugin
from ruxit.api.data import MEAttribute
from ruxit.api.snapshot import pgi_name


import simple_logger

class DemoPlugin(BasePlugin):
    def initialize(self, **kwargs):

        log_level = self.config['debug_level']
        self.logger = simple_logger.restore_logger(__file__, log_level)
        self.logger.debug('INIT DONE')

    def stuff(self):
        sum = 1234 + 5678
        self.logger.debug(f'Res {sum}')

    def query(self, **kwargs):
        self.logger.debug('DEBUG LOG')
        self.logger.info('INFO LOG')
        self.logger.warning('WARNING LOG')
        self.logger.error('ERROR LOG')
        self.stuff()