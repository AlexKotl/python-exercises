class OopsException(Exception):
    pass

try:
    raise OopsException()
except:
    print("Oops fired")
