#  youtube-dl - download videos from youtube.com or other video platforms

# pip install --upgrade youtube-dl

"""
youtube-dl is a command-line program to download videos from YouTube.com and a few more sites.
It requires the Python interpreter, version 2.6, 2.7, or 3.2+, and it is not platform specific.
It should work on your Unix box, on Windows or on macOS. It is released to the public domain,
which means you can modify it, redistribute it or use it however you like.

youtube-dl [OPTIONS] URL [URL...]

"""

#  Geo Restriction:

"""
--geo-verification-proxy URL         Use this proxy to verify the IP address
                                     for some geo-restricted sites. The
                                     default proxy specified by --proxy (or
                                     none, if the option is not present) is
                                     used for the actual downloading.
--geo-bypass                         Bypass geographic restriction via
                                     faking X-Forwarded-For HTTP header
--no-geo-bypass                      Do not bypass geographic restriction
                                     via faking X-Forwarded-For HTTP header
--geo-bypass-country CODE            Force bypass geographic restriction
                                     with explicitly provided two-letter ISO
                                     3166-2 country code
--geo-bypass-ip-block IP_BLOCK       Force bypass geographic restriction
                                     with explicitly provided IP block in
                                     CIDR notation
"""


# OPTIONS

"""
-h, --help                           Print this help text and exit
--version                            Print program version and exit
-U, --update                         Update this program to latest version.
                                     Make sure that you have sufficient
                                     permissions (run with sudo if needed)
-i, --ignore-errors                  Continue on download errors, for
                                     example to skip unavailable videos in a
                                     playlist
--abort-on-error                     Abort downloading of further videos (in
                                     the playlist or the command line) if an
                                     error occurs
--dump-user-agent                    Display the current browser
                                     identification
--list-extractors                    List all supported extractors
--extractor-descriptions             Output descriptions of all supported
                                     extractors
--force-generic-extractor            Force extraction to use the generic
                                     extractor
--default-search PREFIX              Use this prefix for unqualified URLs.
                                     For example "gvsearch2:" downloads two
                                     videos from google videos for youtube-
                                     dl "large apple". Use the value "auto"
                                     to let youtube-dl guess ("auto_warning"
                                     to emit a warning when guessing).
                                     "error" just throws an error. The
                                     default value "fixup_error" repairs
                                     broken URLs, but emits an error if this
                                     is not possible instead of searching.
--ignore-config                      Do not read configuration files. When
                                     given in the global configuration file
                                     /etc/youtube-dl.conf: Do not read the
                                     user configuration in
                                     ~/.config/youtube-dl/config
                                     (%APPDATA%/youtube-dl/config.txt on
                                     Windows)
--config-location PATH               Location of the configuration file;
                                     either the path to the config or its
                                     containing directory.
--flat-playlist                      Do not extract the videos of a
                                     playlist, only list them.
--mark-watched                       Mark videos watched (YouTube only)
--no-mark-watched                    Do not mark videos watched (YouTube
                                     only)
--no-color                           Do not emit color codes in output
"""


# Network Options:

"""
--proxy URL                          Use the specified HTTP/HTTPS/SOCKS
                                     proxy. To enable SOCKS proxy, specify a
                                     proper scheme. For example
                                     socks5://127.0.0.1:1080/. Pass in an
                                     empty string (--proxy "") for direct
                                     connection
--socket-timeout SECONDS             Time to wait before giving up, in
                                     seconds
--source-address IP                  Client-side IP address to bind to
-4, --force-ipv4                     Make all connections via IPv4
-6, --force-ipv6                     Make all connections via IPv6
"""



