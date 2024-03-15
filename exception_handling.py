# interprreter calls threading.excepthook() with one argument i.e. named tuple with 4 arguments
# 1. exception class
# 2. exception intance/value
# 3. a traceback object
# 4. Thread name

# for main thread -> sys.excepthook
# for created thread -> threading.excepthook -> sys.excepthook
