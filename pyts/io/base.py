"""
A base module for the io package.
"""

# This defines the 'endianness' for reading/writing binary files in PyTurbSim.
e = '<'


def convname(fname, sfx=''):
    """
    Change the suffix from '.inp', if necessary.
    """
    if sfx in ['.inp', 'inp']:
        return fname.rsplit('.', 1)[0] + '.inp'
    if fname.endswith('inp'):
        if not sfx.startswith('.'):
            sfx = '.' + sfx
        return fname.rsplit('.', 1)[0] + sfx
    return fname
