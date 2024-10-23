5. Write a program to implement a greedy algorithm for job sequencing with deadlines.

def job_sequencing_with_deadline(jobs):
  jobs.sort(key=lambda x: x[2], reverse=True)
  max_deadline = max(jobs, key=lambda x: x[1])[1]
  slots = [-1]* (max_deadline +1)
  total_profit = 0

  for job_id, deadline, profit in jobs:
    while deadline > 0 and slots[deadline] != -1:
      deadline -= 1
    if deadline > 0:
      slots[deadline] = job_id
      total_profit += profit

  return total_profit, [job for job in slots if job != -1]

num_jobs = int(input("Enter the number of jobs: "))
jobs = I
for i in range(num_jobs):
  job_id = i+1
  deadline = int(input(f"Enter deadline for jobs{i+1}: "))
  profit = int(input(f"Enter profit for jobs{i+1}: "))
  jobs.append((job_id, deadline, profit))

profit, sequence = job_sequencing_with_deadline(jobs)

print("\nResult")
print("Sequence of jobs: ", sequence)
print("Total profit: ", profit)
