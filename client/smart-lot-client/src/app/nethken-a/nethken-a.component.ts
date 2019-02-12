import { Component, OnInit } from '@angular/core';
import { MatCardModule, MatButtonModule, MatProgressSpinner } from '@angular/material'
import { ParkingSpot, LotAvailabilityService } from '../services/lot-availability.service';


@Component({
  selector: 'app-nethken-a',
  templateUrl: './nethken-a.component.html',
  styleUrls: ['./nethken-a.component.css']
})

export class NethkenAComponent implements OnInit {

  constructor(private lotAvailibilityService: LotAvailabilityService) { }
  occupiedSpots;

  isLoading: boolean = true; 
  color = 'primary';
  mode = 'indeterminate';
  value = 50;
  
  isOccupied(spotNumber: number): boolean {
    return this.occupiedSpots.indexOf(spotNumber) != -1
  }

  getLotAvailibility(): void {
    this.lotAvailibilityService.getLotData("NethkenA").subscribe(data => {
      this.isLoading = true;
      this.occupiedSpots = data.filter(item => item.occupied == true).map(item => item.spot_number)
      setTimeout(() => {this.isLoading=false}, 1000)
    })
  }

  ngOnInit() {
    this.getLotAvailibility()
  }
}
