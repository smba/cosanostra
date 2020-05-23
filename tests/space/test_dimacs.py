import unittest
import space.util as util
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
VM_DIR = "{}/variability_models".format(THIS_DIR)

class DimacsTest(unittest.TestCase):

    def setUp(self):
        '''
        This method loads test resources and checks if they exist.

        :return:
        '''

        self.paths = {
            "vp9": "{}/vp9.dimacs".format(VM_DIR),
            #"sqlite": "{}/sqlite.dimacs".format(VM_DIR)
        }

    def test_dimacs_exist(self):
        # Assert that test resources exist
        for key in self.paths:
            path = self.paths[key]
            self.assertTrue(os.path.exists(path), "Cannot find test resource {}".format(path))

    def test_dimacs_parse(self):
        for key in self.paths:
            path = self.paths[key]
            x = util.parse_dimacs(path)
            # TODO assertions of parsing results

    def test_dimacs_to_bit_model(self):
        for key in self.paths:
            path = self.paths[key]
            dimacs, features = util.parse_dimacs(path)
            y = util.dimacs_to_bit_model(dimacs, len(features))
            # TODO assertions of constraints

    def test_dimacs_to_bool_model(self):
        for key in self.paths:
            path = self.paths[key]
            dimacs, features = util.parse_dimacs(path)
            y = util.dimacs_to_bool_model(dimacs, features)
            # TODO assertions of constraints

            print(y[1])

if __name__ == '__main__':
    unittest.main()

