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

(async () => {
  // puppeteer-extra is a drop-in replacement for puppeteer,
  // it augments the installed puppeteer with plugin functionality
  const puppeteer = require('puppeteer-extra')

  // add stealth plugin and use defaults (all evasion techniques)
  const StealthPlugin = require('puppeteer-extra-plugin-stealth')
  puppeteer.use(StealthPlugin())

  const authCookie = 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJjZjdkZTA2ZS02NjBiLTQ1ZmMtODk5Zi0yMmFhZDE5NGU4MDAiLCJpc3MiOiJ1c2Vyc2VydmljZV8wZjdkYWE0MF83MTciLCJzdWIiOiI4ODQ4MTZkNS03NjNlLTQ3OTEtODY3My0xOWZkYzA3YjgxMDEiLCJleHAiOjE3MDc4MTQ4NzgsImlhdCI6MTcwNzgxNDU3OCwicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTBoQUxkVVRpSUJwSzBlTUFkTWNrdlhsZFVIN29GWDZPY3dDRi8rR0cvVTVyZFN4cnRWUlNiWU5VVGJwaEoyczBLR3JwKzRBZFBoTFViYUk2bUN1cW9QV0NnMU1sQktQVzhYVmRoNDRjWTRkOElaMGdOVzBOUG14cVFJa2tCZXoyeDM5NU9uWmR4RjQzT3ZvRW9lVW1RbGZKTXI5elhGcFE4dG1WVFQwY3gyenlQa28yVjMxbXRDMzdvb0xXbEZQTGR6WVJMZm9yMGxMMVdJRTdRUFZ6cjVTRUNSUFl5MERPWDVicWZRdzVrMUU3UFFzUWRFNk51MXVJSHhwZXMrSGMyeWVLaE85NXdOd2tZVHk4aXpLREx6RmNvQVBibnJsKytNM21HZVkvbGJuZzVTVlA4RE5HdHc2V1BjV2oxMEozbk90b1c5U0E5M1BNT3l5NGF6cnd2aCtTRTQwaG16c08vQVNrY0xtaXd0OHdjYjR2SFYyb1N4eitpWHE4M1ZpVThqYlBnVlFzc1hWbmRQRHFpbVhvUXlaLzRDais1R0J4KzdiNzBUbzhmaVpHZzU3czV0aGp5L0RFRGpoSitZK3UwOEZuVDRmQ0x0UDRramhFRDhOa1N3WWdDRUg2SzJNME52YXFMb1BLVGppTmJuY0hOV2Q4TVl4b3FIOW9VczA1ZW84UUgwTkRHajUvZTFzMzVCZllCNnlaZFdVUG00OGdMM1N0WE1LRDB0ZFFFWmVOb2FMYi9Sd3ZKOTVqNkhraUxXY09OaitNZldQc0RIZ0dHcHFQMEhsMXZXTll5eTZkOU5McE1XZ3JxZEx2eEtRZGhOQjl2L0RoWFFLQkVwVFJ5UUdKTEZ2dmRoeWttcGU2U1J4VmN0Zjlwbk93YjJkK3ljM1FVaUVKbGhiQWNEN3RtVE9IczFzUjAvZzlrNWFzNys2aEFGV0R2M2xQNE15RUtYeW5GTDFqTVIzWmNOZGxlRHIxdnpSZ2twS09GNzMwZnVwdktxamEyajdxWEcwM1JoUm5ab3h5eUdBVi85QWdscGN5YS92a0xScTA5aTk0SzhCNXIxUWMvZGVSa1QvYmdoakQ1WGlSZjByOENmY1BGZjZZdEY1Zjk2WlpqWkxUcThvd2t5V3k5ak9DMVJBNVVPMWp3VWtTMTFOIiwicHVibGljIjp7InNlc3Npb25faGFzaCI6Ii0xMjM5NTAxNDc2In19.mL-76eY6KdtFQbq221TeQzBomYZWteIT6PhlgLwlreKk2Mxifuj6dYaG5kfwfWMU4PqB8OXTSY8yvG65fWELXA'

  const url = 'https://www.crunchbase.com/lists/all/8d5bde75-2d8b-445b-9dd5-6fbef3886416/organization.companies'

  // get last cb rank and round up to nearest increment of 1000
  const rangeStart = 0
  const rangeEnd = 3234000
  const rangeIncrement = 1000

  // puppeteer usage as normal
  puppeteer.launch({ headless: false, timeout: 0 }).then(async browser => {
    const page = await browser.newPage()

    await page.setCookie(
      { name: 'authcookie', value: authCookie, domain: 'www.crunchbase.com' },
    );
  
    await page.goto(url)

    const fromInput = await page.$('#mat-input-1')
    const toInput = await page.$('#mat-input-2')
    const searchButton = await page.$('search-button button')
    const exportCsvButton = await page.$('export-csv-button button')

    if (!fromInput || !toInput) {
      console.log('input ids changed, try again')
      
      return
    }

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
      
    // await browser.close()
  })
})()