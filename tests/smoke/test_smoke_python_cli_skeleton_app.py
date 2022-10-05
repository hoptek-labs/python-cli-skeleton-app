import os
import sys

from subprocess import run, PIPE, STDOUT
from unittest import TestCase


class TestSmokePythonCliSkeletonApp(TestCase):

    def test_application_returns_expected_code_and_output_on_error(self):
        python_env = os.environ.copy()
        del python_env["APP_ENV"]
        process = run(
            [sys.executable, "-m", "python_cli_skeleton_app"],
            stdout=PIPE,
            stderr=STDOUT,
            encoding="utf-8",
            env=python_env
        )

        self.assertEqual(
            process.returncode,
            1
        )

        self.assertRegex(
            process.stdout,
            "Missing environment variable APP_ENV"
        )

    def test_application_returns_expected_code_and_output_on_success(self):
        process = run(
            [sys.executable, "-m", "python_cli_skeleton_app"],
            stdout=PIPE,
            stderr=STDOUT,
            encoding="utf-8"
        )

        self.assertEqual(
            process.returncode,
            0
        )

        self.assertRegex(
            process.stdout,
            "returned status code 200"
        )
