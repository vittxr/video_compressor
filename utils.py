import sys
import traceback

def getDetailedLog(e): 
    exception_type, exception_object, exception_traceback = sys.exc_info()
    tb = traceback.extract_tb(exception_traceback)
    print("Exception type: ", exception_type.__name__)
    print("Error: ", e)
    for frame in tb:
        print(f'File: {frame.filename}({frame.lineno}):\n  {frame.line}')