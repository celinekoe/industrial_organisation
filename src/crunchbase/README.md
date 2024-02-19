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
Save the query and Crunchbase will automatically reload those preferences each time Chrome starts
You're free to modify the query, but you'll also have to modify the script accordingly
I used cb rank to partition the data since it guarantees that there will be less rows than the crunchbase's export limit
Adjust range increment as appropriate if the data is sparse. The larger the range increment the faster the export will be

After running, you will have to wait a bit for the 'Allow Multiple Downloads' prompt to appear
Click that before doing other things
Script will occasionally fail due to timeout. Just set rangeStart to the next set of data to download

### Rename Data Files
Run script:
```
./rename.sh country/united_states united_states
./rename.sh investors investors
./rename.sh funding_rounds funding_rounds
```
