import { Component, OnInit } from '@angular/core';
import {MatExpansionModule, matExpansionAnimations, MatButtonModule, MatNavList, MatCardModule} from '@angular/material';
import { ParkingLot, LotAvailabilityService } from '../../services/lot-availibility/lot-availability.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  links = ["Nethken A","About"]
  constructor(private lotAvailibilityService: LotAvailabilityService) { }
  isLoading: boolean = true; 
  currentLat: String;
  currentLong: String;
  currentPosition: String;
  lot_name: String;
  lot_names: any;
  lots: any;
  no_lots: Boolean;
  geolocation_permission: Boolean;
  color = 'primary';
  mode = 'indeterminate';
  value = 50;
  

  loadLotsNearYou() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        this.geolocation_permission = true;
        this.currentLat = String(position.coords.latitude);
        this.currentLong = String(position.coords.longitude);
        this.currentPosition = this.currentLat + "," + this.currentLong
        this.getLotsByLocation(this.currentPosition);
      },
      
      error => { 
        if (error.code == error.PERMISSION_DENIED)
            this.geolocation_permission = false;
            this.isLoading = false;
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
        this.no_lots = true;
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
