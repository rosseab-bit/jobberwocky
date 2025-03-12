import re

def format_data_api(data):
    data_example = {
		"id": None,
		"position": "",
		"country": "",
		"city": None,
		"work_type": None,
		"salary_range_min": "0",
		"salary_range_max": "0",
	}
    keys_data_api = list(data.keys())
    print(keys_data_api)
    list_lobs_api = []
    for country in keys_data_api:
        print(country)
        for job in data[country]:
            skills = re.findall(r'<skill>(.*?)</skill>', job[2])
            job_data = data_example.copy()
            job_data['position'] = job[0]
            job_data['country'] = country 
            job_data['skills'] = ' '.join(skills)
            job_data['salary_range_min'] = '0'
            job_data['salary_range_max'] = str(job[1])
            list_lobs_api.append(job_data)
    print('\n \n \n \n', list_lobs_api)
    return list_lobs_api

