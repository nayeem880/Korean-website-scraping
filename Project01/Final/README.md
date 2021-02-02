## Install the following packages and libraries with mentioned version

Python 3.8.6
requests 2.25.1
beautifulsoup 4.9.3
pandas 1.2.1


### Folder Structure:

- First run `profile_link_extraction.py` . This will get all the profile links of around 4800+ from the target and will store in csv format named `new_profile_links.csv`
and also will create a file named `updated_profile_links.csv` which means - links inside this file is brand new. They are new added to the website.
- Then run `profile_data_extraction.py`. This script will get all the user data and store the data inside  `DATA.csv`
- If you want to see only the updated profile's data then run `update_data.py`.

Done... the script will run perfectly...

Moreover, I've already scraped the data for you and stored in the `DATA.csv` and all profile links in `old_profile_link.csv` for instant use. Thank you
