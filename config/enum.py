from enum import Enum

class AffiliationID(Enum):
	wellcard = '659caaec-c51b-4465-b464-453ffdb900cf'
	higi = 'f3801b83-556a-4ac8-b3a5-a0170a2959ae'
	usarx = '98e0f64c-158f-475a-b8a9-f4530225c0cf'
	capitalrx = 'ce8fa78c-ce91-4497-b3d5-b4807f054735'
	nbrx = 'cefaeebe-8dde-4285-9042-4235b7e4d5be'
	singlecare = 'c318c668-5c63-4850-8fff-4811acdc4a4e'
	genius_rx = 'e1eb127b-c37e-48a9-98fb-8ad204ca9d46'
	goodrx = '5837f2dc-f5f8-401f-88f4-321d22b81815'
	rxsaver = '70a2373a-bb17-489e-bc51-df3781e83287'

class Product_Status(Enum):
	active = 'c90fbc47-0e46-47c3-84f5-f4881908df72'
	inactive = '8fce428b-4698-433c-b472-5952a7d32350'
	deactivated = 'c71778a8-7707-4b51-ae56-ba1a574bee3a'