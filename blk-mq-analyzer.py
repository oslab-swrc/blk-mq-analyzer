import os


nvme_list = sorted(list(filter(lambda x: x.startswith("nvme"), os.listdir("/sys/block"))), key=lambda nvme: float(nvme.split("nvme")[1].split("n")[0]))

nvme_count = len(nvme_list)

for i, nvme in enumerate(nvme_list):
    print(f"{i + 1}: {nvme}")

nvme_num = -1
while nvme_num == -1:
    nvme_num = int(input("Select Number: ")) - 1
    if nvme_num < 0 or nvme_num >= nvme_count:
        nvme_num = -1

nvme_mq_directory = f"/sys/block/{nvme_list[nvme_num]}/mq"

queue_list = sorted(list(map(int, os.listdir(nvme_mq_directory))))

blktrace_file_name = "blktrace.data"
f = open(blktrace_file_name)
blktrace_data = f.read().split("CPU")[1:]
f.close()

dispatched_dict = {}
completed_dict = {}

for i in range(len(blktrace_data)):
    blktrace_data[i] = blktrace_data[i].split("\n")
    cpu_num = int(blktrace_data[i][0].split(" ")[0])
    reads_dispatched = int(blktrace_data[i][2].split("Dispatches:")[1].split(",")[0].lstrip())
    reads_completed = int(blktrace_data[i][4].split("Completed:")[1].split(",")[0].lstrip())
    dispatched_dict[cpu_num] = reads_dispatched
    completed_dict[cpu_num] = reads_completed

result_dict = {}
for queue_number in queue_list:
    cpu_list_path = os.path.join(nvme_mq_directory, str(queue_number), "cpu_list")
    f = open(cpu_list_path)
    cpu_list = list(map(int, f.read().strip().split(",")))
    f.close()
    dispatched_temp = 0
    completed_temp = 0
    for cpu in cpu_list:
        try:
            dispatched_temp += dispatched_dict[cpu]
        except KeyError:
            dispatched_temp = 0
        try:
            completed_temp += completed_dict[cpu]
        except KeyError:
            dispatched_temp = 0

    result_dict[queue_number] = [dispatched_temp, completed_temp]

print("queue_number", "dispatched", "completed")
for key in result_dict.keys():
    print(key, result_dict[key][0], result_dict[key][1])
