from htmd.projections.projection import Projection

import logging
import numpy as np

logger = logging.getLogger(__name__)


class MetricNull(Projection):
    """ A dummy metric returning zero for all frames. May be useful as a template for developers,
    or to get the simulation list without doing any processing.

    Parameters
    ----------
    ndim : int
        number of dimensions of the fake projection space

    """

    def __init__(self, ndim):
        logger.info("Initialized")
        self._ndim = ndim

    # Only called if single topology
    def _precalculate(self, mol):
        logger.info("In _precalculate")
        self._precalculation_enabled = True

    def getMapping(self):
        """ Returns optional information.

        Returns
        -------
        map :
            a dummy value
        """

        return ["Dummy" + str(i + 1) for i in range(self._ndim)]

    def project(self, mol):
        """ Compute the actual metric.

        Parameters
        ------------
        mol : :class:`Molecule <htmd.molecule.molecule.Molecule>`
            A :class:`Molecule <htmd.molecule.molecule.Molecule>` object to project.

        Returns
        -------
        data : np.ndarray
            An array containing the null data.
        """

        trajlen = mol.numFrames
        data = np.zeros((trajlen, self._ndim), dtype=np.float32)

        return data


if __name__ == "__main__":
    import htmd
    import htmd.projections.metricnull

    dd = htmd.home(dataDir="adaptive")
    fsims = htmd.simlist([dd + '/data/e1s1_1/', dd + '/data/e1s2_1/'],
                         dd + '/generators/1/structure.pdb')

    metr2 = htmd.Metric(fsims)
    metr2.projection(htmd.projections.metricnull.MetricNull(2))
    data2 = metr2.project()
    assert data2.dat[0].shape == (6, 2)

    metr1 = htmd.Metric(fsims)
    metr1.projection(htmd.projections.metricnull.MetricNull(1))
    data1 = metr1.project()
    assert data1.dat[0].shape == (6, 1)

    pass
