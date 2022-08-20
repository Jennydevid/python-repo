import time

seconds = time.time()

      # these functions convert the elapsed time to the struct_time object
      # the only diff b/w them is, gmtime returns the struct_time object in UTC
      # and localtime returns local time
print(time.gmtime(seconds))
print(time.localtime(seconds))