#!/usr/bin/python

import sys

FILE = sys.argv[1]

FIND_1 = "      'Release_Base': {"
FIND_2 = "        'xcode_settings': {"
FIND_3 = "          'OTHER_CFLAGS': [ '<@(release_extra_cflags)', ],"
FIND_REPLACE = "          'OTHER_CFLAGS': [ '<@(release_extra_cflags)', '-fembed-bitcode', ],"
REPLACE = "          'OTHER_CFLAGS': [ '<@(release_extra_cflags)', '-fembed-bitcode', ],\n"


def findSubstringInLines(lines, find):
    for i, line in enumerate(lines):
        if find in line:
            return i
    return -1

with open(FILE, 'r+') as content:
    lines = content.readlines()
    index = findSubstringInLines(lines, FIND_1)

if index < 0:
    exit(-1)

index2 = findSubstringInLines(lines[index:], FIND_2)

if index2 < 0:
    exit(-1)

index_replace = findSubstringInLines(lines[(index+index2+1):], FIND_REPLACE)

if index_replace > 0:
    exit(-1)

index3 = findSubstringInLines(lines[(index+index2+1):], FIND_3)

if index3 < 0:
    exit(-1)

lines[(index+index2+index3+1)] = REPLACE

with open(FILE, 'r+') as content:
    content.write("".join(lines))
    content.truncate()
