# GET Start

## Steps for setup
- Run npm i / yarn / another package manager you want
- npm start (it will run all the test under `./tests/**/*.js` automatically)

## Tools
- Selenium(Testing tools for automated browser)
- Mocha(Testing tools)


## Create your own test
- open folder under `./tests/${your_test_name}`
- create your test written in js under `${your_test_name}`
- Run `npm start`

## Customization
- You can e dit .mocharc.json to add config, if it cannot fulfil what you need, you can create a .mocharc.js to solve it (e.g PROCESS_ENV)