import sys
import time
import itertools

def animate():
    # Animation frames (Industrial style)
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    
    print("SYSTEM_INITIALIZING...")
    
    try:
        for _ in range(50): # 50 frames tak chalega
            # \r se cursor line ki shuruat mein wapas aa jata hai
            sys.stdout.write(f'\r[{next(spinner)}] LOADING_ASSETS... ')
            sys.stdout.flush()
            time.sleep(0.1) # Speed control
            
        print("\n\nSUCCESS: SYSTEM_READY_TO_OPERATE")
        
    except KeyboardInterrupt:
        print("\n\nABORTED_BY_USER")

if __name__ == "__main__":
    animate()
