
import unittest

class TestPipeline(unittest.TestCase):
    def test_pipeline_message(self):
        message = "Jenkins CI Pipeline Started"
        self.assertIn("Jenkins", message)
        self.assertIn("CI", message)

    def test_exercise_number(self):
        exercise = 7
        self.assertEqual(exercise, 7)

if __name__ == "__main__":
    unittest.main()
