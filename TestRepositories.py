import unittest
from githubAPI import repositories
from unittest.mock import MagicMock as Mock

class TestRepositories(unittest.TestCase):

    
    def test_repositories(self):

        repos = repositories("markparis1")
        self.assertEqual(len(repos), 6)
        self.assertTrue(repos["Student-Repository"] == 3)
        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
