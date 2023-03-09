import unittest
import test_callings


testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(test_callings)

runner = unittest.TextTestRunner(verbosity=3)
runner.run(suites)
