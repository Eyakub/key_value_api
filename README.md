## Run the proejct
No need to migrate as it's using cloud <b>MongoDB</b>, just <b>Clone</b> & activate the virtualenv & run inside <b>src</b> directory with command 
``` python manage.py runserver ```

###  GET all data
```/values```

### GET values by one or more keys
``` /values?keys=key1,key2 ```

### POST data
``` /values/ ``` and pass information like this ``` {key1: value1, key2: value2}```

### PATCH (update data)
``` /values/ ``` and pass information like this ```{key1: value1...}```