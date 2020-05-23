import unittest
import space.binary as binary
import space.util as util
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
VM_DIR = "{}/variability_models".format(THIS_DIR)

class SpaceSamplingTest(unittest.TestCase):
    def setUp(self):
        self.paths = {
            "vp9": "{}/vp9.dimacs".format(VM_DIR),
        }

    def test_distance_based_sampling(self):
        for key in self.paths:
            path = self.paths[key]
            dimacs, features = util.parse_dimacs(path)
            binary.distance_based_sampling(dimacs, features, size=3)

