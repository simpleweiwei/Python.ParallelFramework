import math, sys, time
import pp

# only in python 2.7

def is_prime(n):
    """Returns True if n is prime and False otherwise"""
    if not isinstance(n, int):
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True


def sum_primes(n):
    """Calculates sum of all primes below given integer n"""
    return sum([x for x in xrange(2, n) if is_prime(x)])

# tuple of all parallel python servers to connect with
ppservers = ()
#  ppservers = ("10.0.0.1",)

if len(sys.argv) > 1:
    ncpus = int(sys.argv[1])
    # Creates jobserver with ncpus workers
    job_server = pp.Server(ncpus, ppservers=ppservers)
else:
    # Creates jobserver with automatically detected number of workers
    job_server = pp.Server(ppservers=ppservers)

print "Starting pp with", job_server.get_ncpus(), "workers"

job1 = job_server.submit(sum_primes, (100,), (is_prime,), ("math",))  # start task

# Retrieves the result calculated by job1
# The value of job1() is the same as sum_primes(100)
# If the job has not been finished yet, execution will wait here until result is available
result = job1()
print "pid", str(job1.tid)
print "Sum of primes below 100 is", result

start_time = time.time()

# The following submits 8 jobs and then retrieves the results
inputs = (100000, 100100, 100200, 100300, 100400, 100500, 100600, 100700)
jobs = [(item, job_server.submit(sum_primes,(item,), (is_prime,), ("math",))) for item in inputs]
for d, job in jobs:
    print "Sum of primes below", d, "is", job()
    print "pid", str(job.tid)

print "Time elapsed: ", time.time() - start_time, "s"
job_server.print_stats()  # Statistics Function by pp itself


