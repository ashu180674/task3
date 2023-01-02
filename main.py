import requests
import unittest

class TestAtgWorldConnection(unittest.TestCase):
    def test_atg_world_connection(self):
        print("Testing connection to atg.world website...")
        try:
            response = requests.get("https://atg.world")
            print("Connection successful!")
            print("Response status code:", response.status_code)
            self.assertEqual(response.status_code, 200)
        except:
            print("Connection failed!")
            self.fail("Connection to atg.world website failed!")

if __name__ == "__main__":
    unittest.main()
