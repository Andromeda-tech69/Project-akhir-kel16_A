import Login.login as login

if __name__ == "__main__":
    try: login.main()
    except Exception as e: print(e) 
    except KeyboardInterrupt: print("KeyBoard  Interrupt")