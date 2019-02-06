import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NethkenAComponent } from './nethken-a.component';

describe('NethkenAComponent', () => {
  let component: NethkenAComponent;
  let fixture: ComponentFixture<NethkenAComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NethkenAComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NethkenAComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
