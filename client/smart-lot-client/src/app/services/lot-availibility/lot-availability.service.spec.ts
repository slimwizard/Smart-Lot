import { TestBed } from '@angular/core/testing';

import { LotAvailabilityService } from './lot-availability.service';

describe('LotAvailabilityService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: LotAvailabilityService = TestBed.get(LotAvailabilityService);
    expect(service).toBeTruthy();
  });
});
