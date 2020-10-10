import pycurl

def header(buffer):
    import sys
    sys.stdout.write(buffer)

def dispatcher(line):
    c = pycurl.Curl()
    c.setopt(pycurl.URL, "http://ubistandard.ml/d/" + line.replace(' ', "%20"))
    c.setopt(c.FOLLOWLOCATION, True)
    c.setopt(pycurl.HEADERFUNCTION, header)
    c.perform()
    c.close()
    
def load_ipython_extension(ipython, *args):
    ipython.register_magic_function(dispatcher, 'line', magic_name="webfetcher")
    
def unload_ipython_extension(ipython):
    pass # No need to implement yet 