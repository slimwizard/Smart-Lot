import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LotModalComponent } from './lot-modal.component';

describe('LotModalComponent', () => {
  let component: LotModalComponent;
  let fixture: ComponentFixture<LotModalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LotModalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LotModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
