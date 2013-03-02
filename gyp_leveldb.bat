"C:\Program Files (x86)\Python27\Scripts\gyp.bat" -f msvs -G msvs_version=2010 --depth=. -Dlibrary=static_library leveldb.gyp

MSBuild.exe .\levelup.sln