def function_with_uncommon_bug(data):
    try:
        #Simulate an uncommon error: trying to iterate over a NoneType object
        if data is None:
            raise TypeError("Data cannot be None")
        for item in data:
            #Process item here
            pass
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    except Exception as e:
        print(f"Caught an unexpected exception: {e}")

#Example usage with NoneType leading to TypeError
function_with_uncommon_bug(None)