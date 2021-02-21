
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from app import sockets
import time

lastCreateTimeEpochMS = 0

def notify():
    print ("notify started")
    #------------------------
    # Setup watchdog patterns
    #------------------------
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = False 
    #path = "c://self//UniWatch2//static//images"
    path = "//Users//richardstanners//Desktop//self//dev//uniwatch2//static//images"
    go_recursively = True 
    #------------------------
    # Setup watchdog handlers
    #------------------------
    event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    event_handler.on_created = on_file_created

    observer = Observer()
    observer.schedule(event_handler, path, recursive=go_recursively)
    observer.start()

def on_file_created(event):
    global lastCreateTimeEpochMS
    #debounce - not sure why I get 2 creates, so wait 0.1 secs

    currentTimeEpochMS  = round(time.time() * 1000)

    if (currentTimeEpochMS > lastCreateTimeEpochMS + 100):
        print (str( {event.src_path} ) + "file created")
        print (str(event))
        sockets.sendMessageToAllCllients() 
    else:      
        lastCreateTimeEpochMS = round(time.time() * 1000)


