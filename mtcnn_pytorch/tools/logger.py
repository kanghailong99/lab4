# Code is from https://gist.github.com/gyglim/1f8dfb1b5c82627ae3efcfbbadb9f514

import numpy as np

from tensorboardX import SummaryWriter


__all__ = ["Logger"]


class Logger:

    def __init__(self, log_dir):
        """Create a summary writer logging to log_dir."""        
        self.writer = SummaryWriter(log_dir)

    def scalar_summary(self, tag, value, step):
        """Log a scalar variable."""        
        self.writer.add_scalar(tag, value, step) 