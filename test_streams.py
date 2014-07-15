import unittest
import subprocess


class CheckStream(unittest.TestCase):

    def testStdOut(self):
        res = subprocess.check_output(["python", "write_to_stderr.py"])
        self.assertEqual(res, "Stdout\n")

    def testStdOutErr(self):
        res = subprocess.check_output(["python", "write_to_stderr.py"], stderr=subprocess.STDOUT)
        self.assertEqual(res, "Stdout\nStderr\n")

    def testStdErr(self):
        p = subprocess.Popen(["python", "-u", "echo.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        (stdout, stderr) = p.communicate(input='Loginput')
        self.assertEqual(stdout, "!! Loginput\n")


def main():
    unittest.main()

if __name__ == '__main__':
    main()