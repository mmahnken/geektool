import subprocess
import re


def get_cpu(source):
    """ Input is either the string user, sys, or idle, and outputs
    the current CPU being used by that source"""

    p1 = subprocess.check_output(["top", "-l1"])
    start_index = p1.find('CPU')
    pattern = re.compile(r'((\d)?\d[.]\d(\d)?)% ' + source)
    match = pattern.findall(p1[start_index:start_index+200])  # returns a list of tuples
    try:
        num = float(match[0][0])
    except:
        num = None
    return num


def get_disc_space():
    """Returns the current percentage of disc space used as integer"""
    p1 = subprocess.check_output(["df", "-Hl"])
    pattern = re.compile(r'((\d)?(\d)?\d)%')
    match = pattern.findall(p1)
    try:
        num = int(match[0][0])
    except:
        num = None
    return num


def convert_to_arc(num):
    """ Takes in any int or float, and converts int
    to number-representing letters for display using
    ARCfont."""
    conversion_dict = make_convertor()
    if type(num) is float:
        num = int(round(num))
    if num % 2 != 0:
        num = num + 1
    return conversion_dict.get(num)


def make_convertor():
    lib = 'abcedfghijklmnopqrstuvwxyz'
    lib = lib + lib.upper()
    lib = [letter for letter in lib]
    count = 0
    d = {}
    for letter in lib:
        d[count] = letter
        count = count + 2
    return d
