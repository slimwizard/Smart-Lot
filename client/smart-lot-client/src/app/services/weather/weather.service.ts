import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class WeatherService {

  API_KEY: string = "8470d59a069473169bc0829191f4bd51"
  API_URL: string = "http://api.openweathermap.org/data/2.5/weather"

  constructor(private http: HttpClient) { }

  getWeather(lat: string, long: string) : Observable<any>{
    return this.http.get<any>(`${this.API_URL}?lat=${lat}&lon=${long}&APPID=${this.API_KEY}`)
  }
}


