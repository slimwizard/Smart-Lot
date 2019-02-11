import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class LotAvailabilityService {

  api_url: string = ''
  api_url_dev: string = 'http://127.0.0.1:5000/smart-lot/lots/'
  
  constructor(private http: HttpClient) { }

  getLotData(lot: string) {
    let url = this.api_url_dev + lot
    return this.http.get(url)
  }
}

export interface ParkingSpot {
  

}
