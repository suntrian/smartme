# one can modify this file using python grammar to dynamically plug modules into the running program
# the last tag should be a Class extended from model

from weather import Weather
from metal import ICBC
from stock.Stock import MyStock
import yaha.tests.test_cuttor

