import web

db = web.database(dbn='mysql', db='CS8083', user='CS8083', pw='CS8083')

def getUserInfo(username, password):
	# easily perform username: ' or ''=' password: ' or ''=', than sql injection will happen
  return db.query("SELECT * FROM `USER` WHERE `NAME` = '%s' and password = '%s'" % (username, password)).list()

def getUserInfoSec(username, password):
  # no sql injection happens:
  return db.query("SELECT * FROM USER WHERE NAME=$username and PASSWORD=$password", vars={'username':username, 'password':password}).list()