#!/usr/bin/env python3
# North American Numbering Plan Administration (NANPA) API Client - Developed by acidvegas in Python (https://git.acid.vegas/nanpa)
# nanpa/client.py

import json
import logging
import urllib.error
import urllib.parse
import urllib.request


class NanpaAPI:
	def __init__(self):
		'''Initialize the NANPA API client.'''

		self.base_url = 'https://api.nanpa.com/reports/public'


	def _make_request(self, endpoint: str, params: dict = None) -> dict:
		'''
		Make a request to the NANPA API.

		:param endpoint: API endpoint to call
		:param params: Optional query parameters
		'''

		url = f'{self.base_url}/{endpoint}'

		if params:
			url += '?' + urllib.parse.urlencode(params)

		try:
			with urllib.request.urlopen(url) as response:
				return json.loads(response.read().decode())
		except urllib.error.URLError as e:
			logging.error(f'Failed to make request to {url}: {e}')
			return None


	def get_9yy_codes(self) -> dict:
		'''Get 9YY specialty codes.'''

		return self._make_request('specialityResources/9yy/codes')


	def get_area_code_info(self, npa: str) -> dict:
		'''
		Get detailed information about a specific area code.

		:param npa: Area code to lookup
		'''

		params = {'npa': npa}

		return self._make_request('npa/areaCodeListing', params)


	def get_area_codes_by_state(self, state: str) -> dict:
		'''
		Get area codes for a specific state.

		:param state: Two-letter state code
		'''

		params = {'states': state, 'isExternal': 'false'}

		return self._make_request('code/getNpasForStates', params)


	def get_co_code_forecast(self, state: str, npa: str) -> dict:
		'''
		Get CO code forecast information.

		:param state: Two-letter state code
		:param npa: Area code

		'''

		params = {'state': state, 'npa': npa}

		return self._make_request('tbco/coCodeForecast', params)


	def get_current_pool_tracking(self, state: str, npa: str) -> dict:
		'''
		Get current pool tracking information.

		:param state: Two-letter state code
		:param npa: Area code
		'''

		params = {'state': state, 'npa': npa}

		return self._make_request('tbco/currentPoolTracking', params)


	def get_lrn_forecast(self, state: str, npa: str) -> dict:
		'''
		Get LRN forecast information.

		:param state: Two-letter state code
		:param npa: Area code
		'''

		params = {'state': state, 'npa': npa}

		return self._make_request('tbco/lrnForecast', params)


	def get_pooling_forecast(self, state: str, npa: str) -> dict:
		'''
		Get pooling forecast information.

		:param state: Two-letter state code
		:param npa: Area code
		'''

		params = {'state': state, 'npa': npa}

		return self._make_request('tbco/poolingForecast', params)


	def get_pstn_activation(self, state: str) -> dict:
		'''
		Get PSTN activation information.

		:param state: Two-letter state code
		'''

		params = {'state': state}

		return self._make_request('tbco/pstnActivation', params)


	def get_rate_center_changes(self, start_date: str, end_date: str) -> dict:
		'''
		Get rate center changes between two dates.

		:param start_date: Start date in format YYYY-MM-DDT00:00:00.000-05:00
		:param end_date: End date in format YYYY-MM-DDT23:59:59.999-05:00
		'''

		params = {'startDate': start_date, 'endDate': end_date}

		return self._make_request('npa/rateCenterChanges', params)


	def get_rate_centers(self, state: str) -> dict:
		'''
		Get rate centers for a specific state.

		:param state: Two-letter state code
		'''

		params = {'state': state}

		return self._make_request('npa/rateCenters', params)


	def get_specialty_codes_aging(self) -> dict:
		'''Get aging 5XX specialty codes.'''

		return self._make_request('specialityResources/5xx/aging')


	def get_specialty_codes_assigned(self) -> dict:
		'''Get assigned 5XX specialty codes.'''

		return self._make_request('specialityResources/5xx/assigned')


	def get_specialty_codes_available(self, code_type: str = '5xx') -> dict:
		'''
		Get available specialty codes.

		:param code_type: Code type ('5xx' or '9yy')
		'''

		return self._make_request(f'specialityResources/{code_type}/available')


	def get_states(self) -> dict:
		'''Get all NANPA states and territories.'''

		return self._make_request('nanpaStates')


	def get_thousands_blocks(self, state: str, npa: str, report_type: str = 'AS') -> dict:
		'''
		Get thousands blocks information.

		:param state: Two-letter state code
		:param npa: Area code
		:param report_type: Report type (default: AS)
		'''

		params = {'state': state, 'npa': npa, 'reportType': report_type}

		return self._make_request('tbco/thousandsBlocks', params)



def main():
	'''Example usage of the NANPA API client.'''

	client = NanpaAPI()

	# Example API calls
	states = client.get_states()
	logging.info(f'States: {json.dumps(states, indent=2)}')

	fl_codes = client.get_area_codes_by_state('FL')
	logging.info(f'Florida area codes: {json.dumps(fl_codes, indent=2)}')

	area_info = client.get_area_code_info('301')
	logging.info(f'301 area code info: {json.dumps(area_info, indent=2)}')


if __name__ == '__main__':
	main()
