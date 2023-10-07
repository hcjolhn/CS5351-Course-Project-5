const {Builder,By,Key,until} = require("selenium-webdriver");

const assert = require("assert");
// using mocha to perform assertion
describe("Perform Search",()=>{
    it("Test search google",async()=>{
        const driver = await new Builder().forBrowser("chrome").build();
        try{
            await driver.get("https://google.com");

            const searchBox = driver.findElement(By.name('q'));
            await searchBox.sendKeys("Test Input~~~",Key.RETURN);
            await driver.wait(until.titleIs("Test~~ - Google Search"),1000);
            const pageTitle = await driver.getTitle();
            assert.strictEqual(pageTitle,"Test~~ - Google Search");
        }catch(err){
            console.debug(err);
            // error report
        }finally{
            await driver.quit();
        }
    })
})