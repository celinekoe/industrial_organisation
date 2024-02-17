const clearInput = async (page) => {
  await page.evaluate( () => document.execCommand( 'selectall', false, null ) );
  await page.keyboard.press('Backspace')
}

const newInput = async (page, value) => {
  await page.keyboard.type(value)
}

const download = async (page, exportCsvButton) => {
  // wait for results to load before exporting
  await page.waitForSelector('grid-row.ng-star-inserted')
  
  await exportCsvButton.click()
}

const delay = async (ms) => {
  return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {
  // puppeteer-extra is a drop-in replacement for puppeteer,
  // it augments the installed puppeteer with plugin functionality
  const puppeteer = require('puppeteer-extra')

  // add stealth plugin and use defaults (all evasion techniques)
  const StealthPlugin = require('puppeteer-extra-plugin-stealth')
  puppeteer.use(StealthPlugin())

  const authCookie = 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJiM2ViODRlMC0wZGM2LTQyMzEtOGJjOS1lMjkzY2E3MTYyY2MiLCJpc3MiOiJ1c2Vyc2VydmljZV83MGJjNjZjOV83MTciLCJzdWIiOiI4ODQ4MTZkNS03NjNlLTQ3OTEtODY3My0xOWZkYzA3YjgxMDEiLCJleHAiOjE3MDgxODYzMjcsImlhdCI6MTcwODE4NjAyNywicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTBoQUxkVVRpSUJwSzBlTUFkTWNrdlhsZFVIN29GWDZPY3dDRi8rR0cvVTVyZFN4cnRWUlNiWU5VVGJwaEoyczBLR3JwKzRBZFBoTFViYUk2bUN1cW9QV0NnMU1sQktQVzhYVmRoNDRjWTRkOElaMGdOVzBOUG14cVFJa2tCZXoyeDM5NU9uWmR4RjQzT3ZvRW9lVW1RbGZKTXI5elhGcFE4dG1WVFQwY3gyenlQa28yVjMxbXRDMzdvb0xXbEZQTGR6WVJMZm9yMGxMMVdJRTdRUFZ6cjVTRUNSUFl5MERPWDVicWZRdzVrMUU3UFFzUWRFNk51MXVJSHhwZXMrSGMyeWVLaE85NXdOd2tZVHk4aXpLREx6RmNvQVBibnJsKytNM21HZVkvbGJuZzVTVlA4RE5HdHc2V1BjV2oxMEozbk90b1c5U0E5M1BNT3l5NGF6cnd2aCtTRTQwaG16c08vQVNrY0xtaXd0OHdjYjR2SFYyb1N4eitpWHE4M1ZpVThqYlBnVlFzc1hWbmRQRHFpbVhvUXlaLzRDais1R0J4KzdiNzBUbzhmaVpHZzU3czV0aGp5L0RFRGpoSitZK3UwOEZuVDRmQ0x0UDRramhFRDhOa1N6UFI1Nm9ySjdEV0NuZk80bjdYUkZ6UWlIWlFzTURxTE1aWGRyMzlSbXYwakp6Tmg0THh5YlIwN09GNXFRSHVodHpuOXRNdnNhUm9FSStERmxyM1RyeXFKRjhDMDRxdXhadEprK1c2QXg4dWlYaWsvMXpoSFREdTdIWk9MYWpGQm5hcUp4cXNjQXcwUU5mYWwraGFuaGlKeWVDNzlUSzJzWC9aVENBcCtscVhEWmF0UHF0V00yRWxiSDhIaHN3ZUFEOCtQbmNqRTNHTXd4aWR4ci9ReFBDY0VnNnJCNnF3dFBNazlmNlg3R2JxU2J4M0luSksvdXltLzZoVzRrQkRweWgzZjYzT1FqaHhGVG9Bc05qMjNtOXNCNlgxUkFIS29pWWhXSTZCQnZCVVU4NWZuanpQQUFIOFJpRFpCaFM0a1BLcUpEc1BVYndoVG5xUk9HQUNMWjlKT25XYkUxTE9PMGtueWt2bmZrcGVGTDRpR3BOWEpCQ1Z3dEVLV3Zta3I1VlhUQVNjWVpKS2VFcm1nZzlkUFAyIiwicHVibGljIjp7InNlc3Npb25faGFzaCI6Ii0xMjM5NTAxNDc2In19.fNbYs8oxCeaHlC-nQQe9HWmI3z2L-gABL93J2hXTZGrtxD1IQPX2EEF5BE9EWPH6Xwq4lfUzOOnM-cDOqKIx-g'

  // const url = 'https://www.crunchbase.com/lists/all/8d5bde75-2d8b-445b-9dd5-6fbef3886416/organization.companies'
  const url = 'https://www.crunchbase.com/lists/funding/e82bb51d-0b57-49f7-a4b3-c731a3487b6f/funding_rounds'

  // get last cb rank and round up to nearest increment of 1000
  const rangeStart = 347200
  const rangeEnd = 627000
  const rangeIncrement = 600
  const delayMs = 2000 // delay before attempting to get input

  // puppeteer usage as normal
  puppeteer.launch({ headless: false, timeout: 0 }).then(async browser => {
    const page = await browser.newPage()
  
    await page.setCookie(
      { name: 'authcookie', value: authCookie, domain: 'www.crunchbase.com' },
    );

    await page.goto(url)

    await delay(delayMs)

    const fromInput = await page.$('#mat-input-1')
    const toInput = await page.$('#mat-input-2')
    const searchButton = await page.$('search-button button')
    const exportCsvButton = await page.$('export-csv-button button')

    if (!fromInput || !toInput) {
      console.log(fromInput)
      console.log(toInput)
      console.log('input ids changed, try again')
    } else {
      // loop through cb rank in increments to get around export limits
      for (let i = rangeStart; i <= rangeEnd; i += rangeIncrement) {
        const fromRange = i
        const toRange = i + rangeIncrement - 1
        console.log(`i: ${i}`)

        await fromInput.click()
        await clearInput(page)
        await newInput(page, fromRange.toString())

        await toInput.click()
        await clearInput(page)
        await newInput(page, toRange.toString())

        await searchButton.click()
        await download(page, exportCsvButton)
      }
    }
    
    // await browser.close()
  })
})()