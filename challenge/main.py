from factory import LogSourceFactory

def main():
    source = LogSourceFactory.create_source("csv")
    logs = source.get_logs()
    
    print("--- Running SOLID Challenge ---")
    for log in logs:
        print(f"Result: {log}")

if __name__ == "__main__":
    main()
