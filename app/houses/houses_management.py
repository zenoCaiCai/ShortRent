from . import houses
from ..db import database

# an example.
# remove it when you begin developing and see this bad...
@houses.route("/test/houses")
def houses_test():
    return 'Hello house!'