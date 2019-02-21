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
        const nethkenAButton = homePage.getNethkenButton();
        nethkenAButton.click();
        browser.sleep(2000)
        expect(browser.driver.getCurrentUrl()).toContain('/nethkenA');
    });

    it('should display a card titled "Lots Near You"', () => {
        expect(homePage.getLotsNearYouText()).toEqual('Lots Near You:')
    });

    })


    afterEach(async () => {
    // Assert that there are no errors emitted from the browser
    const logs = await browser.manage().logs().get(logging.Type.BROWSER);
    expect(logs).not.toContain(jasmine.objectContaining({
        level: logging.Level.SEVERE,
    }));
});

