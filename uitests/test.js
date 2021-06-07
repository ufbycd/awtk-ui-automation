// javascript

require("awtk-appium-js-helpers/setup.js");
let startApp = require("awtk-appium-js-helpers/start-app").startApp;

const wdio = require("webdriverio");
const assert = require("assert");

const appName = '../bin/demo'

const opts = {
  path: '/wd/hub',
  port: 4723,
  capabilities: {
    platformName: "awtk",
    a4aPort: 8000
  }
};

async function main () {
  startApp(appName);
  await new Promise(r => setTimeout(r, 1000));

  const client = await wdio.remote(opts);

  const field = await client.$("~edit");

  await field.setValue("Hello World!");
  assert.strictEqual(await field.getText(), "Hello World!");

  await field.addValue("1234");
  assert.strictEqual(await field.getText(), "Hello World!1234");

  await client.deleteSession();
}

main();
