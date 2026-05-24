import asyncio, random

jobs = {}

#create ID, generate random completion time + success_rate
def create_jobs ()-> dict:
    job_id = 1
    #Don't want random id's because of collision risk+tracability, I think also serialization?
    while True:
        completion_time = random.randint(1,12)
        success_rate = random.random()
        jobs[f'job id: {job_id}'] = (completion_time, success_rate)
        yield jobs
        job_id =+ 1

''' Alright, I'm thinking about nesting a while loop in a while loop.
The inner loop checks for jobs every n seconds the outer loop runs until
the scheduler says all jobs are complete or have timed-out. I'll have
to await so it doesn't block the event loop.

'''

#periodically checks for tasks then assigns them out
#once all jobs are complete or have timed out return something to end the loop
async def task_queue ()-> str:
    queue = list(jobs)
    assigned = []
    completed = []








'''maybe I can model job success by generating a random float and if
chance is >= success_rate the job fails. (raise some error)
'''    
async def worker(jobs: dict):
    completion_time, success_rate, job_id = [*jobs][0]

    await asyncio.sleep(completion_time)
    failure_rate = random.random()
    if failure_rate > success_rate:
        print f'Job: {job_id} failed'
        return tasks[job_id]= False
    print f'Job:{job_id} complete'
    return tasks[job_id]= True

'''while jobs are available spawn workers, what happens if
two workers are working the same job?I think I'll try a queue of jobs
I'm not really sure how to solve this because I can't guarentee to 
workers don't start the same job, but then again does the program crash
if you try to pop a element that is already gone? I wonder can I
try/except the worker and on no element to pop do nothing?'''
async def main (): #I'll have to figure out how many jobs to spawn
    
    while jobs:
        pass
    
    await asycnio.gather (some_gen_workers_function)


    active_workers =+ 1
