import unittest
from unittest import TestCase


class TestReadMe(TestCase):
    """
    Cause, why not?  We want to make sure the README is always in a valid format
    to be rendered.
    """

    def test_readme_valid(self):
        import rstcheck

        with open('README.rst') as f:
            rst = f.read()
            errors = list(rstcheck.check(rst))

            self.assertTrue(len(errors) == 0)


if __name__ == '__main__':
    unittest.main()
