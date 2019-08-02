import sys
sys.path.append("D:\flask-project\ApiPerformanceTest")
sys.path.append("D:\flask-project\ApiPerformanceTest\script\json_script")
from locust import TaskSet, task, HttpLocust

class case_31Task(TaskSet):

	def on_start(self):
		print('start programing...')

	@task(3)
	def getcheckinfolist(self):
		url = 'http://192.168.1.18:8100/api/check/getcheckinfolist?input= {"pageIndex":1,"pageSize":20,"medRecNO":"","accessionNumber":"","visitID":"","outPatientID":"","alternateVisitID":"","iDCardNo":"","addressDetail":"","patientName":"","examStartTime":"2018-01-01 00:00:00","examEndTime":"2018-01-31 23:59:59","registerStartTime":"","registerEndTime":"","resultStartDate":"","resultEndDate":"","requestStartTime":"","requestEndTime":"","lastUpdateStartDate1":"","lastUpdateEndDate1":"","gender":"","age":0,"ageUnit":"岁","birthDay":"","patientClass":[],"requestDeptID":[],"requestDocName":"","organizationID":["local"],"serviceSectID":[],"resultAssistantName":"","examStatus":[],"ifHasImage":"","resultPrintCount":"","criticalValue":"","quicksearch":"","UserInfo":{"userUID":"e7468084-46b3-4560-a64c-a9c200b1e3be","loginName":"jm1","userName":"贾苗","workNO":"004","officePhone":"","privatePhone":"15869525458","email":"30919454@qq.com","isSuperManager":false,"organizationID":"local","organizationName":"武汉中心医院","deptID":"","deptName":null}}'
		header = {'content-type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiNWI3ODM4YWMtNjQxNi00NTg3LTg1N2ItZmNkNTI3ZTYxOTdiIiwiaWF0IjoiMjAxOS83LzMwIDE3OjM0OjA0IiwiZXhwIjoxNTY0NTM2ODQ0LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.OtEkyL2BGBQQnwpU533kEWKV1RYo9I7WYZzO3GzEHaw'}
		name = '查询检查信息列表(一个月)'
		response = self.client.get(url, headers=header, name=name)
		print(response.status_code, response.text)
		response.raise_for_status()

	@task(4)
	def getcheckinfolist_1(self):
		url = 'http://192.168.1.18:8100/api/check/getcheckinfolist?input= {"pageIndex":1,"pageSize":20,"medRecNO":"","accessionNumber":"288046","visitID":"","outPatientID":"","alternateVisitID":"","iDCardNo":"","addressDetail":"","patientName":"","examStartTime":"","examEndTime":"","registerStartTime":"","registerEndTime":"","resultStartDate":"","resultEndDate":"","requestStartTime":"","requestEndTime":"","lastUpdateStartDate1":"","lastUpdateEndDate1":"","gender":"","age":0,"ageUnit":"岁","birthDay":"","patientClass":[],"requestDeptID":[],"requestDocName":"","organizationID":["local"],"serviceSectID":[],"resultAssistantName":"","examStatus":[],"ifHasImage":"","resultPrintCount":"","criticalValue":"","quicksearch":"","UserInfo":{"userUID":"e7468084-46b3-4560-a64c-a9c200b1e3be","loginName":"jm1","userName":"贾苗","workNO":"004","officePhone":"","privatePhone":"15869525458","email":"30919454@qq.com","isSuperManager":false,"organizationID":"local","organizationName":"武汉中心医院","deptID":"","deptName":null}}'
		header = {'content-type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiNWI3ODM4YWMtNjQxNi00NTg3LTg1N2ItZmNkNTI3ZTYxOTdiIiwiaWF0IjoiMjAxOS83LzMwIDE3OjM0OjA0IiwiZXhwIjoxNTY0NTM2ODQ0LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.OtEkyL2BGBQQnwpU533kEWKV1RYo9I7WYZzO3GzEHaw'}
		name = '查询检查信息列表(单个检查号)'
		response = self.client.get(url, headers=header, name=name)
		print(response.status_code, response.text)
		response.raise_for_status()

	@task(3)
	def userlogin(self):
		url = 'http://192.168.1.18:8100/api/Login/userlogin?input= {"organizationID":"local","account":"jm1","password":"123456"}'
		header = {'content-type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiNWI3ODM4YWMtNjQxNi00NTg3LTg1N2ItZmNkNTI3ZTYxOTdiIiwiaWF0IjoiMjAxOS83LzMwIDE3OjM0OjA0IiwiZXhwIjoxNTY0NTM2ODQ0LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.OtEkyL2BGBQQnwpU533kEWKV1RYo9I7WYZzO3GzEHaw'}
		name = '用户登录（IMCIS1.0）'
		response = self.client.get(url, headers=header, name=name)
		print(response.status_code, response.text)
		response.raise_for_status()

	@task(1)
	def registeruser(self):
		url = 'http://192.168.1.18:8100/api/register/registeruser'
		header = {'content-type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiNWI3ODM4YWMtNjQxNi00NTg3LTg1N2ItZmNkNTI3ZTYxOTdiIiwiaWF0IjoiMjAxOS83LzMwIDE3OjM0OjA0IiwiZXhwIjoxNTY0NTM2ODQ0LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.OtEkyL2BGBQQnwpU533kEWKV1RYo9I7WYZzO3GzEHaw'}
		body = {'Name': '张峰', 'Email': '', 'DeptID': '', 'WorkNO': '', 'Account': 'zf', 'Password': '123456', 'checkPwd': '123456', 'OfficePhone': '', 'PrivatePhone': '15865254586', 'OrganizationID': 'local'}
		name = '用户注册（IMCIS1.0）'
		response = self.client.post(url, json=body, headers=header, name=name)
		print(response.status_code, response.text)
		response.raise_for_status()

	@task(1)
	def getcheckinfolist_2(self):
		url = 'http://192.168.1.18:8100/api/check/getcheckinfolist?input= {"pageIndex":1,"pageSize":20,"medRecNO":"","accessionNumber":"","visitID":"","outPatientID":"","alternateVisitID":"","iDCardNo":"","addressDetail":"","patientName":"","examStartTime":"2018-01-01 00:00:00","examEndTime":"2018-07-01 23:59:59","registerStartTime":"","registerEndTime":"","resultStartDate":"","resultEndDate":"","requestStartTime":"","requestEndTime":"","lastUpdateStartDate1":"","lastUpdateEndDate1":"","gender":"","age":0,"ageUnit":"岁","birthDay":"","patientClass":[],"requestDeptID":[],"requestDocName":"","organizationID":[],"serviceSectID":[],"resultAssistantName":"","examStatus":[],"ifHasImage":"","resultPrintCount":"","criticalValue":"","quicksearch":"","UserInfo":{"userUID":"e7468084-46b3-4560-a64c-a9c200b1e3be","loginName":"jm1","userName":"贾苗","workNO":"004","officePhone":"","privatePhone":"15869525458","email":"30919454@qq.com","isSuperManager":false,"organizationID":"local","organizationName":"武汉中心医院","deptID":"","deptName":null}}'
		header = {'content-type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiNWI3ODM4YWMtNjQxNi00NTg3LTg1N2ItZmNkNTI3ZTYxOTdiIiwiaWF0IjoiMjAxOS83LzMwIDE3OjM0OjA0IiwiZXhwIjoxNTY0NTM2ODQ0LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.OtEkyL2BGBQQnwpU533kEWKV1RYo9I7WYZzO3GzEHaw'}
		name = '查询检查信息列表（半年）'
		response = self.client.get(url, headers=header, name=name)
		print(response.status_code, response.text)
		response.raise_for_status()

	@task(4)
	def getpatientlist(self):
		url = 'http://192.168.1.18:8100/api/clinic/getpatientlist?input= {"pageIndex":1,"pageSize":20,"insuranceID":"","healthCardNO":"","IDCardNo":"","PatientName":"石光翠","organizationID":[],"UserInfo":{"userUID":"e7468084-46b3-4560-a64c-a9c200b1e3be","loginName":"jm1","userName":"贾苗","workNO":"004","officePhone":"","privatePhone":"15869525458","email":"30919454@qq.com","isSuperManager":false,"organizationID":"local","organizationName":"武汉中心医院","deptID":"","deptName":null}}'
		header = {'content-type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiNWI3ODM4YWMtNjQxNi00NTg3LTg1N2ItZmNkNTI3ZTYxOTdiIiwiaWF0IjoiMjAxOS83LzMwIDE3OjM0OjA0IiwiZXhwIjoxNTY0NTM2ODQ0LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.OtEkyL2BGBQQnwpU533kEWKV1RYo9I7WYZzO3GzEHaw'}
		name = '获取病人视图列表（姓名查询）'
		response = self.client.get(url, headers=header, name=name)
		print(response.status_code, response.text)
		response.raise_for_status()

	@task(1)
	def getvisitpeople(self):
		url = 'http://192.168.1.18:8100/api/clinic/getvisitpeople?input= {"pageIndex":1,"pageSize":20,"MedRecNO":"","VisitID":"","Bed":"","PatientName":"","AttendingDoctorID":[],"AdmitStartDate":"2018-01-01 00:00:00","AdmitEndDate":"2018-07-01 23:59:59","Gender":"","Age":0,"ageUnit":"岁","BirthDay":"","organizationID":["local"],"AdmitDeptID":[],"PointOfCareID":[],"PatientClass":[],"CurPatCondition":[],"NursingGrade":[],"DietType":[],"UserInfo":{"userUID":"e7468084-46b3-4560-a64c-a9c200b1e3be","loginName":"jm1","userName":"贾苗","workNO":"004","officePhone":"","privatePhone":"15869525458","email":"30919454@qq.com","isSuperManager":false,"organizationID":"local","organizationName":"武汉中心医院","deptID":"","deptName":null}}'
		header = {'content-type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiNWI3ODM4YWMtNjQxNi00NTg3LTg1N2ItZmNkNTI3ZTYxOTdiIiwiaWF0IjoiMjAxOS83LzMwIDE3OjM0OjA0IiwiZXhwIjoxNTY0NTM2ODQ0LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.OtEkyL2BGBQQnwpU533kEWKV1RYo9I7WYZzO3GzEHaw'}
		name = '获取就诊视图列表（IMCIS1.0半年）'
		response = self.client.get(url, headers=header, name=name)
		print(response.status_code, response.text)
		response.raise_for_status()

class case_31user(HttpLocust):
	task_set = case_31Task
	min_wait = 1000
	max_wait = 2000
