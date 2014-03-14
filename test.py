import unittest
import optparse
import sys
# export GAE="/usr/local/google_appengine:/usr/local/google_appengine/lib:/usr/local/google_appengine/lib/yaml-3.10:/usr/local/google_appengine/lib/webob-1.2.3"
# export PYTHONPATH="$PYTHONPATH:$GAE"
# export PATH="$PATH:$GAE"


USAGE = """%prog SDK_PATH TEST_PATH
Run unit tests for App Engine apps.

SDK_PATH    Path to the SDK installation,
            for example usr/local/google_appengine
TEST_PATH   Path to package containing test modules
"""

def main(sdk_path, test_path):
    sys.path.insert(0, sdk_path)
    import dev_appserver
    dev_appserver.fix_sys_path()
    suite = unittest.loader.TestLoader().discover(test_path)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    parser = optparse.OptionParser(USAGE)
    options, args = parser.parse_args()
    if len(args) != 2:
        print 'Error: Exactly 2 arguments required.'
        parser.print_help()
        sys.exit(1)
    SDK_PATH = args[0]
    TEST_PATH = args[1]
    main(SDK_PATH, TEST_PATH)