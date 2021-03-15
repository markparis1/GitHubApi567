import unittest
from githubAPI import repositories
from unittest.mock import MagicMock as Mock

class TestRepositories(unittest.TestCase):

    
    def test_repositories(self):
        
        m = Mock()
        m.repos.return_value = {"GitHubApi567": 16, "HelloWorld": 1, "PokerCalculator": 1, "Student-Repository": 3, "Triangles": 2, "TriangleTests": 8}
        self.assertEqual(len(m.repos()), 6)
        self.assertTrue(m.repos()["Student-Repository"] == 3)
        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
