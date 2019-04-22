import { Component, OnInit } from '@angular/core';
import { LotModalComponent } from './lot-modal/lot-modal.component'
import { ParkingSpot, LotAvailabilityService } from '../../services/lot-availibility/lot-availability.service'
import { MatDialog } from '@angular/material'
import { WeatherService } from '../../services/weather/weather.service'
import {
  transition,
  trigger,
  query,
  style,
  animate,
  group,
  animateChild,
  state
} from '@angular/animations';

@Component({
  selector: 'app-lot',
  templateUrl: './lot.component.html',
  styleUrls: ['./lot.component.scss']
})
export class LotComponent implements OnInit {

  constructor(private lotAvailibilityService: LotAvailabilityService, private weatherService: WeatherService, public dialog: MatDialog) { }
  occupiedSpots
  weatherError: boolean
  Lot_UUID: string[] = ['a19f71fc-4d20-4790-9e38-31df6a02ac76']
  current_UUID: string

  isLoading: boolean = false  //**RESET TO TRUE
  color = 'primary'
  mode = 'indeterminate'
  value = 50
  currentWeather: string
  currentTemp: string
  isNight: boolean
  weatherResponses = {
    "Clear" : false, 
    "Clouds": false,
    "Snow" : false,
    "Rain" : false,
    "Drizzle" : false,
    "Thunderstorm" : false
  }
  latitude: number
  longitude: number
  
  isOccupied(spotNumber: number): boolean {
    return this.occupiedSpots.indexOf(spotNumber) != -1
  }

  // finds all spots where occupied is true and adds the spot numbers to occupied spots list
  getLotAvailibility(): void {
    this.lotAvailibilityService.getLotData(this.current_UUID).subscribe(data => {
      this.isLoading = false; //**RESET TO TRUE
      this.latitude = data[0].latitude;
      this.longitude = data[0].longitude
      this.occupiedSpots = data.filter(item => item.occupied == true).map(item => item.spot_number)
      // use first parking spot location for weather coordinates
      this.getLotWeather(this.latitude, this.longitude)
    }, error => console.log(error))
  }

  getLotWeather(lat, lon): void {
    this.weatherService.getWeather(String(lat), String(lon)).subscribe(data => {
      this.weatherResponses[data.weather[0].main] = true
      this.currentWeather = data.weather[0].description
      this.currentTemp = data.main.temp
      this.isNight = data.weather[0].icon.charAt(data.weather[0].icon.length-1) === 'n' ? true : false
      setTimeout(() => {this.isLoading=false}, 1000)
    }, error => {
      this.weatherError = true
      setTimeout(() => {this.isLoading=false}, 1000)
    })
  }

  kelvinToFahrenheit = (temp: number) : number => (temp-273.15)*(9/5)+32

  openMap(): void {
    // window.open(`https://maps.google.com/?q=${this.latitude},${this.longitude}`)
    if /* if we're on iOS, open in Apple Maps */
    ((navigator.platform.indexOf("iPhone") != -1) || 
     (navigator.platform.indexOf("iPad") != -1) || 
     (navigator.platform.indexOf("iPod") != -1))
    window.open(`maps://maps.google.com/?q=${this.latitude},${this.longitude}`);
    else /* else use Google */
    window.open(`https://maps.google.com/?q=${this.latitude},${this.longitude}`);
  }

  openDialog(): void {
    const dialogRef = this.dialog.open(LotModalComponent,{
      width: "600px"
    })
  }

  ngOnInit() {
    this.getLotAvailibility()
  }
}