# coding: cp1252
import subprocess

print("Hello, welcome to chatverse.\n")
system = input("Are you using Windows or Linux?\n").lower()

if system == 'windows':
    print("""
        Note: boost libraries can be downloaded 
              from https://www.boost.org/users/download/
              developer command prompt is included with Visual Studio
        """)
    boost = input((r'Enter path to boost (i.e., C:\boost_1_81_0)') + '\n')
    project = input((r'Enter path to chatverse (i.e., C:\Users\name\Downloads\chatverse-main)') + '\n')
    print(f"""  
        1. Open developer command prompt
        2. Type "cl /EHsc /I {boost} {project}\server.cpp"
        3. Type "server"
        4. Send a message
        5. Open a second developer command prompt
        6. Type "cl /EHsc /I {boost} {project}\client.cpp"
        7. Type "client"
        8. Enjoy
        """)
    input("Exit? ")

elif system == 'linux':
    print("""
        Note: boost libraries can be downloaded 
              from https://www.boost.org/users/download/
        """)
    boost = input((r'Enter path to boost (i.e., /home/name/boost_1_81_0)') + '\n')
    comp = input(("Enter preferred compiler (i.e., g++ || c++)") + '\n')
    print(f"""
      After typing your message to the client:
        1. Open a second terminal 
        2. Navigate to chatverse-main
        3. Type "{comp} -I {boost} client.cpp -o client; ./client"
        4. Enjoy
        """)
    subprocess.run(f'{comp} -I {boost} server.cpp -o server; ./server', shell = True)