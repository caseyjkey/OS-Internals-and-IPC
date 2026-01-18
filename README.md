# OS Internals and IPC

A deep dive into operating system fundamentals and computer networking, covering process scheduling, inter-process communication, memory management, system calls, and network protocols.

## Overview

This repository explores the inner workings of operating systems and computer networks through hands-on implementation of core concepts in C and Python on Linux.

## Coursework

### Operating Systems
- **CS 370 (OS)** - CPU scheduling algorithms, IPC mechanisms, process synchronization
- **CS 320 (Algorithms)** - Algorithm design and analysis

### Computer Networks
- **CS 457 (Networks and Internet)** - Socket programming, network protocols, UDP/TCP, web servers, video streaming

## Key Topics

| Area | Description |
|------|-------------|
| **Process Scheduling** | FCFS, SJF, Round Robin, Priority Scheduling |
| **IPC** | Anonymous pipes, named pipes (FIFOs), shared memory |
| **Network Programming** | UDP/TCP sockets, HTTP servers, video streaming |
| **Process Synchronization** | Mutexes, semaphores, condition variables |
| **System Calls** | Wrapper functions for kernel interfaces |

## OS Internals Projects

### CPU Scheduling Algorithms
- **First-Come, First-Served (FCFS)** - Non-preemptive, arrival-order scheduling
- **Shortest Job First (SJF)** - Minimum average waiting time
- **Round Robin** - Preemptive time-sliced scheduling
- **Priority Scheduling** - Priority-based execution order

### IPC Mechanisms
- **Anonymous Pipes** - Parent-child process communication
- **Named Pipes (FIFOs)** - Unrelated process communication
- **Shared Memory** - Fastest IPC with explicit synchronization
- **Message Queues** - POSIX message queue patterns

### Process Creation
- Fork/exec patterns for process spawning
- Zombie and orphan process handling
- Copy-on-write semantics

## Networking Projects

### Socket Programming (Labs 2-4)
- **UDP Pinger** - Client-server ping implementation
- **Multiple Connections** - TCP server handling concurrent clients
- **Generic TCP Server** - Reusable server architecture

### Application Layer (Labs 5-9)
- **ICMP Ping** - Raw socket implementation
- **Video Streaming** - RTP-based streaming server
- **Web Server** - HTTP/1.1 server implementation
- **Packet Analysis** - Wireshark-based protocol analysis

### Network Protocols
- **Transport Layer** - UDP, TCP, congestion control
- **Application Layer** - HTTP, DNS, protocol design
- **Network Layer** - IP routing, traceroute, ICMP

## Technical Deep Dive

### Socket Programming
```python
# UDP Server
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((host, port))

# TCP Server
server_sock = socket(AF_INET, SOCK_STREAM)
server_sock.listen(5)
client_sock, addr = server_sock.accept()
```

### IPC Example
```c
int pipefd[2];
pipe(pipefd);  // pipefd[0] = read, pipefd[1] = write

fork();
// Parent writes to pipefd[1], child reads from pipefd[0]
```

### Synchronization
```c
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_lock(&mutex);
// Critical section
pthread_mutex_unlock(&mutex);
```

## Building and Running

```bash
# OS Projects
cd assignments/1
make
./chat

# Network Labs
cd labs/2
python3 cs457_UDPPingerServer.py
python3 client.py

# Web Server
cd labs/9
python3 server.py
# Then visit http://localhost:8080
```

## TODO

### OS Projects
- [ ] Multi-Level Feedback Queue scheduler
- [ ] Memory-mapped files (mmap) examples
- [ ] Dining philosophers problem solutions
- [ ] Deadlock detection and prevention

### Network Projects
- [ ] IPv6 support across all implementations
- [ ] TLS/SSL integration for secure communication
- [ ] Performance benchmarking suite
- [ ] Protocol conformance testing
