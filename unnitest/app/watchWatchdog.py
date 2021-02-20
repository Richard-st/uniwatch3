
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from app import sockets

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

    event_handler.on_created = on_file_change

    observer = Observer()
    observer.schedule(event_handler, path, recursive=go_recursively)
    observer.start()

def on_file_change(event):

    print (str( {event.src_path} ) + "file created")
    sockets.sendMessageToAllCllients()
