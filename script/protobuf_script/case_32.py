import sys
sys.path.append("D:\flask-project\ApiPerformanceTest")
sys.path.append("D:\flask-project\ApiPerformanceTest\script\proto_script")
from locust import TaskSet, task, HttpLocust

class case_32Task(TaskSet):

	def on_start(self):
		print("start programing...")

	@task(1)
	def userlogin(self):
		from script.proto_script.AuthorizeInfoProto_pb2 import AdminLoginInputProto
		url = "http://192.168.1.18:8150/api/Login/userlogin"
		header = {'userinfo': "{'useruid': '29d6a026-f774-4c9d-904c-e492a4246e10', 'organizationid': '-1'}", 'content-type': 'application/octet-stream', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiYzgwYmMyZjQtMGM3MC00NmQyLTk0MjItNjQwNTQxMjYzMTE2IiwiaWF0IjoiMjAxOS83LzMxIDk6NDk6MTkiLCJleHAiOjE1NjQ1OTUzNTksImlzcyI6ImVXb3JkIiwiYXVkIjoiZVdvcmRQT0QifQ.anrUcmYFHRclTqT4WDuOpsG7pfnkRXfkaE4onsHvzac'}
		body = AdminLoginInputProto()
		body.account = "admin"
		body.password = "123456"
		body.loginType = 1
		body.organizationID = "-1"
		data = body.SerializeToString()
		name = "用户登录"
		response = self.client.post(url, data=data, headers=header, name=name)
		result = response.text
		print(response.status_code, result)
		response.raise_for_status()

class case_32User(HttpLocust):
	task_set = case_32Task
	min_wait = 1000
	max_wait = 2000
