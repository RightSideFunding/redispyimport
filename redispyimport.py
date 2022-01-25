from redis import Redis
from dill import dumps, loads

r = Redis(host='localhost',port=6379)

def loadpyfunctoredis(pyfunc:str = None):
    """Load python function into redis for quick usage later"""

    funcname = pyfunc.__name__
    r.set(funcname,dumps(pyfunc))

    print(f"{funcname} added to redis")

def runfuncfromredis(functorun:str = None):
    """Return python function from redis"""

    func = loads(r.get(functorun))
    print(f"Loaded {func.__name__} function")

    return func

if __name__ == "__main__":
    loadpyfunctoredis()
