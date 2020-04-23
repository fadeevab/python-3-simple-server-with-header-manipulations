# python-3-simple-server

Simple Python 3 server to experiment with header manipulations,
e.g. `Set-Cookie`, `Origin`, and `Host` in the current example.

## How-To Use

Run the server:
```
python3 ./server-example-with-headers.py
```

1. `Origin` header is forged by client:
    ```
    $ curl localhost:8080 -H 'Origin: fadeevab.com'

    I believe this request is from fadeevab.com!
    Hello, world!
    ```

2. `Set-Cookie` header is returned:
    ```
    $ curl localhost:8080 -v

    ....
    < HTTP/1.0 200 OK
    < Server: BaseHTTP/0.6 Python/3.7.5
    < Date: ...
    < Set-Cookie: auth=1234; Domain=sub.localhost
    ```
    `-v` is just to show headers

## Tip
To experiment with subdomains on your local machine just modify `/etc/hosts` file (`C:\\Windows\\System32\\Drivers\\etc\\hosts`) like the following:
```
127.0.0.1 sub.localhost
```