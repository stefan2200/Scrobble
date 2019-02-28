# Scrobble
Find hidden backup files

Usage:

pip install requests

scrobble.py -u "some url"

You can supply the -k argument to disable SSL verification

Scans for:
`{original_extension}.txt
{original_extension}.bak
{original_extension}.old
{original_extension}.zip
{original_extension}.rar
{original_extension}.tar.gz
{original_extension}.tar.xz
{original_extension}.conf
{original_extension}.inc
{original_extension}.swp
{original_extension}~
{original_extension}.tar.bz2`

And
`{name}.txt
{name}.bak
{name}.old
{name}.zip
{name}.rar
{name}.tar.gz
{name}.tar.xz
{name}.conf
{name}.inc
{name}.swp
{name}~
{name}.tar.bz2`

Where name is the original URL without the extension