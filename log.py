import time

def timestamp(func):
    def wrapper(*argument, **keywordargument):
        current_time = time.ctime()
        print(current_time)
        func(*argument, **keywordargument)

    return wrapper
