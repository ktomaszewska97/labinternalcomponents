Small Example which uses 2 external python sources and imports both in application.py

when application.py is executed (python3 application.py - e.g. in a dockerized environment) it will start two threads osbd.py (port 5000) and coordinator.py (port 5001)
When you do a POST (inkl. auth: "admin": "SupErSecretP!?") on the ports a json result is created { result : Hello World <or> Hello Coordinator }

