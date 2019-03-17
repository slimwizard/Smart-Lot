import { Component, OnInit } from '@angular/core'

import { ParkingSpot, LotAvailabilityService } from '../../services/lot-availibility/lot-availability.service'
import { WeatherService } from '../../services/weather/weather.service'


@Component({
  selector: 'app-nethken-a',
  templateUrl: './nethken-a.component.html',
  styleUrls: ['./nethken-a.component.scss']
})

export class NethkenAComponent implements OnInit {

  constructor(private lotAvailibilityService: LotAvailabilityService, private weatherService: WeatherService) { }
  occupiedSpots;

  isLoading: boolean = true 
  color = 'primary'
  mode = 'indeterminate'
  value = 50
  currentWeather: string
  currentTemp: string
  
  isOccupied(spotNumber: number): boolean {
    return this.occupiedSpots.indexOf(spotNumber) != -1
  }

  // finds all spots where occupied is true and adds the spot numbers to occupied spots list
  getLotAvailibility(): void {
    this.lotAvailibilityService.getLotData("NethkenA").subscribe(data => {
      this.isLoading = true;
      this.occupiedSpots = data.filter(item => item.occupied == true).map(item => item.spot_number)
      setTimeout(() => {this.isLoading=false}, 1000)
    })
  }

  getLotWeather(): void {
    this.weatherService.getWeather("32.520530", "-92.146500").subscribe(data => {
      console.log(data)
      this.currentWeather = data.weather[0].description
      this.currentTemp = data.main.temp
    })
  }

  kelvinToFahrenheit = (temp: number) : number => (temp-273.15)*(9/5)+32


  ngOnInit() {
    this.getLotAvailibility()
    this.getLotWeather()
  }
}
