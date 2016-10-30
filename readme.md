# jsondb

[![Build Status][travis-image]][travis-build]
[![PyPI version](https://badge.fury.io/py/jsondatabase.svg)](https://badge.fury.io/py/jsondatabase)

This is a utility for managing content in a database which stores
content in JSON format.

## Installation

This package can be installed from [PyPi](https://pypi.python.org/pypi/jsondatabase) by running:

```bash
pip install jsondatabase
```

Note, the package name and the import name are different.
Import the package using `import jsondb`.

## Usage

```python
from jsondb.db import Database
db = Database("mydata.db")
```

The database has an attribute which works similar to
[jQuery's `data`][jquery-data] attribute.

```python
# Getting all data
db = Database("mydata.db")
print(db.data())
```

```python
# Getting a stored value
db = Database("mydata.db")
print(db.data(key="user_count"))
```

**It is important to note that a key will be created regardless of whether it
exists as long as a value is provided.** The database has the same functionality
as a dictionary.

```python
# Setting a value
db = Database("mydata.db")
db.data(key="user_count", value=241)
```

```python
# Passing in a dictionary value
db = Database("mydata.db")
data = {
    "user_id": 234565,
    "user_name": "AwesomeUserName",
    "is_moderator": True,
}
db.data(dictionary=data)
```

```python
# Deleting a value
db = Database("mydata.db")
db.delete("my_key")
```

The database also supports a dictionary-like syntax for retrieving, setting, and
removing values.

```python
db = Database("mydata.db")

# Retrieving a value
value = db["key"]

# Setting a value
db["key"] = value

# Removing a key
del db["key"]

# Checking if a key exists
"key" in db
```

## Performance
If performance is an issue with large databases then the `python-cjson` module
can be installed. jsondb will automatically detect this and use cjson instead.

[jquery-data]: http://api.jquery.com/data/
[travis-build]: https://travis-ci.org/gunthercox/jsondb
[travis-image]: https://travis-ci.org/gunthercox/jsondb.svg
