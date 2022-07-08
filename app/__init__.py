#!/usr/bin/env python3.x
# Flask 
# Author : Muhammet Burak GOLEC


def main():
    try:
        from .views import app
    
    except ImportError:
    
        print("Import Error ")



if __name__=='__init__':
    main()


