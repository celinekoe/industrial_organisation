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

  const authCookie = 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI5NjBhMGE4OC01ODMyLTRmZjktOTVkNi1iOGI4NTg3NjQ4YjMiLCJpc3MiOiJ1c2Vyc2VydmljZV83MGJjNjZjOV83MTciLCJzdWIiOiI4ODQ4MTZkNS03NjNlLTQ3OTEtODY3My0xOWZkYzA3YjgxMDEiLCJleHAiOjE3MDgzMjQ5MzksImlhdCI6MTcwODMyNDYzOSwicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTBoQUxkVVRpSUJwSzBlTUFkTWNrdlhsZFVIN29GWDZPY3dDRi8rR0cvVTVyZFN4cnRWUlNiWU5VVGJwaEoyczBLR3JwKzRBZFBoTFViYUk2bUN1cW9QV0NnMU1sQktQVzhYVmRoNDRjWTRkOElaMGdOVzBOUG14cVFJa2tCZXoyeDM5NU9uWmR4RjQzT3ZvRW9lVW1RbGZKTXI5elhGcFE4dG1WVFQwY3gyenlQa28yVjMxbXRDMzdvb0xXbEZQTGR6WVJMZm9yMGxMMVdJRTdRUFZ6cjVTRUNSUFl5MERPWDVicWZRdzVrMUU3UFFzUWRFNk51MXVJSHhwZXMrSGMyeWVLaE85NXdOd2tZVHk4aXpLREx6RmNvQVBibnJsKytNM21HZVkvbGJuZzVTVlA4RE5HdHc2V1BjV2oxMEozbk90b1c5U0E5M1BNT3l5NGF6cnd2aCtTRTQwaG16c08vQVNrY0xtaXd0OHdjYjR2SFYyb1N4eitpWHE4M1ZpVThqYlBnVlFzc1hWbmRQRHFpbVhvUXlaLzRDais1R0J4KzdiNzBUbzhmaVpHZzU3czV0aGp5L0RFRGpoSitZK3UwOEZuVDRmQ0x0UDRramhFRDhOa1N6TU9XaXBzYjdjcFNoMng4ck5HZnFWem5GUitXTXBZZFRLU0dNbTNkSjVDWkhyKzdTOHNnS1F4dHlaWEdQN3k2bWZ1OTk5bWJwaUJyMXB3NVVEOWczZzE3SUl6K3NzNHpRaGd5RW5vQllzaStkTk1oQ21KU2loYnV6bm04S0dkVnpVSmNHYjN5OUl6YXR0cDlSTFdpTUtOOW5wN3RXa2tFVm1TN1U3N000Vmk5c1NBakF2My9DdTltbFRVdVp5YVN2Z3JGdDRDcDlmUzVsM1RaUllMSm5JdmlmdTBNWldsbGUrOFk4Q2lSVVF1N08wKzJ1Y2kyWkJ4MlFBOUhXU3R3T1RiN3lBY25RWDBkZkM2SE5PYlFPR1h6RzVxbThpSlB1ZVB2STBXTWE3R3dTNGFBK1JHNDZaaVFQMmN3L3djbjJLcmtZb2hiMjNibTVDendsNUFiWTB3S3BaS0sxOWUrcHBPMEw5U0JQY2hzS1dCZEdaaDBqN3NiTVY3aWl3S2xnSGJOZUpLN01PcTRLWHlXNnBwZnlUIiwicHVibGljIjp7InNlc3Npb25faGFzaCI6Ii0xMjM5NTAxNDc2In19.lO_F8Crn8RqQO7mDh0Pf__uTNhzZMwTH3Mxv879FGzMPF80xzJxEZ0VKZWv0HXrlyWdzvvoATlA7seD630C8kA'

  // const url = 'https://www.crunchbase.com/lists/all/8d5bde75-2d8b-445b-9dd5-6fbef3886416/organization.companies'
  const url = 'https://www.crunchbase.com/lists/investors/4a9b01ad-48ad-4e0d-bd40-621f2c5fccd3/principal.investors'
  // const url = 'https://www.crunchbase.com/lists/funding/e82bb51d-0b57-49f7-a4b3-c731a3487b6f/funding_rounds'

  // get last cb rank and round up to nearest increment of 1000
  const rangeStart = 0
  const rangeEnd = 273000
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

    const fromInput = await page.$('#mat-input-0')
    const toInput = await page.$('#mat-input-1')
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