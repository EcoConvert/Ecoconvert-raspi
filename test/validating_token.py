import os
import time
import unittest
from unittest.result import TestResult
from unittest.runner import TextTestRunner
from unittest.suite import TestSuite

import jwt
from dotenv import load_dotenv


class CustomTestResult(TestResult):
    def __init__(self):
        super().__init__()
        self.test_details = []
        self.successes = []  # Add this to track successful tests

    def addSuccess(self, test):
        super().addSuccess(test)
        self.successes.append(test)  # Track successful tests
        self.test_details.append({"test_name": test.shortDescription() or str(test), "status": "PASS", "details": None})

    def addError(self, test, err):
        super().addError(test, err)
        self.test_details.append(
            {"test_name": test.shortDescription() or str(test), "status": "ERROR", "details": str(err[1])}
        )

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.test_details.append(
            {"test_name": test.shortDescription() or str(test), "status": "FAIL", "details": str(err[1])}
        )


class JWTSecurityTests(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.secret_key = os.getenv("SECRET_KEY")
        self.another_secret = "different_secret_key"
        self.valid_payload = {"points": 50}
        self.valid_token = jwt.encode(self.valid_payload, self.secret_key, algorithm="HS256")

    def test_invalid_signature(self):
        """Test token signed with different secret key"""
        token_different_secret = jwt.encode(self.valid_payload, self.another_secret, algorithm="HS256")
        with self.assertRaises(jwt.InvalidSignatureError):
            jwt.decode(token_different_secret, self.secret_key, algorithms=["HS256"])

    def test_invalid_token(self):
        """Test completely invalid token format"""
        invalid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.invalid.token"
        with self.assertRaises(jwt.InvalidTokenError):
            jwt.decode(invalid_token, self.secret_key, algorithms=["HS256"])

    def test_tampered_payload(self):
        """Test token with tampered payload"""
        header, payload, signature = self.valid_token.split(".")
        tampered_payload = payload + "tampered"
        tampered_token = f"{header}.{tampered_payload}.{signature}"
        with self.assertRaises(jwt.InvalidTokenError):
            jwt.decode(tampered_token, self.secret_key, algorithms=["HS256"])

    def test_manual_payload_different_signature(self):
        """Test manually constructed token with mismatched signature"""
        token1 = jwt.encode(self.valid_payload, self.secret_key, algorithm="HS256")
        token2 = jwt.encode(self.valid_payload, self.another_secret, algorithm="HS256")
        parts1 = token1.split(".")
        parts2 = token2.split(".")
        mixed_token = f"{parts1[0]}.{parts1[1]}.{parts2[2]}"
        with self.assertRaises(jwt.InvalidSignatureError):
            jwt.decode(mixed_token, self.secret_key, algorithms=["HS256"])

    def test_successful_decode(self):
        """Verify that valid token still works"""
        decoded = jwt.decode(self.valid_token, self.secret_key, algorithms=["HS256"])
        self.assertEqual(decoded, self.valid_payload)


def run_tests_with_details():
    # Create test suite
    suite = TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(JWTSecurityTests))

    # Run tests with custom result
    result = CustomTestResult()
    runner = TextTestRunner(verbosity=2)
    suite.run(result)

    # Print detailed results
    print("\n=== Detailed Test Results ===")
    print(f"Total Tests Run: {result.testsRun}")
    print(f"Successful Tests: {len(result.successes)}")  # Now this will work
    print(f"Failed Tests: {len(result.failures)}")
    print(f"Tests with Errors: {len(result.errors)}")

    print("\nTest Details:")
    for test_detail in result.test_details:
        status_icon = "✅" if test_detail["status"] == "PASS" else "❌"
        print(f"\n{status_icon} Test: {test_detail['test_name']}")
        print(f"Status: {test_detail['status']}")
        if test_detail["details"]:
            print(f"Details: {test_detail['details']}")

    # Return True if all tests passed
    return len(result.failures) == 0 and len(result.errors) == 0


if __name__ == "__main__":
    all_tests_passed = run_tests_with_details()
    print(f"\nOverall Test Status: {'✅ ALL TESTS PASSED' if all_tests_passed else '❌ SOME TESTS FAILED'}")
