"""
    flask.ext.fixtures.helpers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Helper functions.

    :copyright: (c) 2015 Christopher Roach <ask.croach@gmail.com>.
    :license: MIT, see LICENSE for more details.
"""

from __future__ import print_function

import sys


def print_msg(msg, header):
    """Prints a boardered message to the screen"""
    DEFAULT_MSG_BLOCK_WIDTH = 60

    # Calculate the length of the boarder on each side of the header and the
    # total length of the bottom boarder
    side_boarder_length = (DEFAULT_MSG_BLOCK_WIDTH - (len(header) + 2)) / 2
    msg_block_width = side_boarder_length * 2 + (len(header) + 2)

    # Create the top and bottom boarders
    side_boarder = '#' * side_boarder_length
    top_boarder = '{0} {1} {2}'.format(side_boarder, header, side_boarder)
    bottom_boarder = '#' * msg_block_width

    def pad(line, length):
        """Returns a string padded and centered by the given length"""
        padding_length = length - len(line)
        left_padding = ' ' * (padding_length/2)
        right_padding = ' ' * (padding_length - len(left_padding))
        return '{0} {1} {2}'.format(left_padding, line, right_padding)

    words = msg.split(' ')
    lines = []
    line = ''
    for word in words:
        if len(line + ' ' + word) <= msg_block_width - 4:
            line = (line + ' ' + word).strip()
        else:
            lines.append('#{}#'.format(pad(line, msg_block_width - 4)))
            line = word
    lines.append('#{}#'.format(pad(line, msg_block_width - 4)))

    # Print the full message
    print(file=sys.stderr)
    print(top_boarder, file=sys.stderr)
    print('#{}#'.format(pad('', msg_block_width - 4)), file=sys.stderr)
    for line in lines:
        print(line, file=sys.stderr)
    print('#{}#'.format(pad('', msg_block_width - 4)), file=sys.stderr)
    print(bottom_boarder, file=sys.stderr)
    print(file=sys.stderr)

def print_info(msg):
    print_msg(msg, 'INFORMATION')