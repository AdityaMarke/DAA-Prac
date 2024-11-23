# Define a Job class to store job details
class Job:
    def __init__(self, job_id, profit, deadline):
        self.job_id = job_id
        self.profit = profit
        self.deadline = deadline

def job_scheduling(jobs, max_slots):
    jobs.sort(key=lambda job: job.profit, reverse=True)

    slots = [False] * max_slots 
    scheduled_jobs = [None] * max_slots

    for job in jobs:
        for slot in range(min(max_slots, job.deadline) - 1, -1, -1):
            if not slots[slot]: 
                slots[slot] = True 
                scheduled_jobs[slot] = job.job_id 
                break

    return [job for job in scheduled_jobs if job is not None]

def take_input():
    num_jobs = int(input("Enter the total number of jobs: "))
    jobs = []
    for i in range(num_jobs):
        print(f"\nEnter details for Job {i + 1}:")
        job_id = input("Job ID: ")
        profit = int(input("Profit (integer): "))
        deadline = int(input("Deadline (integer): "))
        jobs.append(Job(job_id, profit, deadline))
    return jobs, max(job.deadline for job in jobs)

if __name__ == "__main__":

    jobs, max_slots = take_input()

    scheduled_jobs = job_scheduling(jobs, max_slots)

    print("\nJobs scheduled for maximum profit:", scheduled_jobs)
