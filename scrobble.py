import optparse
import requests
import sys

file_types = [".txt", ".bak", ".old", ".zip", ".rar", ".tar.gz", ".tar.xz", ".conf", ".inc", ".swp", "~", ".tar.bz2"]

parser = optparse.OptionParser()
parser.add_option("-u", dest="url", help="The file to start with, like http://example.com/config.php", default=None)
parser.add_option("-k", dest="no_verify", help="Disable SSL verification", default=False, action="store_true")

options, args = parser.parse_args()

if not options.url:
    print("Argument -u required, "
          "please enter the file to start with, like http://example.com/config.php")
    sys.exit(1)

url = options.url
# remove url parameters (just to make it more noob friendly)
url = url.split('?')[0]
parts = url.split('.')
original = parts[len(parts) -1]
if "/" in original:
    print("The URL should contain the original extension, "
          "if none is supplied things will probably crash. "
          "You can work around this problem by supplying a random extension :)")
filepath = '.'.join(parts[:len(parts) -1])
print("scanning for backup files of: %s (original extension: %s)" % (filepath, original))
for extension in file_types:
    ext_replace = "%s%s" % (filepath, extension)
    result_original = requests.get(url=ext_replace, verify=not options.no_verify, allow_redirects=False)
    if result_original and result_original.status_code == 200:
        print("%s [200]" % ext_replace)
    ext_append = "%s.%s%s" % (filepath, original, extension)
    result_append = requests.get(url=ext_append, verify=not options.no_verify, allow_redirects=False)
    if result_append and result_append.status_code == 200:
        print("%s [200]" % ext_append)

print("Scanning has finished")

