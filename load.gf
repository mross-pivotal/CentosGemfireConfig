connect --locator=localhost[41111]
start server --name=server1 --cache-xml-file=/Users/mross/workspace/YCSB/gemfire/src/main/conf/cache.xml --locators=localhost[41111] --server-port=0
put --key=999999 --value="matt" --region=/usertable
query --query="select * from /usertable"
