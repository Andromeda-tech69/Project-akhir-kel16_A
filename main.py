import Login.login as login
import os,time

if __name__ == "__main__":
    while True:
        try: login.main()
        except Exception as e: print(e) 
        except KeyboardInterrupt: 
            os.system('cls')
            print("\nKeyBoard  Interrupt")
            for i in range(3,0,-1):
                time.sleep(1)
                print("Auto Logout In ", i )
            continue