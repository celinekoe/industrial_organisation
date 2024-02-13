### You Need
Node

###  Installation
```
yarn install
```

### Configuration
Update init.js:
```
const authCookie = '{crunchbase auth_cookie}'
const rangeStart = 0
const rangeEnd = {cb rank of last row ordered by cb rank desc}
const rangeIncrement = 1000
```
You may have to start a dry run of Puppeteer and login to that first to get the auth_cookie

### Run
Run init.js:
```
node init.js
```
Puppeteer will start Chrome browser to start exporting rows
Crunchbase Query Builder needs to be setup as seen in query_builder.png for the script to run correctly
You can modify the query, but you'll also have to modify the script accordingly
I used cb rank to partition the data since it guarantees that there will be less rows than the crunchbase's export limit
Adjust range increment as appropriate if the data is sparse

After running, you will have to wait a bit for the 'Allow Multiple Downloads' prompt to appear
Click that before doing other things
Script will occasionally fail due to timeout. Just set rangeStart to the next set of data to download

### Check Data
Copy the downloaded csvs to the appropriate data folder
Check if the data is correct by running the following script to return the total line count:
```
./check_data.sh country/united_states
```
Compare the total line count to the results in Query Builder

### Rename Data Files
Install rename utility:
```
brew install rename
```
Rename files so you won't get confused by the generic file names later
This command renames all files in a folder:
```
rename 'our $i; $i++; $_ = sprintf("us_$i.%s", $1)' *
```