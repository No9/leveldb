{
 'Xdependencies': [
      '../snappy/snappy.gyp:snappy'
  ]
, 'dependencies': [
    './libuv/uv.gyp:libuv'
  ]
, 'defines': [
    'XSNAPPY=1'
  , 'LEVELDB_PLATFORM_UV=1'
]
, 'include_dirs': [
    './'
  , 'port'
  , 'libuv_port'
  , 'util'
  , 'include'
]
, 'conditions': [
    ['OS == "win"', {
        'include_dirs': [
            'port/win'
        ]
    }]
  , ['OS == "linux"', {
        'defines': [
            'OS_LINUX=1'
          , 'LDB_UV_POSIX=1'
        ]
      , 'libraries': [
            '-lpthread'
        ]
      , 'ccflags': [
            '-fno-builtin-memcmp'
          , '-pthread'
          , '-fPIC'
        ]
      , 'cflags': [
            '-Wno-sign-compare'
          , '-Wno-unused-but-set-variable'
        ]
      , 'Xsources': [
            'libuv_port/uv_condvar_posix.cc'
        ]
    }]
  , ['OS == "solaris"', {
        'defines': [
            'OS_SOLARIS=1'
          , 'LDB_UV_POSIX=1'
        ]
      , 'libraries': [
            '-lrt'
          , '-lpthread'
        ]
      , 'ccflags': [
            '-fno-builtin-memcmp'
          , '-pthread'
          , '-fPIC'
        ]
      , 'cflags': [
            '-Wno-sign-compare'
          , '-Wno-unused-but-set-variable'
        ]
      , 'Xsources': [
            'libuv_port/uv_condvar_posix.cc'
        ]
    }]
  , ['OS == "mac"', {
        'defines': [
            'OS_MACOSX=1'
          , 'LDB_UV_POSIX=1'
        ]
      , 'libraries': []
      , 'ccflags': [
            '-fno-builtin-memcmp'
          , '-fPIC'
        ]
      , 'xcode_settings': {
            'WARNING_CFLAGS': [
                '-Wno-sign-compare'
              , '-Wno-unused-variable'
              , '-Wno-unused-function'
            ]
        }
      , 'Xsources': [
            'libuv_port/uv_condvar_posix.cc'
        ]
    }]
]
, 'variables': {
      'ldb_testutil': [
          'util/testutil.cc'
        , 'util/testutil.h'
      ]
    , 'ldb_testharness': [
          '<@(ldb_testutil)'
        , 'util/testharness.cc'
        , 'util/testharness.h'
      ]
    , 'ldb_sources': [
          'port/port.h'
        , 'libuv_port/port_uv.h'
        , 'libuv_port/port_uv.cc'
        , 'db/builder.cc'
        , 'db/builder.h'
        , 'db/db_impl.cc'
        , 'db/db_impl.h'
        , 'db/db_iter.cc'
        , 'db/db_iter.h'
        , 'db/filename.cc'
        , 'db/filename.h'
        , 'db/c.cc'
        , 'db/dbformat.cc'
        , 'db/dbformat.h'
        , 'db/log_format.h'
        , 'db/log_reader.cc'
        , 'db/log_reader.h'
        , 'db/log_writer.cc'
        , 'db/log_writer.h'
        , 'db/memtable.cc'
        , 'db/memtable.h'
        , 'db/repair.cc'
        , 'db/skiplist.h'
        , 'db/snapshot.h'
        , 'db/table_cache.cc'
        , 'db/table_cache.h'
        , 'db/version_edit.cc'
        , 'db/version_edit.h'
        , 'db/version_set.cc'
        , 'db/version_set.h'
        , 'db/write_batch.cc'
        , 'db/write_batch_internal.h'
        , 'helpers/memenv/memenv.cc'
        , 'helpers/memenv/memenv.h'
        , 'include/leveldb/cache.h'
        , 'include/leveldb/comparator.h'
        , 'include/leveldb/db.h'
        , 'include/leveldb/env.h'
        , 'include/leveldb/filter_policy.h'
        , 'include/leveldb/iterator.h'
        , 'include/leveldb/options.h'
        , 'include/leveldb/slice.h'
        , 'include/leveldb/status.h'
        , 'include/leveldb/table.h'
        , 'include/leveldb/table_builder.h'
        , 'include/leveldb/write_batch.h'
        , 'table/block.cc'
        , 'table/block.h'
        , 'table/block_builder.cc'
        , 'table/block_builder.h'
        , 'table/filter_block.cc'
        , 'table/filter_block.h'
        , 'table/format.cc'
        , 'table/format.h'
        , 'table/iterator.cc'
        , 'table/iterator_wrapper.h'
        , 'table/merger.cc'
        , 'table/merger.h'
        , 'table/table.cc'
        , 'table/table_builder.cc'
        , 'table/two_level_iterator.cc'
        , 'table/two_level_iterator.h'
        , 'util/arena.cc'
        , 'util/arena.h'
        , 'util/bloom.cc'
        , 'util/cache.cc'
        , 'util/coding.cc'
        , 'util/coding.h'
        , 'util/comparator.cc'
        , 'util/crc32c.cc'
        , 'util/crc32c.h'
        , 'util/env.cc'
        , 'util/env_posix.cc'
        , 'util/filter_policy.cc'
        , 'util/hash.cc'
        , 'util/hash.h'
        , 'util/logging.cc'
        , 'util/logging.h'
        , 'util/mutexlock.h'
        , 'util/options.cc'
        , 'util/random.h'
        , 'util/status.cc'
        , 'util/histogram.cc'
        , 'util/histogram.h'
      ]
  }
}