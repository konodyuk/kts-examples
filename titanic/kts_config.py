# Cache mode defines resources used for caching:
# - disk         -- use only disk space, no RAM is used. Choose it if you don't have much RAM.
# - ram          -- use only RAM space. Best for kaggle kernels.
# - disk_and_ram -- use both. The fastest option. Best for local usage. Default. 
cache_mode = 'disk_and_ram'  # "disk", "disk_and_ram", "ram"

# Cache policy defines which types of files will be saved.
# - everything   -- cache everything including feature constructor calls. Default.
# - service      -- only service files are saved. No feature computation speedup. 
#                   Use if you're not lucky with your resources.
cache_policy = 'everything'  # "everything", "service"

# Full path of storage.
# DO NOT ERASE
storage_path = '/Users/konodyuk/Documents/IT/Lib/kts-examples/titanic/storage/'
