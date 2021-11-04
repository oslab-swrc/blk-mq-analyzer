# blk-mq-analyzer

This project's aim is evaluate balance between software queue and hardware queue.

This python code parses sysfs & blktrace output to count dispatched and completed I/Os to check balance of queue mapping.



## Information

This program uses output of blktrace/blkparse. This output shows I/O dispatch count and I/O complete count per CPU core. 

Program get queue mapping information automatically. Queue mapping information indicates which core is mapped to which hardware queue.

This program merges I/O counts based on queue mapping information. And it shows total I/O count per hardware queue.


## License

MIT License


## Usage

```bash
blktrace /dev/nvme0n1 -o - | blkparse -o blktrace.data -f "%M %m %d %a %S %9n %5T.%9t\n" -i –
```

- Get blktrace data with this command. (Root privileges required)

- Move blktrace.data to same directory with python source code.

```bash
python3 blk-mq-analyzer.py
```

- Run python source code.



## Result

<img width="227" alt="Blk_mq_analyzer_result" src="https://user-images.githubusercontent.com/13490996/138078106-5a9816ca-8130-4e54-b486-d880b5b9b66f.png">

- It shows queue number, count of dispatched I/O, count of completed I/O



<img width="536" alt="Blk_mq_analyzer_result_graph" src="https://user-images.githubusercontent.com/13490996/138078430-413821d6-b2fe-4170-af3f-a925b9430104.png">

- Graph of the above result

<img width="557" alt="Blk_mq_analyzer_result_graph_960pro" src="https://user-images.githubusercontent.com/13490996/138078126-456466a5-86fc-4e47-ad19-1a4ea578f3bc.png">

- Another result of the blk-mq-analyzer.

