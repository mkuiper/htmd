# (c) 2015-2016 Acellera Ltd http://www.acellera.com
# All Rights Reserved
# Distributed under HTMD Software License Agreement
# No redistribution in whole or part
#
import htmd
import os
import inspect
import platform


def home(dataDir=None, libDir=False):
    """Return the pathname of the HTMD root directory (or a data subdirectory).

    Parameters
    ----------
    dataDir : str
        If not None, return the path to a specific data directory
    libDir : bool
        If True, return path to the lib directory

    Returns
    -------
    dir : str
        The directory

    Example
    -------
        >>> htmd.home()                                 # doctest: +ELLIPSIS
        '.../htmd'
        >>> htmd.home(dataDir="dhfr")                   # doctest: +ELLIPSIS
        '.../data/dhfr'
        >>> os.path.join(htmd.home(dataDir="dhfr"),"dhfr.pdb")  # doctest: +ELLIPSIS
        '.../data/dhfr/dhfr.pdb'
    """

    homeDir=os.path.dirname(inspect.getfile(htmd))
    if dataDir:
        return os.path.join(homeDir, "data", dataDir)
    elif libDir:
        libdir = os.path.join(homeDir, "lib")
        if os.path.exists(os.path.join(libdir, "basic")):
            return os.path.join(libdir, "basic", platform.system())
        elif os.path.exists(os.path.join(libdir, "pro")):
            return os.path.join(libdir, "pro", platform.system())
        else:
            raise FileNotFoundError('Could not find libs.')
    else:
        return homeDir



#Don't know how to do this
# def modulehome(modname):
#    return os.path.dirname(os.path.dirname(inspect.getfile(modname)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    h = htmd.home()
    print(h)
