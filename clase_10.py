#==================================================================
# 							 CLASE 10
#==================================================================
import requests


def main():
	params = {
		"category": "MLA1459",
		"has_pictures": "yes"
	}
	req = requests.get("https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&has_pictures=yes", params=params)
	if req.status_code == 200:
		content = req.json()

		results = content["results"]
		for result in results:
			print(result["price"])
			

if __name__ == "__main__":
	main()