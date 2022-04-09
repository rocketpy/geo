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
