"""install_cmdstan test"""

import unittest

from cmdstanpy.install_cmdstan import (
    is_version_available,
    latest_version,
    retrieve_version,
    CmdStanRetrieveError,
)


class InstallCmdStanTest(unittest.TestCase):
    def test_is_version_available(self):
        # check http error for bad version
        self.assertTrue(is_version_available('2.24.1'))
        self.assertFalse(is_version_available('2.222.222-rc222'))

    def test_latest_version(self):
        # examples of known previous version:  2.24-rc1, 2.23.0
        version = latest_version()
        nums = version.split('.')
        self.assertTrue(len(nums) >= 2)
        self.assertTrue(nums[0][0].isdigit())
        self.assertTrue(nums[1][0].isdigit())

    def test_retrieve_version(self):
        # check http error for bad version
        with self.assertRaisesRegex(
            CmdStanRetrieveError, 'not available from github.com'
        ):
            retrieve_version('no_such_version')


if __name__ == '__main__':
    unittest.main()
