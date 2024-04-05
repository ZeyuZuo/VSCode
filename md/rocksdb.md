# 在petalinux上运行rocksdb
这个过程花了我很长时间，我在2024-4-3 17：08跑出来了rocksdb，然后开始跑db_bench，这个过程花了两天，因为编译一次需要3小时，而有的问题出现了，需要重新编译，有时候甚至编译出现问题
linux上可以安装tio来当ssh，很方便
现在是2024-4-5 16：57，我在这段时间碰到了不少问题，有的可能忘记了，我把我记得的写下来
## make static_lib && make install-static
重点是指定librocksdb.a的位置，别的好像没啥

## make db_bench
要先安装gflags，我当时没装，就make db_bench了，然后./db_bench会提示先安装gflags，然后我安装了再运行，结果还是不行，网上说设置CPATH,LIBRARY_PATH，这些不管用，直接重新编译，就好了。

安装好gflags后编译运行还是报错，要安装bzip2

为了以防万一，我安装github上的INSTALL.md文件里，把那些压缩功能的全装上了，在environment压缩包里，麻烦的是snappy，彼得不会有问题，这个会有，一定要1.1.1版本，编译好后设置LD_LIBRARY_PATH路径

安装environment里面的，基本就是make make install之类，snappy需要../configure一下再执行
总之，缺啥安装啥，我当时是从cmake一步步开始的，制作petalinux的时候忘了cmake

```
root@petalinux:/# find / -name libsnappy.so.1
/usr/local/lib/libsnappy.so.1

root@petalinux:~# export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
root@petalinux:~# echo $LD_LIBRARY_PATH
/usr/local/lib:
```

这时候再make db_bench，编译需要3小时，然后./db_bench，编译确实很久，所以很花时间

sd卡运行结果
```
root@petalinux:~/rocksdb_new# ./bench
Set seed to 1712161839221523 because --seed was 0
Initializing RocksDB Options from the specified file
Initializing RocksDB Options from command-line flags
Integrated BlobDB: blob cache disabled
RocksDB:    version 8.11.3
Date:       Wed Apr  3 16:30:39 2024
CPU:        0 * 
CPUCache:   
Keys:       16 bytes each (+ 0 bytes user-defined timestamp)
Values:     100 bytes each (50 bytes after compression)
Entries:    1000000
Prefix:    0 bytes
Keys per prefix:    0
RawSize:    110.6 MB (estimated)
FileSize:   62.9 MB (estimated)
Write rate: 0 bytes/second
Read rate: 0 ops/second
Compression: Snappy
Compression sampling rate: 0
Memtablerep: SkipListFactory
Perf Level: 1
WARNING: Assertions are enabled; benchmarks unnecessarily slow
------------------------------------------------
Initializing RocksDB Options from the specified file
Initializing RocksDB Options from command-line flags
Integrated BlobDB: blob cache disabled
DB path: [/tmp/rocksdbtest-0/dbbench]
fillseq      :      29.752 micros/op 33610 ops/sec 29.752 seconds 1000000 operations;    3.7 MB/s
Please disable_auto_compactions in FillDeterministic benchmark
root@petalinux:~/rocksdb_new# Xilinx Zynq MP First Stage Boot Loader 
Release 2020.1   Apr  3 2024  -  10:31:36
NOTICE:  ATF running on XCZU2CG/silicon v4/RTL5.1 at 0xfffea000
NOTICE:  BL31: v2.2(release):v1.1-5588-g5918e656e
NOTICE:  BL31: Built : 10:28:51, Apr  3 2024
```

nvme运行结果
```
root@petalinux:/media/ssd/rocksdb_new# ./db_bench
Set seed to 1712345123703628 because --seed was 0
Initializing RocksDB Options from the specified file
Initializing RocksDB Options from command-line flags
Integrated BlobDB: blob cache disabled
RocksDB:    version 8.11.3
Date:       Fri Apr  5 19:25:23 2024
CPU:        0 * 
CPUCache:   
Keys:       16 bytes each (+ 0 bytes user-defined timestamp)
Values:     100 bytes each (50 bytes after compression)
Entries:    1000000
Prefix:    0 bytes
Keys per prefix:    0
RawSize:    110.6 MB (estimated)
FileSize:   62.9 MB (estimated)
Write rate: 0 bytes/second
Read rate: 0 ops/second
Compression: Snappy
Compression sampling rate: 0
Memtablerep: SkipListFactory
Perf Level: 1
WARNING: Assertions are enabled; benchmarks unnecessarily slow
------------------------------------------------
Initializing RocksDB Options from the specified file
Initializing RocksDB Options from command-line flags
Integrated BlobDB: blob cache disabled
DB path: [/tmp/rocksdbtest-0/dbbench]
fillseq      :      29.857 micros/op 33493 ops/sec 29.857 seconds 1000000 operations;    3.7 MB/s
Please disable_auto_compactions in FillDeterministic benchmark
```