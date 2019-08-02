# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkbssopenapi.endpoint import endpoint_data

class QueryAvailableInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'QueryAvailableInstances','bssopenapi')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProductCode(self):
		return self.get_query_params().get('ProductCode')

	def set_ProductCode(self,ProductCode):
		self.add_query_param('ProductCode',ProductCode)

	def get_SubscriptionType(self):
		return self.get_query_params().get('SubscriptionType')

	def set_SubscriptionType(self,SubscriptionType):
		self.add_query_param('SubscriptionType',SubscriptionType)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_EndTimeStart(self):
		return self.get_query_params().get('EndTimeStart')

	def set_EndTimeStart(self,EndTimeStart):
		self.add_query_param('EndTimeStart',EndTimeStart)

	def get_ProductType(self):
		return self.get_query_params().get('ProductType')

	def set_ProductType(self,ProductType):
		self.add_query_param('ProductType',ProductType)

	def get_CreateTimeEnd(self):
		return self.get_query_params().get('CreateTimeEnd')

	def set_CreateTimeEnd(self,CreateTimeEnd):
		self.add_query_param('CreateTimeEnd',CreateTimeEnd)

	def get_InstanceIDs(self):
		return self.get_query_params().get('InstanceIDs')

	def set_InstanceIDs(self,InstanceIDs):
		self.add_query_param('InstanceIDs',InstanceIDs)

	def get_EndTimeEnd(self):
		return self.get_query_params().get('EndTimeEnd')

	def set_EndTimeEnd(self,EndTimeEnd):
		self.add_query_param('EndTimeEnd',EndTimeEnd)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_CreateTimeStart(self):
		return self.get_query_params().get('CreateTimeStart')

	def set_CreateTimeStart(self,CreateTimeStart):
		self.add_query_param('CreateTimeStart',CreateTimeStart)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)

	def get_RenewStatus(self):
		return self.get_query_params().get('RenewStatus')

	def set_RenewStatus(self,RenewStatus):
		self.add_query_param('RenewStatus',RenewStatus)