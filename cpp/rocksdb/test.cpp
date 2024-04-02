/**
 * @author: Zeyu Zuo
 * @date: 2024-04-02 21:07:51
 */
#include <iostream>
#include <rocksdb/db.h>
#include <rocksdb/options.h>
#include <rocksdb/slice.h>
using namespace std;
using namespace rocksdb;

int main(int argc, char** argv) {
    DB* db;
    Options options;
    options.create_if_missing = true;
    Status s = rocksdb::DB::Open(options, "/tmp/rocksdb_simple_example", &db);
    assert(s.ok());

    // 插入数据
    s = db->Put(WriteOptions(), "key1", "value1");
    assert(s.ok());
    s = db->Put(WriteOptions(), "key2", "value2");
    assert(s.ok());

    // 创建迭代器
    Iterator* it = db->NewIterator(ReadOptions());
    for (it->SeekToFirst(); it->Valid(); it->Next()) {
        cout << it->key().ToString() << ": " << it->value().ToString() << endl;
    }

    // 删除数据库
    delete db;
    return 0;
}