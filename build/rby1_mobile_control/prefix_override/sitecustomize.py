import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rainbow/rby1_fork_ws/install/rby1_mobile_control'
