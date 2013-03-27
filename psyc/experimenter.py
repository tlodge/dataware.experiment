import time
import urllib2
import urllib

def register_processor(catalog, owner, query, resource_name):

  #set expiry to two hours from now
  expiry = time.time() + (60 * 60 * 2)  
  state = "%d" % time.time()
  client = fetchIdentifier(catalog)

  values = {
            'client_id': client.id,
            'state': state,
            'redirect_uri': client.redirect,
            'scope': '{"resource_name" : "%s", "expiry_time": %s, "query": "%s"}' % (resource_name,expiry,query)
  }

  url = "%s/user/%s/client_request" % (catalog,owner)

  data = urllib.urlencode(values)
  req = urllib2.Request(url,data)
  response = urllib2.urlopen(req)
  result = response.read()
  
  result = json.loads(
        result.replace( '\r\n','\n' ),
        strict=False
  )

  if (not(result['success'])):
     return False
         

  #addProcessorRequest(state=state, catalog=catalog, resource=resource_name,resource_uri=resource_uri,redirect=client.redirect, owner=owner, expiry=int(expiry),query=query)

  return True 

def perform_execution():
  return True
