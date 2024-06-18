import guardian as theguardian_content
import json
# create content
content = theguardian_content.Content(api='55812382-8158-49b8-bad8-3e7c56b53384')

# gets raw_response
raw_content = content.get_request_response()
print("Request Response status code {status}." .format(status=raw_content.status_code))
print("Request Response headers {header}." .format(header=raw_content.headers))

# content
print("Content Response headers {}." .format(content.response_headers()))

# get all results of a page
json_content = content.get_content_response()
all_results = content.get_results(json_content)
#print(f"Responses {json.dumps(all_results, indent=2)}")


print("")
print("---------------------------------------------------------------------------------------------------------------------------------------")
print("")

# actual response
print(f"Response {json.dumps(json_content, indent=2)}")