import { browser, by, element } from 'protractor';

export class NethkenAPage {
  navigateTo() {
    return browser.get('/nethkena') as Promise<any>;
  }

  getLotTitleText() {
    return element(by.className('lotTitle')).getText() as Promise<string>;
  }

  getLotDescriptionText() {
    return element(by.className('lotDescription')).getText() as Promise<string>;
  }

  getBackButton() {
    return element(by.className('backButton'))
  }

  getRefreshButton() {
    return element(by.className('refreshButton'))
  }

  getMap() {
    return element(by.className('map')).isDisplayed() as Promise<boolean>;
  }

  getWeatherDetails() {
    return element(by.className('weather-grid'))
  }
    
}
