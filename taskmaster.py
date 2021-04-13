import yaml, subprocess, time, os, sys, signal
from datetime import datetime
from config import Config
import tskconsol
import process
import logging
import logging.config
import os

if __name__ == "__main__":
  logging.basicConfig(filename="taskmst.log",format='%(asctime)s %(levelname)-8s %(name)-15s %(message)s',level=logging.DEBUG
  )
  tskconsol.loop()