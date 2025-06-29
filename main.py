# To install requirements, run the following command in your terminal:
# pip install -r Requirements.txt
from Scan import scan
from Individualip import printDATA

def main():
    ips = scan()
    for ip in ips:
        printDATA(ip=ip)
         
         
    print("\nScan complete. All IPs processed.")
    
    
if __name__ == "__main__":
    main()
    # This will run the main function when the script is executed directly.