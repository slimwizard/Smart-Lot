import { HomePage } from './home.po';

import { browser, logging } from 'protractor';


let homePage: HomePage;


describe('running home page tests', () => {
    beforeAll(() => {
        homePage = new HomePage();
        homePage.navigateTo();
    });

    it('should display welcome message', () => {
        homePage.navigateTo();
        expect(homePage.getTitleText()).toEqual('SMART LOT');
    });

    it('should display option for Tech campus', () => {
        expect(homePage.getCampusText()).toEqual('Louisiana Tech')
    })

    it('Should redirect to Nethken A when button is clicked', () => {
        const panelHeader = homePage.getPanelHeader();
        panelHeader.click();
        const nethkenAButton = homePage.getNethkenButton();
        browser.sleep(1000);
        nethkenAButton.click();
        expect(browser.driver.getCurrentUrl()).toContain('/nethkenA');
    });

    })

    afterEach(async () => {
    // Assert that there are no errors emitted from the browser
    const logs = await browser.manage().logs().get(logging.Type.BROWSER);
    expect(logs).not.toContain(jasmine.objectContaining({
        level: logging.Level.SEVERE,
    }));
});

