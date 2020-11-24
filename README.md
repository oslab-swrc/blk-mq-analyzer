# blk-mq-analyzer

This project's aim is evaluate balance between software queue and hardware queue.

Python code parses sysfs & blktrace output to count dispatched and completed I/Os to check balance of queue mapping.



## Usage

```bash
sudo blktrace /dev/nvme0n1 -o - | blkparse -o blktrace.data -f "%M %m %d %a %S %9n %5T.%9t\n" -i –
```

- Get blktrace data with this command.

- Move blktrace.data to same directory with python source code.

```bash
python3 blk-mq-analyzer.py
```

- Run python source code.