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
  isNight: boolean
  weatherResponses = {
    "Clear" : false, 
    "Clouds": false,
    "Snow" : false,
    "Rain" : false,
    "Drizzle" : false,
    "Thunderstorm" : false
  }
  
  isOccupied(spotNumber: number): boolean {
    return this.occupiedSpots.indexOf(spotNumber) != -1
  }

  // finds all spots where occupied is true and adds the spot numbers to occupied spots list
  getLotAvailibility(): void {
    this.lotAvailibilityService.getLotData("NethkenA").subscribe(data => {
      this.isLoading = true;
      this.occupiedSpots = data.filter(item => item.occupied == true).map(item => item.spot_number)
      // use first parking spot location for weather coordinates
      this.getLotWeather(data[0].latitude, data[0].longitude)
    })
  }

  getLotWeather(lat, lon): void {
    this.weatherService.getWeather(String(lat), String(lon)).subscribe(data => {
      this.weatherResponses[data.weather[0].main] = true
      this.currentWeather = data.weather[0].description
      this.currentTemp = data.main.temp
      this.isNight = data.weather[0].icon.charAt(data.weather[0].icon.length-1) === 'n' ? true : false
      setTimeout(() => {this.isLoading=false}, 1000)
    }, error => console.log(error))
  }

  kelvinToFahrenheit = (temp: number) : number => (temp-273.15)*(9/5)+32


  ngOnInit() {
    this.getLotAvailibility()
  }
}

