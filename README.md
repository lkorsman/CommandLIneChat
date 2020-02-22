# Python Chatroom
This program acts as both a client and a server for a simple command
line based chatroom. If the server gets disconnected, a random client
will attempt to become the server.

## Usage
Python3 is needed to run the program

The Server should be started before the client. To start the Server,
pass no additional command line arguments, e.g.
```bash
python3 chat.py
```

The Client should have one command line argument which is a username, e.g.
```bash
python3 chat.py <username>
```

## Additional Notes
If you are going to use this on a Windows machine, some minor tweaks are
needed. You will need to import the colorama library and add the line of 
code ```colorama.init()``` before the last ``` while True ``` loop

## License
MIT License

Copyright (c) 2020 Luke Korsman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.