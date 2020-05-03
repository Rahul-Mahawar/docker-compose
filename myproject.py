import os                                                           
import webbrowser
 
os.system("tput setaf 10")
print("\t\t\t\t------------------------------------------------------")

os.system("tput setaf 1")
print("\t\t\t\t ---->>  Welcome to the docker-compose Project <<----")
os.system("tput setaf 10")

print("\t\t\t\t------------------------------------------------------")

while True:
    os.system("tput setaf 10")
    print("""docker-compose files:\n\n\t1: wordpress \n
        2: owncloud \n
        3: joomla \n
        4: nextcloud \n
        5: drupal \n
        6: ghost""")

    print("\n")
    print("select the file number:")
    print("\t")  

    ch = input()

    if ch == '1':
        os.system("docker-compose -f wordpress.yml up -d")
        webbrowser.open("http://192.168.43.41:8085")

    elif ch == '2':
        os.system("docker-compose -f owncloud.yml up -d")
        webbrowser.open("http://192.168.43.41:8083")

    elif ch == '3':
        os.system("docker-compose -f joomla.yml up -d")
        webbrowser.open("http://192.168.43.41:8084")
    
    elif ch == '4':
        os.system("docker-compose -f nextcloud.yml up -d")
        webbrowser.open("http://192.168.43.41:8086")

    elif ch == '5':
        os.system("docker-compose -f drupal.yml up -d")
        webbrowser.open("http://192.168.43.41:8089")

    elif ch == '6':
        os.system("docker-compose -f ghost.yml up -d")
        webbrowser.open("http://192.168.43.41:8088")

    else:
        print("this service is not available :( \ntry again.... \n")
