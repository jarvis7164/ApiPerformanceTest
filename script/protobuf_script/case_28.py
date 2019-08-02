import sys
sys.path.append("D:\flask-project\ApiPerformanceTest")
sys.path.append("D:\flask-project\ApiPerformanceTest\script\proto_script")
from locust import TaskSet, task, HttpLocust

class case_28Task(TaskSet):

	def on_start(self):
		print("start programing...")

	@task(1)
	def registeruser(self):
		from script.proto_script.UserMstProto_pb2 import UserMstProto
		url = "http://192.168.1.18:8150/api/register/registeruser"
		header = {'userinfo': "{'useruid': '29d6a026-f774-4c9d-904c-e492a4246e10', 'organizationid': '-1'}", 'content-type': 'application/octet-stream', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiYTY2OWQ4MTMtMWE0Yi00MDhmLTkyZDktMmViMGNjNDZmNDViIiwiaWF0IjoiMjAxOS83LzI0IDE3OjUyOjE3IiwiZXhwIjoxNTY0MDE5NTM3LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.-ErNDN3NRiJflIVEhSR8o6YZ02ZFBOz2nKusWTIT5_I'}
		body = UserMstProto()
		body.name = "测试"
		body.type = "doctor"
		body.email = "2545854526@qq.com"
		body.deptID = "02332bb9-1f92-4b26-bbe0-d37408b1d492"
		body.status = "0"
		body.workNO = "8512"
		body.account = "test"
		body.address = "杭州紫金花路"
		body.iDCardNO = "352458855452562558"
		body.password = "123456"
		body.createDate = "2019-7-11 13：55：48.297"
		body.officePhone = "0571-85652548"
		body.privatePhone = "15865254528"
		body.createUserUID = "00000000-0000-0000-0000-000000000000"
		body.createUserName = "用户自己注册"
		body.organizationID = "local"
		data = body.SerializeToString()
		name = "用户注册"
		response = self.client.post(url, data=data, headers=header, name=name)
		result = response.text
		print(response.status_code, result)
		response.raise_for_status()

	@task(3)
	def userlogin(self):
		from script.proto_script.AuthorizeInfoProto_pb2 import AdminLoginInputProto
		url = "http://192.168.1.18:8150/api/Login/userlogin"
		header = {'userinfo': "{'useruid': '29d6a026-f774-4c9d-904c-e492a4246e10', 'organizationid': '-1'}", 'content-type': 'application/octet-stream', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiYTY2OWQ4MTMtMWE0Yi00MDhmLTkyZDktMmViMGNjNDZmNDViIiwiaWF0IjoiMjAxOS83LzI0IDE3OjUyOjE3IiwiZXhwIjoxNTY0MDE5NTM3LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.-ErNDN3NRiJflIVEhSR8o6YZ02ZFBOz2nKusWTIT5_I'}
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

	@task(1)
	def getcheckinfolist(self):
		from script.proto_script.CheckInfoProto_pb2 import SearchInputProto
		url = "http://192.168.1.18:8150/api/check/getcheckinfolist"
		header = {'userinfo': "{'useruid': '29d6a026-f774-4c9d-904c-e492a4246e10', 'organizationid': '-1'}", 'content-type': 'application/octet-stream', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiYTY2OWQ4MTMtMWE0Yi00MDhmLTkyZDktMmViMGNjNDZmNDViIiwiaWF0IjoiMjAxOS83LzI0IDE3OjUyOjE3IiwiZXhwIjoxNTY0MDE5NTM3LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.-ErNDN3NRiJflIVEhSR8o6YZ02ZFBOz2nKusWTIT5_I'}
		body = SearchInputProto()
		body.examEndTime = "2018-07-01 23:59:59"
		body.examStartTime = "2018-01-01 00:00:00"
		body.organizationID = "-1"
		data = body.SerializeToString()
		name = "检查信息列表（半年）"
		response = self.client.post(url, data=data, headers=header, name=name)
		result = response.text
		print(response.status_code, result)
		response.raise_for_status()

	@task(4)
	def getcheckinfolist_1(self):
		from script.proto_script.CheckInfoProto_pb2 import SearchInputProto
		url = "http://192.168.1.18:8150/api/check/getcheckinfolist"
		header = {'userinfo': "{'useruid': '29d6a026-f774-4c9d-904c-e492a4246e10', 'organizationid': '-1'}", 'content-type': 'application/octet-stream', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiYTY2OWQ4MTMtMWE0Yi00MDhmLTkyZDktMmViMGNjNDZmNDViIiwiaWF0IjoiMjAxOS83LzI0IDE3OjUyOjE3IiwiZXhwIjoxNTY0MDE5NTM3LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.-ErNDN3NRiJflIVEhSR8o6YZ02ZFBOz2nKusWTIT5_I'}
		body = SearchInputProto()
		body.accessionNumber = "288046"
		data = body.SerializeToString()
		name = "获取检查信息列表（单个检查号）"
		response = self.client.post(url, data=data, headers=header, name=name)
		result = response.text
		print(response.status_code, result)
		response.raise_for_status()

	@task(4)
	def getpatientlist(self):
		from script.proto_script.PatientInputProto_pb2 import PatientInputProto
		url = "http://192.168.1.18:8150/api/clinic/getpatientlist"
		header = {'userinfo': "{'useruid': '29d6a026-f774-4c9d-904c-e492a4246e10', 'organizationid': '-1'}", 'content-type': 'application/octet-stream', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiYTY2OWQ4MTMtMWE0Yi00MDhmLTkyZDktMmViMGNjNDZmNDViIiwiaWF0IjoiMjAxOS83LzI0IDE3OjUyOjE3IiwiZXhwIjoxNTY0MDE5NTM3LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.-ErNDN3NRiJflIVEhSR8o6YZ02ZFBOz2nKusWTIT5_I'}
		body = PatientInputProto()
		body.patientName = "石光翠"
		body.userOrganizationID = "-1"
		data = body.SerializeToString()
		name = "获取病人视图列表(姓名查询)"
		response = self.client.post(url, data=data, headers=header, name=name)
		result = response.text
		print(response.status_code, result)
		response.raise_for_status()

	@task(1)
	def getvisitpeople(self):
		from script.proto_script.VisitInputProto_pb2 import VisitInputProto
		url = "http://192.168.1.18:8150/api/clinic/getvisitpeople"
		header = {'content-type': 'application/octet-stream', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiYTY2OWQ4MTMtMWE0Yi00MDhmLTkyZDktMmViMGNjNDZmNDViIiwiaWF0IjoiMjAxOS83LzI0IDE3OjUyOjE3IiwiZXhwIjoxNTY0MDE5NTM3LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.-ErNDN3NRiJflIVEhSR8o6YZ02ZFBOz2nKusWTIT5_I'}
		body = VisitInputProto()
		body.ageUnit = "岁"
		body.admitEndDate = "2018-07-01 23:59:59"
		body.admitStartDate = "2018-01-01 00:00:00"
		data = body.SerializeToString()
		name = "获取就诊视图列表（半年）"
		response = self.client.post(url, data=data, headers=header, name=name)
		result = response.text
		print(response.status_code, result)
		response.raise_for_status()

	@task(3)
	def getcheckinfolist_2(self):
		from script.proto_script.CheckInfoProto_pb2 import SearchInputProto
		url = "http://192.168.1.18:8150/api/check/getcheckinfolist"
		header = {'userinfo': "{'useruid': '29d6a026-f774-4c9d-904c-e492a4246e10', 'organizationid': '-1'}", 'content-type': 'application/octet-stream', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiYTY2OWQ4MTMtMWE0Yi00MDhmLTkyZDktMmViMGNjNDZmNDViIiwiaWF0IjoiMjAxOS83LzI0IDE3OjUyOjE3IiwiZXhwIjoxNTY0MDE5NTM3LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.-ErNDN3NRiJflIVEhSR8o6YZ02ZFBOz2nKusWTIT5_I'}
		body = SearchInputProto()
		body.examEndTime = "2018-01-31 23:59:59"
		body.examStartTime = "2018-01-01 00:00:00"
		body.organizationID = "-1"
		data = body.SerializeToString()
		name = "获取检查信息列表（一个月）"
		response = self.client.post(url, data=data, headers=header, name=name)
		result = response.text
		print(response.status_code, result)
		response.raise_for_status()

class case_28User(HttpLocust):
	task_set = case_28Task
	min_wait = 1000
	max_wait = 2000
