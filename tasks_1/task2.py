def int32_to_ip(int32):
    return f"{int32 // (256 * 256 * 256) % 256}.{int32 // (256 * 256) % 256}." \
           f"{int32 // 256 % 256}.{int32 % 256}"


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
