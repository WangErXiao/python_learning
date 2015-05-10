from chapter01.make_db_file import loadDbase,storeDbase
db=loadDbase()
db['sue']['pay']=9999
storeDbase(db)