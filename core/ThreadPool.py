from concurrent.futures import ThreadPoolExecutor

class ThreadPool:
    def __init__(self, functions):
        self.functions = functions
        self.executor = None

    def init_executor(self):
        if self.executor is not None:
            self.executor.shutdown(wait=False)
        self.executor = ThreadPoolExecutor(max_workers=len(self.functions))

    def init_pool(self):
        self.init_executor()

        for func in self.functions:
            self.executor.submit(func)