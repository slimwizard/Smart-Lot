
import {NethkenAPage} from './nethkenA.po'

import { browser, logging } from 'protractor';



let nethkenAPage: NethkenAPage

describe('running Nethken A tests', () => {
  beforeAll(() => {
    nethkenAPage = new NethkenAPage();
    nethkenAPage.navigateTo();
  });

  it('should display lot title', () => {
    nethkenAPage.navigateTo();
    expect(nethkenAPage.getLotTitleText()).toEqual('Nethken A');
  });

  it('should display lot description', () => {
    expect(nethkenAPage.getLotDescriptionText()).toEqual('The parking lot adjacent to the back of Nethken Hall')
  })

  it('should display back button', () => {
    expect(nethkenAPage.getBackButton().isDisplayed()).toBeTruthy()
  })

  it('should navigate home when back button is clicked', () => {
    const backButton = nethkenAPage.getBackButton()
    backButton.click();
    expect(browser.driver.getCurrentUrl()).toContain('/home');
  })

  it('should display refresh button', () => {
    expect(nethkenAPage.getRefreshButton().isDisplayed()).toBeTruthy()
  })

  it('should display display svg map', () => {
    expect(nethkenAPage.getMap()).toBeTruthy()
  })

})


afterEach(async () => {
  // Assert that there are no errors emitted from the browser
  const logs = await browser.manage().logs().get(logging.Type.BROWSER);
  expect(logs).not.toContain(jasmine.objectContaining({
    level: logging.Level.SEVERE,
  }));
});

