import asyncio, random
import time

jobs = {}

#create ID, generate random completion time + success_rate
def create_jobs (job_count)-> dict:
    job_id = 1
    
    #Don't want random id's because of collision risk+tracability, I think also serialization?
    while job_id <= job_count:

        completion_time = random.randint(1,12)
        success_rate = random.random()
        jobs[f'job id- {job_id}'] = (completion_time, success_rate)
        yield jobs
        job_id += 1

#take jobs dict unpack and run job. return pass/fail
async def worker(single_job: dict)-> dict:
    tasks = {}
    for k, v in single_job.items():
        job_id = k
        completetion_time, success_rate = v
    await asyncio.sleep(completetion_time)
    failure_rate = random.random()
    if failure_rate > success_rate:
        print (f'Job: {job_id} failed')
        tasks[job_id]= False
        return tasks
    print (f'Job:{job_id} complete')
    tasks[job_id]= True
    return tasks

#Assign worker() coroutine tasks form queue. update assigned, clear queue. 
async def scheduler (jobs: dict):
    queue =[]
    assigned = []

    queue = [{k: v} for k, v in jobs.items()]
    coroutine = ( worker(x) for x in queue)
    active_tasks =[]
    for x in coroutine:
        active_tasks.append (asyncio.create_task (x))

    assigned = queue
    queue = []

    return active_tasks



async def collect_work (workers) -> None:
    for coro in asyncio.as_completed(workers):
        result = await coro
        print(result)
    
    
    
# run the functions collect the workers
async def main ():
    start = time.perf_counter ()
    for x in create_jobs (20):
        created_work = jobs

    active_tasks= await scheduler (created_work)
    await collect_work (active_tasks)

    end = time.perf_counter ()
    print (f'System runtime: {end-start}')
if __name__ == '__main__':
    asyncio.run (main())