#!/usr/bin/python

"""
Tim Fox

This script uses the s2protocol to extract metagame data and insert it
    into a mysql database. This data will index events for a game
    stored in HBase
"""

# Import base protocol and mpyq
from s2protocol.mpyq import mpyq
from s2protocol import protocol15405
import argparse
import sys

# Unarchive the file

parser = argparse.ArgumentParser()
parser.add_argument('replay_file', help='.SC2Replay file to load')
args = parser.parse_args()
archive = mpyq.MPQArchive(args.replay_file)

# Import the correct build protocol

contents = archive.header['user_data_header']['content']
header = protocol15405.decode_replay_header(contents)
baseBuild = header['m_version']['m_baseBuild']
print baseBuild

try:
    protocol = 'protocol%s' % baseBuild
    module = __import__('s2protocol',globals(),locals(),[protocol],-1)
    protocol = getattr(module, protocol)

except:
    print >> sys.stderr, 'Unsupported base build: %d' % baseBuild
    sys.exit(1)

# Extract initdata
contents = archive.read_file('replay.initData')
initdata = protocol.decode_replay_initdata(contents)
print initdata

# Extract details
contents = archive.read_file('replay.details')
details = protocol.decode_replay_details(contents)
print details
