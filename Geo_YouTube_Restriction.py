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
