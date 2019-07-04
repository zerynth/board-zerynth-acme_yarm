from base import *
from devices import *
from jtag import *
import time
import re

class AcmeYarm(Board):
    ids_vendor = {}

    @staticmethod
    def match(dev):
        return False 

    def reset(self):
        pass

    def burn(self,bin,outfn=None):
        return False,"not supported!"
