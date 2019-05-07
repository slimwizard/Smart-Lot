import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
// import 'rxjs/add/operator/catch';
import {LotComponent} from '../../components/lot/lot.component';


@Injectable({
  providedIn: 'root'
})
export class LotAvailabilityService {

  api_url: string = 'https://api.smart-lot.io/smart-lot/lots/'
  api_url_dev: string = 'http://127.0.0.1:5000/smart-lot/lots/'
  
  constructor(private http: HttpClient) { }

  getSpotData(lotID: string): Observable<ParkingSpot[]> {
    let url = this.api_url + lotID
    return this.http.get<ParkingSpot[]>(url)
  }

  getLotsByLocation(location: string): Observable<ParkingLot[]> {
    let url = this.api_url + "by_location/" + location
    return this.http.get<ParkingLot[]>(url)
  }

  getLotData(lotID: string): Observable<ParkingLot[]> {
    let url = this.api_url + "lot/" + lotID
    return this.http.get<ParkingLot[]>(url)
  }
}

export interface ParkingSpot {
  spot_number: number
  spot_id: string
  parking_type: number
  latitude: number
  longitude: number
  occupied: boolean
}

export interface ParkingLot {
  latitude: number
  longitude: number
  lot_id: string
  lot_name: number
  description: string
  lot_number: number
}
