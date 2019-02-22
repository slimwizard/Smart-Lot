import { browser, by, element } from 'protractor';

export class HomePage {
  navigateTo() {
    return browser.get(browser.baseUrl) as Promise<any>;
  }

  getTitleText() {
    return element(by.css('app-root h1')).getText() as Promise<string>;
  }

  getCampusText() {
    return element(by.id('LouisianaTechCampus')).getText() as Promise<string>;
  }

  getPanelHeader() {
    return element(by.id('panel-header'));
  }

  getNethkenButton() {
    return element(by.id('NethkenButton'));
  }
  
  getLotsNearYouText() {
    return element(by.id('lots-near-you-text')).getText() as Promise<string>;
  }
  
}
