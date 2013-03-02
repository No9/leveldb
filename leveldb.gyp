{'targets': [
    {
        'target_name': 'leveldb'
      , 'type': '<(library)'
      , 'includes': [ 'common.gypi' ]
      , 'sources':
          [ '<@(ldb_sources)' ]
    }
  , {
        'target_name': 'db_bench'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [
            '<@(ldb_testutil)'
          , 'db/db_bench.cc'
        ]
    }
  , {
        'target_name': 'leveldbutil'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ 'db/leveldb_main.cc' ]
    }
  , {
        'target_name': 'arena_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'util/arena_test.cc' ]
    }
  , {
        'target_name': 'bloom_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'util/bloom_test.cc' ]
    }
  , {
        'target_name': 'c_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'db/c_test.c' ]
    }
  , {
        'target_name': 'cache_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'util/cache_test.cc' ]
    }
  , {
        'target_name': 'coding_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'util/coding_test.cc' ]
    }
  , {
        'target_name': 'corruption_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'db/corruption_test.cc' ]
    }
  , {
        'target_name': 'crc32c_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'util/crc32c_test.cc' ]
    }
  , {
        'target_name': 'db_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'db/db_test.cc' ]
    }
  , {
        'target_name': 'dbformat_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'db/dbformat_test.cc' ]
    }
  , {
        'target_name': 'env_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'util/env_test.cc' ]
    }
  , {
        'target_name': 'filename_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'db/filename_test.cc' ]
    }
  , {
        'target_name': 'filter_block_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'table/filter_block_test.cc' ]
    }
  , {
        'target_name': 'log_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'db/log_test.cc' ]
    }
  , {
        'target_name': 'skiplist_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'db/skiplist_test.cc' ]
    }
  , {
        'target_name': 'table_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'db/leveldb_main.cc' ]
    }
  , {
        'target_name': 'version_edit_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'db/version_edit_test.cc' ]
    }
  , {
        'target_name': 'version_set_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'db/version_set_test.cc' ]
    }
  , {
        'target_name': 'write_batch_test'
      , 'type': 'executable'
      , 'includes': [ 'common.gypi' ]
      , 'dependencies': [ 'leveldb' ]
      , 'sources': [ '<@(ldb_testharness)', 'db/write_batch_test.cc' ]
    }
]}