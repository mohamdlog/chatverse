# -*- coding: cp1252 -*-


system = input("Are you using Windows or Linux?\n").lower()
if system == 'windows':
    boost = input((r'Enter path to boost (i.e., C:\boost_1_81_0)') + '\n')
    project = input((r'Enter path to chatverse (i.e., C:\Users\name\Desktop\chatverse)') + '\n')
    print(f"""  
        1. Open developer command prompt
        2. Type "cl /EHsc /I {boost} {project}\server.cpp"
        3. Type "server"
        4. Open a second developer command prompt
        5. Type "cl /EHsc /I {boost} {project}\client.cpp"
        6. Type "client"
        """)
elif system == 'linux':
    print("""
        Note: libboost and g++ can be downloaded with
        sudo apt-get install libboost-all-dev 
        sudo apt-get install g++
        """)
    print("""
        1. Open command prompt
        2. Type "g++ server.cpp -o server –lboost_system"
        3. Type "./server"
        4. Open a second command prompt
        5. Type "g++ client.cpp -o client –lboost_system"
        6. Type "./client"
        """)