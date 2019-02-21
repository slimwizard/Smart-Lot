import { Component, OnInit } from '@angular/core';
import {MatExpansionModule, matExpansionAnimations, MatButtonModule, MatNavList, MatCardModule} from '@angular/material';
import { ParkingLot, LotAvailabilityService } from '../services/lot-availability.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private lotAvailibilityService: LotAvailabilityService) { }
  isLoading: boolean = true; 
  currentLat: String;
  currentLong: String;
  currentPosition: String;
  lot_name: String;
  lot_names: any;
  lots: any;
  loadLotsNearYou() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        this.currentLat = String(position.coords.latitude);
        this.currentLong = String(position.coords.longitude);
        this.currentPosition = this.currentLat + "," + this.currentLong
        console.log(this.currentPosition)
        this.getLotsByLocation(this.currentPosition);
      });
    } else {
      alert("Geolocation is not supported by this browser.");
    }
  }

  getLotsByLocation(position): void {
    this.lotAvailibilityService.getLotsByLocation(position).subscribe(data => {
      this.isLoading = true;
      this.lots = []
      this.lot_names = data.map(item => item.lot_name);
      if (this.lot_names.length == 0){
        this.lots.push( {name: "There Are No Lots Near You" , routerLink: "/"})
      }
      for (let i of this.lot_names) {
        this.lots.push( {name: this.formatName(i) , routerLink: this.formatRouterLink(i)} )
      }
      setTimeout(() => {this.isLoading=false}, 1000)
    })
  }

  formatName(name): String {
    return name.split(/(?=[A-Z])/).join(" ")
  }

  formatRouterLink(routerLink): String {
    return "/" + routerLink.charAt(0).toLowerCase() + routerLink.slice(1);    
  }

  ngOnInit() {
    this.loadLotsNearYou()
  }

}
